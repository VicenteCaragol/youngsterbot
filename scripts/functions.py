import numpy as np

from .classes import Mon,Attack
from .database import typechart_data

def typechart(attack_type,target_type):
    if target_type in typechart_data[attack_type].keys():
        return typechart_data[attack_type][target_type]
    else:
        return 1
    
def action_attack(attacking_mon,target_mon,attack_index):
    attack=attacking_mon.attacks[attack_index]
    attack.pp-=1
    multiplier=typechart(attack.info['type'],target_mon.stats['type'])
    if target_mon.hp <= attack.info['BP']*multiplier:
        target_mon.hp=0
    else:
        target_mon.hp-=attack.info['BP']*multiplier
