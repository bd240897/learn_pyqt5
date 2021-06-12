from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog, QLineEdit, QGridLayout, QTextEdit, QLabel, QVBoxLayout, QWidget
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

class Window(QWidget):
    def __init__(self):
        """Создает главное окно опредленного размера"""
        super(QWidget, self).__init__()

        btn2 = QtWidgets.QPushButton(self)


        self.setWindowTitle('Моя научная работа')
        self.setGeometry(300, 250, 400, 400)

        okButton = QtWidgets.QPushButton("OK")
        okButton.clicked.connect(self.plot)
        hbox = QVBoxLayout()
        self.setLayout(hbox)
        hbox.addWidget(okButton)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        hbox.addWidget(self.canvas)

    def plot(self):
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()


def aplication():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    aplication()