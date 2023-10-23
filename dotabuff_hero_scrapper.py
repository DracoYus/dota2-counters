import requests
from bs4 import BeautifulSoup
import re
from utils import write_list_to_file
import config

url = "https://www.dotabuff.com/heroes"
response = requests.get(url, headers=config.headers, proxies=config.proxies)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, features="html.parser")
hero_grid = soup.find("div", class_="hero-grid")
hero_list = hero_grid.find_all("a", href=re.compile("/heroes/"))
hero_name_list = list()
for hero in hero_list:
    hero_name = hero["href"].split("/")[-1]
    hero_name_list.append(hero_name)

write_list_to_file(hero_name_list, config.hero_list_file_name)
