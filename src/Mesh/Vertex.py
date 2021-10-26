##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Vertex
##

# TUPLE UTILS
from src.Mesh.Coordinate import Coordinates as cords

class Vertex:

    vertex : 'tuple[float]'
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.vertex = (x, y, z)
        self.x = x
        self.y = y
        self.z = z
    
    def set_coordinates(self, coords: 'tuple[float]') -> None:
        self.vertex = (coords[cords.X], coords[cords.Y], coords[cords.Z])
        self.x = coords[cords.X]
        self.y = coords[cords.Y]
        self.z = coords[cords.Z]

    def set_coordinates(self, x: float, y: float, z: float) -> None:
        self.vertex = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return 'Vertex: ({:5.2f}, {:5.2f}, {:5.2f})'.format(self.x, self.y, self.z)

    