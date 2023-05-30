from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

texture = None

def load_texture():
    global texture
    texture = glGenTextures(1)  # generate one texture ID and store it in the global variable "texture"
    glBindTexture(GL_TEXTURE_2D, texture)  # bind the texture ID to the 2D texture target
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)  # set the texture's minification filter to "nearest-neighbor"
    image = Image.open("bus.jpg")  # open the image file "texture.jpg"
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)  # flip the image vertically
    img_data = flipped_image.convert("RGBA").tobytes()  # convert the image data to a format suitable for OpenGL texture
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, flipped_image.width, flipped_image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE , img_data)  # create the texture by loading the image data
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw():
    glClear(GL_COLOR_BUFFER_BIT )
    glEnable(GL_TEXTURE_2D)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0.1, 0.2)
    glVertex3f(-1.0, -1.0, 0.0)
    glTexCoord2f(0.9, 0.2)
    glVertex3f(1.0, -1.0, 0.0)
    glTexCoord2f(1.0, 0.8)
    glVertex3f(1.0, 1.0, 0.0)
    glTexCoord2f(0.0, 0.8)
    glVertex3f(-1.0, 1.0, 0.0)


    # glTexCoord2f(0.0, 0.0)
    # glVertex3f(0.0, 0.0, 0.0)
    # glTexCoord2f(1.0, 0.0)
    # glVertex3f(1.0, 0.0, 0.0)
    # glTexCoord2f(1.0, 1.0)
    # glVertex3f(1.0, 1.0, 0.0)
    # glTexCoord2f(0.0, 1.0)
    # glVertex3f(0.0, 1.0, 0.0)


    glEnd()
    glFlush()
    glDisable(GL_TEXTURE_2D)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize(600, 600)
    glutCreateWindow("Texture Example")
    glutDisplayFunc(draw)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    load_texture()
    glutMainLoop()

if __name__ == '__main__':
    main()
