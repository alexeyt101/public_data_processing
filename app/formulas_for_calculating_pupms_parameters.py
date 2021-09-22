"""Модуль с формулами для расчета параметров насоса."""
from typing import Union

import numpy as np

ParamTypes = Union[float, np.ndarray]


def head(dp: ParamTypes, ro_fluid: ParamTypes) -> ParamTypes:
    """
    Функция, которая расчитывает напор насоса.

    dp: перепад давления [кгс/см2]
    ro_fluid: плотность [кг/м3]
    """
    return dp * 98066.5 / ro_fluid / 9.80665


def q_n(volume_flow: ParamTypes, rot_speed: ParamTypes) -> ParamTypes:
    """
    Функция, возвращающая значение параметра Q/n.

    volume_flow: объемный расход [л/ч]
    rot_speed: частота вращения [об/мин]
    """
    return volume_flow / rot_speed


def h_n2(head: ParamTypes, rot_speed: ParamTypes) -> ParamTypes:
    """
    Функция, возвращающая значение параметра H/n2.

    head: напор насоса [м]
    rot_speed: частота вращения [об/мин]
    """
    return head / (rot_speed ** 2)


def n_n3(power: ParamTypes, rot_speed: ParamTypes) -> ParamTypes:
    """
    Фукнция, возвращающая значение параметра N/n3.

    power: потребляемая мощность [Вт]
    rot_speed: частота вращения [об/мин]
    """
    return power / (rot_speed ** 3)


def kpd(delta_press: ParamTypes, volume_flow: ParamTypes, power: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение КПД насоса.

    delta_press: перепад давления [кгс/см2]
    volume_flow: объемный расход [л/ч]
    power: потребляемая мощность [Вт]
    """
    return (volume_flow / 1000 / 3600) * delta_press * 98066.5 / power


def speed_on_inlet(diameter_1: float, diameter_vtulki: float, volume_flow: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение скорости потока на входе в насос [м/с].

    diameter_1: диаметр D1 [м]
    diameter_1: диаметр dвт [м]
    volume_flow: объемный расход [л/ч]
    """
    return ((volume_flow / 1000 / 3600) / ((3.14 * ((diameter_1 / 1000) ** 2) / 4) -
            - (3.14 * ((diameter_vtulki / 1000) ** 2) / 4)))


def dh(p_in: ParamTypes, vap_press: ParamTypes, ro_fluid: ParamTypes, speed_on_inlet: ParamTypes) -> ParamTypes:
    """
    Фукнкция возвращает значение кавитационного запаса [м].

    p_in: давление на входе в насос [ата]
    vap_press: давление насыщенных паров топлива [ата]
    ro_fluid: плотность [кг/м3]
    speed_on_inlet: скорость потока на входе в насос [м/с]
    """
    return (p_in - vap_press) / ro_fluid * 10 * 1000 + (speed_on_inlet ** 2) / (2 * 9.80655)


def dh_n2(delta_h: ParamTypes, rot_speed: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение параметра dh/n2.

    delta_h: кавитационный запас [м]
    rot_speed: частота вращения [об/мин]
    """
    return delta_h / (rot_speed ** 2)


def c_kr(rot_speed: ParamTypes, volume_flow: ParamTypes, delta_h: ParamTypes) -> ParamTypes:
    """
    Функция возвращает значение параметра Скр.

    rot_speed: частота вращения [об/мин]
    volume_flow: объемный расход [л/ч]
    delta_h: кавитационный запас [м]
    """
    return 5.65 * rot_speed * ((volume_flow / 1000 / 3600) ** 0.5) / ((delta_h) ** 0.75)
