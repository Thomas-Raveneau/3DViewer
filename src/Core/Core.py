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
from PyQt5.QtGui import QColor, QImage, QMatrix4x4, QOpenGLContext, QOpenGLShaderProgram, QOpenGLTexture, QOpenGLVersionProfile, QOpenGLShader
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
    
    vsrc = """
attribute highp vec4 vertex;
attribute mediump vec4 texCoord;
varying mediump vec4 texc;
uniform mediump mat4 matrix;
void main(void)
{
    gl_Position = matrix * vertex;
    texc = texCoord;
}
"""

    fsrc = """
uniform sampler2D texture;
varying mediump vec4 texc;
void main(void)
{
    gl_FragColor = texture2D(texture, texc.st);
}
"""
    
    coords = (
        (( +1, -1, -1 ), ( -1, -1, -1 ), ( -1, +1, -1 ), ( +1, +1, -1 )),
        (( +1, +1, -1 ), ( -1, +1, -1 ), ( -1, +1, +1 ), ( +1, +1, +1 )),
        (( +1, -1, +1 ), ( +1, -1, -1 ), ( +1, +1, -1 ), ( +1, +1, +1 )),
        (( -1, -1, -1 ), ( -1, -1, +1 ), ( -1, +1, +1 ), ( -1, +1, -1 )),
        (( +1, -1, +1 ), ( -1, -1, +1 ), ( -1, -1, -1 ), ( +1, -1, -1 )),
        (( -1, -1, +1 ), ( +1, -1, +1 ), ( +1, +1, +1 ), ( -1, +1, +1 ))
    )
    
    PROGRAM_VERTEX_ATTRIBUTE, PROGRAM_TEXCOORD_ATTRIBUTE = range(2)

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
        
        self.createObject()
        self.draw_count = len(self.vertices)

#        self.stl_reader = StlReader()
        
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        
        #self.shader = Shader("Shaders/FogShader", self.gl, self)

        # self.shader = Shader("Shaders/basicShader", self.program)
        filename = "Shaders/basicShader"
        filename = "Shaders/FogShader"        

        vshader = QOpenGLShader(QOpenGLShader.Vertex, self)
        vshader.compileSourceCode(self.vsrc)

        fshader = QOpenGLShader(QOpenGLShader.Fragment, self)
        fshader.compileSourceCode(self.fsrc)

        self.program = QOpenGLShaderProgram()
        
        self.program.addShader(vshader)
        self.program.addShader(fshader)
        
        #self.program.addShaderFromSourceFile(QOpenGLShader.Vertex, filename + '.vs')
        #self.program.addShaderFromSourceFile(QOpenGLShader.Fragment, filename + '.fs')
        
        # self.current_mesh = self.stl_reader.get_mesh_from_file(self.file, self.program)
        
        self.texture = QOpenGLTexture(QImage('Shaders/bricks.jpg'))

        self.program.bindAttributeLocation('vertex',
                self.PROGRAM_VERTEX_ATTRIBUTE)
        self.program.bindAttributeLocation('texCoord',
                self.PROGRAM_TEXCOORD_ATTRIBUTE)
        
        self.program.link()
        self.program.bind()
        self.program.setUniformValue('texture', 0)
        
        print(self.vertices)
        self.program.enableAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE)
        self.program.enableAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE)
        
        self.program.setAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE, self.vertices)
        self.program.setAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE, self.texCoords)
        
        # self.viewer = MeshViewer()
        self.operator = MeshOperator()


    def paintGL(self) -> None:
        # if (self.current_mesh == None):
        #     self.current_mesh = self.stl_reader.get_mesh_from_file(self.file, self.program)
        self.__loop()
        print("all operations ended")

    def resizeGL(self, w: int, h: int):
        glViewport(0, 0, 600, 600)

    def createObject(self):
        self.texCoords = []
        self.vertices = []

        for i in range(6):

            for j in range(4):
                self.texCoords.append(((j == 0 or j == 3), (j == 0 or j == 1)))

                x, y, z = self.coords[i][j]
                self.vertices.append((0.2 * x, 0.2 * y, 0.2 * z))

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
        # self.gl.glLoadIdentity()


        m = QMatrix4x4()
        m.ortho(-1.5, 1.5, 1.5, -1.5, 4.0, 15.0)
        m.translate(0.0, 0.0, -10.0)
        
        self.program.setUniformValue('matrix', m)
        
        self.texture.bind()
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, 0, self.draw_count)
        
        #self.viewer.draw_mesh(self.current_mesh, self.gl)
        # self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        # self.gl.glLoadIdentity()
        # self.gl.glOrtho(-100, 100, -100, 100, -100.0, 100.0)

        # self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        # self.gl.glLoadIdentity()
        #self.gl.glFlush()

   