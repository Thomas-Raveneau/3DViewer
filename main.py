##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# main
##

# --- IMPORTS ---

from logging import debug
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from src.Ui.Ui import Ui
from src.Mesh.Shader import Shader
from PyQt5.QtGui import QOpenGLContext



# class RenderWindow(QWindow):
#     def __init__(self, format: QSurface):
#         super(RenderWindow, self).__init__()
#         self.setSurfaceType(QWindow.OpenGLSurface)
#         self.setFormat(format)
#         self._context = QOpenGLContext(self.mainWidget)
#         self._context.setFormat(self.requestedFormat())
#         if not self._context.create():
#             raise Exception("Unable to create GL Context")
#         self.program = None
#         self.timer = None
#         self.angle = 0
    
#     def initGL(self, filename : str):
#         self.program = QOpenGLShaderProgram(self)
        
#         if not self.program.addShaderFromSourceFile(QOpenGLShader.Vertex, filename + '.vs'):
#             raise Exception("Vertex shader could not be added: {} ({})".format(self.program.log(), filename))
#         if not self.program.addShaderFromSourceFile(QOpenGLShader.Fragment, filename + '.fs'):
#             raise Exception("Fragment shader could not be added: {} ({})".format(self.program.log(), filename))
#         if not self.program.link():
#             raise Exception("Could not link shaders: {}".format(self.program.log()))*
        

# class MainWidget(QWidget):
#     def __init__(self):
#         super(MainWidget, self).__init__()
#         self.renderWindow = RenderWindow(QSurfaceFormat())
#         container = QWidget.createWindowContainer(self.renderWindow)
#         container.setMinimumSize(QSize(600, 600)) 
        
class MainWindow(QMainWindow):
    _context : QOpenGLContext
    _shader : Shader
    _gl : QAbstractOpenGLFunctions
    
    def __init__(self, file="/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Menger_sponge_sample.stl", parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui(file)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.ui.BoxFilled())
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle("BWC Project")
        self.setGeometry(0, 0, 1500, 1000)


        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")

    file = None
    if (len(sys.argv) > 1):
        file = sys.argv[1]
    w = MainWindow(file)
    w.show()
    sys.exit(app.exec_())