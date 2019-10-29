from Root import Root
from state.State import State

class Credit(State):
    x = Root.size[0] / 2 - 100
    director = Root.typing ('프로듀서 및 프로그래머')
    jun = Root.typing ('윤석준')
    designer = Root.typing('기획 및 캐릭터 디자인')
    junhee = Root.typing('이준희')
    specialthank = Root.typing('Special Thanks')
    gojun = Root.typing('고준')
    sci = Root.typing('전한결')
    ethan = Root.typing('최민혁 선생님')
    cicpu = Root.typing('cicpu 2019')
    sanae = Root.typing('Project SaNaE')


    def __init__(self):
        super().__init__()
        self.slot = [
            State.Slot(Root.size[0] / 2 - 100, Root.size[1] / 2),
            ]
        self.menu = [
            State.Input(self.slot[0].x, self.slot[0].y, '', self.go_back)
        ]

    def show_menu(self):
        Root.win.blit(Credit.director, (Credit.x - 50, Root.size[1] / 16))
        Root.win.blit(Credit.jun, (Credit.x, Root.size[1] / 16 + 50 ))
        Root.win.blit(Credit.designer, (Credit.x - 50, Root.size[1] / 16 + 150))
        Root.win.blit(Credit.junhee, (Credit.x, Root.size[1] / 16 + 200))
        Root.win.blit(Credit.specialthank, (Credit.x - 50, Root.size[1] / 16 + 300))
        Root.win.blit(Credit.gojun, (Credit.x, Root.size[1] / 16 + 350))
        Root.win.blit(Credit.sci, (Credit.x, Root.size[1] / 16 + 400))
        Root.win.blit(Credit.ethan, (Credit.x, Root.size[1] / 16 + 450))
        Root.win.blit(Credit.cicpu, (Root.size[0] / 16, Root.size[1] / 16 + 600))
        Root.win.blit(Credit.sanae, (Root.size[0] / 16 + 150, Root.size[1] / 16 + 600))


    @staticmethod
    def go_back():
        Root.state = 0
