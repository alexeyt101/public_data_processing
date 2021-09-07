from typing import Dict, List, Union

ColumnsParamType = Dict[str, Dict[str, List[str]]]
GraphLocationType = Dict[str, Dict[str, str]]
AxisParamType = Dict[str, Dict[str, Dict[str, Dict[str, Union[str, Dict[str, Union[str, float]]]]]]]

'''Размер результирующих графиков'''
CHART_SIZE: Dict[str, int] = {
        'width': 720,
        'height': 400
                }

'''Стиль результирующих графиков'''
CHART_STYLE: int = 2

'''Обозначение колонок с параметрами для графиков'''
PARAM_COLUMNS: ColumnsParamType = {
        'Напор': {
                'Перепад': ['$E$2:$E$100', '$F$2:$F$100'],
                'Мощность': ['$E$2:$E$100', '$H$2:$H$100'],
                'КПД': ['$E$2:$E$100', '$I$2:$I$100'],
                'Н/n2': ['$J$2:$J$100', '$K$2:$K$100'],
                'N/n3': ['$J$2:$J$100', '$L$2:$L$100'],
                'КПД_Q/n': ['$J$2:$J$100', '$I$2:$I$100'],
        },
        'Кавитация': {
                'Напор': ['$G$2:$G$100', '$J$2:$J$100'],
                'Н/n2': ['$R$2:$R$100', '$P$2:$P$100'],
                'N/n3': ['$R$2:$R$100', '$Q$2:$Q$100'],
                'КПД': ['$R$2:$R$100', '$L$2:$L$100'],
        },
}

'''Размещение графиков на листе'''
GRAPH_LOCATIONS: GraphLocationType = {
    'Напор': {
        'Перепад': 'M2',
        'Мощность': 'M17',
        'КПД': 'M32',
        'Н/n2': 'S2',
        'N/n3': 'S17',
        'КПД_Q/n': 'S32',
    },
    'Кавитация': {
        'Напор': 'T2',
        'Н/n2': 'AB2',
    },
    'Сводные': {
        'Н/n2': 'B2',
        'N/n3': 'N2',
        'КПД_Q/n': 'B23',
        'КПД': 'B23',
    }
}

"""Параметры осей для графиков"""
AXISES_PARAM: AxisParamType = {
        'Напор': {
                'Перепад': {
                    'x': {
                        'name': 'Объемный расход, л/ч',
                        'params': {'num_format': '0.0'},
                    },
                    'y': {
                        'name': 'Перепад давления, кгс/см2',
                        'params': {'num_format': '0.0'},
                    },
                },
                'Мощность': {
                    'x': {
                        'name': 'Объемный расход, л/ч',
                        'params': {'num_format': '0.0'},
                    },
                    'y': {
                        'name': 'Мощность насоса, Вт',
                        'params': {'num_format': '0.0'},
                    },
                },
                'КПД': {
                    'x': {
                        'name': 'Объемный расход, л/ч',
                        'params': {'num_format': '0.0'},
                    },
                    'y': {
                        'name': 'КПД',
                        'params': {'num_format': '0.0'},
                    },
                },
                'Н/n2': {
                    'x': {
                        'name': 'Q/n, л·мин/ч',
                        'params': {'num_format': '0.0'},
                    },
                    'y': {
                        'name': 'Н/n2, м·мин2',
                        'params': {'num_format': '0.0E+00'},
                    },
                },
                'N/n3': {
                    'x': {
                        'name': 'Q/n, л·мин/ч',
                        'params': {'num_format': '0.0'},
                    },
                    'y': {
                        'name': 'N/n3, Вт·мин3',
                        'params': {'num_format': '0.0E+00'},
                    },
                },
                'КПД_Q/n': {
                    'x': {
                        'name': 'Q/n, л·мин/ч',
                        'params': {'num_format': '0.0'},
                    },
                    'y': {
                        'name': 'Н/n2, м·мин2',
                        'params': {'num_format': '0.0'},
                    }
                },
        },
        'Кавитация': {
                'Напор': {
                    'x': {
                        'name': 'Pвх - Рп, ата',
                        'params': {'major_unit': 0.1},
                    },
                    'y': {
                        'name': 'Напор насоса, м',
                        'params': {'num_format': '0.0'},
                    },
                },
                'Н/n2': {
                    'x': {
                        'name': 'dh/n2, м·мин',
                        'params': {'num_format': '0.0E+00'},
                    },
                    'y': {
                        'name': 'Н/n2, м·мин2',
                        'params': {'num_format': '0.0E+00'},
                    },
                },
                'N/n3': {
                    'x': {
                        'name': 'dh/n2, м·мин',
                        'params': {'num_format': '0.0E+00'},
                    },
                    'y': {
                        'name': 'N/n3, Вт·мин3',
                        'params': {'num_format': '0.0E+00'},
                    },
                },
                'КПД': {
                    'x': {
                        'name': 'dh/n2, м·мин',
                        'params': {'num_format': '0.0E+00'},
                    },
                    'y': {
                        'name': 'КПД',
                        'params': {'num_format': '0.0'},
                    },
                },
        },
}