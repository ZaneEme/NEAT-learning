from tkinter import W
import pygame
from Game import Game

pygame.init()


class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        self.game = Game(self.window, self.width, self.height)
        self.loopcounter = 0

    def Runner(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(60)

            # set up close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.game.turn(0)
                # print("UP!")
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.game.turn(2)
                # print("DOWN!")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.game.turn(3)
                # print("LEFT!")
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.game.turn(1)
                # print("RIGHT!")

            # Esc -> Create event to quit the game
            if keys[pygame.K_ESCAPE]:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            if self.loopcounter >= 5:
                self.game.loop()
                self.loopcounter = 0
            else:
                self.loopcounter += 1

            pygame.display.update()
        


if __name__ == "__main__":
    SnakeGame(800,800).Runner()
