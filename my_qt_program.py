import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
import morse_code_translator


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testapplikation")
        self.button = QPushButton("Drücke mich!")
        self.label = QLabel('Das ist ein Label.')
        self.textfield = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textfield)
        layout.addWidget(self.button)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)
        self.button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        my_text = self.textfield.text()
        my_translation = morse_code_translator.return_translation_into_morse(my_text)
        self.label.setText(my_translation)


if __name__ == '__main__':
    my_morse = morse_code_translator.return_translation_into_morse("This is a test")
    print(my_morse)
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
