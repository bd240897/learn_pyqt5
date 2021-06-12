from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog, QLineEdit, QGridLayout, QTextEdit, QLabel, QVBoxLayout, QWidget, QHBoxLayout
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

class Window(QWidget):
    def __init__(self):
        """Создает главное окно опредленного размера"""
        super(QWidget, self).__init__()

        self.setWindowTitle('Моя научная работа')
        self.setGeometry(300, 300, 400, 400)

        # self.button()
        self.text_input_area()

    def text_input_area(self):
        """Поля для ввода входных данных"""
        # главный бокс
        self.first_level = QGridLayout()
        self.first_level.setSpacing(5)

        self.N = QtWidgets.QLineEdit()
        self.N_label = QtWidgets.QLabel()
        self.N_label.setText("Введите N")

        self.a = QtWidgets.QLineEdit()
        self.a_label = QtWidgets.QLabel()
        self.a_label.setText("Введите a")

        self.phi_i = QtWidgets.QLineEdit()
        self.phi_i_label = QtWidgets.QLabel()
        self.phi_i_label.setText("Введите phi_i")

        self.btn = QtWidgets.QPushButton()
        self.btn.setText("Запустить?")
        self.btn.clicked.connect(self.plot)

        self.first_level.addWidget(self.a, 1, 1)
        self.first_level.addWidget(self.a_label, 1, 0)
        self.first_level.addWidget(self.N, 2, 1)
        self.first_level.addWidget(self.N_label, 2, 0)
        self.first_level.addWidget(self.phi_i, 3, 1)
        self.first_level.addWidget(self.phi_i_label, 3, 0)
        self.first_level.addWidget(self.btn, 10, 0)

        self.setLayout(self.first_level)
        self.second_level = QtWidgets.QVBoxLayout()
        self.first_level.addLayout(self.second_level, 4, 0)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.second_level.addWidget(self.canvas)

    def plot(self):
        # получим входные данные
        N = int(self.N.text())
        phi_i = (self.phi_i.text())
        a = (self.a.text())

        self.figure.clear()
        data = [random.random() for i in range(N)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, '*-')
        self.canvas.draw()



def aplication():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    aplication()