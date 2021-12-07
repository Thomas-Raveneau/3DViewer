##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Core
##

# --- IMPORTS ---
from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL.raw.GLUT import *
from PyQt5.QtWidgets import QOpenGLWidget
from src.StlReader.StlReader import StlReader
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QImage, QOpenGLShaderProgram, QOpenGLTexture, QOpenGLVersionProfile, QOpenGLShader
from PyQt5.QtWidgets import QOpenGLWidget
from src.Mesh.Shader import Shader
from src.StlReader.StlReader import StlReader

from OpenGL.GLUT import *
from OpenGL.GLU import *

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
    
    left = -20
    right = 20
    bottom = -15
    top = 15
    near = -20
    far = 20
    
    PROGRAM_VERTEX_ATTRIBUTE, PROGRAM_TEXCOORD_ATTRIBUTE = range(2)

    def __init__(self, parent=None, meshFile = '/home/jeanningros/Bureau/Keimyung/ComputerGraph/3DViewer/Objects/Stanford_Bunny_sample.stl', textureFile = 'Shaders/bricks.jpg') -> None:
        super(Core, self).__init__(parent)
        
        self.meshFile = meshFile
        self.textureFile = textureFile
        self.clearColor = QColor(Qt.white)
        self.width = self.right - self.left
        self.height = self.top - self.bottom
        self.depth = self.far - self.near
        
    def initializeGL(self):
        version_profile = QOpenGLVersionProfile()
        version_profile.setVersion(2, 0)
        self.gl = self.context().versionFunctions(version_profile)
        self.gl.initializeOpenGLFunctions()
        
        self.gl.glOrtho(self.left, self.right, self.bottom, self.top, self.near, self.far)

        self.stl_reader = StlReader()        
        
        filename = "Shaders/FogShader"        

        self.program = QOpenGLShaderProgram()
        
        self.program.addShaderFromSourceFile(QOpenGLShader.Vertex, filename + '.vs')
        self.program.addShaderFromSourceFile(QOpenGLShader.Fragment, filename + '.fs')
        
        self.vertices, self.texCoords, self.draw_count = self.stl_reader.get_mesh_from_file(self.meshFile, self.width, self.height, self.depth)
        
        self.updateMesh()

        self.texture = QOpenGLTexture(QImage(self.textureFile))

        self.program.setUniformValue('texture', 0)

        self.operator = MeshOperator()

    def updateMesh(self)-> None:
        self.draw_count = len(self.vertices)
        
        self.program.bindAttributeLocation('vertex',
                self.PROGRAM_VERTEX_ATTRIBUTE)
        self.program.bindAttributeLocation('texCoord',
                self.PROGRAM_TEXCOORD_ATTRIBUTE)
        
        self.program.link()
        self.program.bind()
        
        self.program.enableAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE)
        self.program.enableAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE)
        
        self.program.setAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE, self.vertices)
        self.program.setAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE, self.texCoords)

    def paintGL(self)-> None:
        self.__loop()

    def resizeGL(self, w: int, h: int):
        glViewport(0, 0, w, h)

    # -Change State Function- #
    def onChangeTranslate(self, vertex: Vertex)-> None:
        new_vertex = Vertex(vertex.x / self.width, vertex.y / self.height, vertex.z / self.depth)
        self.operator.translate_mesh(new_vertex)
    
    def onChangeRotateX(self, rotation: float)-> None:
        self.operator.rotate_mesh_x(rotation)
        
    def onChangeRotateY(self, rotation: float)-> None:
        self.operator.rotate_mesh_y(rotation)
    
    def onChangeRotateZ(self, rotation: float)-> None:
        self.operator.rotate_mesh_z(rotation)
    
    def onChangeScale(self, vertex: Vertex)-> None:
        self.operator.scale_mesh(vertex)
    
    def onChangeFile(self, textureFile: str)-> None:
        self.textureFile = textureFile
        self.texture = QOpenGLTexture(QImage(self.textureFile))
    
    def onChangeReflect(self, coordReflect: coords)-> None:
        self.operator.reflect_mesh(coordReflect)

    def clear(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
    ## Loop ##
    def __loop(self) -> None:
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)

        self.gl.glClearColor(self.clearColor.redF(), self.clearColor.greenF(),
                self.clearColor.blueF(), self.clearColor.alphaF())
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        
        self.program.setUniformValue('matrix', self.operator.m)
        
        self.texture.bind()
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, 0, self.draw_count)
