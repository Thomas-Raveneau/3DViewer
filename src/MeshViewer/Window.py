##
## KEIMYUNG PROJECT, 2021
## 3DViewer
## File description:
## Window
##

# --- IMPORTS ---

from types import MethodType
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget


# ---------------

class Window: 

    width: int
    height: int
    
    def __init__(self, mainWindow: QOpenGLWidget, width: int, height: int) -> None:
        self.width = width
        self.height = height
        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(mainWindow)
    
    def set_display_function(self, display_function: MethodType) -> None:
        glutDisplayFunc(display_function)
    
    def set_idle_function(self, idle_function: MethodType) -> None:
        glutIdleFunc(idle_function)
    
    def run_main_loop(self) -> None:
        glutMainLoop()
    
    def coordinates_system_handler(self) -> None:
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -10, 10, -5.0, 5.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
    
    def clear(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
    
    def swap_buffers(self) -> None:
        glutSwapBuffers()
