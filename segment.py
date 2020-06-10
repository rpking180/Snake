import pygame

BLACK = (0, 0, 0)
GREEN = (0, 0, 0)


class Segment(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.color = color
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, color, [0, 0, width, height])
