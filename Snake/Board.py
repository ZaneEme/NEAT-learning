import pygame

WHITE = (220,220,220)

class Board:
    def __init__(self, window, width, height):
        self.width = width
        self.height = height
        self.window = window

    def draw(self):
        """
        Draws the board.
        """
        box_width = 25
        box_height = 25
        for i in range(self.width // box_width):
            pygame.draw.line(
                self.window,
                WHITE,
                (i * 25, 0),
                (i * 25, self.height),
                1
            )

        for i in range(self.height // box_height):
            pygame.draw.line(
                self.window,
                WHITE,
                (0, i * 25),
                (self.width, i * 25),
                1
            )
