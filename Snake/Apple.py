import pygame

class Apple:
    RED = (175,60,50)
    BLUE = (100,90,175)


    def __init__(self, x, y, window, good=True):
        self.x = x
        self.y = y
        self.good = good
        self.window = window

    def draw(self):
        '''
        Draws the apple.
        If the apple is good, it is drawn in red.
        If the apple is bad, it is drawn in blue.
        '''
        if self.good == True:
            pygame.draw.circle(self.window, Apple.RED, (self.x, self.y), 10)
        else:
            pygame.draw.circle(self.window, Apple.BLUE, (self.x, self.y), 10)