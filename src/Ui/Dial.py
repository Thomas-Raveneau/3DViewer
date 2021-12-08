from PyQt5.QtWidgets import *
from enum import Enum

class Color(Enum):
    MAIN_COLOR = "#FC087A"
    SECOND_COLOR = "#C812E6"
    THIRTH_COLOR = "#E85625"

class Dial(QDial):
    color: Color
    def __init__(self, parent=None, color=Color.SECOND_COLOR):
        QDial.__init__(self, parent)
        style = 'QDial { background-color: ' + color.value + '}'
        self.setStyleSheet(style)
        self.setMinimum(0)
        self.setMaximum(30)
        self.setValue(0)
        self.move(30, 50)

