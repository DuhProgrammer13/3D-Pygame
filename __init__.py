import pygame, sys
from view import cube
from pygame.locals import *

class Main:
    def __init__(self, params):
        controller = Controller()

class Controller:
    def __init__(self):
        self.view = pygame.display.set_mode((500, 500), pygame.SRCALPHA)
        self.cube = cube.Cube(300, pygame.image.load("one.bmp"))
        self.timer = pygame.time.Clock()
        self.FPS = 40

        self.mainLoop()
    def mainLoop(self):
        while True:
            self.update()
            self.draw()
            self.timer.tick(self.FPS)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        return # nothing for now

    def draw(self):
        self.cube.draw(self.view)

        pygame.display.update()


myMain = Main("Null")