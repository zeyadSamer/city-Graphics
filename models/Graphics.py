#12th Week Lab Assignment
#Ahmed El-Hussein Ahmed 19106798
#Zeyad Ahmed Samer 20106344

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Graphics:

    def initializeSettings(self):
        
        gluOrtho2D(0,700, 400,0)   
       
        
    def redisplay():
        glutPostRedisplay()

    def swapBuffer():
        glutSwapBuffers()    


    def initializeWindow(self,display,idleFunction,keyboardFunction):

        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE |GLUT_SINGLE| GLUT_RGBA)
        glutInitWindowSize(700, 500)
        glutInitWindowPosition(450,0)
        glutCreateWindow("my window")
        self.initializeSettings()
        glutDisplayFunc(display)
        glutIdleFunc(idleFunction)
        glutKeyboardFunc(keyboardFunction)
        glutMainLoop()
