
class Spell:
    def __init__(self):
        self.name = ''
        self.cost = 0

    def use(self):
        pass


class Buff(Spell):
    def __init__(self):
        super().__init__()
        self.heal = 0
        self.strength_buff = 0

    def use(self, user, target):
        user.hp += self.heal
        user.strength += self.strength_buff
        user.mp -= self.cost
        user.init()
        target.init()



class ATK_Spell(Spell):
    def __init__(self):
        super().__init__()
        self.damage = 0

    def use(self, user, target):
        target.hp -= self.damage
        user.mp -= self.cost
        user.init()
        target.init()



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


class Wowei(ATK_Spell):

    def __init__(self):
        super().__init__()
        self.name = '와우이'
        self.damage = 40
        self.cost = 15

class Museik(ATK_Spell):

    def __init__(self):
        super().__init__()
        self.name = '머쓱'
        self.damage = 40
        self.cost = 15

class Thank(ATK_Spell):

    def __init__(self):
        super().__init__()
        self.name = '감사여'
        self.damage = 40
        self.cost = 15

class Pound(ATK_Spell):

    def __init__(self):
        super().__init__()
        self.name = '파운드'
        self.damage = 40
        self.cost = 15

