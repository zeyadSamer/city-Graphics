from OpenGL.GL import *

class Transformation:

    def translate(objectDisplay,x_trans,y_trans):
        glPushMatrix()
        glTranslatef(x_trans,y_trans,0)
        objectDisplay()
        glPopMatrix()



        

