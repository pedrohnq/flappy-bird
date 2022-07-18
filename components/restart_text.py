from .game_object import GameObject
import constants
import pygame as pg


class RestartText(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = (255, 255, 255)
        self.image = None
        self.current_score = 0
        self.best_score = 0
    
    def draw(self, screen):
        text = 'Pressione Enter'
        text_surface = constants.FONT.render(text, False, self.color)
        super().draw(screen, 50, 150, image = text_surface)
        text = 'para reiniciar'
        text_surface = constants.FONT.render(text, False, self.color)
        super().draw(screen, 58, 175, image = text_surface)
        text = f'Score: {self.current_score}'
        text_surface = constants.FONT.render(text, False, self.color)
        super().draw(screen, 85, 230, image = text_surface)
        text = f'Melhor score: {self.best_score}'
        text_surface = constants.FONT.render(text, False, self.color)
        super().draw(screen, 40, 255, image = text_surface)
        
