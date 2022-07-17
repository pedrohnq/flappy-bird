

class GameObject:
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))