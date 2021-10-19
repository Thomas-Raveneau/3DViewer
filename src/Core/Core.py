##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Core
##

# --- IMPORTS ---
from src.StlReader.StlReader import StlReader

from src.ObjectViewer.Window import Window
from src.ObjectViewer.ObjectViewer import ObjectViewer

from src.Object.Object import Object
from src.Object.Vertex import Vertex

# ---------------

class Core:

    window: Window
    viewer: ObjectViewer
    stl_reader: StlReader

    def __init__(self) -> None:
        self.stl_reader = StlReader()
        self.window = Window('3D Viewer', 600, 600)
        self.viewer = ObjectViewer()

    def run(self) -> None:
        self.window.set_display_function(self.__loop)
        self.window.set_idle_function(self.__loop)
        self.window.run_main_loop()

    def __loop(self) -> None:
        self.window.clear()


        self.window.swap_buffers()