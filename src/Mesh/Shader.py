##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Shader
##

from typing import List
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.raw.GL.VERSION.GL_2_0 import glAttachShader
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
from PyQt5.QtGui import (QOpenGLBuffer, QOpenGLShaderProgram, QOpenGLShader, QOpenGLVersionProfile)
from PyQt5.QtWidgets import QOpenGLWidget

class Shader():
    _shaders : 'list[GLuint]'
    _gl: QOpenGLVersionProfile

    def __init__(self, filename : str, program: QOpenGLShaderProgram,) -> None:
        print("Initializing Shader")
        
        program.addShaderFromSourceFile(QOpenGLShader.Vertex, filename + '.vs')
        program.addShaderFromSourceFile(QOpenGLShader.Fragment, filename + '.fs')
