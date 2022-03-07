from random import random
import pygame
import random


class Apple:
    RED = (175, 60, 50)
    BLUE = (100, 90, 175)

    def __init__(self, window, width, height, good=True):
        self.x = width // 32 * random.randint(1, 33)
        self.y = height // 32 * random.randint(1, 33)
        self.good = good
        self.window = window

    def draw(self):
        """
        Draws the apple.
        If the apple is good, it is drawn in red.
        If the apple is bad, it is drawn in blue.
        """
        if self.good == True:
            pygame.draw.rect(self.window, Apple.RED, (self.x, self.y, 25, 25))
        else:
            pygame.draw.circle(self.window, Apple.BLUE, (self.x, self.y), 10)
