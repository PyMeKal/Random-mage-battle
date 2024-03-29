from Root import Root
from state.State import State

class StartScreen(State):
    text = Root.typing('랜덤 마법 대전')
    version = Root.typing('V.1.0.1 copyright by SaNaE')

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
        Root.win.blit(StartScreen.version, (Root.size[0] / 16, Root.size[1] - Root.size[1] / 16))
        Root.win.blit(self.menu[0].name, (self.slot[0].x, self.slot[0].y))
        Root.win.blit(self.menu[1].name, (self.slot[1].x, self.slot[1].y))

    @staticmethod
    def start():
        Root.choose_turn()
        Root.state = 1


    def credit(self):
        Root.state = 3