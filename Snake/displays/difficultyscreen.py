from displays import screen
from entity import message
import os
import pygame
class DifficultyScreen(screen.Screen):
    def __init__(self):
        super().__init__()
        self.images = dict()
        self.play = False
        self.back = False
        self.diff = 0
        self.entities = []
        self.load_highscores()
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.02 * self.width))

    def load_highscores(self):
        highscore_file = open(os.path.join(os.getcwd(), "res", "highscore.txt"))
        a = highscore_file.readline()
        if a is "":
            a = "None"
        b = highscore_file.readline()
        if b is "":
            b = "None"
        c = highscore_file.readline()
        if c is "":
            c = "None"
        d = highscore_file.readline()
        if d is "":
            d = "None"
        highscore_file.close()
        hs_easy = message.Message((int(0.3125 * self.width), int(0.375 * self.height)),   "Peckish  (%s)" % a.rsplit()[0], True, int(0.03 * self.width))
        hs_medium = message.Message((int(0.3125 * self.width), int(0.4375 * self.height)), "Craving  (%s)" % b.rsplit()[0], False, int(0.03 * self.width))
        hs_hard = message.Message((int(0.3125 * self.width), int(0.5 * self.height)),   "Hungry   (%s)" % c.rsplit()[0], False, int(0.03 * self.width))
        hs_insane = message.Message((int(0.3125 * self.width), int(0.5625 * self.height)), "Starving (%s)" % d.rsplit()[0], False, int(0.03 * self.width))
        self.entities.append(hs_easy)
        self.entities.append(hs_medium)
        self.entities.append(hs_hard)
        self.entities.append(hs_insane)
    def render(self, surf):
        surf.blit(self.font.render("[ESC] Back", False, (0, 0, 0)), (int(0.025 * self.width), int(0.9375 * self.height)))
        surf.blit(self.font.render("[ENTER] Select", False, (0, 0, 0)), (int(0.69375 * self.width), int(0.9375 * self.height)))
        for entity in self.entities:
            entity.draw(surf)
    def on_key_down(self, event):
        if event.key == 273:
            for a in range(len(self.entities)):
                if self.entities[a].highlighted:
                    self.entities[a].highlighted = False
                    self.entities[(a - 1) % 4].highlighted = True
                    break
        if event.key == 274:
            for a in range(len(self.entities) - 1, -1, -1):
                if self.entities[a].highlighted:
                    self.entities[a].highlighted = False
                    self.entities[(a + 1) % 4].highlighted = True
                    break
        if event.key == 13:
            for a in range(len(self.entities)):
                if self.entities[a].highlighted:
                    self.diff = a
            self.play = True
        if event.key == 27:
            self.back = True
