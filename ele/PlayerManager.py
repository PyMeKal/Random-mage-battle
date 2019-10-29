from Root import Root
from ele.Player import Player1, Player2

class RealPlayers:
    player1 = Player1(Root.size[0] / 8 - 20, Root.size[1] / 4 - 30, '플레이어1', Root.mage)
    player2 = Player2(Root.size[0] - Root.size[0] / 8 - 100, Root.size[1] / 4 - 40, '플레이어2', Root.mage2)