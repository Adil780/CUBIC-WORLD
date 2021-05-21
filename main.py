import pygame, view, controller, model
pygame.init()



model.create_level_1()
while True:
    view.draw()


    controller.events()