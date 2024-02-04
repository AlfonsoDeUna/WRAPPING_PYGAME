import pygame
import sys

class ball (pygame.sprite.Sprite):
    def __init__(self, largo, alto):
        super().__init__()
        self.radius = 20
        self.screen_width = 800
        self.screen_height = 600
        self.x = 800 // 2
        self.y = 600 // 2
        self.pos = pygame.math.Vector2 (self.x,self.y)
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        self.rect  = self.image.get_rect(center=self.pos)
        
        pygame.draw.circle(self.image, 'white', (self.radius, self.radius), self.radius)
        self.rect.x = self.screen_width // 2
        self.rect.y = self.screen_height // 2
        self.velocity = [0, 0]
        self.gravity = 0.5
        
    def update (self):
        self.velocity[1] += self.gravity
        self.rect.y += int(self.velocity[1])

        # Rebotar en el suelo --> resto velocidad
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
            self.velocity[1] *= -0.7


pygame.init()
screen = pygame.display.set_mode((800,600)) #800x600 by default
fpsClock = pygame.time.Clock()        

running = True
miBall = ball(30,30)
sprites = pygame.sprite.Group()
sprites.add (miBall)

running = True
        
while running:            
            
        time = fpsClock.tick(60)
        
        # actualice la pantalla importante
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        screen.fill('black')        
        
        # dibuja los pesronajes
        sprites.draw(screen)
        sprites.update()
        
        # Actualizar pantalla. Dibuja sobre la imagen principal todo !! importante tener
        pygame.display.flip()   
       
pygame.quit()
sys.exit()                
    
    
