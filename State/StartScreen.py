from State import State
from Game import Game

class StartScreen(State):
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
        Root.win.blit(StartScreen.text, (Root.size[0] / 2 - 100, Root.size[1] / 2 - 50))
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