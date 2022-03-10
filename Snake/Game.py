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

    def turn(self, direction):
        """
        Turns the snake.
        Checks so you cannot go oposite direction.
        """
        #up and down are even numbers
        current_orientation = self.snake.direction % 2
        if direction % 2 != current_orientation:
            self.snake.turn(direction)

    def loop(self):
        """
        Executes a single game loop.
        """
        for apple in self.apples: 
            print(f"({apple.x // 25} {apple.y // 25})", end=' ')
        print()

        if len(self.apples) < 3:
            self.apples.append(Apple.Apple(self.window, self.width, self.height, self.snake))

        if self.snake.body[0].x < 0 or self.snake.body[0].x > self.width - 25 or self.snake.body[0].y < 0 or self.snake.body[0].y > self.height - 25:
            self.reset()

        for segment in range(len(self.snake.body)):
            if segment == 0:
                continue
            elif self.snake.body[0].x == self.snake.body[segment].x and self.snake.body[0].y == self.snake.body[segment].y:
                self.reset()

        for apple in self.apples:
            if self.snake.body[0].x == apple.x and self.snake.body[0].y == apple.y:
                self.snake.eat()
                self.apples.remove(apple)

        self.draw()

    def draw_score(self):
        """
        Draws the score.
        """

    def reset(self):
        """
        Resets the game.
        """
        pygame.event.post(pygame.event.Event(pygame.QUIT))
