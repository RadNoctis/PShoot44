import pygame
from settings import *
import random
import os

# Load gambar dari folder assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
OBSTACLE_IMG = pygame.image.load(os.path.join(ASSETS_DIR, "stone_obstacle_bg.png"))
GROUND_IMG = pygame.image.load(os.path.join(ASSETS_DIR, "which-nether-rack-texture-bg.jpg"))
BG_IMG = pygame.image.load(os.path.join(ASSETS_DIR, "nether_bg.jpg"))

# Scaling
OBSTACLE_IMG = pygame.transform.scale(OBSTACLE_IMG, (TILE_SIZE, TILE_SIZE))
GROUND_IMG = pygame.transform.scale(GROUND_IMG, (TILE_SIZE, TILE_SIZE))
BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

class TileManager:
    def __init__(self):
        self.tiles = pygame.sprite.Group()
        self.generated_columns = set()

    def generate_if_needed(self, player_x):
        start_col = (player_x // TILE_SIZE) - 2
        end_col = (player_x // TILE_SIZE) + (WIDTH // TILE_SIZE) + 2

        for col in range(start_col, end_col):
            if col in self.generated_columns:
                continue

            # Jalan utama (ground)
            ground_tile = Tile(col * TILE_SIZE, HEIGHT - TILE_SIZE, GROUND_IMG)
            self.tiles.add(ground_tile)

            # Obstacle acak
            if random.random() < 0.2:
                height_above = random.randint(2, 4)
                obstacle_tile = Tile(col * TILE_SIZE, HEIGHT - TILE_SIZE * height_above, OBSTACLE_IMG)
                self.tiles.add(obstacle_tile)

            self.generated_columns.add(col)

    def get_tiles(self):
        return self.tiles

def generate_background(screen):
    screen.blit(BG_IMG, (0, 0))
