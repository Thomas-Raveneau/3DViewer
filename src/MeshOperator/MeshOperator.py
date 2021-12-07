##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Vertex
##

from typing import Any
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PyQt5.QtGui import QMatrix4x4

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex
from src.Mesh.Coordinate import Coordinates as coords

import numpy as np
import math

class MeshOperator:
    def __init__(self) -> None:
        self.m = QMatrix4x4()
        self.m.ortho(-1.5, 1.5, 1.5, -1.5, 4.0, 15.0)
        self.m.translate(0.0, 0.0, -10.0)
    
    def translate_mesh(self, translatingVertex: Vertex) -> None:
        t = QMatrix4x4(1, 0, 0, translatingVertex.x,
        0, 1, 0, translatingVertex.y,
        0, 0, 1, translatingVertex.z,
        0, 0, 0, 1)

        self.m = self.m * t

    def rotate_mesh_x(self, theta: float) -> None:

        theta = math.radians(theta)
        
        t = QMatrix4x4(1, 0, 0, 0,
        0, math.cos(theta), -math.sin(theta), 0,
        0, math.sin(theta), math.cos(theta), 0,
        0, 0, 0, 1)
        self.m = self.m * t

    def rotate_mesh_y(self, theta: float) -> None:
        theta = math.radians(theta)

        t = QMatrix4x4(math.cos(theta), 0, math.sin(theta), 0,
        0, 1, 0, 0,
        -math.sin(theta), 0, math.cos(theta), 0,
        0, 0, 0, 1)

        self.m = self.m * t

    def rotate_mesh_z(self, theta: float) -> None:
        theta = math.radians(theta)

        t = QMatrix4x4(math.cos(theta), -math.sin(theta), 0, 0,
        math.sin(theta), math.cos(theta), 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1)
        self.m = self.m * t

    def scale_mesh(self, scalingVertex: Vertex) -> None:
        t = QMatrix4x4(scalingVertex.x, 0, 0, 0,
        0, scalingVertex.y, 0, 0,
        0, 0, scalingVertex.z, 0,
        0, 0, 0, 1)

        self.m = self.m * t

    def reflect_mesh(self, coordReflect: coords) -> None:
        t = QMatrix4x4(1 + (-2 * (coordReflect == coords.X)), 0, 0, 0,
        0, 1 + (-2 * (coordReflect == coords.Y)), 0, 0,
        0, 0, 1 + (-2 * (coordReflect == coords.Z)), 0,
        0, 0, 0, 1)
        
        self.m = self.m * t
    
    def shear_mesh(self, shearTransform: 'tuple[float, float]', coordShear: coords) -> None:  
        t = QMatrix4x4(1, (coordShear == coords.Y) * shearTransform[0], (coordShear == coords.Z) * shearTransform[0], 0,
        (coordShear == coords.X) * shearTransform[0], 1, (coordShear == coords.Z) * shearTransform[1], 0,
        (coordShear == coords.X) * shearTransform[1], (coordShear == coords.Y) * shearTransform[1], 1, 0,
        0, 0, 0, 1)

        self.m = self.m * t

