import pygame
from settings import *

class SkillUI:
    def __init__(self, skill_name, key):
        self.font = pygame.font.SysFont("Arial", 18)
        self.skill_name = skill_name
        self.key = key

    def draw(self, screen, current_skill):
        skill_text = f"Skill [{current_skill}]: {self.skills[current_skill-1]}"
        render = self.font.render(skill_text, True, WHITE)
        screen.blit(render, (10, 10))

