
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
        self.setMaximum(30)
        self.setValue(0)
        self.move(30, 50)
    

class Ui(QWidget):
    fontSize = 20
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
        ## Scale ##
        self.Scale()


        ##self.layoutMenu.addWidget(self.Button1)
        self.layoutMenu.addStretch(1)

        self.menu.setLayout(self.layoutMenu)
        self.menu.setMaximumWidth(300)

        self.openglWidget1 = Core(self)

    ###########ROTATION FUNCTION#################################
    def Rotate(self):
        self.rotateBlock = QWidget()
        self.layoutRotateBlock = QVBoxLayout()
        self.titleRotate = QLabel("Rotate")
        self.titleRotate.setFont(QFont('Arial', self.fontSize))

        self.layoutRotateBlock.addWidget(self.titleRotate)

        self.layoutDialRotationX = QHBoxLayout()
        self.dialx = Dial(self, Color.MAIN_COLOR)
        self.dialx.valueChanged.connect(self.dialRotateX)
        self.RotateTextX = QLabel("X")
        self.layoutDialRotationX.addWidget(self.RotateTextX)
        self.layoutDialRotationX.addWidget(self.dialx)

        self.layoutRotateBlock.addLayout(self.layoutDialRotationX)

        self.layoutDialRotationY = QHBoxLayout()
        self.dialy = Dial(self, Color.SECOND_COLOR)
        self.dialy.valueChanged.connect(self.dialRotateY)
        self.RotateTextY = QLabel("Y")
        self.layoutDialRotationY.addWidget(self.RotateTextY)
        self.layoutDialRotationY.addWidget(self.dialy)
        self.layoutRotateBlock.addLayout(self.layoutDialRotationY)

        self.layoutDialRotationZ = QHBoxLayout()
        self.dialz = Dial(self, Color.THIRTH_COLOR)
        self.dialz.valueChanged.connect(self.dialRotateZ)
        self.RotateTextZ = QLabel("Z")
        self.layoutDialRotationZ.addWidget(self.RotateTextZ)
        self.layoutDialRotationZ.addWidget(self.dialz)
        self.layoutRotateBlock.addLayout(self.layoutDialRotationZ)

        ##self.layoutDialRotation.addStretch(1)
        # self.layoutRotateBlock.addLayout(self.layoutDialRotation)

        self.rotateBlock.setStyleSheet("background-color: #EAA3FB")
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

    ###########Translate Function#####################
    def Translate(self):
        ## Translate ##
        self.TranslateBlock = QWidget()
        self.layoutTranslateBlock = QVBoxLayout()
        self.titleTranslate = QLabel("Translate")
        self.titleTranslate.setFont(QFont('Arial', self.fontSize))

        self.layoutTranslateBlock.addWidget(self.titleTranslate)

        self.layoutTranslateButton = QHBoxLayout()

        ## UP ##
        self.translateButtonUp = ButtonCustom(self, "↑")
        self.translateButtonUp.clicked.connect(self.buttonTranslateUp)
        self.translateButtonUp.setStyleSheet("color: #011FFF")

        ## DOWN ##
        self.translateButtonDown = ButtonCustom(self, "↓")
        self.translateButtonDown.clicked.connect(self.buttonTranslateDown)
        self.translateButtonDown.setStyleSheet("color: #011FFF")


        ## Right ##
        self.translateButtonRight = ButtonCustom(self, "←")
        self.translateButtonRight.clicked.connect(self.buttonTranslateLeft)
        self.translateButtonRight.setStyleSheet("color: #011FFF")

        ## Left ##
        self.translateButtonLeft = ButtonCustom(self, "→")
        self.translateButtonLeft.clicked.connect(self.buttonTranslateRight)
        self.translateButtonLeft.setStyleSheet("color: #011FFF")


        self.layoutTranslateBlock.addWidget(self.translateButtonUp)
        self.layoutTranslateButton.addWidget(self.translateButtonRight)
        self.layoutTranslateButton.addWidget(self.translateButtonDown)
        self.layoutTranslateButton.addWidget(self.translateButtonLeft)



        self.layoutTranslateBlock.addLayout(self.layoutTranslateButton)

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
        self.translateButton.setContentsMargins(-1, -1, -1, 0)

        self.layoutTranslateBlock.addWidget(self.translateButton)
        self.layoutTranslateBlock.setSpacing(20)

        # self.rotateButton = ButtonCustom(self, "Translate")
        # self.rotateButton.clicked.connect(self.buttonTranslate)
        self.TranslateBlock.setStyleSheet("background-color: #6EF9FF")
        self.TranslateBlock.setLayout(self.layoutTranslateBlock)

        self.layoutMenu.addWidget(self.TranslateBlock)

    def buttonTranslate(self, value):
        print("button Translate %d", value)
        self.openglWidget1.onChangeTranslate(Vertex(0, 0, value))
        self.openglWidget1.update()

    def buttonTranslateDown(self):
        print("button Translate down")
        self.openglWidget1.onChangeTranslate(Vertex(0, 2, 0))
        self.openglWidget1.update()
    def buttonTranslateUp(self):
        print("button Translate down")
        self.openglWidget1.onChangeTranslate(Vertex(0, -2, 0))
        self.openglWidget1.update()
    def buttonTranslateRight(self):
        print("button Translate down")
        self.openglWidget1.onChangeTranslate(Vertex(2, 0, 0))
        self.openglWidget1.update()

    def buttonTranslateLeft(self):
        print("button Translate down")
        self.openglWidget1.onChangeTranslate(Vertex(-2, 0, 0))
        self.openglWidget1.update()
    def TranslateXYZ(self):
        x = int(self.XInput.text())
        y = int(self.YInput.text())
        z = int(self.ZInput.text())
        self.openglWidget1.onChangeTranslate(Vertex(x, y, z))
        self.openglWidget1.update()
#########################################################
    def Scale(self):
        ## Translate ##
        self.ScaleBlock = QWidget()
        self.layoutScaleBlock = QVBoxLayout()
        self.titleScale = QLabel("Scale")
        self.titleScale.setFont(QFont('Arial', self.fontSize))
        self.layoutScaleBlock.addWidget(self.titleScale)

        self.layoutScaleButton = QHBoxLayout()
        self.scaleButtonMignus = ButtonCustom(self, "-")
        self.scaleButtonMignus.clicked.connect(self.ScaleMignus)
        self.layoutScaleButton.addWidget(self.scaleButtonMignus)
        self.scaleButtonMore = ButtonCustom(self, "+")
        self.scaleButtonMore.clicked.connect(self.ScaleMore)
        self.layoutScaleButton.addWidget(self.scaleButtonMore)

        self.layoutScaleBlock.addLayout(self.layoutScaleButton)


        # self.sliderScale = QSlider(Qt.Horizontal, self)
        # self.sliderScale.setGeometry(10, 40, 10, 10)
        # self.sliderScale.setSingleStep(50)
        # self.sliderScale.setRange(0, 100)
        #
        # self.sliderScale.valueChanged[int].connect(self.buttonScale)
        # self.layoutScaleBlock.addWidget(self.sliderScale)

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

        self.scaleButton = ButtonCustom(self, "scale")
        self.scaleButton.clicked.connect(self.ScaleXYZ)
        self.layoutScaleBlock.addWidget(self.scaleButton)
        self.layoutScaleBlock.setSpacing(20)

        self.ScaleBlock.setStyleSheet("background-color: #A6E394")
        self.ScaleBlock.setLayout(self.layoutScaleBlock)

        self.layoutMenu.addWidget(self.ScaleBlock)


    def buttonScale(self, value):
        print("button Scale", value)
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
                                            "Image files (*.vs *.fs *.jpg *.png)")
        ##self.openglWidget1.clear()
        print(fname[0])
        self.openglWidget1.onChangeFile(fname[0])
        self.openglWidget1.update()

        ##self.layoutBox.addWidget(self.openglWidget1)
        # self.openglWidget1.__loop()

    def BoxFilled(self) -> QVBoxLayout:
        self.layoutBox.addWidget(self.menu)
        self.layoutBox.addWidget(self.openglWidget1)
        return self.layoutBox

    def buttonRotate(self):
        print("button Rotate")
        self.openglWidget1.onChangeRotateY(45)
        self.openglWidget1.update()
