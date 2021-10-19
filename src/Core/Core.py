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

from src.Mesh.Mesh import Mesh
from src.Mesh.Vertex import Vertex

# ---------------

class Core:

    window: Window
    viewer: MeshViewer
    stl_reader: StlReader
    current_mesh: Mesh

    def __init__(self) -> None:
        self.stl_reader = StlReader()
        self.window = Window('3D Viewer', 600, 600)
        self.viewer = MeshViewer()

    def run(self) -> None:
        
        self.current_mesh = self.stl_reader.get_mesh_from_file('C:/Users/thoma/Desktop/dev_software/3DViewer/Objects/Cube.stl')

        self.window.set_display_function(self.__loop)
        self.window.set_idle_function(self.__loop)
        self.window.run_main_loop()

    def __loop(self) -> None:
        self.window.clear()

        self.viewer.draw_mesh(self.current_mesh)

        self.window.coordinates_system_handler()
        self.window.swap_buffers()