import pygame
from settings import *

class SkillUI:
    def __init__(self, skill_name, key):
        self.font = pygame.font.SysFont("Arial", 18)
        self.skill_name = skill_name
        self.key = key
        self.skills = ["Plasma Blast", "Fire Wave", "Ice Spike"]  # ✅ Tambahkan ini

    def draw(self, screen, current_skill):
        if 1 <= current_skill <= len(self.skills):
            skill_text = f"Skill [{current_skill}]: {self.skills[current_skill - 1]}"
        else:
            skill_text = "Skill [None]"

        render = self.font.render(skill_text, True, WHITE)
        screen.blit(render, (10, 10))
        