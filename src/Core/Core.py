##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Core
##

# --- IMPORTS ---
from src.StlReader.StlReader import StlReader

from src.MeshViewer.Window import Window
from src.MeshViewer.MeshViewer import MeshViewer
from src.MeshOperator.MeshOperator import MeshOperator

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex
from src.Mesh.Coordinate import Coordinates as coords


# ---------------

class Core:

    window: Window
    viewer: MeshViewer
    operator: MeshOperator
    stl_reader: StlReader
    current_mesh: Mesh
    file: str

    def __init__(self, file = 'C:/Users/thoma/Desktop/dev_software/3DViewer/Objects/Cube.stl') -> None:
        self.stl_reader = StlReader()
        self.window = Window('3D Viewer', 600, 600)
        self.viewer = MeshViewer()
        self.operator = MeshOperator()
        self.file = file

    def run(self) -> None:
        
        self.current_mesh = self.stl_reader.get_mesh_from_file(self.file)

        self.window.set_display_function(self.__loop)
        self.window.set_idle_function(self.__loop)
        translatingVertex = Vertex(2, 0, 0)
        self.operator.translate_mesh(self.current_mesh, translatingVertex)
        self.operator.rotate_mesh_z(self.current_mesh, 30)
        scalingVertex = Vertex(1.5, 2, 1.5)
        self.operator.scale_mesh(self.current_mesh, scalingVertex)
        self.operator.reflect_mesh(self.current_mesh, coords.X)
        self.window.run_main_loop()

    def __loop(self) -> None:
        self.window.clear()

        self.viewer.draw_mesh(self.current_mesh)

        self.window.coordinates_system_handler()
        self.window.swap_buffers()