import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Textured 3D Cube - Marvin Agustin E. Angsioco")

glEnable(GL_DEPTH_TEST)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

def add_texture():
    image = pygame.image.load('texture.png')
    data = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

def draw_square():
    glBegin(GL_TRIANGLES)

    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)

    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)

    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)

    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)

    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)

    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)

    glEnd()

def draw_cube():

    glPushMatrix()

    draw_square()

    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    draw_square()
    glPopMatrix()

    glPopMatrix()

angle = 0
add_texture()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(angle, 1, 1, 1)
    draw_cube()
    glPopMatrix()

    angle += 1
    pygame.display.flip()
    pygame.time.wait(15)
