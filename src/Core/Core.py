##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Core
##

# --- IMPORTS ---
from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL.raw.GLUT import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QOpenGLContext, QOpenGLVersionProfile
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.sip import delete
from src.Mesh.Shader import Shader
from src.StlReader.StlReader import StlReader

from OpenGL.GLUT import *
from OpenGL.GLU import *

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
    shader: Shader

    def __init__(self, parent=None, file = '/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Stanford_Bunny_sample.stl') -> None:
        super(Core, self).__init__(parent)
        
        self.file = file
        self.clearColor = QColor(Qt.white)
        

    def initializeGL(self):
        print("initializing GL")
        version_profile = QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl = self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()
        
        self.stl_reader = StlReader()
        
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        
        self.shader = Shader("Shaders/basicShader", self.gl, self)
        self.shader = Shader("Shaders/FogShader", self.gl, self)
        self.current_mesh = self.stl_reader.get_mesh_from_file(self.file, self.shader._program, self.gl)

        self.viewer = MeshViewer()
        self.operator = MeshOperator()


    def paintGL(self) -> None:
        if (self.current_mesh == None):
            self.current_mesh = self.stl_reader.get_mesh_from_file(self.file, self.shader._program, self.gl)
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
        print("looping")
        self.gl.glClearColor(self.clearColor.redF(), self.clearColor.greenF(),
                self.clearColor.blueF(), self.clearColor.alphaF())
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()

        self.viewer.draw_mesh(self.current_mesh, self.gl)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-10, 10, -10, 10, -10.0, 10.0)

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glLoadIdentity()
        self.gl.glFlush()

   