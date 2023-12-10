import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Color Change Example")

# Definir colores
white = (255, 255, 255)

# Clase para el sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 20))  # Tamaño del sprite (ancho,alto)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)  # Posición inicial del sprite
        self.color_change_timer = 25  # Configura el temporizador a un valor diferente
        self.screen = screen
        self.color = (255, 0, 0)  # Cambia el color inicial a rojo
        self.image.fill(self.color)  # Rellena el sprite con el color inicial
        self.bullets = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
            self.change_color()
        if keys[pygame.K_d]:
            self.rect.x += 5
            self.change_color()
        if keys[pygame.K_w]:
            self.rect.y -= 5
            self.change_color()
        if keys[pygame.K_s]:
            self.rect.y += 5
            self.change_color()

    def change_color(self):
        # Cambiar de color cuando el temporizador alcanza cero
        if self.color_change_timer <= 0:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.image.fill(self.color)  # Rellena el sprite con el nuevo color
            self.color_change_timer = 25  # Reinicia el temporizador
        else:
            self.color_change_timer -= 1

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica de actualización
    all_sprites.update()

    # Limpiar pantalla
    screen.fill((0, 255, 0))

    # Dibujar sprites
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)
