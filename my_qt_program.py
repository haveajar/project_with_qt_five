import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


def button_pressed():
    print('Weeee!')


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testapplikation")
        button = QPushButton("Drücke mich!")
        self.setCentralWidget(button)
        button.clicked.connect(button_pressed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
