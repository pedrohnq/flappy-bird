

class GameObject:
    def draw(self, screen, x, y, **kwargs):
        image = kwargs.get('image', self.image)
        screen.blit(image, (x, y))