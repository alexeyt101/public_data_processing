"""Модуль графического пользовательского интерфейса."""
import os
from typing import Callable, List, Literal, Union

from tkinter import BOTH, Button, Entry, Frame, Label, PhotoImage, Radiobutton, Tk, Variable
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox, Style

from main import main_func as processing_func
from pump_config import PUMP_INLET_SIZE

StateType = Union[Literal['active'], Literal['disabled']]


class App(Frame):
    """Класс, в котором определяется поведение GUI."""

    def __init__(self, parent: Tk) -> None:
        """
        Функция инициализации класса GUI.

        parent: класс, от которого наследуется GUI
        """
        Frame.__init__(self, parent, background='#BBD8E9')
        self.parent = parent
        self.photo = PhotoImage(file='icon.png')

        self.selected_type_processing = Variable()
        self.selected_input_files = Variable()
        self.file_names: List[str] = []

        self.init_ui()
        self.create_gui_label('Выберите вид обработки', 20, 10)
        self.create_radiobutton(
            'Напорные характеристики',
            'Напор',
            self.selected_type_processing,
            self.change_state_combobox,
            40, 50,
        )
        self.create_radiobutton(
            'Кавитационные характеристики',
            'Кавитация',
            self.selected_type_processing,
            self.change_state_combobox,
            40, 80,
        )
        self.create_combobox(45, 120)
        self.create_gui_label('Выберите файлы исходных данных', 20, 150)
        self.create_radiobutton(
            'Все доступные файлы',
            1,
            self.selected_input_files,
            self.change_state_brows_button,
            40, 190,
        )
        self.create_radiobutton(
            'Выбрать вручную',
            2,
            self.selected_input_files,
            self.change_state_brows_button,
            40, 220,
        )
        self.create_brows_button('Обзор', 10, 'disabled', 220, 220)
        self.create_gui_label('Введите имя файла результатов', 20, 260)
        self.create_result_file_name(40, 310)
        self.create_start_button('Начать обработку', 25, 60, 350)

    def init_ui(self) -> None:
        """Метод, который инициирует заголовок, иконку и внешний вид окна GUI."""
        self.parent.title('Обработка данных эксперимента')
        self.parent.iconphoto(False, self.photo)
        self.parent.geometry('340x400+100+100')
        self.parent.resizable(False, False)

        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        self.style.theme_use('alt')

    def create_gui_label(self, text: str, coord_x: int, coord_y: int) -> None:
        """
        Метод, который объявляет виджет Label.

        text: текст внутри виджета
        coord_x: координата по ширине
        coord_y: координата по высоте
        """
        self.label = Label(
            self.parent,
            text=text,
            bg='#BBD8E9',
            width=30, height=2,
            font=('Arial', 12, 'bold'),
        )
        self.label.place(x=coord_x, y=coord_y)

    def create_radiobutton(self, text: str, value: Union[int, str], selected_var: Variable,
                           command: Callable, coord_x: int, coord_y: int) -> None:
        """
        Метод, который объявляет виджет Radiobutton.

        text: текст внутри виджета
        value: значение соответствующее каждой из кнопок
        selected_var: выбранное положение
        command: действие, которое выполняется при нажатии какой-то кнопки
        coord_x: координата по ширине
        coord_y: координата по высоте
        """
        Radiobutton(
            self.parent,
            text=text,
            bg='#BBD8E9',
            value=value,
            font=('Arial', 12),
            width=25, height=1,
            anchor='w',
            variable=selected_var,
            command=command,
        ).place(x=coord_x, y=coord_y)

    def create_combobox(self, coord_x: int, coord_y: int) -> None:
        """
        Метод, который объявляет виджет Combobox.

        coord_x: координата по ширине
        coord_y: координата по высоте
        """
        self.pump_list = Combobox(
            self.parent,
            values=tuple(PUMP_INLET_SIZE.keys()),
            font=('Arial', 12),
            state='disabled',
            width=25,
        )
        self.pump_list.place(x=coord_x, y=coord_y)

    def create_brows_button(self, text: str, width: int, state: StateType, coord_x: int, coord_y: int) -> None:
        """
        Метод, который объявляет виджет Button для выбора файлов исходных данных.

        text: текст внутри виджета
        width: ширина
        state: статус кнопки (активна/неактивна)
        coord_x: координата по ширине
        coord_y: координата по высоте
        """
        self.brows = Button(
            self.parent,
            text=text,
            width=width, height=1,
            font=('Arial', 12),
            state=state,
            command=self.create_brows_files,
        )
        self.brows.place(x=coord_x, y=coord_y)

    def create_start_button(self, text: str, width: int, coord_x: int, coord_y: int) -> None:
        """
        Метод, который объявляет виджет Button для начала обработки.

        text: текст внутри виджета
        width: ширина
        coord_x: координата по ширине
        coord_y: координата по высоте
        """
        self.start = Button(
            self.parent,
            text=text,
            width=width, height=1,
            font=('Arial', 12),
            state='active',
            command=self.start_processing,
        )
        self.start.place(x=coord_x, y=coord_y)

    def create_result_file_name(self, coord_x: int, coord_y: int) -> None:
        """
        Метод, который объявляет виджет Entry для ввода имени файла результатов.

        coord_x: координата по ширине
        coord_y: координата по высоте
        """
        self.entry_res = Entry(
            self.parent,
            width=30,
            font=('Arial', 12),
        )
        self.entry_res.insert(0, 'Result file')
        self.entry_res.place(x=coord_x, y=coord_y)

    def change_state_combobox(self) -> None:
        """Метод, который определяет состояние Combobox с наименованиями агрегатов."""
        if self.selected_type_processing.get() == 'Кавитация':
            self.pump_list['state'] = 'readonly'
        else:
            self.pump_list['state'] = 'disabled'

    def change_state_brows_button(self) -> None:
        """Метод, который определяет состояние Button "Обзор"."""
        if self.selected_input_files.get() == 2:
            self.brows['state'] = 'active'
        else:
            self.brows['state'] = 'disabled'
            self.file_names = []

    def create_brows_files(self) -> None:
        """Метод, который формирует список с названиями файлов исходных данных при ручном выборе."""
        init_dir = os.path.dirname(os.path.abspath(__file__)).replace('app', 'input_data')
        file_abspaths = filedialog.askopenfilenames(initialdir=init_dir)
        self.file_names = []
        for file_abspath in file_abspaths:
            file_name = file_abspath.split('/')[-1]
            self.file_names.append(file_name)

    def get_entry(self) -> str:
        """Метод, который возвращает название файла результатов."""
        if self.entry_res.get():
            return self.entry_res.get()
        else:
            messagebox.showinfo('Элитная прога', 'Введите имя файла для сохранения результатов')
            raise ValueError('Необходимо указать имя файла результатов')

    def start_processing(self) -> None:
        """Метод, который осуществляет вызов функции обработки."""
        type_processing = self.selected_type_processing.get()
        output_file_name = self.get_entry()
        processing_pump_name = self.pump_list.get()
        file_names = self.file_names

        if not type_processing:
            messagebox.showinfo('Элитная прога',
                                'Необходимо выбрать тип обработки')
            raise ValueError('Необходимо выбрать тип обработки')
        if not self.pump_list.get() and self.selected_type_processing.get() == 'Кавитация':
            messagebox.showinfo('Элитная прога',
                                'Для обработки кавитационных испытаний необходимо выбрать тип агрегата')
            raise ValueError('Для обработки кавитационных испытаний необходимо выбрать тип агрегата')
        if not self.selected_input_files.get():
            messagebox.showinfo('Элитная прога',
                                'Необходимо выбрать источник исходных данных')
            raise ValueError('Необходимо выбрать источник исходных данных')

        result = processing_func(type_processing, output_file_name, processing_pump_name, file_names)
        if result != 'OK':
            messagebox.showinfo('Элитная прога', result)
            return
        messagebox.showinfo('Элитная прога', 'Обработка завершена')


def main_func() -> None:
    """Основная функция, которая запускает приложение."""
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main_func()
