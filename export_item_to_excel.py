from utils import read_from_pickle, match_norm, translate_item, winrate_norm
import config

item_data = read_from_pickle(config.item_file_name)
result = list()

for hero in item_data[:1]:
    hero_result = dict()
    hero_result["strong"] = list()
    hero_result["popular"] = list()
    hero_result["potential"] = list()
    hero_result["weak"] = list()
    match_size = match_norm(hero["item"][0]["match"])
    base_winrate = winrate_norm(hero["item"][0]["winRate"])
    for item in hero["item"]:
        item_name = translate_item(item["itemName"])
        item_winrate = winrate_norm(item["winRate"])
        item_match = match_norm(item["match"])
        if item_name == None:
            continue
        if item_winrate >= base_winrate:
            if (item_match / match_size) > config.match_threshold:
                hero_result["strong"].append(
                    {"name": item_name, "winrate": item_winrate, "match": item_match}
                )
            else:
                hero_result["potential"].append(
                    {"name": item_name, "winrate": item_winrate, "match": item_match}
                )
        else:
            if (item_match / match_size) > config.match_threshold:
                hero_result["popular"].append(
                    {"name": item_name, "winrate": item_winrate, "match": item_match}
                )
            else:
                hero_result["weak"].append(
                    {"name": item_name, "winrate": item_winrate, "match": item_match}
                )
    print(hero_result)
