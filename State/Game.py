import pygame
from Root import Root
from state.State import State
from ele.Player import Player1, Player2
from ele.PlayerManager import RealPlayers as P
from state.DeathScreen import DeathScreen
from ele.Spell import Spell, Fireball, Iceball, Thunder, Heal
import ele.SpellManager as Sp
pygame.init()

class Game(State):

    def __init__(self):
        super().__init__()
        self.player1 = P.player1
        self.player2 = P.player2

    def show_menu(self):
        pygame.draw.rect(Root.win, Root.text_color, (0, Root.size[1] / 2, Root.size[0], 5))
        pygame.draw.rect(Root.win, Root.text_color, (Root.size[0] / 2, Root.size[1] / 2, 5, Root.size[1]))
        self.pointer.draw()
        for i in range(len(self.menu)):
            Root.win.blit(self.menu[i].name, (self.menu[i].x, self.menu[i].y))

    def show_status(self):  # 상황 보여줌
        game_turn = Root.typing(f'턴 {int(Root.game_turn / 2)}')
        play_turn = Root.typing(f'{self.get_turn()}의 턴')
        Root.win.blit(game_turn, (Root.size[0] / 2 - 70, Root.size[1] / 16 - 20))
        Root.win.blit(play_turn, (Root.size[0] / 2 - 70, Root.size[1] / 16))
        for i in range(3):
            Root.win.blit(Root.typing(str(self.player1.stat[i])), (Player1.stat_x, Player1.stat_y + i * 20))
            Root.win.blit(Root.typing(str(self.player2.stat[i])), (Player2.stat_x, Player2.stat_y + i * 20))

    def basic_atk(self):
        if Root.turn:
            self.player1.hit(self.player2)
            Game.death(self.player2, self.player1)
        else:
            self.player2.hit(self.player1)
            Game.death(self.player1, self.player2)
        Root.change_turn()
        self.init()

    def use_spell(self):
        if Root.turn:
            self.player1.spell_list[self.place].use(self.player1, self.player2)
            Game.death(self.player2, self.player1)
        else:
            self.player2.spell_list[self.place].use(self.player2, self.player1)
            Game.death(self.player1, self.player2)
        Root.change_turn()
        self.init()

    def recover_mp(self):
        Root.change_turn()
        self.init()

    @staticmethod
    def death(loser, winner):
        if loser.hp <= 0:
            DeathScreen.text = Root.typing(f'{winner.name}(이)가 이겼습니다!')
            Root.state = 2
        else:
            pass

    def get_turn(self):
        if Root.turn:  # 턴이 1이면 플레이어 1 0이면 플레이어 2
            return self.player1.name
        else:
            return self.player2.name

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

        if Root.turn:
            Sp.random_spell(self.player1)
        else:
            Sp.random_spell(self.player2)

        if Root.turn:
            self.menu = [
                State.Input(self.slot[0].x, self.slot[0].y, self.player1.spell_list[0].name, self.use_spell),
                State.Input(self.slot[1].x, self.slot[1].y, self.player1.spell_list[1].name, self.use_spell),
                State.Input(self.slot[2].x, self.slot[2].y, self.player1.spell_list[2].name, self.use_spell),
                State.Input(self.slot[3].x, self.slot[3].y, self.player1.spell_list[3].name, self.use_spell)
            ]

        else:
            self.menu = [
                State.Input(self.slot[0].x, self.slot[0].y, self.player2.spell_list[0].name, self.use_spell),
                State.Input(self.slot[1].x, self.slot[1].y, self.player2.spell_list[1].name, self.use_spell),
                State.Input(self.slot[2].x, self.slot[2].y, self.player2.spell_list[2].name, self.use_spell),
                State.Input(self.slot[3].x, self.slot[3].y, self.player2.spell_list[3].name, self.use_spell)
            ]


        self.pointer = State.Pointer(self.slot[self.place].x, self.slot[self.place].y)

    def control_function(self):
            self.menu[self.place].func()


    def tick(self):
        super().tick()
        self.show_status()
        self.player1.render()
        self.player2.render()
