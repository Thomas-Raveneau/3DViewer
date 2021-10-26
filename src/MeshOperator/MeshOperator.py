##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Vertex
##

from ctypes import Array
from typing import Any
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex
from src.Mesh.Coordinate import Coordinates as coords

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
            #print("l before =", l)
            ret = np.dot(t, l)
            #print("l then =", ret)
            vertex.set_coordinates(ret[0], ret[1], ret[2])

    def rotate_mesh_x(self, mesh: Mesh, theta: float) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.rotate_face_x(face, math.radians(theta))


    def rotate_face_y(self, vertices: 'list[Vertex]', theta: float) -> None:
        t = np.array([[math.cos(theta), 0, math.sin(theta), 0],
        [0, 1, 0, 0],
        [-math.sin(theta), 0, math.cos(theta), 0],
        [0, 0, 0, 1]])
        for vertex in vertices:
            l = np.array([vertex.x, vertex.y, vertex.z, 1])
            #print("l before =", l)
            ret = np.dot(t, l)
            #print("l then =", ret)
            vertex.set_coordinates(ret[0], ret[1], ret[2])

    def rotate_mesh_y(self, mesh: Mesh, theta: float) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.rotate_face_y(face, math.radians(theta))

    def rotate_face_z(self, vertices: 'list[Vertex]', theta: float) -> None:
        t = np.array([[math.cos(theta), -math.sin(theta), 0, 0],
        [math.sin(theta), math.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
        for vertex in vertices:
            l = np.array([vertex.x, vertex.y, vertex.z, 1])
            #print("l before =", l)
            ret = np.dot(t, l)
            #print("l then =", ret)
            vertex.set_coordinates(ret[0], ret[1], ret[2])

    def rotate_mesh_z(self, mesh: Mesh, theta: float) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.rotate_face_z(face, math.radians(theta))
    
    def scale_face(self, vertices: 'list[Vertex]', scaleVertex: Vertex) -> None:
        t = np.array([[scaleVertex.x, 0, 0, 0],
        [0, scaleVertex.y, 0, 0],
        [0, 0, scaleVertex.z, 0],
        [0, 0, 0, 1]])
        for vertex in vertices:
            l = np.array([vertex.x, vertex.y, vertex.z, 1])
            l = np.dot(t, l)
            vertex.set_coordinates(l[0], l[1], l[2])

    def scale_mesh(self, mesh: Mesh, scalingVertex: Vertex) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()

        for face in faces:
            self.scale_face(face, scalingVertex)

    def reflect_face(self, vertices: 'list[Vertex]', reflectMatrix: Any) -> None:
        for vertex in vertices:
            l = np.array([vertex.x, vertex.y, vertex.z, 1])
            l = np.dot(reflectMatrix, l)
            vertex.set_coordinates(l[0], l[1], l[2])

    def reflect_mesh(self, mesh: Mesh, coordReflect: coords) -> None:
        faces: list[list[Vertex]] = mesh.get_faces()
        t = np.array([[1 + (-2 * (coordReflect == coords.X)), 0, 0, 0],
        [0, 1 + (-2 * (coordReflect == coords.Y)), 0, 0],
        [0, 0, 1 + (-2 * (coordReflect == coords.Z)), 0],
        [0, 0, 0, 1]])
        for face in faces:
            self.reflect_face(face, t)
