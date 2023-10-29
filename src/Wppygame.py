import pygame, sys
from pygame.locals import *

class Wppygame:
    
    def __init__ (self, largo=400,ancho=300, caption ="Wppygame AUBv1.0", fps=30):
        self.largo = largo
        self.ancho = ancho
        self.caption = caption
        self.FPS = fps
        self.gameInit()
        
    # por defecto es negro pero podemos modificar el color de fondo
    def setBackgroundColor (self, red=0,green=0,blue=0):
        self.backgroundColor = (red,green,blue)
        DISPLAYSURF = self.backgroundColor

    
    def gameInit(self):
        
        pygame.init()
       
       # FPS
        fpsClock = pygame.time.Clock()
        
        DISPLAYSURF = pygame.display.set_mode(self.largo, self.ancho)
        pygame.display.set_caption (self.caption)
        
        # Se crea el personaje principal del juego
        # personajePpl = Character()
        #
        
        while True:
            
            #El personaje principal gestiona el movimiento
            # personajePpl.manageDirection()
            #El personaje principal realiza blit
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            fpsClock.tick(self.FPS)
            