"""Модуль конфигураций насосов (размеров проточных частей)."""
from typing import Dict, Union

InletSizeType = Dict[str, Dict[str, Union[int, float]]]

"""Доступные для обработки кавитации насосы и размеры их проточных частей (в миллиметрах)"""
PUMP_INLET_SIZE: InletSizeType = {
    'Насос №1': {'D0': 60, 'd_vt': 20},
    'Насос №2': {'D0': 55, 'd_vt': 22},
}
