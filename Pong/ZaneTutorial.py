import pygame
from pong import Game
import neat
import os
import pickle

from pong.game import GameInformation


class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def ai_vs_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        clock = pygame.time.Clock()

        run = True
        while run:
            #clock.tick(300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            output1 = net1.activate(
                (self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x))
            )

            decision1 = output1.index(max(output1))

            if decision1 == 0:
                pass
            elif decision1 == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)

            output2 = net2.activate(
                (
                    self.right_paddle.y,
                    self.ball.y,
                    abs(self.right_paddle.x - self.ball.x),
                )
            )
            decision2 = output2.index(max(output2))
            if decision2 == 0:
                pass
            elif decision2 == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            game_info = self.game.loop()
            self.game.draw(True, True)
            pygame.display.update()
        pygame.quit()

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(120)  # set max frame rate to 60 fps
            # set up close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            # get key pressed and move paddles
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            output = net.activate(
                (
                    self.right_paddle.y,
                    self.ball.y,
                    abs(self.right_paddle.x - self.ball.x),
                )
            )
            decision = output.index(max(output))
            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            game_info = self.game.loop()
            self.game.draw(True, False)
            pygame.display.update()
        pygame.quit()

    #
    # Build two networks from given genomes
    # and test them against each other
    # if one of the paddles misses, end game and add hits number
    # to fitness of each genome
    #
    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output1 = net1.activate(
                (self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x))
            )

            decision1 = output1.index(max(output1))

            if decision1 == 0:
                pass
            elif decision1 == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)

            output2 = net2.activate(
                (
                    self.right_paddle.y,
                    self.ball.y,
                    abs(self.right_paddle.x - self.ball.x),
                )
            )
            decision2 = output2.index(max(output2))
            if decision2 == 0:
                pass
            elif decision2 == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            # print(output1, output2)

            game_info = self.game.loop()
            # self.game.draw(draw_score=False, draw_hits=True)
            # pygame.display.update()

            # if one of the paddles misses, end game
            if (
                game_info.left_score >= 1
                or game_info.right_score >= 1
                or game_info.left_hits > 50
            ):
                self.calculate_fitness(genome1, genome2, game_info)
                break

    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits


def eval_genomes(genomes, config):
    # each ai will play against every other ai
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break

        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i + 1 :]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = PongGame(window, width, height)

            game.train_ai(genome1, genome2, config)


def run_neat(config):
    # To restore from a checkpoint instead of creating a new
    # p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-3")
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    # Add stats and create a checkpoint at every generation
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(10))

    # winner set to either first to hit 400 fitness from config
    # or highest fitness after 50 generations
    winner = p.run(eval_genomes, 100)

    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_ai(config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = PongGame(window, width, height)
    game.test_ai(winner, config)


def aiFight(config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    with open("firstRun.pickle", "rb") as f:
        firstBot = pickle.load(f)

    with open("bestFirst.pickle", "rb") as f:
        secondBot = pickle.load(f)

    game = PongGame(window, width, height)
    game.ai_vs_ai(firstBot, secondBot, config)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    #run_neat(config)
    # test_ai(config)
    aiFight(config)
