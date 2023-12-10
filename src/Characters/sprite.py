import pygame
import sys

pygame.init()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Sprite Color Change Example")


class Cuadrado(pygame.sprite.Sprite):
    def __init__(self,height,width):
        super().__init__()
        self.height=height
        self.width=width
        self.image=pygame.Surface((width,height))
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
            
        if keys[pygame.K_d]:
            self.rect.x += 5
            
        if keys[pygame.K_w]:
            self.rect.y -= 5
            
        if keys[pygame.K_s]:
            self.rect.y += 5
class SpreatSheets:
    def __init__(self,filename,rows,cols):
        self.sheets=pygame.image.load(filename).convert_alpha()
        self.rows=rows
        self.cols=cols
        self.rect = self.sheets.get_rect()
        
        #se dice tamaño de celdas
        w=self.cellWhidht=self.rect.width/cols
        h=self.cellHeight=self.rect.height/rows
        
        #donde se almacenan las imagnes
        self.up_animation=[]
        self.down_animation=[]
        self.left_animation=[]
        self.right_animation=[]
        
        for row in range(0,rows):
            for col in range(0,cols):
                animation=pygame.Rect(w*col, h*col, w, h)
                if(row==0):
                    self.down_animation.append(self.sheets.subsurface(animation))
                if(row==1):
                    self.up_animation.append(self.sheets.subsurface(animation))
                if(row==2):
                    self.left_animation.append(self.sheets.subsurface(animation))
                if(row==3):
                    self.right_animation.append(self.sheets.subsurface(animation))
        

player = Cuadrado(15,10)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    all_sprites.update()

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(100)

