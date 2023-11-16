import json
from aiogram import types


class GSFunction:
    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path

    def open_file(self) -> json:
        with open(self.json_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # returns a list of all found pair key=value for the passed key
    def selecting_values_by_key(self, key: str) -> list[str]:
        return [item.get(key) for item in self.open_file() if item.get(key)]

    # returns a list of all dictionaries that contain the searched pair <key=value>
    def selecting_dicts_by_tuple(self, data: tuple) -> list[dict]:
        return [item for item in self.open_file() if item[data[0]] == data[1]]


# json converter for Google sheets (matrix)
def json_converter(matrix: list[list[str]]) -> list[dict]:
    id = 0
    data = []
    for num, values in enumerate(matrix):
        if not num:
            keys = ['id'] + values[:9]
            continue
        data.append(dict(zip(keys, [id] + values[:9])))
        id += 1
    return data


def unique_names(names: list | tuple | set) -> list:
    unique_names_list = []
    for name in names:
        if name not in unique_names_list:
            unique_names_list.append(name)
    return unique_names_list


def update_statistics(statistics_data: dict, section: str, callback: types.CallbackQuery) -> None:
    if statistics_data.get(section):
        statistics_data[section].append(callback.message.from_user.id)
    else:
        statistics_data[section] = [callback.message.from_user.id]
