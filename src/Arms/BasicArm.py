import pygame

class BasicArm:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 5, 2))  # Dibuja una bala pequeña