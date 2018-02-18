from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
def Draw ():
    #Body
    glColor(0,0.4,0.8)
    glBegin(GL_POLYGON)
    glVertex2d(0.5,0.1)
    glVertex2d(0.5,-0.5)
    glVertex2d(-0.5,-0.5)
    glVertex2d(-0.5,0.1)
    glEnd()
    
    #Head
    glBegin(GL_POLYGON)
    glVertex2d(0.4, 0.35)
    glVertex2d(0.4, 0.9)
    glVertex2d(-0.4, 0.9)
    glVertex2d(-0.4, 0.35)
    glEnd()
    
    #RightHand
    glColor(0.82, 0.82, 0.82)
    glBegin(GL_POLYGON)
    glVertex2d(0.5,0.0)
    glVertex2d(0.6,0.0)
    glVertex2d(0.6,-0.15)
    glVertex2d(0.5,-0.15)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.6,-0.15)
    glVertex2d(0.7,-0.15)
    glVertex2d(0.7,0.4)
    glVertex2d(0.6,0.4)
    glEnd()
    
    #LeftHand
    glColor(0.82, 0.82, 0.82)
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, 0.0)
    glVertex2d(-0.6, 0.0)
    glVertex2d(-0.6, -0.15)
    glVertex2d(-0.5, -0.15)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.6, -0.15)
    glVertex2d(-0.7, -0.15)
    glVertex2d(-0.7, 0.4)
    glVertex2d(-0.6, 0.4)
    glEnd()
    
    #RightLeg
    glBegin(GL_POLYGON)
    glVertex2d(0.2, -0.5)
    glVertex2d(0.2, -0.8)
    glVertex2d(0.36, -0.8)
    glVertex2d(0.36, -0.5)
    glEnd()
    
    #LeftLeg
    glBegin(GL_POLYGON)
    glVertex2d(-0.2, -0.5)
    glVertex2d(-0.2, -0.8)
    glVertex2d(-0.36, -0.8)
    glVertex2d(-0.36, -0.5)
    glEnd()

    #Neck
    glBegin(GL_POLYGON)
    glVertex2d(0.13, 0.1)
    glVertex2d(0.13, 0.35)
    glVertex2d(-0.13, 0.35)
    glVertex2d(-0.13,0.1)
    glEnd()
    
    #Mouth
    glColor(0.4, 0.6, 0.6)
    glBegin(GL_POLYGON)
    glVertex2d(0.2, 0.45)
    glVertex2d(0.2, 0.6)
    glVertex2d(-0.2, 0.6)
    glVertex2d(-0.2, 0.45)
    glEnd()

    #Teeth
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(0.18, 0.45)
    glVertex2d(0.16, 0.5)
    glVertex2d(0.14, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.14, 0.45)
    glVertex2d(0.12, 0.5)
    glVertex2d(0.1, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.1, 0.45)
    glVertex2d(0.08, 0.5)
    glVertex2d(0.06, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.18, 0.45)
    glVertex2d(-0.16, 0.5)
    glVertex2d(-0.14, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.14, 0.45)
    glVertex2d(-0.12, 0.5)
    glVertex2d(-0.1, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.1, 0.45)
    glVertex2d(-0.08, 0.5)
    glVertex2d(-0.06, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.06, 0.45)
    glVertex2d(-0.04, 0.5)
    glVertex2d(-0.02, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.02, 0.45)
    glVertex2d(0.0, 0.5)
    glVertex2d(0.02, 0.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.02, 0.45)
    glVertex2d(0.04, 0.5)
    glVertex2d(0.06, 0.45)
    glEnd()

    #RightEye
    glColor(1, 0, 0)
    glBegin(GL_LINES)
    for theta in np.arange(0, 2 * np.pi, 0.01):
        x = (0.225+0.07 * cos(theta))
        y = (.75+0.07 * sin(theta))
        glVertex2d(0.225, 0.75)
        glVertex2d(x, y)
    glEnd()
    
    # LeftEye
    glBegin(GL_LINES)
    for theta in np.arange(0, 2 * np.pi, 0.01):
        x = (0.225 + 0.07 * cos(theta))
        y = (.75 + 0.07 * sin(theta))
        glVertex2d(-0.225, 0.75)
        glVertex2d(-x, y)
    glEnd()


    #------Bebyon---------------
    glBegin(GL_LINES)
    for theta in np.arange(0, pi, 0.001):
        x = 0.055 * cos(theta)
        y = 0.055 * sin(theta)
        glVertex2d(0,0.05)
        glVertex2d(x, y)
    glEnd()
    
    #---------Buttons--------------
    glBegin(GL_LINES)
    for i in np.arange(0.055, -0.4, -0.05):
        for theta in np.arange(0, 2 * pi, 0.001):
            x = 0.01 * cos(theta)
            y = (i + 0.01 * sin(theta))
            glVertex2d(0, i)
            glVertex2d(x, y)

    glEnd()
    glFlush()

#---Main_Program---------
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow(b"Evil Wall-E")
glutDisplayFunc(Draw)
glutMainLoop()
