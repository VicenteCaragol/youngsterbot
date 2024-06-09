# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:39:14 2024

@author: vicen
"""
import numpy as np

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

type_map={'normal':0, 'fire':1,'water':2,'electric':3,'grass':4,'ice':5,'fighting':6,'poison':7,'ground':8,'flying':9,'psychic':10,
          'bug':11,'rock':12,'ghost':13,'dragon':14,'dark':15,'steel':16,'fairy':17}

type_map_inverted = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 
                     'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']



def build_typechart():
    typechart= np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #Normal
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #Fire
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #Water
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #Electric
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ], dtype=np.float32)
    #Normal
    typechart[type_map['normal'],type_map['rock']]=0.5
    typechart[type_map['normal'],type_map['ghost']]=0
    typechart[type_map['normal'],type_map['steel']]=0.5
    #Fire
    typechart[type_map['fire'],type_map['fire']]=0.5
    typechart[type_map['fire'],type_map['water']]=0.5
    typechart[type_map['fire'],type_map['grass']]=2
    typechart[type_map['fire'],type_map['ice']]=2
    typechart[type_map['fire'],type_map['bug']]=2
    typechart[type_map['fire'],type_map['rock']]=0.5
    typechart[type_map['fire'],type_map['dragon']]=0.5
    typechart[type_map['fire'],type_map['steel']]=2
    #Water
    typechart[type_map['water'],type_map['fire']]=2
    typechart[type_map['water'],type_map['water']]=0.5
    typechart[type_map['water'],type_map['grass']]=0.5
    typechart[type_map['water'],type_map['ground']]=2
    typechart[type_map['water'],type_map['rock']]=2
    typechart[type_map['water'],type_map['dragon']]=0.5
    #Electric
    typechart[type_map['electric'],type_map['water']]=2
    typechart[type_map['electric'],type_map['electric']]=0.5
    typechart[type_map['electric'],type_map['grass']]=0.5
    typechart[type_map['electric'],type_map['ground']]=0
    typechart[type_map['electric'],type_map['flying']]=2
    typechart[type_map['electric'],type_map['dragon']]=0.5
    #Grass
    for type,mult in [['fire',0.5],['water',2],['grass',0.5],['poison',0.5],['ground',2],['bug',0.5],['rock',2],['dragon',0.5],['steel',0.5]]:
        typechart[type_map['grass'],type_map[type]]=mult
    #Ice
    for type,mult in [['fire',0.5],['water',0.5],['grass',2],['ice',0.5],['ground',2],['flying',2],['dragon',2],['steel',0.5]]:
        typechart[type_map['ice'],type_map[type]]=mult
    #Fighting
    for type,mult in [['normal',2],['ice',2],['poison',0.5],['flying',0.5],['psychic',0.5],['bug',0.5],['rock',2],['ghost',0],['dark',2],['steel',2],['fairy',0.5]]:
        typechart[type_map['fighting'],type_map[type]]=mult
    #Poison
    typechart[type_map['poison'],type_map['grass']]=2
    typechart[type_map['poison'],type_map['poison']]=0.5
    typechart[type_map['poison'],type_map['ground']]=0.5
    typechart[type_map['poison'],type_map['rock']]=0.5
    typechart[type_map['poison'],type_map['ghost']]=0.5
    typechart[type_map['poison'],type_map['steel']]=0
    typechart[type_map['poison'],type_map['fairy']]=2
    #Ground
    typechart[type_map['ground'],type_map['fire']]=2
    typechart[type_map['ground'],type_map['electric']]=2
    typechart[type_map['ground'],type_map['grass']]=0.5
    typechart[type_map['ground'],type_map['poison']]=2
    typechart[type_map['ground'],type_map['flying']]=0
    typechart[type_map['ground'],type_map['bug']]=0.5
    typechart[type_map['ground'],type_map['rock']]=2
    typechart[type_map['ground'],type_map['steel']]=2


    return typechart
typechart= build_typechart()