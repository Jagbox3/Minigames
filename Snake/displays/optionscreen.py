from displays import screen
from entity import message
import os
import pygame

class OptionScreen(screen.Screen):
    def __init__(self):
        super().__init__()
        self.images = dict()
        self.back = False
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 16)
        self.entities = [message.Message((int(0.28125 * self.width), int(self.width * 0.375)), "Reset Highscores", True, 24)]
    def render(self, surf):
        surf.blit(self.font.render("[ESC] Back", False, (0, 0, 0)), (int(0.025 * self.width), int(0.9375 * self.height)))
        surf.blit(self.font.render("[ENTER] Select", False, (0, 0, 0)), (int(0.69375 * self.width), int(0.9375 * self.height)))
        for entity in self.entities:
            entity.draw(surf)
    def on_key_down(self, event):
        if event.key == 273:
            for a in range(len(self.entities)):
                if self.entities[a].highlighted and a > 0:
                    self.entities[a].highlighted = False
                    self.entities[a-1].highlighted = True
        if event.key == 274:
            for a in range(len(self.entities) - 1, -1, -1):
                if self.entities[a].highlighted and a < len(self.entities) - 1:
                    self.entities[a].highlighted = False
                    self.entities[a+1].highlighted = True
        if event.key == 13:
            for a in range(len(self.entities)):
                if self.entities[a].highlighted:
                    if self.entities[a].text == "Reset Highscores":
                        highscore_file = open(os.path.join(os.getcwd(), "res", "highscore.txt"), "w")
                        lines = ["0\n"] * 4
                        print(lines)
                        highscore_file.writelines(lines)
                        highscore_file.close()
                        self.back = True
        if event.key == 27:
            self.back = True
