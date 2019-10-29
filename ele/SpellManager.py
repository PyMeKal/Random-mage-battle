import random
from ele.Spell import Fireball, Iceball, Thunder, Heal, Pound, Wowei, YoudieIdie, Museik, PorkGukBab, HellChang1, HellChang2, LeftOver, Teeth, Stun, Slime, InstaKill, FireOverload

distribute_list = [Fireball(), Iceball(), Thunder(), Heal(), Pound(), Wowei(), YoudieIdie(), Museik(), PorkGukBab(), HellChang1(), HellChang2(),
                   LeftOver(), Teeth(), Stun(), Slime(), InstaKill(), FireOverload()]




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

    distribute_list = [Fireball(), Iceball(), Thunder(), Heal(), Pound(), Wowei(), YoudieIdie(), Museik(), PorkGukBab(),
                       HellChang1(), HellChang2(),
                       LeftOver(), Teeth(), Stun(), Slime(), InstaKill(), FireOverload()]




