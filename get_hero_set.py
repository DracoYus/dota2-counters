import config
from utils import read_from_pickle, write_list_to_file, name_norm


counter_data = read_from_pickle(config.counter_pickle_file_name)
hero_set = set()

for hero in counter_data:
    hero_set.add(name_norm(hero["name"]) + ",")
    for counter_hero in hero["counters"]:
        hero_set.add(name_norm(counter_hero) + ",")

hero_set_list = list(hero_set)
hero_set_list.sort()

write_list_to_file(hero_set_list, config.hero_set_file_name)
