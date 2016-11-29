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
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 16)

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
        hs_easy = message.Message((250, 300),   "Peckish  (%s)" % a.rsplit()[0], True, 24)
        hs_medium = message.Message((250, 350), "Craving  (%s)" % b.rsplit()[0], False, 24)
        hs_hard = message.Message((250, 400),   "Hungry   (%s)" % c.rsplit()[0], False, 24)
        hs_insane = message.Message((250, 450), "Starving (%s)" % d.rsplit()[0], False, 24)
        self.entities.append(hs_easy)
        self.entities.append(hs_medium)
        self.entities.append(hs_hard)
        self.entities.append(hs_insane)
    def render(self, surf):
        surf.blit(self.font.render("[ESC] Back", False, (0, 0, 0)), (20, 750))
        surf.blit(self.font.render("[ENTER] Select", False, (0, 0, 0)), (555, 750))
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