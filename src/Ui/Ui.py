
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.Ui.ButtonCustom import ButtonCustom
from src.Mesh.Vertex import Vertex
from src.Core.Core import Core
from enum import Enum

class Color(Enum):
    MAIN_COLOR = "#FC087A"
    SECOND_COLOR = "#C812E6"
    THIRTH_COLOR = "#F5E555"


class Dial(QDial):
    color: Color
    def __init__(self, parent=None, color = Color.SECOND_COLOR):
        QDial.__init__(self, parent)
        print(color.value)
        style = 'QDial { background-color: ' +  color.value  + '}'

        print (style)
        self.setStyleSheet(style)
 
        # self.style().subControlRect(QStyle.CC_Dial, opt,
        #                                QStyle.SC_DialHandle)
        self.setMinimum(0)
        self.setMaximum(360)
        self.setValue(0)
        self.move(30, 50)
    

class Ui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.menu = QWidget()
        self.layoutBox =  QHBoxLayout()
        self.layoutMenu =  QVBoxLayout()
        ##self.layoutMenu.setSizeConstraint(self, )

        self.layoutDialGetObject =  QHBoxLayout()
        self.btnGetFiles = QPushButton("Object")
        self.btnGetFiles.clicked.connect(self.getfile)
        self.btnGetTexture = QPushButton("Texture")
        self.btnGetTexture.clicked.connect(self.loadTexture)
        self.layoutDialGetObject.addWidget(self.btnGetFiles)
        self.layoutDialGetObject.addWidget(self.btnGetTexture)
        ##self.layoutDialGetObject.setFixedHeight(50)
        self.layoutMenu.addLayout(self.layoutDialGetObject)


        ## Rotate ##
        self.Rotate()
        ## Translate ##
        self.Translate()

        ## Rotate ##
        self.translateButton = ButtonCustom(self, "Rotate")
        self.translateButton.clicked.connect(self.buttonRotate)
        self.layoutMenu.addWidget(self.translateButton)

        ## Scale ##
        self.Scale()


        ##self.layoutMenu.addWidget(self.Button1)
        self.layoutMenu.addStretch(1)

        self.menu.setLayout(self.layoutMenu)
        self.menu.setMaximumWidth(200)

        self.openglWidget1 = Core(self, "/home/yann/2020_repositories/KMU/Graphics/tests/3DViewer/Objects/Cube.stl")
    
    def BoxFilled(self) -> QVBoxLayout:
        self.layoutBox.addWidget(self.menu)
        self.layoutBox.addWidget(self.openglWidget1)
        return self.layoutBox




    def buttonTranslate(self, value):
        print("button Translate %d", value)
        self.openglWidget1.onChangeTranslate(Vertex(-60, 30, value))
        self.openglWidget1.update()

    def buttonRotate(self):
        print("button Rotate")
        self.openglWidget1.onChangeRotateX(-90)
        self.openglWidget1.update()

    def buttonScale(self):
        print("button Scale")
        self.openglWidget1.onChangeScale(Vertex(2, 2, 2))
        self.openglWidget1.__loop()

