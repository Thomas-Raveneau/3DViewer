##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Object
##

# --- IMPORTS ---

from .Vertex import Vertex

# ---------------

class Object:

    vertices: list[Vertex] = []

    def __init__(self, vertices: list[list[float]]) -> None:
        print('Object created.')
        
        for vertex in vertices:
            new_vertex = Vertex(vertex[0], vertex[1], vertex[2])
            self.vertices.append(new_vertex)
        