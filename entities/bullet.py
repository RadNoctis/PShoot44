import pygame
import os
from settings import *

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Load gambar
SKILL1_IMG = pygame.image.load(os.path.join(ASSETS_DIR, "blue fire_bg.jpg"))
SKILL2_IMG = pygame.image.load(os.path.join(ASSETS_DIR, "fire_bg.jpg"))
SKILL3_IMG = pygame.image.load(os.path.join(ASSETS_DIR, "ice_bg.png"))

# Optional: Ubah ukuran agar lebih pas
SKILL1_IMG = pygame.transform.scale(SKILL1_IMG, (40, 20))
SKILL2_IMG = pygame.transform.scale(SKILL2_IMG, (45, 30))
SKILL3_IMG = pygame.transform.scale(SKILL3_IMG, (30, 30))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=10):
        super().__init__()
        self.image = pygame.Surface((8, 4))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()


class Skill(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=5, skill_type=1):
        super().__init__()
        self.speed = speed
        self.skill_type = skill_type

        # Gunakan gambar berdasarkan skill type
        if skill_type == 1:
            self.image = SKILL1_IMG.convert_alpha()
        elif skill_type == 2:
            self.image = SKILL2_IMG.convert_alpha()
        elif skill_type == 3:
            self.image = SKILL3_IMG.convert_alpha()
        else:
            # Default jika salah
            self.image = pygame.Surface((30, 10))
            self.image.fill(CYAN)

        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()
