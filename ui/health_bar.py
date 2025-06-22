def draw(self, screen, health):
    pygame.draw.rect(screen, RED, (10, 40, 100, 10))
    pygame.draw.rect(screen, GREEN, (10, 40, max(0, health), 10))
