import pygame
pygame.init()

def events():
    """
    process events
    """
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()