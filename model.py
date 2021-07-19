import pygame, cubic, settings, random, ball
pygame.init()


cub_list = []
group = pygame.sprite.LayeredUpdates()
coin = 0
b = ball.Ball(100, 100, 9, 9)
group.add(b)
c = ball.Ball(200, 900, -9, -9)
group.add(c)



def create_level_1():

    colums = 5

    start = int(settings.SCREEN_WIDTH / 2) - int(colums / 2 * cubic.Cub.CUBIC_SIZE_W)
    stop = int(settings.SCREEN_WIDTH / 2) + int(colums / 2 * cubic.Cub.CUBIC_SIZE_W)
    step = cubic.Cub.CUBIC_SIZE_W + 2

    for p in range(start, stop, step):
        for i in range(0, settings.SCREEN_HEIGHT - cubic.Cub.CUBIC_SIZE_H, cubic.Cub.CUBIC_SIZE_H + 2):

            a = cubic.Cub(p, i, random.randint(1, 10), random.choice([True, False]))
            cub_list.append(a)
            group.add(a)




def always():
    global coin

    coin += b.fly(cub_list)

    coin += c.fly(cub_list)







