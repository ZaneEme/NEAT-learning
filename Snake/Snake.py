import pygame
import COLORS

class Snake:
    def __init__(self, window, x, y, length=3):
        self.length = length
        self.x = x
        self.y = y
        self.body = []
        self.window = window
        self.direction = 0
        self.green = COLORS.GREEN

        for i in range(1, length):
            self.body.append(SnakeSegment(window, self.x + (25 * i), self.y))

    def move(self):
        """
        Moves the entire snake one space
        """
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        if self.direction == 0:
            self.body[0].x += 1
        elif self.direction == 1:
            self.body[0].y += 1
        elif self.direction == 2:
            self.body[0].x -= 1
        elif self.direction == 3:
            self.body[0].y -= 1
        else:
            raise ValueError("Invalid direction")

    def eat(self):
        """
        Adds a new segment to the snake.
        """
        self.body.append(SnakeSegment(self.body[-1].x, self.body[-1].y))

    def turn(self, direction=0):
        """
        Sets the direction of the snake.
        """
        self.direction = direction

    def draw(self):
        """
        Draws the snake to the screen.
        """
        for segment in self.body:
            segment.draw()


class SnakeSegment:
    def __init__(self, window, x, y):
        self.x = x
        self.y = y
        self.window = window

    def draw(self):
        """
        Draws the snake segment to the screen.
        """
        pygame.draw.rect(self.window, COLORS.GREEN, pygame.Rect(self.x, self.y, 25, 25))
