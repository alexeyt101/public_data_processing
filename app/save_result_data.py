from typing import Dict

from pandas.core.frame import DataFrame
from pandas.io.excel._xlsxwriter import XlsxWriter
from xlsxwriter.workbook import Workbook, Worksheet

from graphs_config import AXISES_PARAM, CHART_SIZE, CHART_STYLE, GRAPH_LOCATIONS, PARAM_COLUMNS


def add_chart_settings(name: str, major_unit: float = 0, num_format: str = '') -> Dict:
    '''Функци, которая формирует словарь параметров для графиков'''

    chart_config = {
        'name': name,
        'name_font': {
            'name': 'Times New Roman',
            'size': 14,
            'bold': False
                        },
        'num_font': {
            'name': 'Times New Roman',
            'size': 14,
            'bold': False
                        },
        'major_gridlines': {
            'visible': True
                        },
        }
    if major_unit:
        chart_config['major_unit'] = major_unit
    if num_format:
        chart_config['num_format'] = num_format
    return chart_config


def get_legend_settings(font_size: int = 14, position: str = 'bottom') -> Dict:
    '''Функция, которая возращает словарь параметров для легенды графика'''

    settings = {
        'position': position,
        'font': {
            'name': 'Times New Roman',
            'size': font_size,
            'bold': False
                        },
    }
    return settings


def set_graph_settings(graphs_list: list, graph_size: bool = False, legend: bool = False) -> None:
    '''Функция, которая настраивает стиль, заголовок, легенду и размер графиков'''
    for graph in graphs_list:
        graph.set_style(CHART_STYLE)
        graph.set_title({'none': True})
        if legend and graph_size:
            graph.set_size(CHART_SIZE)
            graph.set_legend(get_legend_settings())
        else:
            graph.set_legend({'none': True})


def set_axises_settings(type_processing: str, graphs_list: list, graph_names: list) -> None:
    '''Функция, которая настраивает названия осей на графиках, а также другие параметры форматирования'''
    for graph, graph_name in zip(graphs_list, graph_names):
        x_axis_name = AXISES_PARAM[type_processing][graph_name]['x']['name']
        x_axis_params = AXISES_PARAM[type_processing][graph_name]['x']['params']
        y_axis_name = AXISES_PARAM[type_processing][graph_name]['y']['name']
        y_axis_params = AXISES_PARAM[type_processing][graph_name]['y']['params']
        graph.set_x_axis(add_chart_settings(x_axis_name, **x_axis_params))
        graph.set_y_axis(add_chart_settings(y_axis_name, **y_axis_params))


def get_chart_dict(sheet_name: str, x_values: str, y_values: str) -> Dict:
    '''Функция, которая заполняет словарь параметров для добавления данных на график'''
    chart_series_dict = {
        'name': sheet_name,
        'categories': f"='{sheet_name}'!{x_values}",
        'values': f"='{sheet_name}'!{y_values}",
        'marker': {'type': 'automatic', 'size': 5}
                            }
    return chart_series_dict


def add_series_to_chart(type_processing: str, graphs_list: list, graph_names: list, sheet_name: str) -> None:
    '''Функция, которая добавляет данные со страницы Excel документа на график'''
    for graph, graph_name in zip(graphs_list, graph_names):
        graph.add_series(
            get_chart_dict(sheet_name, *PARAM_COLUMNS[type_processing][graph_name])
        )


def insert_graph(worksheet: Worksheet, type_processing: str,
                 graphs_list: list, graphs_names: list, graph_of_all: bool = False) -> None:
    '''Функция, которая производит размещение графиков на листе в Excel документе'''
    for graph, graph_name in zip(graphs_list, graphs_names):
        if not graph_of_all:
            graph_location = GRAPH_LOCATIONS[type_processing][graph_name]
        else:
            graph_location = GRAPH_LOCATIONS['Сводные'][graph_name]
        worksheet.insert_chart(graph_location, graph)


def add_chart_to_worksheet(workbook: Workbook, worksheet: Worksheet, type_processing: str) -> None:
    '''Функция, которая на основе данных, записанных в эксель, строит графики и размещает их странице'''

    sheet_name = worksheet.get_name()

    if type_processing == 'Напор':
        """ Графики для напорных характеристик """

        head_chart = workbook.add_chart({'type': 'scatter'})
        power_chart = workbook.add_chart({'type': 'scatter'})
        kpd_chart = workbook.add_chart({'type': 'scatter'})
        h_n2_chart = workbook.add_chart({'type': 'scatter'})
        N_n3_chart = workbook.add_chart({'type': 'scatter'})
        kpd_Qn_chart = workbook.add_chart({'type': 'scatter'})

        graphs = [head_chart, power_chart, kpd_chart, h_n2_chart, N_n3_chart, kpd_Qn_chart]
        graphs_names = ['Перепад', 'Мощность', 'КПД', 'Н/n2', 'N/n3', 'КПД_Q/n']

        add_series_to_chart(type_processing, graphs, graphs_names, sheet_name)
        set_graph_settings(graphs)
        set_axises_settings(type_processing, graphs, graphs_names)
        insert_graph(worksheet, type_processing, graphs, graphs_names)

    else:
        """ Графики для кавитационных характеристик """
        H_pvh_chart = workbook.add_chart({'type': 'scatter'})
        H_dh_chart = workbook.add_chart({'type': 'scatter'})

        graphs = [H_pvh_chart, H_dh_chart]
        graphs_names = ['Напор', 'Н/n2']

        add_series_to_chart(type_processing, graphs, graphs_names, sheet_name)
        set_graph_settings(graphs)
        set_axises_settings(type_processing, graphs, graphs_names)
        insert_graph(worksheet, type_processing, graphs, graphs_names)


def add_complex_chart(writer: XlsxWriter, type_processing: str) -> None:
    """ Функция, которая стоит сводные графики по серии испытаний на основе обработанных данных """

    workbook = writer.book
    worksheets = workbook.worksheets()
    all_data_chart_worksheet = workbook.add_worksheet('Сводные графики')

    head_chart_all = workbook.add_chart({'type': 'scatter'})
    power_chart_all = workbook.add_chart({'type': 'scatter'})
    kpd_chart_all = workbook.add_chart({'type': 'scatter'})

    graphs = [head_chart_all, power_chart_all, kpd_chart_all]

    set_graph_settings(graphs, graph_size=True, legend=True)

    if type_processing == 'Напор':
        graphs_names = ['Н/n2', 'N/n3', 'КПД_Q/n']
        for worksheet in worksheets:
            sheet_name = worksheet.get_name()
            if sheet_name == 'Сводные графики':
                break
            add_series_to_chart(type_processing, graphs, graphs_names, sheet_name)
            set_axises_settings(type_processing, graphs, graphs_names)
    else:
        graphs_names = ['Н/n2', 'N/n3', 'КПД']
        for worksheet in worksheets:
            sheet_name = worksheet.get_name()
            if sheet_name == 'Сводные графики':
                break
            add_series_to_chart(type_processing, graphs, graphs_names, sheet_name)
            set_axises_settings(type_processing, graphs, graphs_names)

    insert_graph(all_data_chart_worksheet, type_processing, graphs, graphs_names, graph_of_all=True)


def save_result_data(writer: XlsxWriter, sheet_name: str, type_processing: str, result_data: DataFrame) -> None:
    '''Функция, которая сохраняет обработанные данные в exel-файл'''
    result_data.to_excel(writer, sheet_name=sheet_name, startrow=1, header=False)
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    header_format = workbook.add_format({
                                        'bold': True,
                                        'text_wrap': True,
                                        'valign': 'top',
                                        'fg_color': '#D7E4BC',
                                        'border': 1
                                        })
    header_format.set_align('center')
    header_format.set_align('vcenter')
    worksheet.set_column('A:P', 13)
    for col_num, value in enumerate(result_data.columns.values):
        worksheet.write(0, col_num + 1, value, header_format)
    add_chart_to_worksheet(workbook, worksheet, type_processing)
