# coding=utf-8
import random
import pygame

pygame.init()


class Root:  # 기초

    turn = random.randint(0, 2)
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


def typing(text):  # 텍스트 바꿈
    return Root.font.render(text, True, Root.text_color)


def change_turn():
    if Root.turn:
        Root.turn = 0
    else:
        Root.turn = 1
    Root.game_turn += 1


def get_turn():
    if Root.turn:
        return '플레이어1'
    else:
        return '플레이어2'


class Player:

    def __init__(self, x, y, image):
        self.x, self.y = x, y
        self.image = image

        self.max_hp = 0
        self.hp = 0
        self.mp = 0
        self.strength = 0
        self.stat = []

    def hit(self, target):
        target.hp -= self.strength
        target.init()

    def render(self):
        Root.win.blit(self.image, (self.x, self.y))

    def init(self):
        self.stat[1] = self.hp
        self.stat[2] = self.mp


class Player1(Player):
    stat_x = Root.size[0] / 8
    stat_y = Root.size[1] / 16

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.max_hp = 100
        self.hp = 100
        self.mp = 20
        self.strength = 20
        self.stat = ['플레이어1', self.hp, self.mp]


class Player2(Player):
    stat_x = Root.size[0] - Root.size[0] / 8 - 74
    stat_y = Root.size[1] / 16

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.max_hp = 100
        self.hp = 100
        self.mp = 20
        self.strength = 20
        self.stat = ['플레이어2', self.hp, self.mp]


class State:
    class Slot:
        def __init__(self, x, y):
            self.x, self.y = x, y

    class Pointer:
        def __init__(self, x, y):
            self.x, self.y = x - 15, y + 5

        def draw(self):
            pygame.draw.polygon(Root.win, Root.text_color,
                                [[self.x, self.y], [self.x + 8, self.y + 8], [self.x, self.y + 16]])

    class Input:
        def __init__(self, x, y, name, func):
            self.x, self.y = x, y
            self.name = typing(name)
            self.func = func

    def __init__(self):
        self.slot = []
        self.menu = []

    def show_menu(self):
        pass


class Game(State):

    def __init__(self):
        super().__init__()

        self.slot = []
        self.place = 0
        self.pointer = State.Pointer(1, 1)

        self.menu = []

    def show_menu(self):
        pygame.draw.rect(Root.win, Root.text_color, (0, Root.size[1] / 2, Root.size[0], 5))
        pygame.draw.rect(Root.win, Root.text_color, (Root.size[0] / 2, Root.size[1] / 2, 5, Root.size[1]))
        self.pointer.draw()
        for i in range(3):
            Root.win.blit(self.menu[i].name, (self.menu[i].x, self.menu[i].y))

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Root.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.menu[self.place].func()
                    change_turn()
                    self.init()
                elif event.key == pygame.K_w:
                    self.place -= 1
                    self.init()
                elif event.key == pygame.K_s:
                    self.place += 1
                    self.init()

    @staticmethod
    def show_status():  # 상황 보여줌
        game_turn = typing(f'턴 {int(Root.game_turn / 2)}')
        play_turn = typing(f'{get_turn()}의 턴')
        Root.win.blit(game_turn, (Root.size[0] / 2 - 70, Root.size[1] / 16 - 20))
        Root.win.blit(play_turn, (Root.size[0] / 2 - 70, Root.size[1] / 16))
        for i in range(3):
            Root.win.blit(typing(str(Play1.stat[i])), (Player1.stat_x, Player1.stat_y + i * 20))
            Root.win.blit(typing(str(Play2.stat[i])), (Player2.stat_x, Player2.stat_y + i * 20))

    @staticmethod
    def basic_atk():
        if Root.turn:
            Play1.hit(Play2)
        else:
            Play2.hit(Play1)

    def use_skill(self):
        pass

    def recover_mp(self):
        pass

    def init(self):
        if self.place > 4:
            self.place = 4
        elif self.place < 0:
            self.place = 0
        if not Root.turn:
            self.slot = [
                State.Slot(Root.size[0] / 16 + Root.size[0] / 2, Root.size[1] / 2 + 50),
                State.Slot(Root.size[0] / 16 + Root.size[0] / 2, Root.size[1] / 2 + 50 * 2),
                State.Slot(Root.size[0] / 16 + Root.size[0] / 2, Root.size[1] / 2 + 50 * 3),
                State.Slot(Root.size[0] / 16 + Root.size[0] / 2, Root.size[1] / 2 + 50 * 4),
                State.Slot(Root.size[0] / 16 + Root.size[0] / 2, Root.size[1] / 2 + 50 * 5)
            ]
        else:
            self.slot = [
                State.Slot(Root.size[0] / 16, Root.size[1] / 2 + 50),
                State.Slot(Root.size[0] / 16, Root.size[1] / 2 + 50 * 2),
                State.Slot(Root.size[0] / 16, Root.size[1] / 2 + 50 * 3),
                State.Slot(Root.size[0] / 16, Root.size[1] / 2 + 50 * 4),
                State.Slot(Root.size[0] / 16, Root.size[1] / 2 + 50 * 5)
            ]
        self.menu = [
            State.Input(self.slot[0].x, self.slot[0].y, '기본 공격', self.basic_atk),
            State.Input(self.slot[1].x, self.slot[1].y, '스킬', self.use_skill),
            State.Input(self.slot[2].x, self.slot[2].y, '마나 회복', self.recover_mp)
        ]
        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)


Play1 = Player1(Root.size[0] / 8, Root.size[1] / 4, Root.mage)

Play2 = Player2(Root.size[0] - Root.size[0] / 8 - 74, Root.size[1] / 4, Root.mage2)

Sys = Game()
Sys.init()

while Root.run:
    pygame.time.delay(50)

    Root.win.fill(Root.color)
    Play1.render()
    Play2.render()
    Sys.control()
    Sys.show_menu()
    Sys.show_status()
    pygame.display.update()

pygame.quit()
