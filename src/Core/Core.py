##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Core
##

# --- IMPORTS ---
from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL.raw.GLUT import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.sip import delete
from src.StlReader.StlReader import StlReader

from src.MeshViewer.Window import Window
from src.MeshViewer.MeshViewer import MeshViewer
from src.MeshOperator.MeshOperator import MeshOperator

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex
from src.Mesh.Coordinate import Coordinates as coords


# ---------------

class Core(QOpenGLWidget):
    viewer: MeshViewer
    operator: MeshOperator
    stl_reader: StlReader
    current_mesh: Mesh
    file: str

    def __init__(self, parent=None, file = '/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Stanford_Bunny_sample.stl') -> None:
        QOpenGLWidget.__init__(self, parent)
        self.file = file
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__loop)
        self.timer.start(0)

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        self.stl_reader = StlReader()
        ##self.window = Window('3D Viewer', 600, 600)
        self.viewer = MeshViewer()

        self.operator = MeshOperator()


    def paintGL(self) -> None:
        self.current_mesh = self.stl_reader.get_mesh_from_file(self.file)
        self.__loop()
        print("all operations ended")

    def resizeGL(self, w: int, h: int):
        glViewport(0, 0, 600, 600)


    def onChangeTranslate(self, vertex: Vertex)-> None:
        self.operator.translate_mesh(self.current_mesh, vertex)
    
    def onChangeRotateX(self, rotation: float)-> None:
        self.operator.rotate_mesh_x(self.current_mesh, rotation)
    
    def onChangeScale(self, vertex: Vertex)-> None:
        self.operator.scale_mesh(self.current_mesh, vertex)

    def __loop(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        self.viewer.draw_mesh(self.current_mesh)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -10, 10, -5.0, 5.0)

        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
        glFlush()

   