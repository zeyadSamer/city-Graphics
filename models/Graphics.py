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
        glClearColor(1.0, 0.9, 0.0, 1.0)
        #glClearColor(0,0,0,0)
        glPointSize(5)
        glColor3f(1,0,0)

        gluOrtho2D(0,700, 400,0)   
       
        
    def redisplay():
        glutPostRedisplay()






    def initializeWindow(self,display,idleFunction,keyboardFunction):
        glutInit()
      
        glutInitDisplayMode(GLUT_DOUBLE| GLUT_RGBA)

        glutInitWindowSize(700, 500)
        glutInitWindowPosition(450,0)
        glutCreateWindow("my window")
        
        self.initializeSettings()
        
        glutDisplayFunc(display)
        glutIdleFunc(idleFunction)
        glutKeyboardFunc(keyboardFunction)
     
        
        glutMainLoop()
