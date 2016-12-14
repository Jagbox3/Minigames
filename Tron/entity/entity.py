import pygame

class Entity:
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image

    def draw(self, surf):
        surf.blit(self._image, (self._pos[0], self._pos[1]))
