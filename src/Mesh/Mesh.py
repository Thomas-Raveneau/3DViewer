##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# Mesh
##

# --- IMPORTS ---

from ctypes import sizeof, c_float, pointer
from enum import IntEnum
from OpenGL.arrays.arraydatatype import GLuintArray
from OpenGL.raw.GL.VERSION.GL_1_5 import GL_ARRAY_BUFFER, GL_STATIC_DRAW, glBindBuffer, glBufferData, glGenBuffers
from OpenGL.raw.GL.VERSION.GL_2_0 import glEnableVertexAttribArray, glVertexAttribPointer
from OpenGL.raw.GL.VERSION.GL_3_0 import GL_FLOAT_32_UNSIGNED_INT_24_8_REV, glBindVertexArray, glGenVertexArrays
from OpenGL.GL import GLuint, GL_FLOAT, GL_FALSE
from OpenGL.raw.GL.VERSION.GL_4_5 import glVertexArrayAttribFormat
from PyQt5.QtGui import QAbstractOpenGLFunctions, QImage, QOpenGLShaderProgram, QOpenGLTexture
from PyQt5.QtCore import QFileInfo
from .Vertex import Vertex

import OpenGL.GL as GL

import math as m

import numpy as np

# ---------------


class Mesh:

    PROGRAM_VERTEX_ATTRIBUTE, PROGRAM_TEXCOORD_ATTRIBUTE = range(2)

    vertices: 'list[Vertex]'= []
    positions: 'list[list[float]]'= []
    texCoords: 'list[list[float]]' = []
    _vao: GLuint
    _vab: 'list[GLuint]' = []
    _program: QOpenGLShaderProgram

    def __init__(self, vertices: 'list[list[float]]', program : QOpenGLShaderProgram, gl : QAbstractOpenGLFunctions) -> None:
        print('Mesh created.')
        self._program = program
        self.gl = gl
        
        self.draw_count = len(vertices)

        positions = []
        texCoords = []

        for vertex in vertices:
            new_vertex = vertex * 0.2
            new_vertex = [new_vertex[0], new_vertex[1], new_vertex[2] + 1]
            new_vertex = vertex
            print("New Vertex = ", new_vertex)

            maxPoint = max(new_vertex[0], new_vertex[1], new_vertex[2])
            minPoint = min(new_vertex[0], new_vertex[1], new_vertex[2])
            
            divisor = (maxPoint - minPoint) if (maxPoint - minPoint) != 0 else minPoint 
            
            new_texCoord = [new_vertex[0] / divisor, new_vertex[1] / divisor, new_vertex[2] / divisor]
            self.positions.append(new_vertex)
            self.vertices.append(Vertex(new_vertex[0], new_vertex[1], new_vertex[2]))
            self.texCoords.append(new_texCoord)
        
        print("nb Vertex =", len(vertices))

        print("nb triangles =", len(vertices) / 3)
        
        print("nb faces =", len(vertices) / 3 / 2)
        
        self.texture = QOpenGLTexture(QImage('Shaders/bricks.jpg'))

        self._program.bindAttributeLocation('vertex',
                self.PROGRAM_VERTEX_ATTRIBUTE)
        self._program.bindAttributeLocation('texCoord',
                self.PROGRAM_TEXCOORD_ATTRIBUTE)
        
        self._program.link()
        self._program.bind()
        self._program.setUniformValue('texture', 0)
        
        self._program.enableAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE)
        self._program.enableAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE)
        
        self._program.setAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE, self.positions)
        self._program.setAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE, self.texCoords)
    
    def update(self) -> None:
        self._program.setAttributeArray(self.PROGRAM_VERTEX_ATTRIBUTE, self.positions)
        self._program.setAttributeArray(self.PROGRAM_TEXCOORD_ATTRIBUTE, self.texCoords)


    def get_faces(self) -> 'list[list[Vertex]]':
        length: int = len(self.vertices)
        nb_faces: int = length // 3 #Stl file are only composed of triangles

        return (np.array_split(self.vertices, nb_faces))