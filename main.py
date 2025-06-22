import pygame
from settings import *
from entities.player import Player
from entities.enemy import Enemy
from level import generate_background, load_level
from ui.skill_ui import SkillUI
import sys
import os
sys.path.append(os.path.dirname(__file__))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Platform Shooter")
clock = pygame.time.Clock()

# Grup
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
skills = pygame.sprite.Group()

# Player
player = Player(100, HEIGHT - 150, bullets, skills)
all_sprites.add(player)

# Musuh
enemy = Enemy(600, HEIGHT - 150)
all_sprites.add(enemy)
enemies.add(enemy)

# UI
skill_ui = SkillUI("Plasma Blast", pygame.K_e)

# Tilemap obstacles
tile_group = load_level()

# Game loop
running = True
while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == player.skill_key:
                player.cast_skill()

    # Background
    generate_background(screen)

    # Hitung offset kamera sebelum menggambar tile/sprite
    camera_offset = -player.rect.x + WIDTH // 4

    # Gambar tile dengan offset kamera
    for tile in tile_group:
        screen.blit(tile.image, (tile.rect.x + camera_offset, tile.rect.y))

    # Update semua entity
    for sprite in all_sprites:
        if isinstance(sprite, Player):
            sprite.update(keys, pygame.mouse.get_pressed(), tile_group)
        elif isinstance(sprite, Enemy):
            sprite.update(bullets, skills)
        else:
            sprite.update()

    # Gambar semua sprite dengan offset kamera
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x + camera_offset, sprite.rect.y))

    # UI
    skill_ui.draw(screen, player.selected_skill)

    # Flip layar
    pygame.display.flip()