from displays import screen
import os
import pygame

class ScoreScreen(screen.Screen):
    def __init__(self, score, diff):
        super().__init__()
        self.images = dict()
        self.back = False
        self.big_font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 48)
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 16)
        self.score = score
        self.diff = diff
        self.text = self.check_high_score()
    def render(self, surf):
        surf.blit(self.font.render("[ENTER] Continue", False, (0, 0, 0)), (525, 750))
        surf.blit(self.big_font.render(self.text[0], False, self.text[1]), (self.text[2], 300))
        surf.blit(self.big_font.render(str(self.score), False, self.text[1]),
                  (380 - sum(c.isdigit() for c in str(self.score)) * 17, 380))
    def check_high_score(self):
        highscore_file = open(os.path.join(os.getcwd(), "res", "highscore.txt"), "r")
        lines = highscore_file.readlines()
        highscore_file.close()
        if self.score > int(lines[self.diff]):
            return "New Highscore:", (244, 158, 66), 100
        return "Score:", (223, 66, 244), 260

    def on_key_down(self, event):
        if event.key == 13:
            self.back = True