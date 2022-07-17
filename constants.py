import os
import pygame as pg
pg.font.init()

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
BACKGROUND = pg.image.load(os.path.join('images', 'bg.png'))
BIRD_1 = pg.image.load(os.path.join('images', 'bird1.png'))
BIRD_2 = pg.image.load(os.path.join('images', 'bird2.png'))
BIRD_3 = pg.image.load(os.path.join('images', 'bird3.png'))
FLOOR = pg.image.load(os.path.join('images', 'base.png'))
PIPE_1 = pg.image.load(os.path.join('images', 'pipe1.png'))
PIPE_2 = pg.image.load(os.path.join('images', 'pipe2.png'))
FONT = pg.font.Font(os.path.join('fonts', 'font.ttf'), 40)
BIRD_INITIAL_X = 75
BIRD_INITIAL_Y = 300
BACKGROUND_INITIAL_X = 0
BACKGROUND_INITIAL_Y = 0
FRAMES_PER_IMAGE_TO_BIRD = 3