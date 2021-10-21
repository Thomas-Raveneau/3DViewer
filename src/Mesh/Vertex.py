##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Vertex
##

# TUPLE UTILS
X = 0
Y = 1
Z = 2

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
        self.vertex = (coords[X], coords[Y], coords[Z])
        self.x = coords[X]
        self.y = coords[Y]
        self.z = coords[Z]

    def set_coordinates(self, x: float, y: float, z: float) -> None:
        self.vertex = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return 'Vertex: ({:5.2f}, {:5.2f}, {:5.2f})'.format(self.x, self.y, self.z)

    