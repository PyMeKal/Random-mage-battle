# coding=utf-8
import random
import pygame

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
    mage = pygame.image.load('./res/mage.png')  # 일단 이미지임
    mage2 = pygame.image.load('./res/mage2.jpg')

    @staticmethod
    def choose_turn():
        Root.turn = random.randint(0,2)

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


class Player:

    def __init__(self, x, y, name, image):
        self.x, self.y = x, y
        self.name = name
        self.image = image

        self.max_hp = 100
        self.hp = 100
        self.max_mp = 20
        self.mp = 20
        self.strength = 20
        self.stat = []

    def hit(self, target):
        target.hp -= self.strength
        target.init()

    def render(self):
        Root.win.blit(self.image, (self.x, self.y))

    def init(self):
        self.stat[1] = self.hp
        self.stat[2] = self.mp
        self.death()

    def death(self):
        global Sys
        if self.hp <= 0:
            Sys = Death_Screen()
        else: pass

    def revive(self):
        self.hp = self.max_hp
        self.mp = self.max_mp

class Player1(Player):
    stat_x = Root.size[0] / 8
    stat_y = Root.size[1] / 16

    def __init__(self, x, y, name, image):
        super().__init__(x, y, name, image)
        self.stat = [self.name, self.hp, self.mp]

    def death(self):
        super().death()
        Sys.text = Root.typing(f'{Play2.name}(이)가 이겼습니다!')

class Player2(Player):
    stat_x = Root.size[0] - Root.size[0] / 8 - 74
    stat_y = Root.size[1] / 16

    def __init__(self, x, y, name, image):
        super().__init__(x, y, name, image)
        self.stat = [self.name, self.hp, self.mp]

    def death(self):
        super().death()
        Sys.text = Root.typing(f'{Play1.name}(이)가 이겼습니다!')

class Spell:
    def __init__(self):
        self.name = ''
        self.cost = 0

    def use(self):
        Play1.init()
        Play2.init()
        Root.change_turn()
        Sys.init()

class Buff(Spell):
    def __init__(self):
        super().__init__()
        self.heal = 0
        self.strength_buff = 0

    def use(self):
        global Play1, Play2
        if Root.turn:
            Play1.hp += self.heal
            Play1.strength += self.strength_buff
            Play1.mp -= self.cost
        else:
            Play2.hp += self.heal
            Play2.strength += self.strength_buff
            Play2.mp -= self.cost
        super().use()


class ATK_Spell(Spell):
    def __init__(self):
        super().__init__()
        self.damage = 0

    def use(self):
        global Play1, Play2
        if Root.turn:
            Play2.hp -= self.damage
            Play1.mp -= self.cost
        else:
            Play1.hp -= self.damage
            Play2.mp -= self.cost
        super().use()


class Heal(Buff):
    def __init__(self):
        super().__init__()
        self.name = '힐'
        self.heal = 30
        self.cost = 10

        
class Fireball(ATK_Spell):

    def __init__(self):
        self.name = '파이어볼'
        self.damage = 30
        self.cost = 10


class Iceball(ATK_Spell):

    def __init__(self):
        self.name = '아이스볼'
        self.damage = 25
        self.cost = 5


class Thunder(ATK_Spell):

    def __init__(self):
        self.name = '번개'
        self.damage = 40
        self.cost = 15


class State:
    class Slot:
        def __init__(self, x, y):
            self.x, self.y = x, y

    class Pointer:
        def __init__(self, x, y):
            self.x, self.y = x - 15, y + 5

        def draw(self):
            pygame.draw.polygon(Root.win, Root.text_color,
                                ((self.x, self.y), (self.x + 8, self.y + 8), (self.x, self.y + 16)))

    class Input:
        def __init__(self, x, y, name, func):
            self.x, self.y = x, y
            self.name = Root.typing(name)
            self.func = func

    def __init__(self):
        self.slot = []
        self.menu = []
        self.place = 0

    def show_menu(self):
        pass

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Root.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.menu[self.place].func()
                elif event.key == pygame.K_UP:
                    self.place -= 1
                    self.pointer_limit()
                elif event.key == pygame.K_DOWN:
                    self.place += 1
                    self.pointer_limit()

    def pointer_limit(self):
        if self.place < 0: self.place = 0
        elif self.place >= len(self.menu): self.place = len(self.menu) - 1
        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)

    def tick(self):
        self.control()
        self.show_menu()



class Start_Screen(State):
    text = Root.typing('랜덤 마법 대전')


    def __init__(self):
        super().__init__()
        self.slot = [
            State.Slot(Root.size[0] / 2 - 100, Root.size[1] / 2),
            State.Slot(Root.size[0] / 2 - 100, Root.size[1] / 2 + 30)
        ]
        self.menu = [
            State.Input(self.slot[0].x, self.slot[0].y, '시작하기', self.start),
            State.Input(self.slot[1].x, self.slot[1].y, '만든 사람들', self.credit)
        ]
        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)

    def show_menu(self):
        self.pointer.draw()
        Root.win.blit(Start_Screen.text, (Root.size[0] / 2 - 100, Root.size[1] / 2 - 50))
        Root.win.blit(self.menu[0].name, (self.slot[0].x, self.slot[0].y))
        Root.win.blit(self.menu[1].name, (self.slot[1].x, self.slot[1].y))

    @staticmethod
    def start():
        global Sys
        Root.choose_turn()
        Sys = Game()
        Sys.init()

    def credit(self):
        pass


class Game(State):

    def __init__(self):
        super().__init__()

    def show_menu(self):
        pygame.draw.rect(Root.win, Root.text_color, (0, Root.size[1] / 2, Root.size[0], 5))
        pygame.draw.rect(Root.win, Root.text_color, (Root.size[0] / 2, Root.size[1] / 2, 5, Root.size[1]))
        self.pointer.draw()
        for i in range(len(self.menu)):
            Root.win.blit(self.menu[i].name, (self.menu[i].x, self.menu[i].y))

    @staticmethod
    def show_status():  # 상황 보여줌
        game_turn = Root.typing(f'턴 {int(Root.game_turn / 2)}')
        play_turn = Root.typing(f'{Root.get_turn()}의 턴')
        Root.win.blit(game_turn, (Root.size[0] / 2 - 70, Root.size[1] / 16 - 20))
        Root.win.blit(play_turn, (Root.size[0] / 2 - 70, Root.size[1] / 16))
        for i in range(3):
            Root.win.blit(Root.typing(str(Play1.stat[i])), (Player1.stat_x, Player1.stat_y + i * 20))
            Root.win.blit(Root.typing(str(Play2.stat[i])), (Player2.stat_x, Player2.stat_y + i * 20))

    def basic_atk(self):
        if Root.turn:
            Play1.hit(Play2)
        else:
            Play2.hit(Play1)
        Root.change_turn()
        self.init()


    def recover_mp(self):
        Root.change_turn()
        self.init()

    def init(self):
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
            State.Input(self.slot[1].x, self.slot[1].y, '스킬', self.open_magic_menu),
            State.Input(self.slot[2].x, self.slot[2].y, '마나 회복', self.recover_mp)
        ]
        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)


    def open_magic_menu(self):
        self.place = 0

        self.menu = [
            State.Input(self.slot[0].x, self.slot[0].y, Fireball().name, Fireball().use),
            State.Input(self.slot[1].x, self.slot[1].y, Iceball().name, Iceball().use),
            State.Input(self.slot[2].x, self.slot[2].y, Thunder().name, Thunder().use),
            State.Input(self.slot[3].x, self.slot[3].y, Heal().name, Heal().use)
        ]

        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)


    def tick(self):
        super().tick()
        self.show_status()
        Play1.render()
        Play2.render()



class Death_Screen(State):

    def __init__(self):
        super().__init__()
        self.text = Root.typing('')
        self.slot = [
            State.Slot(Root.size[0] / 2 - 100, Root.size[1] / 2),
            State.Slot(Root.size[0] / 2 - 100, Root.size[1] / 2 + 30),
            State.Slot(Root.size[0] / 2 - 100, Root.size[1] / 2 + 60)
        ]
        self.menu = [
            State.Input(self.slot[0].x, self.slot[0].y, '다시하기', self.restart),
            State.Input(self.slot[1].x, self.slot[1].y, '메인화면으로', self.start_screen),
            State.Input(self.slot[2].x, self.slot[2].y, '끝내기', self.end)
        ]
        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)

    def show_menu(self):
        self.pointer.draw()
        Root.win.blit(self.text, (Root.size[0] / 2 - 160, Root.size[1] / 2 - 50))
        for i in range(len(self.menu)):
            Root.win.blit(self.menu[i].name, (self.slot[i].x, self.slot[i].y))


    def restart(self):
        self.reset()
        global Sys
        Sys = Game()
        Sys.init()


    def start_screen(self):
        self.reset()
        global Sys
        Sys = Start_Screen()

    @staticmethod
    def reset():
        Root.choose_turn()
        Root.game_turn = 2
        global Sys, Play1, Play2
        Play1.revive()
        Play1.init()
        Play2.revive()
        Play2.init()


    @staticmethod
    def end():
        Root.run = False


Play1 = Player1(Root.size[0] / 8, Root.size[1] / 4, '섹시도발봉찬이', Root.mage)
Play2 = Player2(Root.size[0] - Root.size[0] / 8 - 74, Root.size[1] / 4, '귀염뽀짝진택이', Root.mage2)

Sys = Start_Screen()


while Root.run:
    pygame.time.delay(50)
    Root.win.fill(Root.color)
    Sys.tick()
    pygame.display.update()

pygame.quit()
