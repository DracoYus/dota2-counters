#!/usr/bin/python3
"""
    Script used to scrap the Dota Buff website to retrieve counters of some hero.
    Created: Oct, 21 2020.
"""
import sys
import requests
import time
from bs4 import BeautifulSoup
from utils import read_list_from_file, write_to_pickle
import config


heroes = read_list_from_file(config.hero_list_file_name)

counters = []


def dotaBuffScrapping(hero):
    # Set the URL you want to webscrape from
    url = "https://www.dotabuff.com/heroes/" + hero + "/counters"

    # Connect to the URL. User agent is to prevent the browser to give the 429 response (too many requests)
    response = requests.get(url, headers=config.headers, proxies=config.proxies)

    # Give some time to load the page
    time.sleep(config.sleep_time)

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    countered_by_section = soup.find("section", class_="counter-outline")
    countered_by_list = countered_by_section.find_all("tr")

    if countered_by_list is not None:
        temp = []
        for counterHero in countered_by_list:
            td = counterHero.find_all("td")
            if len(td) >= 1:
                value = td[1].text
                temp.append(value)

        counters.append({"name": hero, "counters": temp})


def doLoopThroughHeroes():
    for hero in heroes:
        print(f"Parsing {hero}...")
        dotaBuffScrapping(hero)
        time.sleep(config.sleep_time)
    write_to_pickle(counters, config.counter_pickle_file_name)



def herofinder(myhero):
    for hero in heroes:
        if hero == myhero:
            dotaBuffScrapping(hero)
            time.sleep(config.sleep_time)
            write_to_pickle(counters, config.counter_pickle_file_name)
            return True
    return False

if __name__ == "__main__":
    if len(sys.argv) == 1:
        doLoopThroughHeroes()
        print(
            "DotaBuffScrapping Done! Open countersByHero file to check out the results"
        )

    elif len(sys.argv) == 2:
        h = sys.argv[1]
        if herofinder(h):
            print(
                f"DotaBuffScrapping Done! Open countersByHero file to check {h}'s counters"
            )
        else:
            print("Error: Hero Not Found")

    else:
        print("Error: unknown hero")
