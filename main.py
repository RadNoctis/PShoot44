import pygame
from settings import *
from entities.player import Player
from entities.enemy import Enemy
from level import generate_background, TileManager
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

# Tile Manager
tile_manager = TileManager()

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

    # Hitung offset kamera
    camera_offset = -player.rect.x + WIDTH // 4

    # Update tilemap (endless)
    tile_manager.generate_if_needed(player.rect.x)
    tiles = tile_manager.get_tiles()

    # Gambar tile dengan offset kamera
    for tile in tiles:
        screen.blit(tile.image, (tile.rect.x + camera_offset, tile.rect.y))

    # Update semua entity
    for sprite in all_sprites:
        if isinstance(sprite, Player):
            sprite.update(keys, pygame.mouse.get_pressed(), tiles)
        elif isinstance(sprite, Enemy):
            sprite.update(bullets, skills)
        else:
            sprite.update()

    # ✅ Update semua skill
    skills.update()

    # Gambar semua sprite
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x + camera_offset, sprite.rect.y))

    # ✅ Gambar semua skill
    for skill in skills:
        screen.blit(skill.image, (skill.rect.x + camera_offset, skill.rect.y))

    # UI
    skill_ui.draw(screen, player.selected_skill)

    # Flip layar
    pygame.display.flip()
