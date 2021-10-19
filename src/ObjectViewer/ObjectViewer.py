##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## ObjectViewer
##

# --- IMPORTS ---

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from src.Object.Object import Object
from src.Object.Vertex import Vertex

# ---------------

class ObjectViewer:

    def __init__(self) -> None:
        pass

    def draw_quad(self, vertices: list[Vertex]) -> None:
        glColor3d(0, 0, 0);
        glBegin(GL_POLYGON);

        for vertex in vertices:
            glVertex2d(vertex.x, vertex.y, vertex.z);

        glEnd();
    
