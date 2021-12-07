#version 330 core
layout (location = 0) in vec3 aPos;

out vec4 vertexColor;
attribute highp vec4 vertex;
attribute mediump vec4 texCoord;
varying mediump vec4 texc;
uniform mediump mat4 matrix;

void main() {
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
    gl_Position = matrix * vertex;
    texc = texCoord;
    vertexColor = vec4(gl_Position.z, gl_Position.z, gl_Position.z, 1.0);
}
