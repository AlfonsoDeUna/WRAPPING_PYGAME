import pygame, sys
from Maps.Map import Map
from Characters.Character import Character


class Wppygame:
    
    def __init__ (self, largo=800,ancho=600, caption ="Wppygame AUBv1.0", fps=30):
        self.largo = largo
        self.ancho = ancho
        self.caption = caption
        self.FPS = fps
        self.SCREEN = pygame.display.set_mode((largo,ancho)) #800x600 by default
        
    # por defecto es negro pero podemos modificar el color de fondo
    def setBackgroundColor (self, red=0,green=0,blue=0):
        self.backgroundColor = (red,green,blue)
        DISPLAYSURF = self.backgroundColor

    def init(self):
        
        pygame.init()
       
        # FPS
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption (self.caption)
        
        #TODO: quitar esto relativas ... !!
        game_map = Map('./src/Maps/tiles.png', './src/Maps/map.txt', 16)            
        game_map.draw(self.SCREEN)    
        personaje = Character(self.SCREEN) 
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #self.SCREEN.fill((0, 0, 0))
                   
            
            ## Gestión de personajes 
            
            
            personaje.movements()
            pygame.display.flip()
            pygame.time.delay(30)        
            pygame.display.update()
            fpsClock.tick(self.FPS)
        pygame.quit()
        sys.exit()               
            

# TEST game
# creación del juego por defecto
game = Wppygame()
game.init()