# Crear sprites y grupos
mi_sprite = MiSprite(rojo, 50, 50)
sprites = pygame.sprite.Group()
sprites.add(mi_sprite)

# En el bucle del juego
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

# Actualizar sprites
sprites.update()

# Dibujar sprites
screen.fill(negro)  # Fondo
sprites.draw(screen)

pygame.display.flip()
