from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import *
from numpy import cos,sin,pi,arange
r = 0.1
def white_character():
    global r
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0,0,0)
    glMatrixMode(GL_MODELVIEW)
    # Head
    glLineWidth(1)
    glTranslate(0, 0.4, 0)
    glBegin(GL_LINES)
    for i in arange(0, 100, 0.1):
        x = r * cos(i * 2 * pi / 100)
        y = r * sin(i * 2 * pi / 100)
        glVertex2d(0, 0)
        glVertex2d(-x, -y)
    glEnd()

    glLoadIdentity()
    #The Body
    glBegin(GL_LINE_LOOP)
    glVertex2d(.2,-.2)
    glVertex2d(-.2,-.2)
    glVertex2d(-0.05,.3)
    glVertex2d(0.05,.3)
    glEnd()
    #The Hands
    #Right
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2d(0.07,0.25)
    glVertex2d(0.3,0)
    glEnd()
    #Left
    glBegin(GL_LINES)
    glVertex2d(-0.07, 0.25)
    glVertex2d(-0.3, 0)
    glEnd()
    #Legs
    #Right
    glLineWidth(1)
    glBegin(GL_LINE_LOOP)
    glVertex2d(0.05,-0.2)
    glVertex2d(0.1,-0.2)
    glVertex2d(0.1, -0.45)
    glVertex2d(0.05,-0.45)
    glEnd()
    #Left
    glBegin(GL_LINE_LOOP)
    glVertex2d(-0.05,-0.2)
    glVertex2d(-0.1,-0.2)
    glVertex2d(-0.1, -0.45)
    glVertex2d(-0.05,-0.45)
    glEnd()



    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"White Character")
glutDisplayFunc(white_character)
glutMainLoop()

