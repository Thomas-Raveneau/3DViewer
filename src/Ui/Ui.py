
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QOpenGLContext
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
    def __init__(self, file="/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Menger_sponge_sample.stl", parent=None):
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

###########Translate Function#####################
    def Translate(self):
        ## Translate ##
        self.TranslateBlock = QWidget()
        self.layoutTranslateBlock = QVBoxLayout()
        self.titleTranslate = QLabel("Translate")
        self.layoutTranslateBlock.addWidget(self.titleTranslate)

        self.sliderTranslate = QSlider(Qt.Horizontal, self)
        self.sliderTranslate.setGeometry(10, 40, 10, 10)
        self.sliderTranslate.valueChanged[int].connect(self.buttonTranslate)
        self.layoutTranslateBlock.addWidget(self.sliderTranslate)

        self.layoutTranslateTexField = QHBoxLayout()

        self.XInput = QLineEdit(self)
        self.XInput.setPlaceholderText("x")
        self.XInput.move(20, 20)
        self.XInput.resize(80, 40)
        self.layoutTranslateTexField.addWidget(self.XInput)

        self.YInput = QLineEdit(self)
        self.YInput.setPlaceholderText("y")
        self.YInput.move(20, 20)
        self.YInput.resize(80, 40)
        self.layoutTranslateTexField.addWidget(self.YInput)

        self.ZInput = QLineEdit(self)
        self.ZInput.setPlaceholderText("z")
        self.ZInput.move(20, 20)
        self.ZInput.resize(80, 40)
        self.layoutTranslateTexField.addWidget(self.ZInput)
        self.layoutTranslateBlock.addLayout(self.layoutTranslateTexField)

        self.translateButton = ButtonCustom(self, "Translate")
        self.translateButton.clicked.connect(self.TranslateXYZ)
        self.layoutTranslateBlock.addWidget(self.translateButton)

        # self.rotateButton = ButtonCustom(self, "Translate")
        # self.rotateButton.clicked.connect(self.buttonTranslate)
        self.TranslateBlock.setStyleSheet("background-color: #E6C96E")
        self.TranslateBlock.setLayout(self.layoutTranslateBlock)

        self.layoutMenu.addWidget(self.TranslateBlock)

    def buttonTranslate(self, value):
        print("button Translate %d", value)
        self.openglWidget1.onChangeTranslate(Vertex(value, value, value))
        self.openglWidget1.update()
    def TranslateXYZ(self):
        x = self.XInput.text()
        y = self.YInput.text()
        z = self.ZInput.text()
        self.openglWidget1.onChangeTranslate(Vertex(x, y, z))
        self.openglWidget1.update()
#########################################################
    def Scale(self):
        ## Translate ##
        self.ScaleBlock = QWidget()
        self.layoutScaleBlock = QVBoxLayout()
        self.titleScale = QLabel("Scale")
        self.layoutScaleBlock.addWidget(self.titleScale)

        self.sliderScale = QSlider(Qt.Horizontal, self)
        self.sliderScale.setGeometry(10, 40, 10, 10)
        self.sliderScale.valueChanged[int].connect(self.buttonScale)
        self.layoutScaleBlock.addWidget(self.sliderScale)

        self.layoutScaleTexField = QHBoxLayout()

        self.XInputS = QLineEdit(self)
        self.XInputS.setPlaceholderText("x")
        self.XInputS.move(20, 20)
        self.XInputS.resize(80, 40)
        self.layoutScaleTexField.addWidget(self.XInputS)

        self.YInputS = QLineEdit(self)
        self.YInputS.setPlaceholderText("y")
        self.YInputS.move(20, 20)
        self.YInputS.resize(80, 40)
        self.layoutScaleTexField.addWidget(self.YInputS)

        self.ZInputS = QLineEdit(self)
        self.ZInputS.setPlaceholderText("z")
        self.ZInputS.move(20, 20)
        self.ZInputS.resize(80, 40)
        self.layoutScaleTexField.addWidget(self.ZInputS)
        self.layoutScaleBlock.addLayout(self.layoutScaleTexField)

        # self.rotateButton = ButtonCustom(self, "Translate")
        # self.rotateButton.clicked.connect(self.buttonTranslate)
        self.ScaleBlock.setStyleSheet("background-color: #E6C96E")
        self.ScaleBlock.setLayout(self.layoutScaleBlock)

        self.layoutMenu.addWidget(self.ScaleBlock)


###########ROTATION FUNCTION#################################
    def Rotate(self):
        self.rotateBlock = QWidget()
        self.layoutRotateBlock = QVBoxLayout()
        self.titleRotate = QLabel("Rotate")
        self.layoutRotateBlock.addWidget(self.titleRotate)

        self.layoutDialRotation = QHBoxLayout()
        self.dialx = Dial(self, Color.MAIN_COLOR)
        self.dialx.valueChanged.connect(self.dialRotateX)
        self.dialy = Dial(self, Color.SECOND_COLOR)
        self.dialy.valueChanged.connect(self.dialRotateY)
        self.dialz = Dial(self, Color.THIRTH_COLOR)
        self.dialz.valueChanged.connect(self.dialRotateZ)

        self.layoutDialRotation.addWidget(self.dialx)
        self.layoutDialRotation.addWidget(self.dialy)
        self.layoutDialRotation.addWidget(self.dialz)
        ##self.layoutDialRotation.addStretch(1)
        self.layoutRotateBlock.addLayout(self.layoutDialRotation)

        self.rotateBlock.setStyleSheet("background-color: #E6C96E")
        self.rotateBlock.setLayout(self.layoutRotateBlock)

        self.layoutMenu.addWidget(self.rotateBlock)

    def dialRotateX(self):
        print("Dial value = %i" % (self.dialx.value()))
        self.openglWidget1.onChangeRotateX(self.dialx.value())
        self.openglWidget1.update()

    def dialRotateY(self):
        print("Dial value = %i" % (self.dialy.value()))
        self.openglWidget1.onChangeRotateY(self.dialy.value())
        self.openglWidget1.update()

    def dialRotateZ(self):
        print("Dial value = %i" % (self.dialz.value()))
        self.openglWidget1.onChangeRotateZ(self.dialz.value())
        self.openglWidget1.update()
#########################################################

    def getfile(self):
        self.layoutBox.removeWidget(self.openglWidget1)
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects', "Image files (*.STL *.stl)")
        self.openglWidget1.clear()
        print(fname[0])
        self.openglWidget1 = Core(self, fname[0])
        self.layoutBox.addWidget(self.openglWidget1)
        #self.openglWidget1.__loop()

    def loadTexture(self):
        self.layoutBox.removeWidget(self.openglWidget1)
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects',
                                            "Image files (*.STL *.txt)")
        self.openglWidget1.clear()
        print(fname[0])
        self.openglWidget1 = Core(self, fname[0])
        self.layoutBox.addWidget(self.openglWidget1)
        # self.openglWidget1.__loop()

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
        self.openglWidget1.onChangeRotateY(45)
        self.openglWidget1.update()

    def buttonScale(self):
        print("button Scale")
        self.openglWidget1.onChangeScale(Vertex(2, 2, 2))
        self.openglWidget1.__loop()

