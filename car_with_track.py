from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


x = 0
angle = 0
#speed of Traslate and Rotate
r = 0.04
theta = 1


def init():
    glClearColor(0.4,0.8,0.1,1)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,0.1,500)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glMatrixMode(GL_MODELVIEW)

def Road():
    '''The Road'''
    glColor(0, 0, 0)
    glLoadIdentity()
    glTranslate(0, -5, 0)
    glScale(140, 0.1, 10)
    glutSolidCube(1)

    '''The Middle Lines'''
    for i in range(-70,70,7):
        glLoadIdentity()
        glColor(0.5, 0.5, 0.5)
        glTranslate(i, -5, 0)
        glScale(4, 0.2, 0.5)
        glutSolidCube(1)

def Car():
    global x
    '''The Body'''
    glColor(1,0,0)
    #lower Body
    glLoadIdentity()
    glTranslate(x, -1.5, 0.5)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    # Higher Body
    glLoadIdentity()
    glTranslate(x, (5 * 0.25 - 1.5) , 0.5)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    '''The Doors'''
    glColor(0.5,0,1)
    glLoadIdentity()
    glTranslate(x, -1, 1.8)
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(2)

    glLoadIdentity()
    glTranslate(x, -1, -0.8)
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(2)
    ''''' The Tires '''''
    '''Forward'''
    #Left
    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x + 2.5, -8 * 0.25, 2.5 * 0.5 + 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 20, 8)
    # Right
    glLoadIdentity()
    glColor(0,0,1)
    glTranslate(x + 2.5, -8 * 0.25, -2.5 * 0.5 + 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 20, 8)
    '''Backward'''
    #Left
    glLoadIdentity()
    glColor(0, 0, 1)
    glTranslate(x - 2.5, -8 * 0.25, -2.5 * 0.5 + 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 20, 8)
    # Right
    glLoadIdentity()
    glColor(0, 0, 1)
    glTranslate(x - 2.5, -8 * 0.25, 2.5 * 0.5 + 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 20, 8)

    '''Lights'''
    #Left
    glColor(1, 1, 0)
    glLoadIdentity()
    glTranslate(x + 2.5, -1.5, 1.25 * 0.5 + 0.5)
    glutWireSphere(0.25, 100, 100)

    # Right
    glLoadIdentity()
    glTranslate(x + 2.5, -1.5, -1.25 * 0.5 +0.5)
    glutWireSphere(0.25, 100, 100)

def Trailer():
    global x,angle
    glColor(0.5, 0.5, 0)
    glLoadIdentity()
    glTranslate(x-7, -2, 0.5)
    glScale(4, 0.1, 4)
    glutSolidCube(1)

    glColor(0.1, 0, 0.5)
    glLoadIdentity()
    glTranslate(x -5, -1, 0.5)
    glRotate(90, 0, 0, 1)
    glScale(2, 0.1, 4)
    glutSolidCube(1)

    glLoadIdentity()
    glTranslate(x - 9, -1, 0.5)
    glRotate(90, 0, 0, 1)
    glScale(2, 0.1, 4)
    glutSolidCube(1)

    glLoadIdentity()
    glTranslate(x -7, -1, -1.5)
    glRotate(90, 1, 0, 0)
    glScale(4, 0.1, 2)
    glutSolidCube(1)

    glLoadIdentity()
    glTranslate(x -7, -1, 2.5)
    glRotate(90, 1, 0, 0)
    glScale(4, 0.1, 2)
    glutSolidCube(1)

    '''Tires'''
    #Right
    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x - 7, -1.5, 2.7)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 20, 8)
    #Left
    glLoadIdentity()
    glTranslate(x - 7, -1.5, -1.7)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 20, 8)

def Bar():
    global x
    glLoadIdentity()
    glColor(1, 0, 0)
    glTranslate(x - 3.7, -1.5, 0.5)
    glScale(2.5, 0.1, 0.3)
    glutSolidCube(1)


def draw():
    global x,r,theta,angle
    #x,r for the direction and movment
    #theta , angle  for the torus rotation
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    Car()
    Bar()
    Trailer()
    Road()

    glutSwapBuffers()


    if x>=15 or x <= -5:
        r = -r          #reverse the movment direction
        theta = -theta  #reverse the rotation dircetion
    x += r
    angle -= theta






glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Car With Trailer")
glutDisplayFunc(draw)
glutIdleFunc(draw)
init()
glutMainLoop()

