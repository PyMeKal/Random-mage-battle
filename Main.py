# coding=utf-8
import pygame
from Root import Root
from State import StartScreen, Game, DeathScreen

pygame.init()

Sys = StartScreen()

while Root.run:
    pygame.time.delay(50)
    Root.win.fill(Root.color)
    Sys.tick()
    pygame.display.update()

pygame.quit()
