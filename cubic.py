import pygame
pygame.init()
from pygame.sprite import Sprite



class Cub(Sprite):
    def dessapear(self):
        print("12")
    def __init__(self, posx, posy):
        Sprite.__init__(self)
        self.image = pygame.Surface([70, 50], pygame.SRCALPHA)
        self.rect = pygame.Rect(posx, posy, 70, 50)
        self.image.fill([0, 255, 237], [3, 3, 70, 43])
        self.boards = pygame.draw.rect(self.image, [0, 0, 0], [0, 0, 70, 50], 5, 6)













