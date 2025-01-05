from PyQt6.QtWidgets import QWidget

from ui.task_widget import Ui_task_widget

from widgets.base.base_widget_mixins import BaseWidgetMixin

class TaskWidget(QWidget, BaseWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui=Ui_task_widget()
        self.ui.setupUi(self)
        
    def __str__(self):
        return super().__str__() + f'(date:{self.ui.task_date_label.text()})'
        

