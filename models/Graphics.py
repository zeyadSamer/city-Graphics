#12th Week Lab Assignment
#Ahmed El-Hussein Ahmed 19106798
#Zeyad Ahmed Samer 20106344

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500


class Graphics:

    def initializeSettings(self):
        
        gluOrtho2D(0,700, 400,0)  

        
    def redisplay():
        glutPostRedisplay()

    def swapBuffer():
        glutSwapBuffers()    

    def load_texture(self):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        image = Image.open("speedlimit.jpg")
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = flipped_image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, flipped_image.width, flipped_image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE , img_data)


    def initializeWindow(self,display,idleFunction,keyboardFunction):

        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        glutInitWindowPosition(450,0)
        glutCreateWindow("my window")
        self.initializeSettings()
        glutDisplayFunc(display)
        
        glutIdleFunc(idleFunction)
        
        glutKeyboardFunc(keyboardFunction)
        self.load_texture()
        glutMainLoop()
