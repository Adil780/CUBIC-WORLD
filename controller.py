import pygame,  cubic, model
pygame.init()

def events():
    """
    process events
    """
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            pos = i.pos
            b = model.group.sprites()
            for v in b:
                if v.rect.collidepoint(pos):
                    v.minus_hp(model.cub_list)
                    model.coin += 1



