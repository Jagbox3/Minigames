from displays import screen
import pygame
import os
from entity import player

class GameScreen(screen.Screen):
#player.Player((14, 9), image1, self.width, self.height),
    def __init__(self):
        super().__init__()
        self.game_speed = .03125 * self.width
        image1 = pygame.image.load(os.path.join(os.getcwd(), "res", "player.png"))
        self.entities = [player.Player(0, image1, self.width, self.height), player.Player(1, image1, self.width, self.height)]
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.0175 * self.width))
        self.winner = -1

    def render(self, surf):
        for entity in self.entities:
            entity.draw(surf)
        # wait
        pygame.time.wait(int(self.game_speed))

    def track_logic(self):
        self.entities[0].move()
        self.entities[1].move()
        self.entities[0].check_bounds()
        self.entities[1].check_bounds()
        for a in range(2):
            for index in range(self.entities[0].length - 1, -1, -1):
                if self.entities[a].x[0] is self.entities[(a + 1) % 2].x[index] and self.entities[a].y[0] is self.entities[(a + 1) % 2].y[index]:
                    self.entities[(a + 1) % 2].game_over = True
                    self.winner = a
                    print("Game Over")

    def on_key_down(self, event):
        print(event.key)
        #Player 1:
        if event.key == 119 and self.entities[0].direction is not "DOWN":
            #up
            self.entities[0].direction = "UP"
        if event.key == 115 and self.entities[0].direction is not "UP":
            #down
            self.entities[0].direction = "DOWN"
        if event.key == 100 and self.entities[0].direction is not "LEFT":
            #right
            self.entities[0].direction = "RIGHT"
        if event.key == 97 and self.entities[0].direction is not "RIGHT":
            #left
            self.entities[0].direction = "LEFT"
        #Player 2:
        if event.key == 273 and self.entities[1].direction is not "DOWN":
            #up
            self.entities[1].direction = "UP"
        if event.key == 274 and self.entities[1].direction is not "UP":
            #down
            self.entities[1].direction = "DOWN"
        if event.key == 275 and self.entities[1].direction is not "LEFT":
            #right
            self.entities[1].direction = "RIGHT"
        if event.key == 276 and self.entities[1].direction is not "RIGHT":
            #left
            self.entities[1].direction = "LEFT"

    def is_game_over(self):
        return self.entities[0].game_over or self.entities[1].game_over
