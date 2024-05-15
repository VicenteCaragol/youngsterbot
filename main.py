# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:48:18 2024

@author: vicen
"""
# Problems to fix:
# Speed is not taken into account.
# Fainted Pokemon should end turn.
# Second player switching should happen before player 1 attacks.

from scripts.classes import Mon
from scripts.functions import action_attack,typechart
from scripts.game import choose_pokemon,game_v0

#team1=choose_pokemon()
pikachu=Mon(species='Pikachu')
bulbasaur=Mon(species='Bulbasaur')
charmander=Mon(species='Charmander')

pikachu.set_attack('Thunder Shock',0)
pikachu.set_attack('Tackle',1)
bulbasaur.set_attack('Vine Whip',0)
charmander.set_attack('Ember',0)



placeholder_team=[pikachu,bulbasaur,charmander]
placeholder_team2=[pikachu.copy(),bulbasaur.copy(),charmander.copy()]




game_v0(placeholder_team,placeholder_team2)
print('hallo')