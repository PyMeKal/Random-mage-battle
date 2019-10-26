# coding=utf-8
import pygame
from Root import Root
from state.StateManager import StateManager as S

pygame.init()

while Root.run:
    Root.clock.tick(30)
    Root.win.fill(Root.color)
    S.tick()
    pygame.display.update()

pygame.quit()
