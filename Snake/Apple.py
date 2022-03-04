import pygame

class Apple:
    RED = 0
    BLUE = 0


    def __init__(self, x, y, good=True):
        self.x = x
        self.y = y
        self.good = good

    def draw(self):
        '''
        Draws the apple to the screen.
        Red is good and adds score, blue is bad and subtracts score.
        '''