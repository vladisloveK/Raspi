# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication

from EnterNumber import EnterNumberWindow

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(319, 141)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.number_bt = QtWidgets.QPushButton(self.centralwidget)
        self.number_bt.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.number_bt.setObjectName("number_bt")
        self.qrcode_bt = QtWidgets.QPushButton(self.centralwidget)
        self.qrcode_bt.setGeometry(QtCore.QRect(160, 40, 75, 23))
        self.qrcode_bt.setObjectName("qrcode_bt")
        self.language_bt = QtWidgets.QPushButton(self.centralwidget)
        self.language_bt.setGeometry(QtCore.QRect(270, 0, 41, 23))
        self.language_bt.setObjectName("language_bt")
        self.number_bt.clicked.connect(self.go_to_second)
        self.qrcode_bt.clicked.connect(self.go_to_first)
        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.number_bt.setText(_translate("MainWindow", "Номер"))
        self.qrcode_bt.setText(_translate("MainWindow", "QR-Код"))
        self.language_bt.setText(_translate("MainWindow", "RU"))
    def go_to_first(self):
        stackedWidget.setCurrentIndex(2)

    def go_to_second(self):
        stackedWidget.setCurrentIndex(1)
app = QApplication(sys.argv)
window = Window()
stackedWidget = QtWidgets.QStackedWidget()
ne_widget = EnterNumberWindow()
stackedWidget.addWidget(window)
stackedWidget.addWidget(ne_widget)

stackedWidget.show()
sys.exit(app.exec())