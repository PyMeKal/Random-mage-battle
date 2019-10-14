# coding=utf-8
import random
import pygame

pygame.init()

Play1 = Player1(Root.size[0] / 8, Root.size[1] / 4, '섹시도발태현이', Root.mage)
Play2 = Player2(Root.size[0] - Root.size[0] / 8 - 74, Root.size[1] / 4, '머리반짝승준이', Root.mage2)

Sys = Start_Screen()

while Root.run:
    pygame.time.delay(50)
    Root.win.fill(Root.color)
    Sys.tick()
    pygame.display.update()

pygame.quit()
