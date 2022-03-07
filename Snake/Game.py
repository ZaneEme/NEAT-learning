import Board
import Apple
import Snake
import pygame


class Game:
    def __init__(self, window, width, height):
        self.width = width
        self.height = height
        self.window = window
        self.apples = []    

        self.board = Board.Board(self.window, self.width, self.height)
        self.snake = Snake.Snake(self.window, self.width, self.height)

    def draw(self):
        """
        Draws the game.
        """
        self.window.fill((255,255,255))
        self.board.draw()
        self.snake.draw()

        for apple in self.apples:
            apple.draw()
        

    def loop(self):
        """
        Executes a single game loop.
        """
        self.draw()

    def draw_score(self):
        """
        Draws the score.
        """

    def reset(self):
        """
        Resets the game.
        """
