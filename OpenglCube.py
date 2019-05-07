import sys
import os
import linecache
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

ROTATE_X = 0.0
ROTATE_Y = 0.0
ROTATE_Z = 0.0


def InitGL(Width, Height):

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)  # glDepthFunc(GL_LEQUAL)
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POLYGON_SMOOTH)
    glEnable(GL_BLEND)
    # Wire frame:  glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glShadeModel(GL_SMOOTH)  # glShadeModel(GL_FLAT)
    ReSizeGLScene(Width, Height)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def ReSizeGLScene(width, height):

    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # set perspective and aspect ratio.
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


#    glLoadIdentity()


def input_handler(*args):
    """args: a tuple of (key, x, y)"""

    global ROTATE_X, ROTATE_Y, ROTATE_Z
    if args[0] == '\033' or args[0] == 'q':
        sys.exit()
    elif args[0] == 'h':
        ROTATE_Y = ROTATE_Y - 2.333
    elif args[0] == 'l':
        ROTATE_Y = ROTATE_Y + 2.333
    elif args[0] == 'j':
        ROTATE_X = ROTATE_X + 2.333
    elif args[0] == 'k':
        ROTATE_X = ROTATE_X - 2.333
    elif args[0] == 'i':
        ROTATE_Z = ROTATE_Z - 2.333
    elif args[0] == 'u':
        ROTATE_Z = ROTATE_Z + 2.333
    if ROTATE_X > 360 or ROTATE_X == 0 or ROTATE_X < -360:
        ROTATE_X = 0.0
    if ROTATE_Y > 360 or ROTATE_Y == 0 or ROTATE_Y < -360:
        ROTATE_Y = 0.0
    if ROTATE_Z > 360 or ROTATE_Z == 0 or ROTATE_Z < -360:
        ROTATE_Z = 0.0
    DrawGLScene()


def DrawGLScene():

    global ROTATE_X, ROTATE_Y, ROTATE_Z

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    glTranslatef(0.0, 0.0, -6.0)
    glRotatef(ROTATE_X, 1.0, 0.0, 0.0)
    glRotatef(ROTATE_Y, 0.0, 1.0, 0.0)
    glRotatef(ROTATE_Z, 0.0, 0.0, 1.0)

    glPushMatrix()
    glBegin(GL_QUADS)
    glColor4f(0.4, 0.4, 0.4, 1.0)  # 0.666)
    glVertex3f(1.5, 1.5, -1.5)
    glVertex3f(1.5, 1.5, 1.5)
    glVertex3f(1.5, -1.5, 1.5)
    glVertex3f(1.5, -1.5, -1.5)

    # side 1: blue
    glColor4f(0.0, 0.0, 1.0, 1.0)  # 0.666)
    # upper right -> upper left -> lower left -> lower right
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # side 2: green
    glColor4f(0.0, 1.0, 0.0, 1.0)  # 0.666)
    # upper right -> upper left -> lower left -> lower right
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # side 3: red
    glColor4f(1.0, 0.0, 0.0, 1.0)  # 0.666)
    # upper right -> upper left -> lower left -> lower right
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # side 4: yellow
    glColor4f(1.0, 1.0, 0.0, 1.0)  # 0.666)
    # upper right -> upper left -> lower left -> lower right
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    # side 5: white
    glColor4f(1.0, 1.0, 1.0, 1.0)  # 0.666)
    # upper right -> upper left -> lower left -> lower right
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # side 6: cyan
    glColor4f(0.0, 1.0, 1.0, 1.0)  # 0.666)
    # upper right -> upper left -> lower left -> lower right
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()
    glPopMatrix()
    glutSwapBuffers()


def main():

    glutInit(sys.argv)
    # pyopengl bug causes a "Segmentation fault" when glutCreateWindow is called after glutInitDisplayMode.
    window = glutCreateWindow('cube')
    glutInitWindowSize(480, 272)
    glutInitWindowPosition(0, 0)
    # Setting only GLUT_DOUBLE seems to have the same effect. What are the others good for?
    glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH)
    glutDisplayFunc(DrawGLScene)
    # glutIdleFunc uses 50% of the CPU while "idle". Seems to run fine without it.
    # glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(input_handler)
    # glutFullScreen()
    InitGL(480, 272)
    glutMainLoop()


if __name__ == "__main__":

    main()
