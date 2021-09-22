"""Модуль для получения свойств рабочего тела (по Дубовкину)."""
from typing import Union

import numpy as np


ParamTypes = Union[float, np.ndarray]


def density(temp: ParamTypes) -> ParamTypes:
    """
    Функция возвращает плотность керосина.

    temp: температура [C]
    """
    return -0.72000 * temp + 794


def kinematic_visc(temp: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение кинематической вязкости.

    temp: температура [C]
    """
    return 1E-08 * temp ** 4 - 4E-06 * temp ** 3 + 0.0005 * temp ** 2 - 0.0374 * temp + 1.888


def dynamic_visc(temp: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение динамической вязкости.

    temp: температура [C]
    """
    return -0.0000010764 * temp ** 3 + 0.0002723512 * temp ** 2 - 0.0274593254 * temp + 1.4972619048


def vap_press(temp: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение давления насыщенных паров.

    temp: температура [C]
    """
    return (0.000000001581368 * temp ** 4 - 0.000000078430240 * temp ** 3 + 0.000013698229167 * temp ** 2 -
            - 0.000081065945138 * temp + 0.005731999998965)
