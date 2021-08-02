import pygame, cubic, settings, random, ball
pygame.init()

level = 1
cub_list = []
group = pygame.sprite.LayeredUpdates()
coin = 0
button_buy = pygame.Rect(settings.SCREEN_WIDTH - 250, 70, 70, 50)
ball_list = []


def buy_ball():
    global coin
    if coin >= 10:
        coin -= 10
        b = ball.Ball(100, 800, 1, 2)
        ball_list.append(b)
        group.add(b)




def create_level_1():

    colums = 5

    start = int(settings.SCREEN_WIDTH / 2) - int(colums / 2 * cubic.Cub.CUBIC_SIZE_W)
    stop = int(settings.SCREEN_WIDTH / 2) + int(colums / 2 * cubic.Cub.CUBIC_SIZE_W)
    step = cubic.Cub.CUBIC_SIZE_W + 2

    for p in range(start, stop, step):
        for i in range(0, settings.SCREEN_HEIGHT - cubic.Cub.CUBIC_SIZE_H, cubic.Cub.CUBIC_SIZE_H + 2):

            a = cubic.Cub(p, i, 1, False)
            cub_list.append(a)
            group.add(a)




def always():
    global coin
    for i in ball_list:
        coin += i.fly(cub_list)

    #coin += c.fly(cub_list)







