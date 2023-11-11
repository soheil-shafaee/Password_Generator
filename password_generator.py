from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QSlider, QCheckBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI File
        uic.loadUi("password_generator.ui", self)
        self.setFixedSize(698, 528)

        # Define Our Widgets
        self.picLabel = self.findChild(QLabel, "picLabel")
        self.passwordLine = self.findChild(QLineEdit, "passwordLine")
        self.passwordGenerate = self.findChild(QPushButton, "passwordGenerate")
        self.passwordLenghts = self.findChild(QSlider, "passwordLenghtsVertical")
        self.number = self.findChild(QCheckBox, "numberCheckbox")
        self.upper = self.findChild(QCheckBox, "upperCheckBox")
        self.symbol = self.findChild(QCheckBox, "symbolCheckBox")

        # Add Image To Label and Icon
        self.setWindowIcon(QIcon("png/002-password.png"))
        self.pixmapPic = QPixmap("png/001-password-code.png")
        self.picLabel.setPixmap(self.pixmapPic)

        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
