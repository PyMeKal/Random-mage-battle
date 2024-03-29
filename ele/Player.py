from Root import Root

class Player:

    def __init__(self, x, y, name, image):
        self.x, self.y = x, y
        self.name = name
        self.image = image

        self.max_hp = 100
        self.hp = 100
        self.max_mp = 300
        self.mp = 300
        self.strength = 10
        self.strength_buffed = False
        self.strength_buffed_time = -10
        self.stun = False
        self.stun_time = -10
        self.slime = False
        self.slime_time = -10
        self.stat = []
        self.spell_list = []

    def hit(self, target):
        target.hp -= self.strength
        target.init()

    def render(self):
        Root.win.blit(self.image, (self.x, self.y))

    def init(self):
        self.stat[1] = self.hp
        self.stat[2] = self.mp

    def revive(self):
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.stun = False
        self.slime = False
        self.strength = 10
        self.strength_buffed = False
        self.returned()

    def returned(self):
        pass




class Player1(Player):
    stat_x = Root.size[0] / 8
    stat_y = Root.size[1] / 16

    def __init__(self, x, y, name, image):
        super().__init__(x, y, name, image)
        self.stat = [self.name, self.hp, self.mp]

    def returned(self):
        self.image = Root.mage


class Player2(Player):
    stat_x = Root.size[0] - Root.size[0] / 8 - 74
    stat_y = Root.size[1] / 16

    def __init__(self, x, y, name, image):
        super().__init__(x, y, name, image)
        self.stat = [self.name, self.hp, self.mp]

    def returned(self):
        self.image = Root.mage2


