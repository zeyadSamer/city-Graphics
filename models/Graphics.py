from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from models.Shape import Shape

class Graphics:
    
    def initializeSettings(self):
        glClearColor(1.0, 0.9, 0.0, 1.0)
        #glClearColor(0,0,0,0)
        glPointSize(5)
        glColor3f(1,0,0)

        gluOrtho2D(0,700, 400,0)    
        


    def initializeWindow(self,display):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

        glutInitWindowSize(700, 500)
        glutInitWindowPosition(450,0)
        glutCreateWindow("my window")
   
        self.initializeSettings()
        glutDisplayFunc(display)
    
        
        glutMainLoop()
