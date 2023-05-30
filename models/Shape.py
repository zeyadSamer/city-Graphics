import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from models.Point import Point

class Shape:
    x=0

    def displayRectangle(points:list,color):
      
        
        glBegin(GL_QUADS)
        glColor4f(*color)
       
        for point in points:
             glVertex2f(point.x,point.y)

       

        glEnd()
        glFlush()

            
    def displayTriangle(points:list,color):
        

        # Draw the triangle 
        glBegin(GL_TRIANGLES)
        glColor4f(*color)
      
        for point in points:
            glVertex2f(point.x,point.y)

        glEnd()
        glFlush()


    def displayCircle(centerPoint:Point,radius,color:set):
          
          #The problem was here 
          #glClear(GL_COLOR_BUFFER_BIT) 

          glBegin(GL_POLYGON)
          glColor4f(*color)
          x_centre = centerPoint.x
          y_centre = centerPoint.y
          r = radius
          for theta in np.arange(0, 2*math.pi, 0.01):
            x =x_centre+ r*math.cos(theta)
            y = y_centre+r*math.sin(theta)
           
            glVertex2f(x, y)
         
          glEnd()
          glFlush()

    
     

    def displayLine(p1,p2,color):
      glBegin(GL_LINE_STRIP)
      glColor4f(*color)
      glVertex2f(p1.x,p1.y)
      glVertex2f(p2.x,p2.y)
      glEnd()
      glFlush()
