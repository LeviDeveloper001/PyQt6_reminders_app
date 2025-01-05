from PyQt6.uic import *
import sys

UI_DIR = sys.path[0]+'\\'
PY_DIR = '\\'.join(sys.path[0].split('\\')[:-1]) + '\\ui\\'

def ui_to_py(ui_name:str, py_name:str=None, mode='w'):
    ui_allowed_end = ui_name.endswith('.ui')
    py_allowed_end = py_name.endswith('.py') if isinstance(py_name, str) else False
    
    if not ui_allowed_end:
        ui_name = ui_name + '.ui'
    if not isinstance(py_name, str):
        py_name=''.join(list(ui_name)[:-3])+'.py'
    elif not py_allowed_end:
        py_name+='.py'
        
    with open(PY_DIR+py_name, mode=mode, encoding='utf-8') as py_file: 
        compile_ui.compileUi(UI_DIR+ui_name, py_file)
        
ui_to_py('task_widget')
ui_to_py('main_window')
