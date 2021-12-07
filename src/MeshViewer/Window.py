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
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtWidgets import QOpenGLWidget, QWidget



# ---------------

class Window(QWidget): 

    width: int
    height: int
    
    def __init__(self, mainWindow: QOpenGLWidget, width: int, height: int, parent: QWidget = None) -> None:
        
        self.width = width
        self.height = height

        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        
        glutInitContextVersion(3, 3)
        glutInitContextProfile(GLUT_CORE_PROFILE)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(mainWindow)
    
    def set_display_function(self, display_function: MethodType) -> None:
        glutDisplayFunc(display_function)
    
    def set_idle_function(self, idle_function: MethodType) -> None:
        glutIdleFunc(idle_function)
    
    def run_main_loop(self) -> None:
        if (self._context == None):
            self._context = QOpenGLContext(self)
            self._context.create()
        self._context.makeCurrent()
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
