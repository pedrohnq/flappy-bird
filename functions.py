import pygame as pg

def check_events(game):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.handle_exit()