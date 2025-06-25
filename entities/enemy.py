import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.direction = 1
        self.vel_y = 0

    def update(self, bullets=None, skills=None):
        # Gerak bolak-balik
        self.rect.x += self.speed * self.direction
        if self.rect.left <= 0 or self.rect.right >= 5000:  # dunia luas
            self.direction *= -1

        # Gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.vel_y = 0

        # Damage
        if bullets:
            if pygame.sprite.spritecollide(self, bullets, True):
                self.kill()

        if skills:
            if pygame.sprite.spritecollide(self, skills, False):
                self.kill()
