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

    def get_mesh_from_file(self, file_fullpath: str, program : QOpenGLShaderProgram, gl : QAbstractOpenGLFunctions) -> Mesh:
        stl_mesh = mesh.Mesh.from_file(file_fullpath)

        vertices = np.row_stack((stl_mesh.v0, stl_mesh.v1, stl_mesh.v2))
        
        return Mesh(vertices, program, gl)
