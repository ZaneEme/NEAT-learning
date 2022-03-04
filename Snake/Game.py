import Board
import Apple
import Snake
import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = Board.Board(self.width, self.height)
    
    def draw(self):
        '''
        Draws the game.
        '''
    
    def loop(self):
        '''
        Executes a single game loop.
        '''

    def draw_score(self):
        '''
        Draws the score.
        '''
    
    def reset(self):
        '''
        Resets the game.
        '''
    