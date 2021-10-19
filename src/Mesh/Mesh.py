##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# Mesh
##

# --- IMPORTS ---

from .Vertex import Vertex

import numpy as np

# ---------------


class Mesh:

    vertices: list[Vertex] = []

    def __init__(self, vertices: list[list[float]]) -> None:
        print('Mesh created.')

        for vertex in vertices:
            new_vertex = Vertex(vertex[0], vertex[1], vertex[2])
            self.vertices.append(new_vertex)
    
    def get_faces(self) -> list[list[Vertex]]:
        length: int = len(self.vertices)
        nb_faces: int = length // 3 #Stl file are only composed of triangles

        return (np.array_split(self.vertices, nb_faces))


