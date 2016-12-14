from displays import screen
import os
import pygame

class ScoreScreen(screen.Screen):
    def __init__(self, winner):
        super().__init__()
        self.images = dict()
        self.back = False
        self.big_font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.06 * self.width))
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.02 * self.width))
        self.text = ("Purple wins!", (244, 66, 152), int(0.2 * self.width)) if winner == 0 else ("Blue wins!", (66, 182, 244), int(.225 * self.width))
    def render(self, surf):
        surf.blit(self.font.render("[ENTER] Continue", False, (0, 0, 0)), (int(0.65625 * self.width), int(0.9375 * self.height)))
        surf.blit(self.big_font.render(self.text[0], False, self.text[1]), (self.text[2], int(0.375 * self.height)))
    def on_key_down(self, event):
        if event.key == 13:
            self.back = True
