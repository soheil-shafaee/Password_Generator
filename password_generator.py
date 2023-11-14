from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QSlider, QCheckBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
import sys
import random


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI File
        uic.loadUi("password_generator.ui", self)
        self.setFixedSize(698, 528)

        # Add Image To Label and Icon
        self.setWindowIcon(QIcon("png/002-password.png"))
        self.pixmapPic = QPixmap("png/001-password-code.png")
        self.picLabel.setPixmap(self.pixmapPic)

        # Define Our Widgets
        self.picLabel = self.findChild(QLabel, "picLabel")
        self.passwordLine = self.findChild(QLineEdit, "passwordLine")
        self.passwordGenerate = self.findChild(QPushButton, "passwordGenerate")
        self.passwordLengths = self.findChild(QSlider, "passwordLengthsVertical")
        self.passwordLengthsLabel = self.findChild(QLabel, "passwordLengthsLabel")
        self.number = self.findChild(QCheckBox, "numberCheckbox")
        self.upper = self.findChild(QCheckBox, "upperCheckBox")
        self.symbol = self.findChild(QCheckBox, "symbolCheckBox")

        # Click The Button
        self.passwordGenerate.clicked.connect(self.generate_password)

        # The Number Of Character
        self.passwordLengths.valueChanged.connect(self.move)
        self.passwordLengths.setMinimum(5)
        self.passwordLengths.setMaximum(20)
        self.passwordLengths.setValue(5)
        self.passwordLengths.setTickPosition(QSlider.TicksBelow)
        self.passwordLengths.setTickInterval(1)

        # Set Default Check Of Number, Symbol, Uppercase
        self.number.setChecked(True)
        self.upper.setChecked(True)
        self.symbol.setChecked(True)

        # Show The App
        self.show()

    # Define The Change Value Slider Function
    def move(self, value):
        # Change The Number Of Password Lengths
        self.passwordLengthsLabel.setText(str(value))

    # Define The Generate Password Function
    def generate_password(self, value):
        # Password letter List
        password_list = []
        self.passwordLengths.valueChanged.connect(self.move)
        print(str(self.passwordLengths.valueChanged.connect(self.move)))
        # The Letter and Symbols and Number For Making Password
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']

        if self.upper.isChecked():
            upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            letters += upper
        if self.number.isChecked():
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            letters += numbers
        if self.symbol.isChecked():
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
            letters += symbols

        # for i in range(value):
        #     password_letter = random.choice(letters)
        #     password_list.append(password_letter)
        # password = "".join(password_list)
        # self.passwordLine.setText(password)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
