import random
from Root import Root
from ele.PlayerManager import RealPlayers as P
from ele.Spell import Spell, Fireball, Iceball, Thunder, Heal, Pound, Wowei, Thank, Museik

distribute_list = [Fireball(), Iceball(), Thunder(), Heal(), Pound(), Wowei(), Thank(), Museik()]


def random_spell(player):
    global distribute_list

    if len(player.spell_list) > 3:
        for i in range(4):
            player.spell_list.remove(player.spell_list[0])
            spell = random.choice(distribute_list)
            player.spell_list.append(spell)
            distribute_list.remove(spell)
    else:
        for i in range(4):
            spell = random.choice(distribute_list)
            player.spell_list.append(spell)
            distribute_list.remove(spell)

    distribute_list = [Fireball(), Iceball(), Thunder(), Heal(), Pound(), Wowei(), Thank(), Museik()]


