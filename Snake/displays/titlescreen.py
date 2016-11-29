from displays import screen
from entity import message
import os
import pygame

class TitleScreen(screen.Screen):
    def __init__(self):
        super().__init__()
        self.images = dict()
        self.play = False
        self.quit = False
        self.options = False
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 16)
        self.big_font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 64)
        self.entities = [message.Message((350, 350), "Play", True, 24), message.Message((320, 400), "Options", False, 24), message.Message((350, 450), "Quit", False, 24)]
    def render(self, surf):
        surf.blit(self.big_font.render("Snake", False, (50, 255, 0)), (250, 200))
        surf.blit(self.font.render("[ESC] Quit", False, (0, 0, 0)), (20, 750))
        surf.blit(self.font.render("[ENTER] Select", False, (0, 0, 0)), (555, 750))
        for entity in self.entities:
            entity.draw(surf)
    def on_key_down(self, event):
        if event.key == 273:
            for a in range(len(self.entities)):
                if self.entities[a].highlighted:
                    self.entities[a].highlighted = False
                    self.entities[(a - 1) % 3].highlighted = True
                    break
        if event.key == 274:
            for a in range(len(self.entities) - 1, -1, -1):
                if self.entities[a].highlighted:
                    self.entities[a].highlighted = False
                    self.entities[(a + 1) % 3].highlighted = True
                    break
        if event.key == 13:
            for entity in self.entities:
                if entity.highlighted:
                    if entity.text is "Play":
                        self.play = True
                        break
                    if entity.text is "Options":
                        self.options = True
                        break
                    if entity.text is "Quit":
                        self.quit = True
                        break
        if event.key == 27:
            self.quit = True