import pygame
pygame.init()
from pygame.sprite import Sprite



class Cub(Sprite):
    CUBIC_SIZE_W = 70
    CUBIC_SIZE_H = 48
    def dessapear(self):
        print("12")
    def __init__(self, posx, posy):
        Sprite.__init__(self)
        self.image = pygame.Surface([self.CUBIC_SIZE_W, self.CUBIC_SIZE_H], pygame.SRCALPHA)
        self.rect = pygame.Rect(posx, posy, self.CUBIC_SIZE_W, self.CUBIC_SIZE_H)
        self.image.fill([0, 255, 237], [3, 3, self.CUBIC_SIZE_W, self.CUBIC_SIZE_H - 7])
        self.boards = pygame.draw.rect(self.image, [0, 0, 0], [0, 0, self.CUBIC_SIZE_W, self.CUBIC_SIZE_H], 5, 6)













