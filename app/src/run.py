import sys

from PyQt6 import QtWidgets as qtw

from widgets.window.window import Window



class Application(qtw.QApplication):
    def __init__(self):
        super().__init__(sys.argv)

def main():
    app = Application()
    window = Window()
    window.show()
    app.exec()



if __name__=='__main__':
    main()

