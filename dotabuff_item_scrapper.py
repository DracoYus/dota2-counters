import requests
from bs4 import BeautifulSoup
from utils import read_list_from_file, write_to_pickle
import config
from constants import *
import time
from tqdm import tqdm


def get_html_text(url):
    global session
    session = requests.Session()
    response = session.get(url, headers=config.headers, proxies=config.proxies)
    response.encoding = "utf-8"
    return response


def parse_html(html):
    result = list()
    soup = BeautifulSoup(html.text, features="html.parser")
    table = soup.find("table", class_="sortable")
    for item in table.tbody.children:
        item_dict = dict()
        item_dict["itemName"] = item.contents[1].text.strip()
        item_dict["match"] = item.contents[2].text.strip()
        item_dict["winRate"] = item.contents[3].text.strip()
        result.append(item_dict)
    return result


if __name__ == "__main__":
    result = list()
    hero_list = read_list_from_file(config.hero_list_file_name)
    pbar = tqdm(hero_list)
    for hero in pbar:
        pbar.set_description(hero)
        url = BASE_URL + f"/heroes/{hero}/items"
        html = get_html_text(url, session)
        item_list = parse_html(html)
        result.append({"heroName": hero, "item": item_list})
        time.sleep(config.sleep_time)
    write_to_pickle(result, config.item_file_name)
