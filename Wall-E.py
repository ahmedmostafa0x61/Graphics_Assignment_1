from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def Draw ():
    #Body
    glColor(0.7,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(0.6,0.1)
    glVertex2d(0.6,-0.5)
    glVertex2d(-0.6,-0.5)
    glVertex2d(-0.6,0.1)
    glEnd()

    #RightLeg
    glColor(1, 0.8, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.2, -0.5)
    glVertex2d(0.2, -0.8)
    glVertex2d(0.5, -0.8)
    glVertex2d(0.5, -0.5)
    glEnd()

    #LeftLeg
    glColor(1, 0.8, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.2, -0.5)
    glVertex2d(-0.2, -0.8)
    glVertex2d(-0.5, -0.8)
    glVertex2d(-0.5, -0.5)
    glEnd()

    #Neck
    glColor(0.6, 0.4, 0.3)
    glBegin(GL_POLYGON)
    glVertex2d(0.13, 0.1)
    glVertex2d(0.13, 0.35)
    glVertex2d(-0.13, 0.35)
    glVertex2d(-0.13,0.1)
    glEnd()

    #Head
    glColor(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2d(0.44, 0.35)
    glVertex2d(0.44, 0.9)
    glVertex2d(-0.44, 0.9)
    glVertex2d(-0.44, 0.35)
    glEnd()

    # RightEye
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.15, 0.7)
    glVertex2d(0.15, 0.8)
    glVertex2d(0.3, 0.8)
    glVertex2d(0.3, 0.7)
    glEnd()

    # LeftEye
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.15, 0.7)
    glVertex2d(-0.15, 0.8)
    glVertex2d(-0.3, 0.8)
    glVertex2d(-0.3, 0.7)
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


    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Report")
glutDisplayFunc(Draw)
glutMainLoop()
