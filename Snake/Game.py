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

        self.snake.eat()
        self.snake.move()

        self.board.draw()
        self.snake.draw()

        for apple in self.apples:
            apple.draw()
        
    def loop(self):
        """
        Executes a single game loop.
        """
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.snake.direction = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.snake.direction = 2
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.snake.direction = 3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.snake.direction = 1

        # Esc -> Create event to quit the game
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        self.draw()

    def draw_score(self):
        """
        Draws the score.
        """

    def reset(self):
        """
        Resets the game.
        """
