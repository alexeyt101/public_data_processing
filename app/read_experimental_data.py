"""Модуль считывания данных из файла."""
import pandas as pd

import config


def search_experimental_data(input_data: pd.DataFrame) -> pd.DataFrame:
    """Функция, которая осуществляет поиск и фильтрацию экспериментальных данных."""
    column_drop_num = input_data.columns[input_data.isin(['Подача бол, л/ч']).any()].tolist()[0]
    input_data = input_data.drop(columns=range(column_drop_num))
    for row in input_data.index:
        if input_data.loc[row].hasnans:
            input_data = input_data.drop(index=row)
    labels = input_data.loc[1]
    input_data = input_data.drop(index=1)
    input_data.columns = labels
    try:
        input_data = input_data.stack().str.replace(',', '.').unstack()
    except AttributeError:
        pass
    input_data = input_data.apply(pd.to_numeric)
    return input_data


def read_experimantal_data(file_name: str) -> pd.DataFrame:
    """Функция считывает и подготавливает данные испытаний."""
    abs_path_to_file = f'{config.DIRECTORY_FOR_SEARCH_XLS_FILES}\\{file_name}'
    input_data = pd.read_excel(abs_path_to_file, header=None).T
    input_data = search_experimental_data(input_data)
    if input_data.empty:
        print('Исходные данные не найдены')
        return False
    return input_data
