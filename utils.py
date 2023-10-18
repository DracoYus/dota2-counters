import pickle
import config


def write_list_to_file(list, filename):
    with open(filename, "w") as f:
        for item in list:
            f.write(item + "\n")


def read_list_from_file(filename):
    return_list = list()
    with open(filename, "r") as f:
        for line in f:
            return_list.append(line.strip())
    return return_list


def write_to_pickle(obj, file_name):
    with open(file_name, "wb") as f:
        pickle.dump(obj, f)


def read_from_pickle(file_name):
    loaded_data = None
    with open(file_name, "rb") as f:
        loaded_data = pickle.load(f)
    return loaded_data


def name_norm(name):
    return name.lower().replace("-", " ").replace("'", "")


def read_translation_from_file(file_name):
    return_dict = dict()
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            key = line.split(",")[0]
            value = line.split(",")[1]
            return_dict[key] = value
    return return_dict


def translate_name(name):
    global translate_dict
    translate_dict = read_translation_from_file(config.translation_file_name)
    return translate_dict[name]
