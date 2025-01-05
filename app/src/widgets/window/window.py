import datetime as dt

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout

from ui.main_window import Ui_MainWindow


from widgets.base.base_widget_mixins import BaseWidgetMixin
from states.window_states import WindowStateCollection
        
from widgets.tasks.task import TaskWidget


class Window(QMainWindow, BaseWidgetMixin):
    def __init__(self):
        super().__init__()
        self.__setup_all()
    
    def __setup_all(self):
        self.__setup_props()
        self.__setup_logic()
        
    def __setup_props(self):
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tasks_list_widget.setLayout(QVBoxLayout())
        self.state_collection = WindowStateCollection()
        self.state = self.state_collection.START
        self.__changed_task = None
    
    def __setup_logic(self):
        self.ui.delete_task_button.setDisabled(True)
        self.ui.add_task_button.setEnabled(True)
        self.add_click_connect(
            self.ui.add_task_button,
            lambda : self.on_add_task_button_click()
        )
    
    @property
    def changed_task(self):
        return self.__changed_task
    
    @changed_task.setter
    def changed_task(self, value):
        self.__changed_task = value
        self.ui.delete_task_button.setEnabled(True)
        
        
    def on_add_task_button_click(self, ):
        _tasks_list_widget = self.ui.tasks_list_widget
        task_widget = TaskWidget(_tasks_list_widget)
        task_widget.ui.task_date_label.setText(
            dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        )
        _tasks_list_widget.layout().addWidget(task_widget)
        self.changed_task = task_widget
        print(self.changed_task)
        
        
        
    
    
    



        


