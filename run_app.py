import os
from sys import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if platform == 'win32':
    os.system(
        f'cd {BASE_DIR} &\
        {BASE_DIR}\\env\\Scripts\\activate &\
        cd {BASE_DIR}\\app &\
        python {BASE_DIR}\\app\\gui_to_processing.py'
    )
elif platform == 'linux':
    os.system(
        f'cd {BASE_DIR} &\
        {BASE_DIR}/env/bin/activate &\
        cd {BASE_DIR}/app &\
        python {BASE_DIR}/app/gui_to_processing.py'
    )
