import pygame, settings, model
pygame.init()

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
screen.fill([255, 0, 0])



def draw():
    model.group.draw(screen)


    pygame.display.flip()

