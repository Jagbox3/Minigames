from displays import screen
from entity import message
import os
import pygame

class TitleScreen(screen.Screen):
    def __init__(self):
        super().__init__()
        print(self.width, self.height)
        self.images = dict()
        self.play = False
        self.quit = False
        self.options = False
        self.font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.02 * self.width))
        self.big_font = pygame.font.Font(os.path.join(os.getcwd(), "res", "8bit.ttf"), int(0.08 * self.width))
        self.entities =[message.Message((int(0.4375 * self.width), int(0.4375 * self.height)), "Play", True, int(0.03 * self.width)),
         message.Message((int(0.4 * self.width), int(0.5 * self.height)), "Options", False, int(0.03 * self.width)),
          message.Message((int(0.4375 * self.width), int(0.5625 * self.height)), "Quit", False, int(0.03 * self.width))]

    def render(self, surf):
        surf.blit(self.big_font.render("Snake", False, (50, 255, 0)), (int(0.3125 * self.width), int(0.25 * self.height)))
        surf.blit(self.font.render("[ESC] Quit", False, (0, 0, 0)), (int(0.025 * self.width), int(0.9375 * self.height)))
        surf.blit(self.font.render("[ENTER] Select", False, (0, 0, 0)), (int(0.69375 * self.width), int(0.9375 * self.height)))
        for entity in self.entities:
            entity.draw(surf)
            
    def on_key_down(self, event):
        if event.key == 273:
            for a in range(len(self.entities)):
                if self.entities[a].highlighted:
                    self.entities[a].highlighted = False
                    self.entities[(a - 1) % 3].highlighted = True
                    break
        if event.key == 274:
            for a in range(len(self.entities) - 1, -1, -1):
                if self.entities[a].highlighted:
                    self.entities[a].highlighted = False
                    self.entities[(a + 1) % 3].highlighted = True
                    break
        if event.key == 13:
            for entity in self.entities:
                if entity.highlighted:
                    if entity.text is "Play":
                        self.play = True
                        break
                    if entity.text is "Options":
                        self.options = True
                        break
                    if entity.text is "Quit":
                        self.quit = True
                        break
        if event.key == 27:
            self.quit = True
