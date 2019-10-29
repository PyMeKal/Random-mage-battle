import random
from Root import Root

class Spell:
    def __init__(self):
        self.name = ''
        self.cost = 0
        self.heal = 0
        self.strength_buff = 0
        self.damage = 0
        self.recoil = 0
        self.give_stun = False
        self.give_slime = False

    def use(self):
        pass


class Buff(Spell):
    def __init__(self):
        super().__init__()
        self.heal = 0
        self.strength_buff = 0
        self.recoil = 0

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
        self.give_slime = False

    def use(self, user, target):
        target.hp -= self.damage
        user.hp -= self.recoil
        user.mp -= self.cost
        if self.give_stun:
            target.stun = True
        if self.give_slime:
            target.slime = True
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
        self.damage = 30
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

class YoudieIdie(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '너죽고나죽자 MP 150'
        self.damage = 50
        self.recoil = 50
        self.cost = 150


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

    def use(self, user, target):
        user.strength_buffed_time = Root.game_turn
        super().use(user, target)

class HellChang1(Buff):

    def __init__(self):
        super().__init__()
        self.name = '데드리프트 hp 10'
        self.strength_buff = 20
        self.recoil = 10

    def use(self, user, target):
        user.strength_buffed_time = Root.game_turn
        super().use(user, target)


class HellChang2(Buff):

    def __init__(self):
        super().__init__()
        self.name = '스쾃 hp 5'
        self.strength_buff = 15
        self.recoil = 5

    def use(self, user, target):
        user.strength_buffed_time = Root.game_turn
        super().use(user, target)

class LeftOver(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '찌끄레기 스펠 MP 40'
        self.damage = 25
        self.cost = 40

class Teeth(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '틀니 가즈아!!!! MP 랜덤'
        self.damage = 25
        self.cost = random.randint(20, 80)

class Stun(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '스턴 맥여버리기 MP 120'
        self.damage = 20
        self.cost = 120
        self.give_stun = True

    def use(self, user, target):
        target.stun_time = Root.game_turn
        super().use(user,target)

class Slime(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '수리수리마수리슬라임으로변해라얍 MP 100'
        self.cost = 100
        self.give_slime = True

    def use(self, user, target):
        target.slime_time = Root.game_turn
        super().use(user,target)

class InstaKill(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '거열 MP 200'
        self.chance = random.randint(0,100)
        self.cost = 200

    def use(self, user, target):
        if self.chance < 30:
            self.damage = 200
        else:
            self.recoil = 10
        super().use(user, target)

class FireOverload(AtkSpell):

    def __init__(self):
        super().__init__()
        self.name = '작열폭참 MP 200'
        self.damage = 70
        self.cost = 200

