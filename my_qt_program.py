import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
# TODO: Why can I not use this import and have to import the above QtCore library again for the button alignment to
#  work? The world wonders.
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QRadioButton
import morse_code_translator


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Morse-Code-Übersetzer')

        self.plaintext_to_morse_button = QRadioButton('Fließtext in Morsecode übersetzen')
        self.plaintext_to_morse_button.clicked.connect(self.radio_button_clicked)
        self.plaintext_to_morse_button.setChecked(True)

        self.morse_to_plaintext_button = QRadioButton('Morsecode in Fließtext übersetzen')
        self.morse_to_plaintext_button.clicked.connect(self.radio_button_clicked)

        self.button = QPushButton('Übersetzen')
        self.button.setFixedSize(150, 50)

        self.label = QLabel()
        self.label.setMargin(10)
        self.label.setFont(QFont('Times New Roman', 18))

        self.textfield = QLineEdit()
        self.textfield.setAlignment(Qt.AlignVCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.plaintext_to_morse_button)
        layout.addWidget(self.morse_to_plaintext_button)
        layout.addWidget(self.textfield)
        layout.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        layout.setContentsMargins(20, 20, 20, 20)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)
        self.button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        my_text = self.textfield.text()
        if self.plaintext_to_morse_button.isChecked():
            print('Plaintext to morse button pressed.')
            my_translation = morse_code_translator.return_translation_into_morse(my_text)
        elif self.morse_to_plaintext_button.isChecked():
            print('Morse to plaintext button pressed.')
            my_translation = morse_code_translator.return_translation_into_text(my_text)
        else:
            my_translation = 'Es wurde kein Übersetzungsmodus gewählt.'
        self.label.setText(my_translation)

    def radio_button_clicked(self):
        self.textfield.setText('')
        print('The RadioButton input has changed.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
