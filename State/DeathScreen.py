from Root import Root
from state.State import State
from ele.PlayerManager import RealPlayers as P

class DeathScreen(State):
    text = Root.typing('')

    def __init__(self):
        super().__init__()
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
        Root.win.blit(DeathScreen.text, (Root.size[0] / 2 - 160, Root.size[1] / 2 - 50))
        for i in range(len(self.menu)):
            Root.win.blit(self.menu[i].name, (self.slot[i].x, self.slot[i].y))

    def restart(self):
        self.reset()
        Root.state = 1


    def start_screen(self):
        self.reset()
        Root.state = 0

    @staticmethod
    def reset():
        Root.choose_turn()
        P.player1.revive()
        P.player2.revive()
        P.player1.init()
        P.player2.init()
        Root.game_turn = 2

    @staticmethod
    def end():
        Root.run = False

    def init(self):
        pass