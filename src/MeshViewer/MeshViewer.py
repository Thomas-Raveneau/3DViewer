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

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex

# ---------------

class MeshViewer:

    def __init__(self) -> None:
        pass

    def draw_quad(self, quad_vertices: 'list[Vertex]') -> None:
        glColor3d(0, 1, 0);
        glBegin(GL_POLYGON);

        for vertex in quad_vertices:
            glVertex3d(vertex.x, vertex.y, vertex.z)

        glEnd();
    
    def draw_triangle(self, triangle_vertices: 'list[Vertex]') -> None:
        glColor3d(0, 1, 0);
        glBegin(GL_TRIANGLES);

        for vertex in triangle_vertices:
            glVertex3d(vertex.x, vertex.y, vertex.z)

        glEnd();

    def draw_mesh(self, mesh: Mesh) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.draw_triangle(face)
    
