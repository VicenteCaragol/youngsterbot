# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:39:14 2024

@author: vicen
"""

mon_data= {'Pikachu': {'HP':100, 'attack':100,'defense':100,'type':'electric'},
           'Bulbasaur': {'HP':100, 'attack':100,'defense':100,'type':'grass'},
           'Charmander': {'HP':100, 'attack':100,'defense':100,'type':'fire'},
           'Squirtle': {'HP':100, 'attack':100,'defense':100,'type':'water'},
           'Pidgey': {'HP':100, 'attack':100,'defense':100,'type':'flying'}
           }

attack_data = {
    "Tackle": {"BP": 20, "maxPP": 20, "type": "normal"},
    "Vine Whip": {"BP": 20, "maxPP": 20, "type": "grass"},
    "Bubble": {"BP": 20, "maxPP": 20, "type": "water"},
    "Ember": {"BP": 20, "maxPP": 20, "type": "fire"},
    "Thunder Shock": {"BP": 20, "maxPP": 20, "type": "electric"},
    "Gust": {"BP": 20, "maxPP": 20, "type": "flying"},
}

typechart_data={'normal':{'ghost':0},
                'grass':{'fire':0.5,'grass':0.5,'water':2},
                'fire':{'fire':0.5,'water':0.5,'grass':2},
                'water':{'water':0.5,'grass':0.5,'fire':2},
                'electric':{'electric':0.5,'grass':0.5,'water':2,'flying':2},
                'flying':{'electric':0.5,'grass':2}
                }