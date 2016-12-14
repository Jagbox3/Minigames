import entity.entity as entity
import pygame
import os

class Message(entity.Entity):
    def __init__(self, pos, text, hl, size):
        self.pos = pos
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), size)
        self.text = text
        self.highlighted = hl
    def draw(self, surf):
        surf.blit(self.font.render(self.text, False, self.is_highlighted()), (self.pos[0], self.pos[1]))
    def is_highlighted(self):
        if self.highlighted:
            return 0, 255, 255
        return 0, 0, 255