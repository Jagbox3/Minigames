from displays import screen
import pygame
import os
from entity import player
from entity import goal

class GameScreen(screen.Screen):

    def __init__(self, diff):
        super().__init__()
        self.diff = diff
        speeds = [80, 50, 25, 5]
        self.game_speed = speeds[diff]
        image1 = pygame.image.load(os.path.join(os.getcwd(), "res", "snake.png"))
        self.bg = image1.subsurface(pygame.Rect((32, 48), (16,16)))
        self.entities = [player.Player((60, 60), image1), goal.Goal((0, 0), image1.subsurface(pygame.Rect((48, 48), (16, 16))))]
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), 14)
        self.score = 0

    def render(self, surf):
        for a in range(1, 49):
            for b in range(1, 49):
                surf.blit(self.bg, (16 * a, b * 16))
        self.entities[1].draw(surf)
        self.entities[0].draw(surf)
        surf.blit(self.font.render("Score- %i" % self.score, False, (0, 255, 255)), (0, 2))
        # wait
        pygame.time.wait(self.game_speed)

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