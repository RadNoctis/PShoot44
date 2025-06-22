import pygame
from settings import *
from entities.bullet import Bullet, Skill

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group, skill_group):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -12
        self.on_ground = False

        self.bullets = bullet_group
        self.skills = skill_group
        self.skill_key = pygame.K_e

    def update(self, keys, mouse, obstacles):
        # Movement WASD
        dx = dy = 0
        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_w] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

        # Gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Collision with tiles
        dx, dy = self.handle_collisions(dx, dy, obstacles)
        self.rect.x += dx
        self.rect.y += dy

        # Shoot: enter or right click
        if keys[pygame.K_RETURN] or mouse[2]:
            self.shoot()

        # Skill selection
        if keys[pygame.K_1]: self.selected_skill = 1
        if keys[pygame.K_2]: self.selected_skill = 2
        if keys[pygame.K_3]: self.selected_skill = 3

        # Skill cast (auto)
        if self.skill_cast:
            self.cast_skill()
            self.skill_cast = False

        # Flash merah jika kena damage
        if self.damage_flash_timer > 0:
            self.image.fill(RED)
            self.damage_flash_timer -= 1
        else:
            self.image.fill(self.original_color)

def handle_collisions(self, dx, dy, obstacles):
    # Cek tabrakan horizontal
    self.rect.x += dx
    for obstacle in obstacles:
        if self.rect.colliderect(obstacle.rect):
            if dx > 0:
                self.rect.right = obstacle.rect.left
            elif dx < 0:
                self.rect.left = obstacle.rect.right
            dx = 0  # Hentikan gerakan horizontal jika tabrakan

    # Reset status on_ground sebelum cek vertikal
    self.on_ground = False

    # Cek tabrakan vertikal
    self.rect.y += dy
    for obstacle in obstacles:
        if self.rect.colliderect(obstacle.rect):
            if dy > 0:
                self.rect.bottom = obstacle.rect.top
                self.vel_y = 0
                self.on_ground = True
            elif dy < 0:
                self.rect.top = obstacle.rect.bottom
                self.vel_y = 0
            dy = 0  # Hentikan gerakan vertikal jika tabrakan

    return dx, dy
