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
    # noinspection SpellCheckingInspection
    font = pygame.font.Font("./res/malgun.ttf", 20)  # 기본 폰트
    pygame.display.set_caption("랜덤마법대전입니다 ~~")
    mage = pygame.image.load('./res/mage.jpg')  # 일단 이미지임
    mage2 = pygame.image.load('./res/mage2.jpg')

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

    @staticmethod
    def get_turn():
        global Play1, Play2
        if Root.turn:  # 턴이 1이면 플레이어 1 0이면 플레이어 2
            return Play1.name
        else:
            return Play2.name
