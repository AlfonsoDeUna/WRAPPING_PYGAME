import pygame
from Arms.BasicArm import BasicArm

class SpreatSheets:
    def __init__(self, filename, rows, cols):
        
        # Obtener la imagen de los sprites de los personajes
        self.sheets = pygame.image.load(filename).convert_alpha()
        
        # COLS AND ROWS OF THE SPREET SHEET IMAGE    
        self.cols = cols
        self.rows = rows
        
        # Todavía no sé para que tengo esto
        self.totalCellCount = cols * rows
        
        self.rect = self.sheets.get_rect()
        
        # width y height de cada una de las imagenes
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows
        
        self.animation_down = []
        self.animation_up = []
        self.animation_left =[]
        self.animation_right = []      
        
        for row in range(0, rows):
            for col in range(0, cols):
                animation = pygame.Rect (w*col,  h*row, w, h)
                if (row == 0):
                    self.animation_down.append(self.sheets.subsurface(animation))
                
                if (row == 1):
                    self.animation_up.append(self.sheets.subsurface(animation))
                    
                if (row == 2):
                     self.animation_left.append(self.sheets.subsurface(animation))
                    
                if (row == 3):
                    self.animation_right.append(self.sheets.subsurface(animation))
                    
    def getAnimationUP (self):
        return self.animation_up
    
    def getAnimationDOWN (self):
        return self.animation_down
    
    def getAnimationLEFT (self):
        return self.animation_left
    
    def getAnimationRIGHT (self):
        return self.animation_right
                  
class AnimationCharacter (pygame.sprite.Sprite):
    
    def __init__(self, filename, rows, cols, velocity = 10):
        super().__init__()
        self.spreatSheet = SpreatSheets(filename, rows, cols)
        self.animationUP = self.spreatSheet.getAnimationUP()
        self.animationDOWN = self.spreatSheet.getAnimationDOWN()
        self.animationLEFT = self.spreatSheet.getAnimationLEFT()
        self.animationRIGHT = self.spreatSheet.getAnimationRIGHT()
        
        self.velocity = velocity
        
        #obligatorio
        self.direction = "RIGHT"
        self.image = self.animationRIGHT[0]
        self.image = pygame.transform.scale(self.image, (30,30))
        
        self.rect = self.image.get_rect()
        self.rect.center = (800 // 2, 600 // 2) 
        
        self.index = 0
    
    def update (self):
        if self.index >= 3:
            self.index = 0
        print (self.index)
        
        if self.direction == "RIGHT":
            self.image = self.animationRIGHT[self.index]
        if self.direction == "LEFT":
            self.image = self.animationLEFT[self.index]
        if self.direction == "UP":
            self.image = self.animationUP[self.index]
        if self.direction == "DOWN":
            self.image = self.animationDOWN[self.index]
            
            
        self.image = pygame.transform.scale(self.image, (30,30))
        self.index += 1
        
         # Obtener teclas presionadas
        keys = pygame.key.get_pressed()

        # Mover el rectángulo
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
            self.direction = "LEFT"
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
            self.direction = "RIGHT"
        if keys[pygame.K_UP]:
            self.rect.y-= self.velocity
            self.direction = "UP"
        if keys[pygame.K_DOWN]:
            self.rect.y+= self.velocity
            self.direction = "DOWN"
    
           
class Character (pygame.sprite.Sprite):
    
    def __init__(self,screen, x=30,y=30, direction='right', velocity = 10):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (800 // 2, 600 // 2) 
        self.x = 800 //2
        self.y = 800 //2
        self.velocity = velocity
        self.screen = screen
        self.bullets = []
    
        
    def update(self):
        
        # Obtener teclas presionadas
        keys = pygame.key.get_pressed()

        # Mover el rectángulo
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y-= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y+= self.velocity
            
         # Disparar balas
        if keys[pygame.K_SPACE]:
            self.bullets.append(BasicArm(self.rect.x + 800 // 2, self.rect.y, 10))   
            
        for bullet in self.bullets[:]:
            bullet.update()
            bullet.draw(self.screen)
            if bullet.x > 800 or bullet.x < 0:
                self.bullets.remove(bullet)
        
    # basic rectangle element in screen with movements  
    #def draw (self):
        
       #size by while this!!
     #  pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, 10, 20))        