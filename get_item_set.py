from utils import read_from_pickle, write_list_to_file
import config


if __name__ == "__main__":
    item_set = set()
    item_data = read_from_pickle(config.item_file_name)
    for hero in item_data[:1]:
        for item in hero["item"]:
            item_name = item["itemName"]
            if not "Recipe" in item_name:
                item_set.add(item_name + ",")
    item_list = list(item_set)
    item_list.sort()
    write_list_to_file(item_list, "item_list.txt")
