class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=10, color=YELLOW):
        super().__init__()
        self.image = pygame.Surface((8, 4))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()
