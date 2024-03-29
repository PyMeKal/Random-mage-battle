import pygame
import random
pygame.init()

class Root:  # 기초

    turn = 0
    game_turn = 2
    size = (1080, 720)
    color = (0, 0, 0)
    text_color = (255, 255, 255)
    run = True
    win = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    state = 0
    # noinspection SpellCheckingInspection
    font = pygame.font.Font("./res/malgun.ttf", 20)  # 기본 폰트
    pygame.display.set_caption("랜덤마법대전입니다 ~~")
    mage = pygame.image.load('./res/wizard.png')  # 일단 이미지임
    mage2 = pygame.image.load('./res/wizard2.png')
    attackmotion1 = pygame.image.load('./res/wizard_attack.png')
    attackmotion2 = pygame.image.load('./res/wizard_attack2.png')
    hitmotion1 = pygame.image.load('./res/wizard_be attacked.png')
    hitmotion2 = pygame.image.load('./res/wizard_be attacked2.png')

    @staticmethod
    def choose_turn():
        Root.turn = random.randint(0, 2)

    @staticmethod
    def typing(text):  # 텍스트 바꿈
        return Root.font.render(text, True, Root.text_color)

    @staticmethod
    def change_turn():
        if Root.turn:
            Root.turn = 0
        else:
            Root.turn = 1
        Root.game_turn += 1




