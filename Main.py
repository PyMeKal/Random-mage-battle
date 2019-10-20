# coding=utf-8
import pygame
from Root import Root
import State
pygame.init()


while Root.run:
    Root.clock.tick(30)
    Root.win.fill(Root.color)
    State.Sys.tick()
    pygame.display.update()

pygame.quit()
