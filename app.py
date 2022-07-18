from functions import check_events
import pygame as pg
from classes import *
from components import *
import constants


pg.init()


def main():
    game = FlappyBird()
    game.init_objects()
    clock = pg.time.Clock()
    while game.running:
        clock.tick(30)
        check_events(game)
        if not game.lost:
            if game.started:
                if game.can_create_pipe:
                    game.generate_pipe()
                    constants.SPEED_PIPES += 0.2
                game.check_collisions()
                game.remove_old_pipes()
                game.update_score()

        game.update_screen()
        
if __name__ == '__main__':
    main()