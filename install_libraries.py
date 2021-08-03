import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.system(
    f'cd {BASE_DIR} &\
    python -m venv env &\
    {BASE_DIR}\\env\\Scripts\\activate.bat &\
    pip install -r {BASE_DIR}\\requirements.txt'
)
input('Необходимые библиотеки установлены. Нажмите Enter')
