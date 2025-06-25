import pygame
from settings import *

class HealthBar:
    def __init__(self, x, y, width=100, height=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, health, max_health=100):
        # Bar latar belakang (merah)
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        # Bar HP (hijau)
        current_width = int(self.width * max(0, health) / max_health)
        pygame.draw.rect(screen, GREEN, (self.x, self.y, current_width, self.height))