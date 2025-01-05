from PyQt6.QtWidgets import QPushButton

class BaseWidgetMixin:
    def __str__(self):
        return self.__class__.__name__
        
    def add_click_connect(self, button:QPushButton, slot):
        return button.clicked.connect(slot)
        
        
        
        
        