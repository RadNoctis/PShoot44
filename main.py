import pygame
import random
import sys
import os
from settings import *
from entities.player import Player
from entities.enemy import Enemy
from level import generate_background, TileManager
from ui.skill_ui import SkillUI
from ui.health_bar import HealthBar

sys.path.append(os.path.dirname(__file__))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Platform Shooter")
clock = pygame.time.Clock()

# Grup sprite
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
skills = pygame.sprite.Group()

# === PLAYER ===
def reset_player():
    global player
    player = Player(100, HEIGHT - 150, bullets, skills)
    all_sprites.add(player)

reset_player()

# === SPAWN MUSUH ===
def spawn_enemies(player_x, count=3):
    for _ in range(count):
        x = player_x + random.randint(600, 1200)
        y = HEIGHT - 150
        enemy = Enemy(x, y)
        enemies.add(enemy)
        all_sprites.add(enemy)

spawn_enemies(player.rect.x)

# === UI ===
skill_ui = SkillUI("Plasma Blast", pygame.K_e)
health_bar = HealthBar(10, 40)

# === TILE ===
tile_manager = TileManager()

# === TIMER ===
SPAWN_INTERVAL = 2500  # ms
last_spawn_time = pygame.time.get_ticks()

# === GAME LOOP ===
running = True
while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    # === EVENT ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == player.skill_key:
                player.cast_skill()

    # === SPAWN MUSUH SECARA BERKALA ===
    now = pygame.time.get_ticks()
    if now - last_spawn_time > SPAWN_INTERVAL:
        last_spawn_time = now
        spawn_enemies(player.rect.x)

    # === CAMERA OFFSET ===
    camera_offset = WIDTH // 2 - player.rect.centerx

    # === BACKGROUND ===
    generate_background(screen)

    # === TILE ===
    tile_manager.generate_if_needed(player.rect.x)
    tiles = tile_manager.get_tiles()
    for tile in tiles:
        screen.blit(tile.image, (tile.rect.x + camera_offset, tile.rect.y))

    # === CEK TABRAKAN PLAYER DENGAN MUSUH ===
    if pygame.sprite.spritecollideany(player, enemies):
        all_sprites.empty()
        enemies.empty()
        bullets.empty()
        skills.empty()
        tile_manager = TileManager()
        reset_player()
        spawn_enemies(player.rect.x)
        continue

    # === UPDATE ENTITY SECARA GLOBAL (TIDAK TERGANTUNG KAMERA) ===
    player.update(keys, pygame.mouse.get_pressed(), tiles)
    bullets.update()
    skills.update()
    enemies.update(bullets, skills)

    # === RENDER ENTITY DALAM RANGE KAMERA (EFISIEN) ===
    for sprite in all_sprites:
        sprite_x_on_screen = sprite.rect.x + camera_offset
        if -100 <= sprite_x_on_screen <= WIDTH + 100:
            screen.blit(sprite.image, (sprite_x_on_screen, sprite.rect.y))

    for skill in skills:
        skill_x_on_screen = skill.rect.x + camera_offset
        if -100 <= skill_x_on_screen <= WIDTH + 100:
            screen.blit(skill.image, (skill_x_on_screen, skill.rect.y))

    # === UI ===
    skill_ui.draw(screen, player.selected_skill)
    health_bar.draw(screen, 100)

    # === FLIP DISPLAY ===
    pygame.display.flip()
