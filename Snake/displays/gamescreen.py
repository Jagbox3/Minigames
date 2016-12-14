from displays import screen
import pygame
import os
from entity import player
from entity import goal

class GameScreen(screen.Screen):

    def __init__(self, diff):
        super().__init__()
        self.diff = diff
        speeds = [0.1, 0.0625, 0.03125, 0.00625]
        self.high_score = self.load_high_score()
        self.game_speed = speeds[diff]
        image1 = pygame.image.load(os.path.join(os.getcwd(), "res", "snake.png"))
        self.entities = [player.Player((4, 9), image1, self.width, self.height), goal.Goal((0, 0), image1.subsurface(pygame.Rect((48, 48), (16, 16))), self.width, self.height)]
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.0175 * self.width))
        self.score = 0

    def render(self, surf):
        self.entities[1].draw(surf)
        self.entities[0].draw(surf)
        surf.blit(self.font.render("Score- %i" % self.score, False, (0, 255, 255)), (int(0.03 * self.width), 2))
        surf.blit(self.font.render("Highscore- %s" % self.highest_score(), False, (0, 255, 255)),
                  (int(0.78 * self.width) - sum(c.isdigit() for c in str(self.highest_score())) * 17, 2))
        # wait
        pygame.time.wait(int(self.game_speed * self.width))

    def highest_score(self):
        return self.high_score if int(self.high_score) > self.score else str(self.score)
    def track_logic(self):
        self.entities[0].move()
        self.entities[0].check_bounds()
        if self.entities[0].x[0] is self.entities[1].pos[0] and self.entities[0].y[0] is self.entities[1].pos[1]:
            self.increment_score()

    def increment_score(self):
        self.score += 1
        self.entities[1].new_pos()
        self.entities[0].grow = True
        print("Score: %i" % self.score)

    def load_high_score(self):
        highscore_file = open(os.path.join(os.getcwd(), "res", "highscore.txt"), "r")
        lines = highscore_file.readlines()
        highscore_file.close()
        return lines[self.diff].rstrip()

    def on_key_down(self, event):
        if event.key == 273 and self.entities[0].direction is not "DOWN":
            #up
            self.entities[0].direction = "UP"
        if event.key == 274 and self.entities[0].direction is not "UP":
            #down
            self.entities[0].direction = "DOWN"
        if event.key == 275 and self.entities[0].direction is not "LEFT":
            #right
            self.entities[0].direction = "RIGHT"
        if event.key == 276 and self.entities[0].direction is not "RIGHT":
            #left
            self.entities[0].direction = "LEFT"

    def is_game_over(self):
        return self.entities[0].game_over
