import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GRAY)  # atau warna lain untuk tile
        self.rect = self.image.get_rect(topleft=(x, y))

def generate_background(screen):
    screen.fill((30, 30, 30))
    tile_size = 20
    for y in range(0, HEIGHT, tile_size):
        for x in range(0, WIDTH, tile_size):
            color = GRAY if (x//tile_size + y//tile_size) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))

def load_level():
    tile_map = [
        "                                ",
        "                                ",
        "                                ",
        "    111                         ",
        "                                ",
        "         11111                  ",
        "                                ",
        "1111111111111111111111111111111",
    ]
    tiles = pygame.sprite.Group()
    for y, row in enumerate(tile_map):
        for x, char in enumerate(row):
            if char == "1":
                tile = Tile(x * TILE_SIZE, y * TILE_SIZE)
                tiles.add(tile)
    return tiles
