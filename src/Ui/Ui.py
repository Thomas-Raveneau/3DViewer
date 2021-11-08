
from PyQt5.QtWidgets import *
from src.Ui.ButtonCustom import ButtonCustom
from src.Mesh.Vertex import Vertex
from src.Core.Core import Core


class Ui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layoutBox =  QVBoxLayout()
        self.layoutMenu =  QHBoxLayout()

        ## Dial ##
        self.dial = QDial(self)
        self.layoutMenu.addWidget(self.dial)


        ## Translate ##
        self.rotateButton = ButtonCustom(self, "Translate")
        self.rotateButton.clicked.connect(self.buttonTranslate)
        self.layoutMenu.addWidget(self.rotateButton)

        ## Rotate ##
        self.translateButton = ButtonCustom(self, "Rotate")
        self.translateButton.clicked.connect(self.buttonRotate)
        self.layoutMenu.addWidget(self.translateButton)

        ## Scale ##
        self.Button1 = ButtonCustom(self, "Scalling")
        self.Button1.clicked.connect(self.buttonScale)
        self.layoutMenu.addWidget(self.Button1)


        self.openglWidget1 = Core(self, "/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Menger_sponge_sample.stl")
    
    def BoxFilled(self) -> QVBoxLayout:
        self.layoutBox.addLayout(self.layoutMenu)
        self.layoutBox.addWidget(self.openglWidget1)
        return self.layoutBox

    def buttonTranslate(self):
        print("button Translate")
        self.openglWidget1.onChangeTranslate(Vertex(-60, 30, 50))
        self.openglWidget1.update()

    def buttonRotate(self):
        print("button Rotate")
        self.openglWidget1.onChangeRotateX(-90)
        self.openglWidget1.update()

    def buttonScale(self):
        print("button Scale")
        self.openglWidget1.onChangeScale(Vertex(2, 2, 2))
        self.openglWidget1.update()

