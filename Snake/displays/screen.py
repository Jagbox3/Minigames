import pygame
import os
import cevent

class Screen(cevent.CEvent):
    def __init__(self):
        self.images = dict()
        self.load_images()
        self.entities = []

    def load_images(self):
        pass

    def render(self, surf):
        pass