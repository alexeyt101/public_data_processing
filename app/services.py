import os

import pandas as pd
import numpy as np

import config as config
from formulas_for_calculating_pupms_parameters import head, q_n, h_n2, n_n3, kpd, speed_on_inlet, dh, dh_n2, c_kr
from property_components import density, vap_press
from pump_config import PUMP_INLET_SIZE
from read_experimental_data import read_experimantal_data


def search_input_files(directory: str) -> list:
    """
    Функция, которая производит поиск файлов с исходными данными в директории

    """
    xls_files_names = []
    directory_files = os.listdir(directory)
    for file_ in directory_files:
        xls_files_names.append(file_)
    return xls_files_names


def processing_data(type_processing: str, file_name: str, lable_agr: str) -> pd.DataFrame:
    '''
    Функция, которая производит обработку результатов из файла исходных данных.
    Принимает на вход название файла, тип обработки (напорки или кавитация), наименование агрегата и возвращает
    DataFrame с параметрами, готовыми к записыванию в файл результатов.

    '''

    file_2 = read_experimantal_data(file_name)
    Q_array = np.array(file_2['Подача мал, л/ч'])
    if Q_array[0] < 50:
        Q_array = np.array(file_2['Подача бол, л/ч'])
    dp_array = np.array(file_2['Перепад, кгс/см2'])
    if type_processing == 'Кавитация':
        d_0 = PUMP_INLET_SIZE[lable_agr]['D0']
        d_vt = PUMP_INLET_SIZE[lable_agr]['d_vt']
        P_vh_array = np.array(file_2['Р вход, кгс/см2'])
    T_vh_array = np.array(file_2['t вход, ºС'])
    n_array = np.array(file_2['Частота вращения, об/мин'])
    T_vih_array = np.array(file_2['t выход, ºС'])
    Power_array = np.array(file_2['Мощность, кВт']) * 1000

    del file_2

    density_array_all = density(np.mean([T_vh_array, T_vih_array], axis=0))
    head_array_all = head(dp_array, density_array_all)
    q_n_array_all = q_n(Q_array, n_array)
    h_n2_array_all = h_n2(head_array_all, n_array)
    n_n3_array_all = n_n3(Power_array, n_array)
    kpd_array_all = kpd(dp_array, Q_array, Power_array)
    if type_processing == 'Кавитация':
        vel_in_array_all = speed_on_inlet(d_0, d_vt, Q_array)
        vap_press_array = vap_press(T_vih_array)
        dh_array_all = dh(P_vh_array, vap_press_array, density_array_all, vel_in_array_all)
        dh_n2_array_all = dh_n2(dh_array_all, n_array)
        c_kr_array_all = c_kr(n_array, Q_array, dh_array_all)
        p_vh_p_vap_array_all = P_vh_array - vap_press_array

    output_data = [
        T_vih_array, density_array_all, n_array, Q_array, dp_array, head_array_all,
        Power_array, kpd_array_all, q_n_array_all, h_n2_array_all, n_n3_array_all,
                    ]
    output_columns = config.head_output_columns
    if type_processing == 'Кавитация':
        output_data = [
            T_vih_array, density_array_all, n_array, P_vh_array, vap_press_array, p_vh_p_vap_array_all,
            Q_array, dp_array, head_array_all, Power_array, kpd_array_all, vel_in_array_all, dh_array_all,
            q_n_array_all, h_n2_array_all, n_n3_array_all, dh_n2_array_all, c_kr_array_all
                        ]
        output_columns = config.cavitation_output_columns

    processed_dataframe = pd.DataFrame(np.array(output_data).T, columns=output_columns)

    return processed_dataframe
