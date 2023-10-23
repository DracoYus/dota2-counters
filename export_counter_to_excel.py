import config
from utils import read_from_pickle, translate_hero, name_norm
import pandas as pd

counter_data = read_from_pickle(config.counter_pickle_file_name)

counter_data = {
    "name": [item["name"] for item in counter_data],
    "counter1": [item["counters"][0] for item in counter_data],
    "counter2": [item["counters"][1] for item in counter_data],
    "counter3": [item["counters"][2] for item in counter_data],
    "counter4": [item["counters"][3] for item in counter_data],
    "counter5": [item["counters"][4] for item in counter_data],
}
df = pd.DataFrame(counter_data)
df = df.map(lambda name: translate_hero(name_norm(name)))
df.to_excel(config.counter_excel, index=False)
