# Form implementation generated from reading ui file 'c:\Users\Лев\Desktop\programs\desktop_python\reminders_app\app\src\ui_files\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 601)
        MainWindow.setMinimumSize(QtCore.QSize(1058, 601))
        MainWindow.setMaximumSize(QtCore.QSize(1058, 601))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1061, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.main_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_label.setObjectName("main_label")
        self.verticalLayout.addWidget(self.main_label)
        self.body_scroll_area = QtWidgets.QScrollArea(parent=self.verticalLayoutWidget)
        self.body_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.body_scroll_area.setWidgetResizable(True)
        self.body_scroll_area.setObjectName("body_scroll_area")
        self.content_wrapper_widget = QtWidgets.QWidget()
        self.content_wrapper_widget.setGeometry(QtCore.QRect(0, 0, 1057, 558))
        self.content_wrapper_widget.setObjectName("content_wrapper_widget")
        self.tasks_label = QtWidgets.QLabel(parent=self.content_wrapper_widget)
        self.tasks_label.setGeometry(QtCore.QRect(6, 2, 881, 51))
        self.tasks_label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.tasks_label.setObjectName("tasks_label")
        self.management_group_box = QtWidgets.QGroupBox(parent=self.content_wrapper_widget)
        self.management_group_box.setGeometry(QtCore.QRect(900, 0, 151, 551))
        self.management_group_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.management_group_box.setObjectName("management_group_box")
        self.delete_task_button = QtWidgets.QPushButton(parent=self.management_group_box)
        self.delete_task_button.setEnabled(True)
        self.delete_task_button.setGeometry(QtCore.QRect(10, 80, 51, 51))
        self.delete_task_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_task_button.setMouseTracking(True)
        self.delete_task_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.delete_task_button.setObjectName("delete_task_button")
        self.add_task_button = QtWidgets.QPushButton(parent=self.management_group_box)
        self.add_task_button.setEnabled(True)
        self.add_task_button.setGeometry(QtCore.QRect(90, 80, 51, 51))
        self.add_task_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_task_button.setMouseTracking(True)
        self.add_task_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 32pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);")
        self.add_task_button.setObjectName("add_task_button")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.management_group_box)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 160, 51, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.management_group_box)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 160, 51, 51))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.management_group_box)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 240, 51, 51))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.management_group_box)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 320, 51, 51))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.management_group_box)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 320, 51, 51))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setMouseTracking(True)
        self.pushButton_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.management_group_box)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 240, 51, 51))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setMouseTracking(True)
        self.pushButton_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(170, 85, 255, 255));")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.delete_task_button_label = QtWidgets.QLabel(parent=self.management_group_box)
        self.delete_task_button_label.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.delete_task_button_label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.delete_task_button_label.setObjectName("delete_task_button_label")
        self.add_task_button_label = QtWidgets.QLabel(parent=self.management_group_box)
        self.add_task_button_label.setGeometry(QtCore.QRect(90, 60, 51, 20))
        self.add_task_button_label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.add_task_button_label.setObjectName("add_task_button_label")
        self.tasks_list_widget_scrollarea = QtWidgets.QScrollArea(parent=self.content_wrapper_widget)
        self.tasks_list_widget_scrollarea.setGeometry(QtCore.QRect(10, 50, 881, 501))
        self.tasks_list_widget_scrollarea.setMinimumSize(QtCore.QSize(881, 501))
        self.tasks_list_widget_scrollarea.setMaximumSize(QtCore.QSize(881, 501))
        self.tasks_list_widget_scrollarea.setWidgetResizable(True)
        self.tasks_list_widget_scrollarea.setObjectName("tasks_list_widget_scrollarea")
        self.tasks_list_widget = QtWidgets.QWidget()
        self.tasks_list_widget.setGeometry(QtCore.QRect(0, 0, 879, 499))
        self.tasks_list_widget.setObjectName("tasks_list_widget")
        self.tasks_list_widget_scrollarea.setWidget(self.tasks_list_widget)
        self.body_scroll_area.setWidget(self.content_wrapper_widget)
        self.verticalLayout.addWidget(self.body_scroll_area)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reminders"))
        self.main_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#aa0000;\">Reminders</span></p></body></html>"))
        self.tasks_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Tasks</span></p></body></html>"))
        self.management_group_box.setTitle(_translate("MainWindow", "Management"))
        self.delete_task_button.setText(_translate("MainWindow", "—"))
        self.add_task_button.setText(_translate("MainWindow", "+"))
        self.delete_task_button_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa0000;\">Delete</span></p></body></html>"))
        self.add_task_button_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Add</span></p></body></html>"))
