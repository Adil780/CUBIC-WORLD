import pygame, time, view, controller, model
pygame.init()



model.create_level_1()
while True:
    time.sleep(1/60)
    view.draw()
    model.always()

    controller.events()