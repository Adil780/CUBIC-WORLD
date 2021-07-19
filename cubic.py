import pygame

pygame.init()
from pygame.sprite import DirtySprite

f = pygame.font.SysFont("arial", 40, True)


class Cub(DirtySprite):
    CUBIC_SIZE_W = 70
    CUBIC_SIZE_H = 50

    def dessapear(self):
        print("12")



    def __init__(self, posx, posy, hp, defended):
        DirtySprite.__init__(self)
        self.rect = pygame.Rect(posx, posy, self.CUBIC_SIZE_W, self.CUBIC_SIZE_H)
        self.hp = hp
        self.defended = defended
        self.create_image()




    def create_image(self):
        if self.defended == False:
            lifes = f.render(str(self.hp), True, [2, 94, 0])
        else:
            lifes = f.render("\u221e", True, [2, 94, 0])
        width = lifes.get_width()
        height = lifes.get_height()
        self.image = pygame.Surface([self.CUBIC_SIZE_W, self.CUBIC_SIZE_H], pygame.SRCALPHA)
        self.image.fill([0, 255, 237], [3, 3, self.CUBIC_SIZE_W, self.CUBIC_SIZE_H - 7])
        self.image.blit(lifes, [self.CUBIC_SIZE_W / 2 - width / 2, self.CUBIC_SIZE_H / 2 - height / 2])
        pygame.draw.rect(self.image, [0, 0, 0], [0, 0, self.CUBIC_SIZE_W, self.CUBIC_SIZE_H], 5, 6)




    def minus_hp(cubic, list):
        if cubic.defended != True:
            cubic.hp -= 1

        cubic.create_image()
        if cubic.hp <= 0:
            a = cubic.groups()
            for i in a:
                i.remove(cubic)
            list.remove(cubic)

