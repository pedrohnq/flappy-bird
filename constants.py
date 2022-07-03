import os
import pygame as pg

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
BACKGROUND = pg.image.load(os.path.join('images', 'bg.png'))
BIRD_1 = pg.image.load(os.path.join('images', 'bird1.png'))
BIRD_2 = pg.image.load(os.path.join('images', 'bird2.png'))
BIRD_3 = pg.image.load(os.path.join('images', 'bird3.png'))
BIRD_INITIAL_X = 75
BIRD_INITIAL_Y = 300
BACKGROUND_INITIAL_X = 0
BACKGROUND_INITIAL_Y = 0
FRAMES_PER_IMAGE_TO_BIRD = 3