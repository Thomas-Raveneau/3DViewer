##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# StlReader
##

# --- IMPORTS ---

from PyQt5.QtGui import QAbstractOpenGLFunctions, QOpenGLShaderProgram
from stl import mesh
import numpy as np

from src.Mesh.Mesh import Mesh


# ---------------


class StlReader:

    def __init__(self) -> None:
        print('StlReader created.')

    def __del__(self) -> None:
        print('StlReader destroyed')

    def get_mesh_from_file(self, file_fullpath: str, width: int, height: int, depth: int) -> Mesh:
        stl_mesh = mesh.Mesh.from_file(file_fullpath)

        verticesRaw = np.row_stack((stl_mesh.v0, stl_mesh.v1, stl_mesh.v2))
        draw_count = len(verticesRaw)

        vertices = []
        texCoords = []

        for vertex in verticesRaw:
            new_vertex = [vertex[0] / width, vertex[1] / height, vertex[2] / depth]

            maxPoint = max(new_vertex[0], new_vertex[1], new_vertex[2])
            minPoint = min(new_vertex[0], new_vertex[1], new_vertex[2])
            
            divisor = (maxPoint - minPoint) if (maxPoint - minPoint) != 0 else minPoint 
            
            new_texCoord = [new_vertex[0] / divisor, new_vertex[1] / divisor, new_vertex[2] / divisor]
            vertices.append(new_vertex)
            texCoords.append(new_texCoord)
        return vertices, texCoords, draw_count