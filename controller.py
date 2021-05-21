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
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = i.pos


            a = model.group.sprites()
            for v in a:
                print(v.rect.collidepoint(pos))
                if v.rect.collidepoint(pos):
                    model.coin += 1
                    model.group.remove(v)
