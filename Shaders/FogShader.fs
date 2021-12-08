#version 330 core

out vec4 fragmentColor;

in vec4 vertexColor;
uniform sampler2D texture;
varying mediump vec4 texc;

void main() {
    gl_FragColor = texture2D(texture, texc.st);
}