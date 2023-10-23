from utils import *
import config
import pandas as pd
from tqdm import tqdm


def parse_hero_item(hero):
    hero_result = dict()
    hero_result["name"] = hero["heroName"]
    hero_result["strong"] = list()
    hero_result["popular"] = list()
    hero_result["potential"] = list()
    hero_result["weak"] = list()
    base_match = match_norm(hero["item"][0]["match"])
    base_winrate = winrate_norm(hero["item"][0]["winRate"])
    for item in hero["item"]:
        item_name = translate_item(item["itemName"])
        item_winrate = winrate_norm(item["winRate"])
        item_match = match_norm(item["match"])
        item_pickrate = item_match / base_match
        if item_name == None:
            continue
        if item_pickrate < config.minimal_pickrate:
            continue
        hero_dict = {
            "name": item_name,
            "winRate": item_winrate,
            "match": item_match,
            "pickRate": round(item_pickrate * 100, 2),
        }
        if item_winrate >= base_winrate:
            if (item_match / base_match) > config.popular_threshold:
                hero_result["strong"].append(hero_dict)
            else:
                hero_result["potential"].append(hero_dict)
        else:
            if (item_match / base_match) > config.popular_threshold:
                hero_result["popular"].append(hero_dict)
            else:
                hero_result["weak"].append(hero_dict)
    hero_result["strong"].sort(key=lambda x: x["pickRate"], reverse=True)
    hero_result["popular"].sort(key=lambda x: x["pickRate"], reverse=True)
    hero_result["potential"].sort(key=lambda x: x["winRate"], reverse=True)
    hero_result["weak"].sort(key=lambda x: x["pickRate"], reverse=True)
    return hero_result


if __name__ == "__main__":
    item_data = read_from_pickle(config.item_file_name)
    result = list()

    for hero in tqdm(item_data):
        result.append(parse_hero_item(hero))
    result_df = {
        "name": [translate_hero(name_norm(hero["name"])) for hero in result],
        "strong": [
            ",".join([item["name"] for item in hero["strong"]]) for hero in result
        ],
        "popular": [
            ",".join([item["name"] for item in hero["popular"]]) for hero in result
        ],
        "potential": [
            ",".join([item["name"] for item in hero["potential"]]) for hero in result
        ],
        "weak": [",".join([item["name"] for item in hero["weak"]]) for hero in result],
    }
    df = pd.DataFrame(result_df)
    df.to_excel(config.item_excel, index=False)
