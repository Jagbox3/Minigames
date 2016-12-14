import pygame
import os
import cevent

class Screen(cevent.CEvent):
    def __init__(self):
        self.images = dict()
        self.load_images()
        self.entities = []
        self.width = self.get_width()
        self.height = self.get_height()

    def load_images(self):
        pass

    def render(self, surf):
        pass

    def get_width(self):
        options_file = open(os.path.join(os.getcwd(), "res", "options.txt"))
        screen_size = options_file.readline().strip().split(",")
        options_file.close()
        return int(screen_size[0]) * 8
    def get_height(self):
        options_file = open(os.path.join(os.getcwd(), "res", "options.txt"))
        screen_size = options_file.readline().strip().split(",")
        options_file.close()
        return int(screen_size[1]) * 8
