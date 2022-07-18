import pygame as pg

def check_events(game):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.handle_exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game.fly_bird()
            if event.key == pg.K_RETURN and game.lost:
                game.restart()