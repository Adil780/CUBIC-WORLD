import pygame, settings, model
pygame.init()

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])


f = pygame.font.SysFont("arial", 50, True)






def draw():
    screen.fill([255, 0, 0])
    model.group.draw(screen)

    coins = f.render("COINS " + str(model.coin), True, [255, 247, 9])
    screen.blit(coins, [settings.SCREEN_WIDTH - 250, 10])

    pygame.display.flip()

