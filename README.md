# Data processor (public version)

## Описание
Приложение предназначено для автоматизации обработки экспериментальных данных, полученных при испытаниях шнекоцентробежных насосов, и состоит из двух основных частей: 
  1. Простой GUI для сотрудников, разработанный для сотрудников, которые не используют командную строку;
  2. Алгоритм обработки данных, включающий поиск начала данных в входном файле, отбор необходимых данных, вычисление результирующих параметров, сохранение результатов расчета в файл и построение графиков.

## Исходные данные и файл результатов
Приложение считывает предварительно форматированные файлы исходных данных в формате Excel-файл из папки input_data в корне проекта. Несколько файлов с синтетическими исходными данными вложены в указанную папку для демострации работы приложения. 
Результаты расчетов, а также графики сохраняются также в Excel-файл с пользовательским названием в корень проекта.

## Демо

<p align="center"><img  src="./readme_assets/demo.png" width="70%"></p>

## Технологии 
Проект разрабатывается на Python 3.8.3 с ипользованием:
    - **pandas**, **numpy** для обработки данных;
    - **thinker** для GUI;
    - **xlsxwriter** для взаимодействия с итоговым Excel-файлом

## Установка 
Выполните в терминале:
'''
git clone https://github.com/alexeyt101/public_data_processing.git
cd public_data_processing
python
'''
Далее для Windows :
'''
python install_libraries.py
python run_app.py
'''
Для Linux:
'''
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python run_app.py
'''

## P.S. 
В данный момент проект продолжает своё развитие, вносятся правки. В ближайшее время планируется добавление тестов. 