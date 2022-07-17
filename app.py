from functions import check_events
import pygame as pg
from classes import *
from components import *


def main():
    pg.init()
    game = FlappyBird()
    background = Background()
    bird = Bird()
    floor = Floor()
    pipes = []
    clock = pg.time.Clock()
    while game.running:
        if game.started and game.can_create_pipe:
            pipes.append(game.generate_pipe(Pipe))
        check_events(game, bird)
        clock.tick(30)
        game.update_screen(background, bird, *pipes, floor)
        game.remove_old_pipes(pipes)
        game.update_score(pipes, bird)

        pg.display.update() 


if __name__ == '__main__':
    main()