from functions import check_events
import pygame as pg
from classes import *


def main():
    pg.init()
    game = FlappyBird()
    background = Background()
    bird = Bird()
    clock = pg.time.Clock()
    while game.running:
        check_events(game, bird)
        clock.tick(30)
        game.update_screen(background, bird)
        pg.display.update() 


if __name__ == '__main__':
    main()