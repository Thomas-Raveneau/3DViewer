from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtWidgets import *
from src.Mesh.Coordinate import Coordinates
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
    meshIsValid: bool = False
    textureIsValid: bool = False
    fontSize = 20
    nameOfMesh: str = "Mesh is undefined"
    nameOfTexture: str = "Texture is undefined"

    def __init__(self, file="/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Menger_sponge_sample.stl",
                 parent=None):
        QWidget.__init__(self, parent)
        self.font = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont("Font/PressStart2P-Regular.ttf"))[0]
        self.iconGuitare = QIcon('Images/coeurnoire.png')

        ##QApplication.setFont(QFont(self.font))
        self.init()

    def init(self):
        if self.meshIsValid and self.textureIsValid:
            self.layoutBox.removeWidget(self.menuInit)
            self.menuInit.deleteLater()
            self.menuInit = None
            self.coreApp()
            self.layoutBox.addWidget(self.menu)
            self.layoutBox.addWidget(self.openglWidget1)
            self.layoutBox.update()
        else:
            self.initObjectAndTexture()
    def coreApp(self):
        self.menu = QWidget()
        self.layoutMenu = QVBoxLayout()
        self.layoutGetElement = QHBoxLayout()

        ## Button Load Object ##
        self.btnGetFiles = QPushButton("Object")
        self.btnGetFiles.clicked.connect(self.getfile)
        self.btnGetFiles.setIcon(self.iconGuitare)
        self.btnGetFiles.setStyleSheet('''
                                       border-style: outset;
                                       border-width: 2px;
                                       border-radius: 15px;
                                       border-color: black;
                                       padding: 4px;
                                       ''')
        self.layoutGetElement.addWidget(self.btnGetFiles)


        ## Button Load Texture ##
        self.btnGetTexture = QPushButton("Texture")
        self.btnGetTexture.clicked.connect(self.loadTexture)
        self.btnGetTexture.setIcon(self.iconGuitare)
        self.btnGetTexture.setStyleSheet('''
                                          border-style: outset;
                                          border-width: 2px;
                                          border-radius: 15px;
                                          border-color: black;
                                          padding: 4px;
                                          ''')
        self.layoutGetElement.addWidget(self.btnGetTexture)

        self.layoutMenu.addLayout(self.layoutGetElement)
        ## Rotate ##
        self.Rotate()
        ## Translate ##
        self.Translate()
        ## Scale ##
        self.Scale()


        self.layoutMenu.addStretch(1)
        self.btnMirrorX = QPushButton("Mirror X")
        self.btnMirrorX.setIcon(self.iconGuitare)
        self.btnMirrorX.clicked.connect(self.funcMirrorX)
        self.btnMirrorX.setStyleSheet('''
                                                      border-style: outset;
                                                      border-width: 2px;
                                                      border-radius: 15px;
                                                      border-color: black;
                                                      padding: 4px;
                                                      ''')
        self.btnMirrorY = QPushButton("Mirror Y")
        self.btnMirrorY.setIcon(self.iconGuitare)
        self.btnMirrorY.clicked.connect(self.funcMirrorY)
        self.btnMirrorY.setStyleSheet('''
                                                      border-style: outset;
                                                      border-width: 2px;
                                                      border-radius: 15px;
                                                      border-color: black;
                                                      padding: 4px;
                                                      ''')
        self.btnMirrorZ = QPushButton("Mirror Z")
        self.btnMirrorZ.setIcon(self.iconGuitare)
        self.btnMirrorZ.clicked.connect(self.funcMirrorZ)
        self.btnMirrorZ.setStyleSheet('''
                                                      border-style: outset;
                                                      border-width: 2px;
                                                      border-radius: 15px;
                                                      border-color: black;
                                                      padding: 4px;
                                                      ''')
        self.layoutMenu.addWidget(self.btnMirrorX)
        self.layoutMenu.addWidget(self.btnMirrorY)
        self.layoutMenu.addWidget(self.btnMirrorZ)

        self.menu.setLayout(self.layoutMenu)
        self.menu.setMaximumWidth(300)

        self.openglWidget1 = Core(self, self.nameOfMesh, self.nameOfTexture)

    def funcMirrorX(self):
        self.openglWidget1.onMirrorChange(Coordinates.X)
        self.openglWidget1.update()

    def funcMirrorY(self):
        self.openglWidget1.onMirrorChange(Coordinates.Y)
        self.openglWidget1.update()

    def funcMirrorZ(self):
        self.openglWidget1.onMirrorChange(Coordinates.Z)
        self.openglWidget1.update()
    
    def funcShearX(self):
        x = float(self.XInputSh.text())
        y = float(self.YInputSh.text())
        self.openglWidget1.onChangeShear((x, y), Coordinates.X)
        self.openglWidget1.update()
    
    def funcShearY(self):
        x = float(self.XInputSh.text())
        y = float(self.YInputSh.text())
        self.openglWidget1.onChangeShear((x, y), Coordinates.Y)
        self.openglWidget1.update()
    
    def funcShearZ(self):
        x = float(self.XInputSh.text())
        y = float(self.YInputSh.text())
        self.openglWidget1.onChangeShear((x, y), Coordinates.Z)
        self.openglWidget1.update()
        

    def initObjectAndTexture(self):
        self.menuInit = QWidget()
        self.layoutInit = QVBoxLayout()

        self.layoutInitTitle = QHBoxLayout()
        self.titleInitmenu = QLabel(self)
        self.titleInitmenu.setFont(QFont(self.font))
        self.titleInitmenuImg = QPixmap('Images/title.png')
        self.titleInitmenu.setPixmap(
            self.titleInitmenuImg.scaled(self.titleInitmenuImg.width(), self.titleInitmenuImg.height()))

        self.headDeadImage = QLabel(self)
        self.headDeadImage2 = QLabel(self)
        self.pixmapheadDead = QPixmap('Images/coeur.png')
        self.headDeadImage.setPixmap(self.pixmapheadDead.scaled(self.pixmapheadDead.width() / 2, self.pixmapheadDead.height() / 2))
        self.headDeadImage2.setPixmap(self.pixmapheadDead.scaled(self.pixmapheadDead.width() / 2, self.pixmapheadDead.height() / 2))

        self.layoutInitTitle.addWidget(self.headDeadImage)

        self.layoutInitTitle.addWidget(self.titleInitmenu)
        self.layoutInitTitle.addWidget(self.headDeadImage2)
        self.layoutInit.addLayout(self.layoutInitTitle)

        ## Button Load Object ##
        self.getObjBlock = QWidget()
        self.layoutInitObj = QHBoxLayout()
        self.btnGetFiles = QPushButton("Get Object")
        self.btnGetFiles.setIcon(self.iconGuitare)
        self.btnGetFiles.clicked.connect(self.initfile)
        self.btnGetFiles.setStyleSheet('''
                                        border-style: outset;
                                        border-width: 2px;
                                        border-radius: 15px;
                                        border-color: black;
                                        padding: 4px;
                                        ''')

        self.titleMesh = QLabel(self.nameOfMesh)
        self.titleMesh.setFont(QFont(self.font, 10))
        self.layoutInitObj.addWidget(self.btnGetFiles)
        self.layoutInitObj.addWidget(self.titleMesh)
        self.layoutInitObj.addStretch(1)
        self.getObjBlock.setMaximumHeight(300)
        self.getObjBlock.setLayout(self.layoutInitObj)


        ## Button Load Texture ##
        self.layoutInitTexture = QHBoxLayout()

        self.btnGetTexture = QPushButton("Get Texture")
        self.btnGetTexture.clicked.connect(self.initTexture)
        self.btnGetTexture.setIcon(self.iconGuitare)
        self.btnGetTexture.setStyleSheet('''
                                                    border-style: outset;
                                                    border-width: 2px;
                                                    border-radius: 15px;
                                                    border-color: black;
                                                    padding: 4px;
                                                    ''')
        self.titleTexture = QLabel(self.nameOfTexture)
        self.titleTexture.setFont(QFont(self.font, 10))
        self.layoutInitTexture.addWidget(self.btnGetTexture)
        self.layoutInitTexture.addWidget(self.titleTexture)
        self.layoutInitTexture.addStretch(1)

        self.layoutInit.addWidget(self.getObjBlock)
        self.layoutInit.addLayout(self.layoutInitTexture)

        self.btnValidInit = QPushButton("Validate")
        self.btnValidInit.clicked.connect(self.init)
        self.btnValidInit.setStyleSheet('''
                                            border-style: outset;
                                            border-width: 2px;
                                            border-radius: 15px;
                                            border-color: black;
                                            padding: 4px;
                                            ''')
        self.layoutInit.addWidget(self.btnValidInit)

        self.menuInit.setLayout(self.layoutInit)


    def initfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.STL *.stl)")
        self.nameOfMesh = fname[0]
        self.meshIsValid = True
        self.titleMesh.setText(self.nameOfMesh)
        self.menuInit.update()

    def initTexture(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.vs *.fs *.jpg *.png)")
        self.nameOfTexture = fname[0]
        self.textureIsValid = True
        self.titleTexture.setText(self.nameOfTexture)
        print(self.nameOfTexture)
        print(self.nameOfTexture)
        self.menuInit.update()

    def getfile(self):
        self.layoutBox.removeWidget(self.openglWidget1)
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.STL *.stl)")
        self.nameOfMesh = fname[0]
        self.openglWidget1.clear()
        self.openglWidget1 = Core(self, self.nameOfMesh)
        self.layoutBox.addWidget(self.openglWidget1)

    def loadTexture(self):
        ##self.layoutBox.removeWidget(self.openglWidget1)
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.vs *.fs *.jpg *.png)")
        self.nameOfTexture = fname[0]
        self.openglWidget1.onChangeFile(self.nameOfTexture)
        self.openglWidget1.update()

    def BoxFilled(self) -> QVBoxLayout:
        self.layoutBox = QHBoxLayout()
        if self.meshIsValid and self.textureIsValid:
            self.layoutBox.removeWidget(self.menuInit)
            self.layoutBox.addWidget(self.menu)
            self.layoutBox.addWidget(self.openglWidget1)
            self.layoutBox.update()
            return self.layoutBox
        else:
            self.initObjectAndTexture()
            self.layoutBox.addWidget(self.menuInit)
            self.layoutBox.update()
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
