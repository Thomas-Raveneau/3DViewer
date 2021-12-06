##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## MeshViewer
##

# --- IMPORTS ---

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
from PyQt5.QtGui import QAbstractOpenGLFunctions

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex

import numpy as np

# ---------------

class MeshViewer:

    def __init__(self) -> None:
        pass

    def draw_mesh(self, mesh: Mesh, gl: QAbstractOpenGLFunctions) -> None:
        print("Drawing mesh")
        mesh.texture.bind()
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, mesh.draw_count)
        #gl.glBindVertexArray(0)
    
