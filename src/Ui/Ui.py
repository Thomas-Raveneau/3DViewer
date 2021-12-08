from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtWidgets import *
from src.Ui.ButtonCustom import ButtonCustom
from src.Ui.Dial import Dial
from src.Mesh.Vertex import Vertex
from src.Core.Core import Core
from enum import Enum


class Color(Enum):
    MAIN_COLOR = "#FC087A"
    SECOND_COLOR = "#C812E6"
    THIRTH_COLOR = "#E85625"

class Ui(QWidget):
    fontSize = 20
    def __init__(self, file="/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Menger_sponge_sample.stl",
                 parent=None):
        QWidget.__init__(self, parent)
        self.menu = QWidget()
        self.layoutBox = QHBoxLayout()
        self.layoutMenu = QVBoxLayout()
        self.layoutGetElement = QHBoxLayout()

        ## Button Load Object ##
        self.btnGetFiles = QPushButton("Object")
        self.btnGetFiles.clicked.connect(self.getfile)
        self.layoutGetElement.addWidget(self.btnGetFiles)

        ## Button Load Texture ##
        self.btnGetTexture = QPushButton("Texture")
        self.btnGetTexture.clicked.connect(self.loadTexture)
        self.layoutGetElement.addWidget(self.btnGetTexture)

        self.layoutMenu.addLayout(self.layoutGetElement)
        ## Rotate ##
        self.Rotate()
        ## Translate ##
        self.Translate()
        ## Scale ##
        self.Scale()

        self.layoutMenu.addStretch(1)
        self.menu.setLayout(self.layoutMenu)
        self.menu.setMaximumWidth(300)
        self.openglWidget1 = Core(self, "Objects/Cube.stl")

    def getfile(self):
        self.layoutBox.removeWidget(self.openglWidget1)
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.STL *.stl)")
        self.openglWidget1.clear()
        self.openglWidget1 = Core(self, fname[0])
        self.layoutBox.addWidget(self.openglWidget1)

    def loadTexture(self):
        self.layoutBox.removeWidget(self.openglWidget1)
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.vs *.fs *.jpg *.png)")
        self.openglWidget1.onChangeFile(fname[0])
        self.openglWidget1.update()

    def BoxFilled(self) -> QVBoxLayout:
        self.layoutBox.addWidget(self.menu)
        self.layoutBox.addWidget(self.openglWidget1)
        return self.layoutBox

    def Rotate(self):
        self.rotateBlock = QWidget()
        self.layoutRotateBlock = QVBoxLayout()

        ## Title Rotate
        self.titleRotate = QLabel("Rotate")
        self.titleRotate.setFont(QFont('Arial', self.fontSize))
        self.layoutRotateBlock.addWidget(self.titleRotate)

        ## Dial X Rotate ##
        self.layoutDialRotationX = QHBoxLayout()
        self.dialx = Dial(self, Color.MAIN_COLOR)
        self.dialx.valueChanged.connect(self.dialRotateX)
        self.RotateTextX = QLabel("X")
        self.layoutDialRotationX.addWidget(self.RotateTextX)
        self.layoutDialRotationX.addWidget(self.dialx)
        self.layoutRotateBlock.addLayout(self.layoutDialRotationX)

        ## Dial Y Rotate ##
        self.layoutDialRotationY = QHBoxLayout()
        self.dialy = Dial(self, Color.SECOND_COLOR)
        self.dialy.valueChanged.connect(self.dialRotateY)
        self.RotateTextY = QLabel("Y")
        self.layoutDialRotationY.addWidget(self.RotateTextY)
        self.layoutDialRotationY.addWidget(self.dialy)
        self.layoutRotateBlock.addLayout(self.layoutDialRotationY)

        ## Dial Z Rotate ##
        self.layoutDialRotationZ = QHBoxLayout()
        self.dialz = Dial(self, Color.THIRTH_COLOR)
        self.dialz.valueChanged.connect(self.dialRotateZ)
        self.RotateTextZ = QLabel("Z")
        self.layoutDialRotationZ.addWidget(self.RotateTextZ)
        self.layoutDialRotationZ.addWidget(self.dialz)
        self.layoutRotateBlock.addLayout(self.layoutDialRotationZ)

        ## Block Style ##
        self.rotateBlock.setStyleSheet("background-color: #EAA3FB")
        self.rotateBlock.setLayout(self.layoutRotateBlock)
        self.layoutMenu.addWidget(self.rotateBlock)

    def dialRotateX(self):
        self.openglWidget1.onChangeRotateX(self.dialx.value())
        self.openglWidget1.update()

    def dialRotateY(self):
        self.openglWidget1.onChangeRotateY(self.dialy.value())
        self.openglWidget1.update()

    def dialRotateZ(self):
        self.openglWidget1.onChangeRotateZ(self.dialz.value())
        self.openglWidget1.update()

    #########################################################

    def Translate(self):
        ## Translate ##
        self.TranslateBlock = QWidget()
        self.layoutTranslateBlock = QVBoxLayout()

        ## Title Translate ##
        self.titleTranslate = QLabel("Translate")
        self.titleTranslate.setFont(QFont('Arial', self.fontSize))
        self.layoutTranslateBlock.addWidget(self.titleTranslate)

        #### X  ####
        self.layoutTranslateButtonX = QHBoxLayout()
        self.translateX = QLabel("x")
        ## RightX ##
        self.translateButtonXR = ButtonCustom(self, "←")
        self.translateButtonXR.clicked.connect(lambda checked: self.buttonTranslateMove(-2, 0, 0))
        self.translateButtonXR.setStyleSheet("color: #011FFF")
        ## LeftX ##
        self.translateButtonXL = ButtonCustom(self, "→")
        self.translateButtonXL.clicked.connect(lambda checked: self.buttonTranslateMove(2, 0, 0))
        self.translateButtonXL.setStyleSheet("color: #011FFF")
        self.layoutTranslateButtonX.addWidget(self.translateX)
        self.layoutTranslateButtonX.addWidget(self.translateButtonXR)
        self.layoutTranslateButtonX.addWidget(self.translateButtonXL)
        self.layoutTranslateBlock.addLayout(self.layoutTranslateButtonX)

        #### Y  ####
        self.layoutTranslateButtonY = QHBoxLayout()
        self.translateY = QLabel("y")
        ## RightY ##
        self.translateButtonYR = ButtonCustom(self, "←")
        self.translateButtonYR.clicked.connect(lambda checked: self.buttonTranslateMove(0, -2, 0))
        self.translateButtonYR.setStyleSheet("color: #011FFF")
        ## LeftY ##
        self.translateButtonYL = ButtonCustom(self, "→")
        self.translateButtonYL.clicked.connect(lambda checked: self.buttonTranslateMove(0, 2, 0))
        self.translateButtonYL.setStyleSheet("color: #011FFF")
        self.layoutTranslateButtonY.addWidget(self.translateY)
        self.layoutTranslateButtonY.addWidget(self.translateButtonYR)
        self.layoutTranslateButtonY.addWidget(self.translateButtonYL)
        self.layoutTranslateBlock.addLayout(self.layoutTranslateButtonY)

        #### Z  ####
        self.layoutTranslateButtonZ = QHBoxLayout()
        self.translateZ = QLabel("z")
        ## RightZ ##
        self.translateButtonZR = ButtonCustom(self, "←")
        self.translateButtonZR.clicked.connect(lambda checked: self.buttonTranslateMove(0, 0, -2))
        self.translateButtonZR.setStyleSheet("color: #011FFF")
        ## LeftZ ##
        self.translateButtonZL = ButtonCustom(self, "→")
        self.translateButtonZL.clicked.connect(lambda checked: self.buttonTranslateMove(0, 0, 2))
        self.translateButtonZL.setStyleSheet("color: #011FFF")
        self.layoutTranslateButtonZ.addWidget(self.translateZ)
        self.layoutTranslateButtonZ.addWidget(self.translateButtonZR)
        self.layoutTranslateButtonZ.addWidget(self.translateButtonZL)
        self.layoutTranslateBlock.addLayout(self.layoutTranslateButtonZ)

        ## Text field ##
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

        ## Button validation Translate ##
        self.translateButton = ButtonCustom(self, "Translate")
        self.translateButton.clicked.connect(self.TranslateXYZ)
        self.translateButton.setStyleSheet("color: #011FFF")
        self.layoutTranslateBlock.addWidget(self.translateButton)

        ## Block Style ##
        self.layoutTranslateBlock.setSpacing(20)
        self.TranslateBlock.setStyleSheet("background-color: #6EF9FF")
        self.TranslateBlock.setLayout(self.layoutTranslateBlock)

        self.layoutMenu.addWidget(self.TranslateBlock)

    def buttonTranslate(self, value):
        self.openglWidget1.onChangeTranslate(Vertex(0, 0, value))
        self.openglWidget1.update()

    def buttonTranslateMove(self, x, y, z):
        vertex = Vertex(x, y, z)
        self.openglWidget1.onChangeTranslate(vertex)
        self.openglWidget1.update()

    def TranslateXYZ(self):
        x = int(self.XInput.text())
        y = int(self.YInput.text())
        z = int(self.ZInput.text())
        self.openglWidget1.onChangeTranslate(Vertex(x, y, z))
        self.openglWidget1.update()

    #########################################################

    def Scale(self):
        self.ScaleBlock = QWidget()
        self.layoutScaleBlock = QVBoxLayout()

        ## Title ##
        self.titleScale = QLabel("Scale")
        self.titleScale.setFont(QFont('Arial', self.fontSize))
        self.layoutScaleBlock.addWidget(self.titleScale)

        ## Button ##
        self.layoutScaleButton = QHBoxLayout()
        self.scaleButtonMignus = ButtonCustom(self, "-")
        self.scaleButtonMignus.clicked.connect(self.ScaleMignus)
        self.scaleButtonMignus.setStyleSheet("color: #006B0B")
        self.layoutScaleButton.addWidget(self.scaleButtonMignus)
        self.scaleButtonMore = ButtonCustom(self, "+")
        self.scaleButtonMore.clicked.connect(self.ScaleMore)
        self.scaleButtonMore.setStyleSheet("color: #006B0B")
        self.layoutScaleButton.addWidget(self.scaleButtonMore)
        self.layoutScaleBlock.addLayout(self.layoutScaleButton)

        ## Text Field ##
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

        ## Button Validation Value ##
        self.scaleButton = ButtonCustom(self, "scale")
        self.scaleButton.clicked.connect(self.ScaleXYZ)
        self.scaleButton.setStyleSheet("color: #006B0B")
        self.layoutScaleBlock.addWidget(self.scaleButton)

        ## Block Style ##
        self.layoutScaleBlock.setSpacing(20)
        self.ScaleBlock.setStyleSheet("background-color: #A6E394")
        self.ScaleBlock.setLayout(self.layoutScaleBlock)
        self.layoutMenu.addWidget(self.ScaleBlock)

    def buttonScale(self, value):
        self.openglWidget1.onChangeScale(Vertex(value, value, value))
        self.openglWidget1.update()

    def ScaleMignus(self):
        self.openglWidget1.onChangeScale(Vertex(0.5, 0.5, 0.5))
        self.openglWidget1.update()

    def ScaleMore(self):
        self.openglWidget1.onChangeScale(Vertex(2, 2, 2))
        self.openglWidget1.update()

    def ScaleXYZ(self):
        x = int(self.XInputS.text())
        y = int(self.YInputS.text())
        z = int(self.ZInputS.text())
        self.openglWidget1.onChangeScale(Vertex(x, y, z))
        self.openglWidget1.update()

    #########################################################################
