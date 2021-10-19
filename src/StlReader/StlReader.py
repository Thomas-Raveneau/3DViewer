##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# StlReader
##

# --- IMPORTS ---

from stl import mesh
import numpy as np

from src.Mesh.Mesh import Mesh


# ---------------


class StlReader:

    def __init__(self) -> None:
        print('StlReader created.')

    def __del__(self) -> None:
        print('StlReader destroyed')

    def get_mesh_from_file(self, file_fullpath: str) -> Mesh:
        stl_mesh = mesh.Mesh.from_file(file_fullpath)

        vertices = np.row_stack((stl_mesh.v0, stl_mesh.v1, stl_mesh.v2))
        # unique_vertices = np.unique(vertices, axis = 0)
        
        return Mesh(vertices)
