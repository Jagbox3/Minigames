import os
import pygame
import entity.entity as entity
import random

class Goal(entity.Entity):
    def __init__(self, pos, image):
        super().__init__(pos, image)
        self._image = image
        self.pos = pos
        self.new_pos()
    def new_pos(self):
        self.pos = (random.randint(1, 48), random.randint(1, 48))
        print("New goal at %s" % str(self.pos))
    def draw(self, surf):
        surf.blit(self._image, (self.pos[0] * 16, self.pos[1] * 16))