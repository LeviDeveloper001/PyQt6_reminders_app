import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class FlexWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Основной вертикальный компоновщик
        main_layout = QVBoxLayout()

        # Горизонтальный компоновщик
        h_layout = QHBoxLayout()

        # Создаем виджеты
        label = QLabel("Гибкий интерфейс")
        button1 = QPushButton("Кнопка 1")
        button2 = QPushButton("Кнопка 2")
        button3 = QPushButton("Кнопка 3")

        # Добавляем виджеты в горизонтальный компоновщик
        h_layout.addWidget(button1)
        h_layout.addWidget(button2)
        h_layout.addWidget(button3)

        # Добавляем метку и горизонтальный компоновщик в основной компоновщик
        main_layout.addWidget(label)
        main_layout.addLayout(h_layout)

        # Устанавливаем основной компоновщик для главного виджета
        self.setLayout(main_layout)

        # Устанавливаем заголовок и размер окна
        self.setWindowTitle("Flex аналог в PyQt6")
        self.resize(300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FlexWidget()
    window.show()
    sys.exit(app.exec())
