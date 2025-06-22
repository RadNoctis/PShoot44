import pygame
from settings import *
from entities.bullet import Bullet, Skill

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group, skill_group):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(BLUE)
        self.original_color = BLUE
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -12
        self.on_ground = False

        self.bullets = bullet_group
        self.skills = skill_group
        self.skill_key = pygame.K_e

        self.selected_skill = 1
        self.skill_cast = False
        self.damage_flash_timer = 0

    def update(self, keys, mouse, obstacles):
        dx = dy = 0

        # ➤ Gerak kiri
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -self.speed

        # ➤ Gerak kanan
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed

        # ➤ Lompat
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

        # ➤ Gravity
        self.vel_y += GRAVITY

        # ➤ Turun lebih cepat
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.vel_y += 1

        dy += self.vel_y

        # ➤ Handle tumbukan
        dx, dy = self.handle_collisions(dx, dy, obstacles)
        self.rect.x += dx
        self.rect.y += dy

        # ➤ Menembak (klik kanan)
        if mouse[2]:
            self.shoot()

        # ➤ Cast skill (ENTER atau klik kiri)
        if keys[pygame.K_RETURN] or mouse[0]:
            self.skill_cast = True

        # ➤ Pilih skill
        if keys[pygame.K_1]: self.selected_skill = 1
        if keys[pygame.K_2]: self.selected_skill = 2
        if keys[pygame.K_3]: self.selected_skill = 3

        # ➤ Cast skill jika aktif
        if self.skill_cast:
            self.cast_skill()
            self.skill_cast = False

        # ➤ Efek terkena damage
        if self.damage_flash_timer > 0:
            self.image.fill(RED)
            self.damage_flash_timer -= 1
        else:
            self.image.fill(self.original_color)

    def handle_collisions(self, dx, dy, obstacles):
        self.rect.x += dx
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if dx > 0:
                    self.rect.right = obstacle.rect.left
                elif dx < 0:
                    self.rect.left = obstacle.rect.right
                dx = 0

        self.on_ground = False
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
                dy = 0

        return dx, dy

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery, 10)
        self.bullets.add(bullet)

    def cast_skill(self):
        skill = Skill(self.rect.centerx, self.rect.centery, 10, self.selected_skill)
        self.skills.add(skill)
