from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog, QLineEdit, QGridLayout, QTextEdit, QLabel, QVBoxLayout, QWidget, QHBoxLayout
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from EFIE_circl import EFEI_circl_run

class Window(QWidget):
    def __init__(self):
        """Создает главное окно опредленного размера"""
        super(QWidget, self).__init__()

        self.setWindowTitle('Моя научная работа')
        self.setGeometry(300, 300, 400, 400)

        # главный виджет - СЛОЙ СЕТКА
        self.first_level = QGridLayout()
        self.first_level.setSpacing(5)

        # вставка входных полей
        self.text_input_area()

        # вставка и настройки кнопки расчета
        self.calc_button()

        # настройка полей для графика
        self.graph()

    def text_input_area(self):
        """Поля для ввода входных данных и их метки"""
        # главный бокс

        # поле ввода N
        self.N = QtWidgets.QLineEdit()
        self.N_label = QtWidgets.QLabel()
        self.N_label.setText("Введите число точек расчета 'N' [шт]:")

        # поле ввода a
        self.a = QtWidgets.QLineEdit()
        self.a_label = QtWidgets.QLabel()
        self.a_label.setText("Введите радиус цилиндра 'a' [в длин. волн]:")

        # поле ввода phi_i
        self.phi_i = QtWidgets.QLineEdit()
        self.phi_i_label = QtWidgets.QLabel()
        self.phi_i_label.setText("Введите угол падения волны 'phi_i' [град]:")

        # добавим окна в главный ВИДЖЕТ
        self.first_level.addWidget(self.a, 1, 1)
        self.first_level.addWidget(self.a_label, 1, 0)
        self.first_level.addWidget(self.N, 2, 1)
        self.first_level.addWidget(self.N_label, 2, 0)
        self.first_level.addWidget(self.phi_i, 3, 1)
        self.first_level.addWidget(self.phi_i_label, 3, 0)

        # добавим СЛОЙ к главному окну
        self.setLayout(self.first_level)

        # значения по умолчанию строк
        self.a.setText('2')
        self.N.setText('100')
        self.phi_i.setText('0')

    def graph(self):
        """Настрйока полей для графика"""
        # новый СЛОЙ для графика
        self.second_level = QtWidgets.QVBoxLayout()
        # добавим СЛОЙ к первому СЛОЮ
        self.first_level.addLayout(self.second_level, 4, 0)
        # настройка ГРАФИКА
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # добавим ВИДЖЕТ ко 2-м СЛОЮ
        self.second_level.addWidget(self.canvas)

    def calc_button(self):
        """Настройка кнопки для расчета"""
        # поле для кнопки
        self.btn = QtWidgets.QPushButton()
        self.btn.setText("Запустить?")
        # связь кнопки с функцией
        self.btn.clicked.connect(self.plot)
        # добавим в главный ВИДЖЕТ
        self.first_level.addWidget(self.btn, 10, 0)

    def plot(self):
        """Функция для построения уже натсроенного графика"""

        # получим входные данные
        N = int(self.N.text())
        phi_i = int(self.phi_i.text())
        a = int(self.a.text())

        # очищаем фигуру
        self.figure.clear()
        # фукнция для расчета МЕТОДА - рисует новый график
        EFEI_circl_run(a, N, phi_i, self.figure)
        # обновляем ХОЛСТ
        self.canvas.draw()

def aplication():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    aplication()