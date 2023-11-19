import pygame

class Character ():
    
    '''
    Tiene que tener unas coordenadas de inicio
    un personaje se puede mover
    un personaje tiene una representación 
    un personaje puede tener sprite y se puede gestionar desde aquí
    
    '''
    
    def __init__(self,screen, x=30,y=30, direction='right', velocity = 10):
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = direction
        self.velocity = velocity
        self.color =   (255,0,0)
        #self.draw()
        
    def movements(self):
        
        # Obtener teclas presionadas
        keys = pygame.key.get_pressed()

        # Mover el rectángulo
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity

        # limits--> Hay que crear clases que controlen los límites del mapa o bien añadirlo al mapa
        #TODO: configurar height and with
        #self.x = max(0, min(self.x, 10 - 5))
        #self.y = max(0, min(self.y, 20 - 5))
        print (self.x)
        print (self.y)
        # draw the new position
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 10, 20))

        # disply update after movements
    
        
    # basic rectangle element in screen with movements  
    def draw (self):
        
       #size by while this!!
       pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, 10, 20))         

