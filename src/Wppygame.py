import pygame, sys
from pygame.locals import *

class Wppygame:
    
    def __init__ (self, largo=400,ancho=300, caption ="Wppygame AUBv1.0"):
        self.largo = largo
        self.ancho = ancho
        self.caption = caption
        self.gameInit()
    
    
    def gameInit(self):
        DISPLAYSURF = pygame.display.set_mode(self.largo, self.ancho)
        pygame.display.set_caption (self.caption)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()