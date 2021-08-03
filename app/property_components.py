from typing import Union

import numpy as np

'''
Свойства керосина ТС-1 по данным Дубовкина

'''

ProjectType = Union[float, np.ndarray]


def density(t: ProjectType) -> ProjectType:
    '''Функция возвращает плотность керосина при температуре t [C]'''
    return -0.72000 * t + 794


def kinematic_visc(t: ProjectType) -> ProjectType:
    '''Функция возвращает значение кинематической вязкости при температуре t [C]'''
    return 1E-08 * t ** 4 - 4E-06 * t ** 3 + 0.0005 * t ** 2 - 0.0374 * t + 1.888


def dynamic_visc(t: ProjectType) -> ProjectType:
    '''Функция возвращает значение динамической вязкости при температуре t [C]'''
    return -0.0000010764 * t ** 3 + 0.0002723512 * t ** 2 - 0.0274593254 * t + 1.4972619048


def vap_press(t: ProjectType) -> ProjectType:
    '''Функция возвращает значение давления насыщенных паров при температуре t [C]'''
    return (0.000000001581368 * t ** 4 - 0.000000078430240 * t ** 3 + 0.000013698229167 * t ** 2 -
            0.000081065945138 * t + 0.005731999998965)
