import pygame
import entity.entity as entity

class Player(entity.Entity):
    def __init__(self, pos, image, screen_width, screen_height):
        self.image = image
        self.x = [1] * 3
        self.y = [1] * 3
        for a in range(3):
            self.x[a] = 5 - a * 1;
            self.y[a] = 1;
        self.length = len(self.x)
        self.images = None
        self.load_images()
        self.direction = "RIGHT"
        self.game_over = False
        self.grow = False
        self.max_width = screen_width
        self.max_height = screen_height

    def load_images(self):
        images = dict()
        #faces
        images["f_left"] = self.image.subsurface(pygame.Rect((0, 16), (16, 16)))
        images["f_right"] = self.image.subsurface(pygame.Rect((16, 16), (16, 16)))
        images["f_up"] = self.image.subsurface(pygame.Rect((0, 0), (16, 16)))
        images["f_down"] = self.image.subsurface(pygame.Rect((16, 0), (16, 16)))
        #turns
        images["topleft"] = self.image.subsurface(pygame.Rect((0, 32), (16, 16)))
        images["topright"] = self.image.subsurface(pygame.Rect((16, 32), (16, 16)))
        images["botleft"] = self.image.subsurface(pygame.Rect((0, 48), (16, 16)))
        images["botright"] = self.image.subsurface(pygame.Rect((16, 48), (16, 16)))
        #ends
        images["e_up"] = self.image.subsurface(pygame.Rect((32, 0), (16, 16)))
        images["e_down"] = self.image.subsurface(pygame.Rect((48, 0), (16, 16)))
        images["e_right"] = self.image.subsurface(pygame.Rect((32, 16), (16, 16)))
        images["e_left"] = self.image.subsurface(pygame.Rect((48, 16), (16, 16)))
        #straights
        images["vertical"] = self.image.subsurface(pygame.Rect((32, 32), (16, 16)))
        images["horizontal"] = self.image.subsurface(pygame.Rect((48, 32), (16, 16)))
        self.images = images

    def move(self):
        if self.grow:
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
            self.grow = False
            return
        for index in range(self.length-1, 0, -1):
            self.x[index] = self.x[index - 1]
            self.y[index] = self.y[index - 1]
        if self.direction is "LEFT":
            self.x[0] -= 1
        elif self.direction is "RIGHT":
            self.x[0] += 1
        elif self.direction is "UP":
            self.y[0] -= 1
        elif self.direction is "DOWN":
            self.y[0] +=1

    def draw(self, surf):
        if len(self.x) is not len(self.y):
            print("Position lists are not the same size")
        for index in range(self.length-1, -1, -1):
            image = None
            if self.x[index] is not self.x[index - 1]:
                image = self.images["horizontal"]
            if self.y[index] is not self.y[index - 1]:
                image = self.images["vertical"]
            if 0 < index < self.length - 1:
                if self.y[index+1] > self.y[index-1] and self.x[index+1] > self.x[index-1]:
                    if self.y[index-1] == self.y[index]:
                        image = self.images["topright"]
                    else:
                        image = self.images["botleft"]
                if self.y[index+1] > self.y[index-1] and self.x[index+1] < self.x[index-1]:
                    if self.y[index-1] == self.y[index]:
                        image = self.images["topleft"]
                    else:
                        image = self.images["botright"]
                if self.y[index+1] < self.y[index-1] and self.x[index+1] > self.x[index-1]:
                    if self.y[index-1] == self.y[index]:
                        image = self.images["botright"]
                    else:
                        image = self.images["topleft"]
                if self.y[index+1] < self.y[index-1] and self.x[index+1] < self.x[index-1]:
                    if self.y[index-1] == self.y[index]:
                        image = self.images["botleft"]
                    else:
                        image = self.images["topright"]
            if self.x[index] < self.x[index - 1] and index is self.length - 1:
                image = self.images["e_right"]
            if self.x[index] > self.x[index - 1] and index is self.length - 1:
                image = self.images["e_left"]
            if self.y[index] < self.y[index - 1] and index is self.length - 1:
                image = self.images["e_down"]
            if self.y[index] > self.y[index - 1] and index is self.length - 1:
                image = self.images["e_up"]
            if index is 0:
                if self.direction == "UP":
                    image = self.images["f_up"]
                if self.direction == "DOWN":
                    image = self.images["f_down"]
                if self.direction == "LEFT":
                    image = self.images["f_left"]
                if self.direction == "RIGHT":
                    image = self.images["f_right"]
            surf.blit(image, (self.x[index] * 16, self.y[index] * 16))

    def check_bounds(self):
        for index in range(self.length-1, -1, -1):
            if index > 4 and self.x[0] is self.x[index] and self.y[0] is self.y[index]:
                self.game_over = True
                print("Game Over")
        if self.x[0] <= 0 or self.x[0] >= int(self.max_width / 16):
            self.game_over = True
            print("Game Over")
        if self.y[0] <= 0 or self.y[0] >= int(self.max_height / 16):
            self.game_over = True
            print("Game Over")
