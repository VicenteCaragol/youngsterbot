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
    typechart= np.array([[1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 0.5,
        0. , 1. , 1. , 0.5, 1. ],#Normal
       [1. , 0.5, 0.5, 1. , 2. , 2. , 1. , 1. , 1. , 1. , 1. , 2. , 0.5,
        1. , 0.5, 1. , 2. , 1. ],#Fire
       [1. , 2. , 0.5, 1. , 0.5, 1. , 1. , 1. , 2. , 1. , 1. , 1. , 2. ,
        1. , 0.5, 1. , 1. , 1. ],#Water
       [1. , 1. , 2. , 0.5, 0.5, 1. , 1. , 1. , 0. , 2. , 1. , 1. , 1. ,
        1. , 0.5, 1. , 1. , 1. ],#Grass
       [1. , 0.5, 2. , 1. , 0.5, 1. , 1. , 0.5, 2. , 1. , 1. , 0.5, 2. ,
        1. , 0.5, 1. , 0.5, 1. ],#Electric
       [1. , 0.5, 0.5, 1. , 2. , 0.5, 1. , 1. , 2. , 2. , 1. , 1. , 1. ,
        1. , 2. , 1. , 0.5, 1. ],#Ice
       [2. , 1. , 1. , 1. , 1. , 2. , 1. , 0.5, 1. , 0.5, 0.5, 0.5, 2. ,
        0. , 1. , 2. , 2. , 0.5],#Fighting
       [1. , 1. , 1. , 1. , 2. , 1. , 1. , 0.5, 0.5, 1. , 1. , 1. , 0.5,
        0.5, 1. , 1. , 0. , 2. ],#Poison
       [1. , 2. , 1. , 2. , 0.5, 1. , 1. , 2. , 1. , 0. , 1. , 0.5, 2. ,
        1. , 1. , 1. , 2. , 1. ],#Ground
       [1. , 1. , 1. , 0.5, 2. , 1. , 2. , 1. , 1. , 1. , 1. , 2. , 0.5,
        1. , 1. , 1. , 0.5, 1. ],#Flying
       [1. , 1. , 1. , 1. , 1. , 1. , 2. , 2. , 1. , 1. , 1. , 0.5, 1. ,
        1. , 1. , 0. , 0.5, 1. ],#Psychic
       [1. , 0.5, 1. , 1. , 2. , 1. , 0.5, 0.5, 1. , 0.5, 2. , 1. , 1. ,
        0.5, 1. , 2. , 0.5, 0.5],#Bug
       [1. , 2. , 1. , 1. , 1. , 2. , 0.5, 1. , 0.5, 2. , 1. , 2. , 1. ,
        1. , 1. , 1. , 0.5, 1. ],#Rock
       [0. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 2. , 1. , 1. ,
        2. , 1. , 0.5, 1. , 1. ],#Ghost
       [1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. ,
        1. , 2. , 1. , 0.5, 0. ],#Dragon
       [1. , 1. , 1. , 1. , 1. , 1. , 0.5, 1. , 1. , 1. , 2. , 1. , 1. ,
        2. , 1. , 0.5, 1. , 0.5],#Dark
       [1. , 0.5, 0.5, 0.5, 1. , 2. , 1. , 1. , 1. , 1. , 1. , 1. , 2. ,
        1. , 1. , 1. , 0.5, 2. ],#Steel
       [1. , 0.5, 1. , 1. , 1. , 1. , 2. , 0.5, 1. , 1. , 1. , 1. , 1. , #Fairy
        1. , 2. , 2. , 0.5, 1. ]], dtype=np.float32)

    #typechart[type_map['ground'],type_map['steel']]=2


    return typechart
typechart= build_typechart()