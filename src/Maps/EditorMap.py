import pygame

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
window_size = [640, 320]  # Ajusta según sea necesario
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Editor de Tiles")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tamaño del tile
tile_size = 64

# Cargar la imagen de tiles
tile_sheet = pygame.image.load('./src/Maps/tiles.png')

# Función para extraer tiles
def get_tile(tile_sheet, x, y):
    """Extrae un tile individual de la hoja de tiles."""
    image = pygame.Surface((tile_size, tile_size))
    image.blit(tile_sheet, (0, 0), (x * tile_size, y * tile_size, tile_size, tile_size))
    image.set_colorkey(image.get_at((0, 0)))
    return image

def draw_grid():
    for x in range(0, window_size[0], tile_size):
        for y in range(0, window_size[1], tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Extraer tiles individuales
tiles = []
for i in range(tile_sheet.get_width() // tile_size):
    for j in range(tile_sheet.get_height() // tile_size):
        tile = get_tile(tile_sheet, i, j)
        tiles.append((tile, (i * tile_size, j * tile_size)))

# Crear cuadrícula para colocar tiles
grid = [[None for _ in range(window_size[0] // tile_size)] for _ in range(window_size[1] // tile_size)]

# Tile seleccionado
selected_tile = None

# Bucle principal del juego
running = True
dragging = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            mouse_presses = pygame.mouse.get_pressed()

            # Calcular la fila y columna
            column = x // tile_size
            row = y // tile_size

            # Imprimir la fila y columna
            print(f"Fila: {row}, Columna: {column}")
            print(f"Fila: {row}, Columna: {column}")

            # Seleccionar y copiar tile
            if mouse_presses[0] and y < tile_sheet.get_height():
                selected_tile = tiles[row + (column * (tile_sheet.get_width() // tile_size))]
            
            if mouse_presses[2] and selected_tile is not None:   
                    grid[row][column] = selected_tile


    # Fondo de pantalla
    screen.fill(BLACK)
    
    draw_grid()

# Dibujar los tiles
    for tile, pos in tiles:
        screen.blit(tile, pos)

    # Dibujar la cuadrícula con los tiles colocados
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile:
                tile_surface = tile[0]  # Accede solo a la superficie del tile
                screen.blit(tile_surface, (x * tile_size, y * tile_size))


    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()