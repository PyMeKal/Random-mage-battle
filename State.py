import pygame

from Player import Player1, Player2
from Root import Root


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
        if self.place < 0:
            self.place = 0
        elif self.place >= len(self.menu):
            self.place = len(self.menu) - 1
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


class DeathScreen(State):

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

    def init(self):
        pass

