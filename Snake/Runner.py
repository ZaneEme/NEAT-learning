from tkinter import W
import pygame
from Game import Game

pygame.init()


def SnakeGame():
    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    game = Game(window, width, height)
    clock = pygame.time.Clock()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break


        game.loop()
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    SnakeGame()
