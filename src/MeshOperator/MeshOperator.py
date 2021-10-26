##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Vertex
##

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex

import numpy as np
import math

class MeshOperator:
    def __init__(self) -> None:
        pass

    def translate_face(self, vertices: 'list[Vertex]', translatingVertex: Vertex) -> None:
        t = np.array([[1, 0, 0, translatingVertex.x],
        [0, 1, 0, translatingVertex.y],
        [0, 0, 1, translatingVertex.z],
        [0, 0, 0, 1]])
        for vertex in vertices:
            l = np.array([vertex.x, vertex.y, vertex.z, 1])
            l = np.dot(t, l)
            vertex.set_coordinates(l[0], l[1], l[2])
    
    def translate_mesh(self, mesh: Mesh, translatingVertex: Vertex) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.translate_face(face, translatingVertex)

    def rotate_face_x(self, vertices: 'list[Vertex]', theta: float) -> None:
        t = np.array([[1, 0, 0, 0],
        [0, math.cos(theta), -math.sin(theta), 0],
        [0, math.sin(theta), math.cos(theta), 0],
        [0, 0, 0, 1]])
        for vertex in vertices:
            l = np.array([vertex.x, vertex.y, vertex.z, 1])
            l = np.dot(t, l)
            print(l)
            vertex.set_coordinates(l[0], l[1], l[2])

    def rotate_mesh_x(self, mesh: Mesh, theta: float) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.rotate_face_x(face, math.radians(theta))
