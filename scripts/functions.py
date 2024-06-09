import numpy as np

from .classes import Mon,Attack
from .database import typechart


    
def action_attack(attacking_mon,target_mon,attack_index):
    attack=attacking_mon.attacks[attack_index]
    attack.pp-=1
    print(f'{attacking_mon.species} used {attack.name}!')
    multiplier=typechart[attack.info['type'],target_mon.stats['type']]
    if target_mon.hp <= attack.info['BP']*multiplier:
        target_mon.hp=0
    else:
        target_mon.hp-=attack.info['BP']*multiplier
