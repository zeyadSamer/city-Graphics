#Final Project
#Ahmed El-Hussein Ahmed 19106798
#Zeyad Ahmed Samer 20106344


from OpenGL.GL import *

class Transformation:

    def translate(objectDisplay,x_trans,y_trans):
        glPushMatrix()
        glTranslatef(x_trans,y_trans,0)
        objectDisplay()
        glPopMatrix()
