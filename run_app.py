import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.system(
    f'cd {BASE_DIR} &\
    {BASE_DIR}\\env\\Scripts\\activate &\
    cd {BASE_DIR}\\app &\
    python {BASE_DIR}\\app\\gui_to_processing.py'
)
