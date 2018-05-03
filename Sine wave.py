from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import arange,sin,pi

def draw():
    glColor(1,1,1)
    glLineWidth(5)
    freq=2
    peak=0.5

    glBegin(GL_LINES)
    for x in arange(-1,1,0.001):
        y=peak*sin(freq*2*pi*x)
        glVertex2d(x, 0)
        glVertex2d(x,y)
    glEnd()

    glFlush()




glutInit()
glutInitWindowSize(500,500)
glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
glutCreateWindow(b"Title")
glutDisplayFunc(draw)
glutMainLoop()