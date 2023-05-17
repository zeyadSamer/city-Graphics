from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from models.Shape import Shape

class Graphics:




    
    # def __init__(self,idleFunction,keyboardFunction) :
    #     self.idleFunction=idleFunction
    #     self.keyboardFunction=keyboardFunction
        
    # def initializeTransformation(self):
    #     glutIdleFunc(self.idleFunction)
    #     glutKeyboardFunc(self.keyboardFunction)
       


        
    
    def initializeSettings(self):
        
        gluOrtho2D(0,700, 400,0)   
       
        
    def redisplay():
        glutPostRedisplay()


    def initializeWindow(self,display,idleFunction,keyboardFunction):

        glutInit()
     
      
        glutInitDisplayMode( GLUT_DOUBLE |GLUT_SINGLE| GLUT_RGBA)

        glutInitWindowSize(700, 500)
        glutInitWindowPosition(450,0)

        glutCreateWindow("my window")
        #glMatrixMode(GL_PROJECTION)
        self.initializeSettings()
        
        glutDisplayFunc(display)
        glutIdleFunc(idleFunction)
        glutKeyboardFunc(keyboardFunction)
        
        glutMainLoop()
