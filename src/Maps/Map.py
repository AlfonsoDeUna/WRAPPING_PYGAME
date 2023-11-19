import pygame

class Map:
    
    def __init__(self, tile_file, map_file, tile_size):
        self.tile_size = tile_size
        self.tiles = self.load_tiles(tile_file)
        self.map_data = self.load_map(map_file)
        
    def load_tiles(self, filename):
        # Carga los tiles desde el archivo de tiles
        tiles = []
        tile_image = pygame.image.load(filename)
        for y in range(0, tile_image.get_height(), self.tile_size):
            for x in range(0, tile_image.get_width(), self.tile_size):
                rect = (x, y, self.tile_size, self.tile_size)
                tiles.append(tile_image.subsurface(rect))
        return tiles        
    
    def readFile (self, filename):
        mapFile = open(filename, "r")
        self.content = mapFile.readlines() + ['/r/n']
        mapFile.close()
        
    def load_map(self, filename):
        # Carga el mapa desde un archivo
        with open(filename, 'r') as file:
            map_data = [line.strip() for line in file]
        return map_data
    
    def draw(self, screen):
        # Dibuja el mapa en la pantalla
        for y, row in enumerate(self.map_data):
            row = row.split(',')
            for x, tile in enumerate(row):
                if tile != '':
                    screen.blit(self.tiles[int(tile)], (x * self.tile_size, y * self.tile_size))
            

            