from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

texture1 = None
texture2 = None
train_x = 0
r = .0001
train_x_pos = 0
def load_textures():
    global texture1, texture2
    
    # Load the first texture
    texture1 = glGenTextures(2)
    glBindTexture(GL_TEXTURE_2D, texture1[0])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    image = Image.open("texture3.jpg")
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data_1 = flipped_image.convert("RGBA").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, flipped_image.width, flipped_image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE , img_data_1)
    
    # Load the second texture
    #texture2 = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture1[1])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    image = Image.open("texture4.jpg")
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data_2 = flipped_image.convert("RGBA").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, flipped_image.width, flipped_image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE , img_data_2)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)  #### 1 step ###
    
    # Draw the first texture
    glLoadIdentity()
    glTranslatef(train_x, 0.0, 0.0)
    glBindTexture(GL_TEXTURE_2D, texture1[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.5, 0.5, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glEnd()
    
    # Draw the second texture
    glLoadIdentity()
    glTranslatef(train_x_pos, 0.0, 0.0)
    glBindTexture(GL_TEXTURE_2D, texture1[1])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.5, 0.5, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glEnd()
    
    glFlush()
    glDisable(GL_TEXTURE_2D)

def update_textures():
    global train_x , train_x_pos
    train_x -= r
    train_x_pos+= r
    if train_x <= -1:
        train_x = 1
    if train_x_pos >= 1:
        train_x_pos = -1

def idle():
    update_textures()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize(600, 600)
    glutCreateWindow("Texture Example")
    glutDisplayFunc(draw)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    load_textures()  # corrected function call
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == '__main__':
    main()
