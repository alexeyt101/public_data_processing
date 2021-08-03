import pandas as pd
from pandas.core.frame import DataFrame

import config


def search_experimental_data(input_data: DataFrame) -> DataFrame:
    '''Функция, которая осуществляет поиск и фильтрацию экспериментальных данных'''
    column_drop_num = input_data.columns[input_data.isin(['Подача Мир 50, л/ч']).any()].tolist()[0]
    input_data = input_data.drop(columns=range(column_drop_num))
    for row in input_data.index:
        if input_data.loc[row].hasnans:
            input_data = input_data.drop(index=row)
    labels = input_data.loc[1]
    input_data = input_data.drop(index=1)
    input_data.columns = labels
    input_data = input_data.stack().str.replace(',', '.').unstack()
    input_data = input_data.apply(pd.to_numeric)
    return input_data


def read_experimantal_data(file_name: str) -> DataFrame:
    '''
    Функция, которая считывает данные из файла испытаний и подготовливает
    DataFrame для дальнейшей обработки

    '''
    abs_path_to_file = f'{config.DIRECTORY_FOR_SEARCH_XLS_FILES}\\{file_name}'
    input_data = pd.read_excel(abs_path_to_file, header=None).T
    input_data = search_experimental_data(input_data)
    if input_data.empty:
        print('Исходные данные не найдены')
        return False
    return input_data
