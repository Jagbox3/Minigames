import pygame
import os
import cevent
from displays import gamescreen
from displays import titlescreen
from displays import difficultyscreen
from displays import optionscreen
from displays import scorescreen

class App(cevent.CEvent):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._current_screen = None
        self._mouse_pos = [0, 0]
        options_file = open(os.path.join(os.getcwd(), "res", "options.txt"))
        screen_size = options_file.readline().strip().split(",")
        options_file.close()
        print(int(screen_size[0]), int(screen_size[1]))
        self.size = self.width, self.height = int(screen_size[0]), int(screen_size[1])

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        # load images
        self._background = pygame.image.load(os.path.join(os.getcwd(), "res", "background.png")).convert()
        self.icon = pygame.image.load(os.path.join(os.getcwd(), "res", "icon.png")).convert_alpha()
        self._current_screen = titlescreen.TitleScreen()

        # set settings
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Snake")
        pygame.display.set_icon(self.icon)

    def on_loop(self):
        '''
        @purpose: Handles all changes in logic
        @summary: checks type of screen it is and for key variables within to decide whether to change screens
        :return:
        '''
        '''
        Title Screen
        '''
        if type(self._current_screen) is titlescreen.TitleScreen:
            if self._current_screen.quit:
                print("Quitting...")
                self.on_exit()
            if self._current_screen.play:
                self._current_screen = difficultyscreen.DifficultyScreen()
                print("Switching to Difficulty Screen...")
                return
            if self._current_screen.options:
                self._current_screen = optionscreen.OptionScreen()
                print("Switching to Option Screen...")
                return
        '''
        Difficulty Screen
        '''
        if type(self._current_screen) is difficultyscreen.DifficultyScreen:
            if self._current_screen.play:
                self._current_screen = gamescreen.GameScreen(self._current_screen.diff)
                print("Switching to Game Screen...")
                return
            if self._current_screen.back:
                print("Switching to Title Screen...")
                self._current_screen = titlescreen.TitleScreen()
        '''
        Game Screen
        '''
        if type(self._current_screen) is gamescreen.GameScreen:
            self._current_screen.track_logic()
            if self._current_screen.is_game_over():
                print("Switching to Score Screen...")
                self._current_screen = scorescreen.ScoreScreen(self._current_screen.score, self._current_screen.diff)
                self.set_high_score()
        '''
        Score Screen
        '''
        if type(self._current_screen) is scorescreen.ScoreScreen:
            if self._current_screen.back:
                print("Switching to Title Screen...")
                self._current_screen = titlescreen.TitleScreen()
        '''
        Option Screen
        '''
        if type(self._current_screen) is optionscreen.OptionScreen:
            if self._current_screen.back:

                print("Switching to Title Screen...")
                self._current_screen = titlescreen.TitleScreen()

    def set_high_score(self):
        highscore_file = open(os.path.join(os.getcwd(), "res", "highscore.txt"), "r")
        lines = highscore_file.readlines()
        highscore_file.close()
        if self._current_screen.score > int(lines[self._current_screen.diff]):
            highscore_file = open(os.path.join(os.getcwd(), "res", "highscore.txt"), "w")
            print("Saving new high score...")
            lines[self._current_screen.diff] = str(self._current_screen.score) + "\n"
            print(lines)
            highscore_file.writelines(lines)
            highscore_file.close()

    def on_render(self):
        # drawing
        self._display_surf.blit(self._background, (0, 0))
        self._current_screen.render(self._display_surf)
        # finish drawing
        pygame.display.flip()

    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def on_key_down(self, event):
        self._current_screen.on_key_down(event)

    def on_lbutton_down(self, event):
        print("Click at %s" % str(event.pos))
        pass

    def on_mouse_move(self, event):
        self._mouse_pos[0] = event.pos[0]
        self._mouse_pos[1] = event.pos[1]


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()