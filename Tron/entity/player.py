import pygame
import entity.entity as entity

class Player(entity.Entity):
    def __init__(self, team, image, screen_width, screen_height):
        self.image = image
        if team == 0:
            self.x = [9]
            self.y = [39]
            self.direction = "RIGHT"
        else:
            self.x = [69]
            self.y = [39]
            self.direction = "LEFT"
        self.length = 1
        self.images = None
        self.load_images(team)
        self.game_over = False
        self.grow = True
        self.max_width = screen_width
        self.max_height = screen_height

    def load_images(self, team):
        images = dict()
        if team == 0:
            images["head"] = self.image.subsurface(pygame.Rect((0, 0), (8, 8)))
            images["body"] = self.image.subsurface(pygame.Rect((8, 0), (8, 8)))
        else:
            images["head"] = self.image.subsurface(pygame.Rect((0, 8), (8, 8)))
            images["body"] = self.image.subsurface(pygame.Rect((8, 8), (8, 8)))
        self.images = images

    def move(self):
        self.x.insert(1, self.x[0])
        self.y.insert(1, self.y[0])
        if self.direction is "LEFT":
            self.x[0] -= 1
        elif self.direction is "RIGHT":
            self.x[0] += 1
        elif self.direction is "UP":
            self.y[0] -= 1
        elif self.direction is "DOWN":
            self.y[0] += 1
        self.length += 1

    def draw(self, surf):
        if len(self.x) is not len(self.y):
            print("Position lists are not the same size")
        for index in range(self.length-1, -1, -1):
            if not index == 0:
                image = self.images["body"]
            else:
                image = self.images["head"]
            surf.blit(image, (self.x[index] * 8, self.y[index] * 8))

    def check_bounds(self):
        for index in range(self.length-1, -1, -1):
            if index > 4 and self.x[0] is self.x[index] and self.y[0] is self.y[index]:
                self.game_over = True
                print("Game Over")
        if self.x[0] <= 0 or self.x[0] >= int(self.max_width / 8) - 1:
            self.game_over = True
            print("Game Over")
        if self.y[0] <= 0 or self.y[0] >= int(self.max_height / 8) - 1:
            self.game_over = True
            print("Game Over")
