import pandas as pd

from config import DIRECTORY_FOR_SAVE_RESULT_FILE, DIRECTORY_FOR_SEARCH_XLS_FILES
from save_result_data import add_complex_chart, save_result_data
from services import processing_data, search_input_files


def main_func(type_processing: str, result_file_name: str, pump_name: str, file_names: list) -> str:
    '''Функция верхнего уровня, вызывающая необходимые функции'''
    if not file_names:
        file_names = search_input_files(DIRECTORY_FOR_SEARCH_XLS_FILES)
    result_file_name = result_file_name + '.xlsx'
    try:
        writer = pd.ExcelWriter(f'{DIRECTORY_FOR_SAVE_RESULT_FILE}\\{result_file_name}', engine='xlsxwriter')
    except PermissionError:
        return f'Необходимо закрыть файл {result_file_name}'
    for file_name in file_names:
        result = processing_data(type_processing, file_name, pump_name)
        file_name = file_name.replace('.xls', '')
        save_result_data(writer, file_name, type_processing, result)
    add_complex_chart(writer, type_processing)
    writer.close()
    return 'OK'
