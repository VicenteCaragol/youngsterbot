
from typing import Optional
import numpy as np
from gymnasium import Env
from gymnasium.core import ActType, ObsType
from gymnasium import spaces
import random

from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from scripts.database import type_map,typechart,type_map_inverted
from scripts.classes import Mon


class BasicPokeEnv(Env):

    def __init__(self):

        # Observations are dictionaries with the agent's and the target's location.
        # opponent-type,opponent-hp, own-hp
        self.observation_space = spaces.Dict(
            {
                "Opponent Active": spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),

                "Own Active": spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),
                
                "Opponent Team-0":spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),
                "Opponent Team-1":spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),   #Mon 2 Attributes
                "Opponent Team-2":spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),  #Mon 3 Attributes

                "Own Team-0":spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),
                "Own Team-1":spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),   #Mon 2 Attributes
                "Own Team-2":spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int)  #Mon 3 Attributes
            }
        )

        # We have 3 types to choose
        self.action_space = spaces.Discrete(4)


# Function to get the multiplier
    ''''
    def get_multiplier(self, a, b):
        multipliers = [
        [1, 2, 0.5],  # Grass against Grass, Water, Fire
        [0.5, 1, 2],  # Water against Grass, Water, Fire
        [2, 0.5, 1]   # Fire against Grass, Water, Fire
        ]
        return multipliers[int(a)][int(b)]
    '''''
    

    def _get_obs(self):
        opponent0=self.opponent_team[0]
        opponent1=self.opponent_team[1]
        opponent2=self.opponent_team[2]

        own0=self.own_team[0]
        own1=self.own_team[1]
        own2=self.own_team[2]


        state_dict={
                "Opponent Active": np.array([type_map[self.active_opponent.stats['type']], self.active_opponent.hp], dtype=int),
                #spaces.Box(low=np.array([0, 0]), high=np.array([18, 1000]), dtype=int),

                "Own Active": np.array([type_map[self.active_pokemon.stats['type']], self.active_pokemon.hp], dtype=int),
                
                "Opponent Team-0": np.array([type_map[opponent0.stats['type']], opponent0.hp], dtype=int),
                "Opponent Team-1": np.array([type_map[opponent1.stats['type']], opponent1.hp], dtype=int),
                "Opponent Team-2": np.array([type_map[opponent2.stats['type']], opponent2.hp], dtype=int),  

                "Own Team-0": np.array([type_map[own0.stats['type']], own0.hp], dtype=int),
                "Own Team-1": np.array([type_map[own1.stats['type']], own1.hp], dtype=int),   #Mon 2 Attributes
                "Own Team-2": np.array([type_map[own2.stats['type']], own2.hp], dtype=int)  #Mon 3 Attributes
        }

        return state_dict
    def _get_info(self):
        return {"opponent-hp": self.active_opponent.hp, "own-hp": self.active_pokemon.hp}
    
    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)
        bulbasaur=Mon(species='Bulbasaur')
        squirtle=Mon(species='Squirtle')
        charmander=Mon(species='Charmander')
        placeholder_team=[squirtle,bulbasaur,charmander]
        placeholder_team2=[squirtle.copy(),bulbasaur.copy(),charmander.copy()]
        self.opponent_team= placeholder_team
        self.own_team= placeholder_team2

        opponent_lead=np.random.randint(0,len(self.opponent_team))
        own_lead=np.random.randint(0,len(self.opponent_team))

        self.active_pokemon=self.own_team[own_lead]
        self.active_pokemon_index=  own_lead
        self.active_opponent=self.opponent_team[opponent_lead]
        self.active_opponent_index=  opponent_lead

        self.available_opponents = list(range(len(self.opponent_team)))
        self.available_own = list(range(len(self.own_team)))

        self.must_choose_next=False
        

        observation = self._get_obs()
        info = self._get_info()


        return observation, info
    
    def step(self, action):

        reward=0
        terminated=False

        #chose next
        if self.must_choose_next:
            if action.item()-1 in self.available_own:
                self.active_pokemon_index=action.item()-1
                self.active_pokemon=self.own_team[self.active_pokemon_index]
                self.must_choose_next=False
                observation = self._get_obs()
                info = self._get_info()
                return observation, reward, terminated, False, info
            else:
                observation = self._get_obs()
                info = self._get_info()
                return observation, reward, terminated, False, info



        #chose to attack
        if action.item()==0:
            att=int(type_map[self.active_pokemon.stats["type"]])
            defend=int(type_map[self.active_opponent.stats["type"]])
        
            damage= int(10*typechart[att,defend])
            damage_to_player = int(10*typechart[defend,att])
            #ded enemy
            if self.active_opponent.hp<damage:
                self.active_opponent.hp=0
                self.available_opponents.remove(self.active_opponent_index)
                #victory
                if len(self.available_opponents)==0:
                    reward=3
                    terminated=True
                #opponent choose next
                else:
                    self.active_opponent_index=random.choice(self.available_opponents)
                    self.active_opponent=self.opponent_team[self.active_opponent_index]
                    reward=1
            #enemy takes damage
            else:
                self.active_opponent.hp-=damage
                self.active_pokemon.hp-=damage_to_player
                if self.active_pokemon.hp<=0:
                    self.available_own.remove(self.active_pokemon_index)
                    #loss
                    if len(self.available_own)==0:
                        terminated=True
                    #choose next
                    else:
                        self.must_choose_next=True
        #choose to switch
        else:
            if action.item()-1 in self.available_own:
                if action.item()-1 == self.active_pokemon_index:
                    pass
                else:
                    self.active_pokemon_index=action.item()-1
                    self.active_pokemon=self.own_team[self.active_pokemon_index]

                    att=int(type_map[self.active_pokemon.stats["type"]])
                    defend=int(type_map[self.active_opponent.stats["type"]])
                    damage_to_player = int(10*typechart[defend,att])
                    self.active_pokemon.hp-=damage_to_player
                    if self.active_pokemon.hp<=0:
                        self.active_pokemon.hp=0
                        self.available_own.remove(self.active_pokemon_index)
                        #loss
                        if len(self.available_own)==0:
                            terminated=True
                        #choose next
                        else:
                            self.must_choose_next=True


            else:
                pass



                

            
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, terminated, False, info
    
    def  render(self):
        if self.must_choose_next:
            print('Waiting For Player to choose Next Pokemon')
        if len(self.available_opponents)==0:
            print('Easy Moneeeey')
        elif len(self.available_own)==0:
            print('Soy Remanco')
        else:
            print('New turn')
            print(f'Opponent HP: {self.active_opponent.hp}, Oponnent type: {self.active_opponent.stats["type"]}')
            print(f'My HP: {self.active_pokemon.hp}, My type: {self.active_pokemon.stats["type"]}')
              #, My last attack: {map[int(self._lastmove)]}')
        return

env = BasicPokeEnv()
check_env(env)  # does not output any warnings

model = PPO("MultiInputPolicy", env, verbose=1)
model.learn(total_timesteps=100000)

episodes = 2

for ep in range(episodes):
    print('----------------')
    print(f'Game {ep+1}')
    vec_env = model.get_env()
    obs = vec_env.reset()
    done = False
    while not done:
        # pass observation to model to get predicted action
        action, _ = model.predict(obs)
        
        if action.item()==0:
            if env.must_choose_next:
                pass
            else:
                env.render()
                print('I attack')
        elif action.item()-1 in env.available_own:
            if action.item()-1 == env.active_pokemon_index:
                pass
            else:
                env.render()
                print(f'I switch to {env.own_team[action.item()-1].species}') 
        else:
            pass
            #print('I attempt to switch to a dead pokemon')

        # pass action to env and get info back
        obs, rewards, done ,_, info = env.step(action)


        # show the environment on the screen
    env.render()
        
pass