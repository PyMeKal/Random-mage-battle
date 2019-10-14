





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
        super().__init__()
        self.name = '파이어볼'
        self.damage = 30
        self.cost = 10


class Iceball(ATK_Spell):

    def __init__(self):
        super().__init__()
        self.name = '아이스볼'
        self.damage = 25
        self.cost = 5


class Thunder(ATK_Spell):

    def __init__(self):
        super().__init__()
        self.name = '번개'
        self.damage = 40
        self.cost = 15

