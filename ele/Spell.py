import random

class Spell:
    def __init__(self):
        self.name = ''
        self.cost = 0
        self.heal = 0
        self.strength_buff = 0
        self.damage = 0
        self.recoil = 0

    def use(self):
        pass


class Buff(Spell):
    def __init__(self):
        super().__init__()
        self.heal = 0
        self.strength_buff = 0
        self.recoil

    def use(self, user, target):
        user.hp += self.heal
        if user.hp > user.max_hp:
            user.hp = user.max_hp
        user.strength += self.strength_buff
        if self.strength_buff > 0:
            user.strength_buffed = True
        user.hp -= self.recoil
        user.mp -= self.cost
        user.init()
        target.init()



class AtkSpell(Spell):
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
        self.name = '힐 MP 70'
        self.heal = 30
        self.cost = 70


class Fireball(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '파이어볼 MP 30 HP 5'
        self.damage = 20
        self.cost = 30
        self.recoil = 5


class Iceball(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '아이스볼 MP 40'
        self.damage = 15
        self.cost = 40


class Thunder(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '번개 MP 150'
        self.damage = 40
        self.cost = 150


class Wowei(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '와우이 MP 50'
        self.damage = 30
        self.cost = 50

class Museik(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '머쓱 MP 1'
        self.damage = 0
        self.cost = 1

class Thank(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '감사여 MP 70'
        self.damage = 33
        self.cost = 70

class Pound(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '박치기 MP 100'
        self.damage = 40
        self.cost = 100
        self.recoil = 5

class PorkGukBab(Buff):

    def __init__(self):
        super().__init__()
        self.name = '돼지국밥 Mp 100'
        self.heal = 20
        self.strength_buff = 5
        self.cost = 100

class HellChang1(Buff):

    def __init__(self):
        super().__init__()
        self.name = '데드리프트 hp 10'
        self.strength_buff = 20
        self.recoil = 10

class HellChang2(Buff):

    def __init__(self):
        super().__init__()
        self.name = '스쾃 hp 5'
        self.strength_buff = 15
        self.recoil = 5

class LeftOver(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '찌끄레기 스펠 MP 20'
        self.damage = 25
        self.cost = 40

class Teeth(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '틀니 가즈아!!!! MP 랜덤'
        self.damage = 25
        self.cost = random.randint(20, 80)
