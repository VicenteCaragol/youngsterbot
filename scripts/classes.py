# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:25:10 2024

@author: vicen
"""
from .database import mon_data,attack_data

class Attack():
    
    def __init__(self, name):
        """
        Initialize Attack object.
        """
        self.name = name
        self.info = attack_data[name]
        self.pp= self.info['maxPP']


class Mon():
    
    def __init__(self,species):
        """
        Initialize Mon object.
        """

        self.species= species
        self.stats = mon_data[species]
        self.attacks= [None]*4
        self._hp= self.stats['HP']
        self._fainted=False


    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = value
        # Update b based on the new value of a
        self._fainted = True if self._hp == 0 else False

    @property
    def fainted(self):
        return self._fainted

    
    def set_attack(self,name,index):
        self.attacks[index]= Attack(name)

    def copy(self):
        copymon=Mon(species=self.species)
        copymon.attacks=self.attacks
        return copymon
        
    def get_attack_info(self) -> str:
        """
        Returns a string containing the names and pp of a Mon's attacks.
        """
        info = ""
        for i, attack in enumerate(self.attacks):
            if attack is not None:
                info += f"{i}:{attack.name} (pp: {attack.pp}), "
        return info[:-2]

        
        
    