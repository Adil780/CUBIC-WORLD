import pygame, time,  cubic, settings
pygame.init()


group = pygame.sprite.Group()

coin = 0

def create_level_1():
    colums = 5

    start = int(settings.SCREEN_WIDTH / 2) - int(colums / 2 * cubic.Cub.CUBIC_SIZE_W)
    stop = int(settings.SCREEN_WIDTH / 2) + int(colums / 2 * cubic.Cub.CUBIC_SIZE_W)
    step = cubic.Cub.CUBIC_SIZE_W + 2

    for p in range(start, stop, step):
        for i in range(0, settings.SCREEN_HEIGHT - cubic.Cub.CUBIC_SIZE_H, cubic.Cub.CUBIC_SIZE_H + 2):

            a = cubic.Cub(p, i)
            group.add(a)



