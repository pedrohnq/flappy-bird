from .game_object import GameObject
import constants


class Background(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = constants.BACKGROUND
    
    def draw(self, screen):
        screen_width = screen.get_size()[0]
        aux_bg_x = screen_width + self.x
        self.x -= 0.5
        if self.x < -1 * screen_width:
            self.x = 0
        super().draw(screen, aux_bg_x, self.y)
        super().draw(screen, self.x, self.y)