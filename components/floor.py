from .game_object import GameObject
import constants


class Floor(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 400
        self.image = constants.FLOOR
    def draw(self, screen):
        screen_width = screen.get_size()[0]
        aux_floor_x = screen_width + self.x
        self.x -= 2
        if self.x < -1 * screen_width:
            self.x = 0
        super().draw(screen, aux_floor_x, self.y)
        super().draw(screen, self.x, self.y)