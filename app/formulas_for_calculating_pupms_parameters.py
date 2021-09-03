from typing import Union

import numpy as np

'''
Формулы для расчета параметров лопастного насоса

'''
ParamTypes = Union[float, np.ndarray]


def head(dp: ParamTypes, ro_fluid: ParamTypes) -> ParamTypes:
    '''
    Функция, которая расчитывает напор насоса на основе
    перепада давления [кгс/см2] и плотности [кг/м3]

    '''
    return dp * 98066.5 / ro_fluid / 9.80665


def q_n(Q: ParamTypes, n: ParamTypes) -> ParamTypes:
    '''Функция, возвращающая значение параметра Q/n'''
    return Q / n


def h_n2(H: ParamTypes, n: ParamTypes) -> ParamTypes:
    '''Функция, возвращающая значение параметра H/n2'''
    return H / (n ** 2)


def n_n3(N: ParamTypes, n: ParamTypes) -> ParamTypes:
    '''Фукнция, возвращающая значение параметра N/n3'''
    return N / (n ** 3)


def kpd(dp: ParamTypes, Q: ParamTypes, power: ParamTypes) -> ParamTypes:
    '''
    Функция возвращает значение КПД лопастного насоса, расчитанного
    по перепаду давления [кгс/см2], объемному расходу [л/ч], потребляемой
    мощности [Вт]

    '''
    return (Q / 1000 / 3600) * dp * 98066.5 / power


def speed_on_inlet(d1: float, d_vtulki: float, Q: ParamTypes) -> ParamTypes:
    '''
    Функция возвращает значение скорости потока на входе в насос [м/с],
    расчитанную по размерам колеса [мм] и объемному расходу [л/ч]

    '''
    return (Q / 1000 / 3600) / ((3.14 * ((d1 / 1000) ** 2) / 4) - (3.14 * ((d_vtulki / 1000) ** 2) / 4))


def dh(p_in: ParamTypes, vap_press: ParamTypes, ro_fluid: ParamTypes, speed_on_inlet: ParamTypes) -> ParamTypes:
    '''
    Фукнкция возвращает значение кавитационного запаса [м], который расчитывается
    на основе давления на входе в насос и давления насыщенных паров [кгс/см2],
    плотности рабочего тела [кг/м3], скорости потока на входе в насос [м/с]

    '''
    return (p_in - vap_press) / ro_fluid * 10 * 1000 + (speed_on_inlet ** 2) / (2 * 9.80655)


def dh_n2(dh: ParamTypes, n: ParamTypes) -> ParamTypes:
    '''Функция возвращает значение параметра dh/n2'''
    return dh / (n ** 2)


def c_kr(n: ParamTypes, Q: ParamTypes, dh: ParamTypes) -> ParamTypes:
    '''
    Функция возвращает значение параметра Скр, который расчитан на основе
    оборотов [об/мин], объемного расхода [л/ч], кавитационного запаса [м]

    '''
    return 5.65 * n * ((Q / 1000 / 3600) ** 0.5) / ((dh) ** 0.75)
