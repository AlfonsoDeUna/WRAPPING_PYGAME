import pygame, sys
from Maps.Map import Map
from Characters.Character import Character
from Characters.Character import AnimationCharacter

class Wppygame:
    
    def __init__ (self, largo=800,ancho=600, caption ="Wppygame AUBv1.0", fps=10):
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
        
        # Generar los mapas
        game_map = Map('./src/Maps/tiles.png', './src/Maps/map.txt', 16)            
        game_map.draw(self.SCREEN)
        
        # Crear grupos de sprites
        all_sprites = pygame.sprite.Group()
         
        #Ejemplo basico de character
        #personaje = Character(self.SCREEN)
        
        #personaje le paso la imagen y las filas y columnas del sprite. en una sola imagen
        personaje =  AnimationCharacter('./src/Characters/exampleSheet.png',4,4)
        all_sprites.add(personaje)    
        
        running = True
        
        while running:            
            
            fpsClock.tick(self.FPS)
            
            # actualice la pantalla importante
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
            
            # dibuja los pesronajes
            all_sprites.draw(self.SCREEN)
            all_sprites.update()
            
            # Actualizar pantalla. Dibuja sobre la imagen principal todo !! importante tener
            pygame.display.flip()   
            
            # dibuja el mapa.       
            game_map.draw(self.SCREEN) 
       
        pygame.quit()
        sys.exit()               
            

# TEST game
# creación del juego por defecto
game = Wppygame()
game.init()