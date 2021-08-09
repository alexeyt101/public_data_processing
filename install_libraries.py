import os
from sys import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if platform == 'win32':
    os.system(
        f'cd {BASE_DIR} &\
        python -m venv env &\
        {BASE_DIR}\\env\\Scripts\\activate &\
        pip install -r {BASE_DIR}\\requirements.txt'
    )
elif platform == 'linux':
    os.system(
        f'cd {BASE_DIR} &\
        python -m venv env &\
        source {BASE_DIR}/env/bin/activate &\
        pip install -r {BASE_DIR}/requirements.txt'
    )
else:
    print('Ваша операционная система не распознана, выполните инициализацию виртуального окружения и установку библиотек вручную')
