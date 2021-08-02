import pygame, settings, model, cubic
pygame.init()

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])



f = pygame.font.SysFont("arial", 50, True)




def draw():
    screen.fill([255, 0, 0])
    model.group.draw(screen)

    coins = f.render("COINS " + str(model.coin), True, [255, 247, 9])
    screen.blit(coins, [settings.SCREEN_WIDTH - 250, 10])
    pygame.draw.rect(screen, [0, 255, 0], model.button_buy)
    buy = f.render("-10", True, [0, 0, 0])
    screen.blit(buy, model.button_buy)
    pygame.display.flip()

