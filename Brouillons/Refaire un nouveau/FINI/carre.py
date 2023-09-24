import pygame
from pygame.locals import *
pygame.init()

size = 30

red = ((249, 104, 84), (204, 51, 19), (240, 75, 40))
yellow=((249, 209, 85), (221, 172, 19), (245, 193,30))
blue=((118, 191, 255), (57, 141, 216), (65, 161, 247))                 
green= ((93, 220 ,137), (40, 170, 89), (42, 202, 98))                  
purple=((153, 113, 239), (111, 69, 227), (136, 86, 245))                 
turquoise=((103, 231, 212), (57, 190, 170), (50, 216, 191))
orange=((251, 156, 76), (215, 113, 27), (249, 136, 43))
              
def carre(screen,couleur,pos,taille,size):
    pygame.draw.rect(screen, couleur[0], (X+x*size, Y+y*size, size, size))
    pygame.draw.polygon(screen, couleur[1], ([X+x*size, Y+y*size+size], [X+x*size+size, Y+y*size+size], [X+x*size+size,Y+y*size]))
    pygame.draw.rect(screen, couleur[2], (X+x*size+round(size/8), Y+y*size+round(size/8), size*(6/8), size*(6/8)))

