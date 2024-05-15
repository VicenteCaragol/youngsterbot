from .database import mon_data,attack_data
from .classes import Mon
from .functions import action_attack

def choose_pokemon():
    selected_pokemon = []

    pokemon_list = list(mon_data.keys())
    display=True
    first=True
    while len(selected_pokemon) < 3:
        if display:
            if first:
                print("Please select a Pokemon, or type 'exit' to finish:")
                first=False
            else:
                print("Please select another Pokemon, or type 'exit' to finish:")
            input_text = input(f"Available Pokemon: {pokemon_list}\n")
        else: 
            input_text = input()
        if input_text == 'exit':
            if len(selected_pokemon)==0:
                print("Please select at least one Pokemon.")
                display=False
                continue
            else:
                break
        if input_text in pokemon_list:
            selected_pokemon.append(Mon(species=input_text))
            pokemon_list.remove(input_text)
            display=True
            continue

        else:
            print("Invalid input. Please try again.")
            display=False

    print(f'You have chosen: {", ".join([mon.species for mon in selected_pokemon])}')
    return selected_pokemon

def game_v0(team1,team2):

    
    input_index = input(f'Player 1, select your lead ({", ".join([f"{i}: {mon.species}" for i, mon in enumerate(team1)])}): ')
    active_pokemon1=team1[int(input_index)]

    input_index = input(f'Player 1, select your lead ({", ".join([f"{i}: {mon.species}" for i, mon in enumerate(team2)])}): ')
    active_pokemon2=team2[int(input_index)]
    turn_count=0
    while True:
        turn_count+=1
        print(f'Turn {turn_count}')
        print(f'Player 1: {active_pokemon1.species} (HP:{active_pokemon1.hp})')
        print(f'Player 2: {active_pokemon2.species} (HP:{active_pokemon2.hp})')

        while True:
            action_index1 = input('Player 1, choose an option: [0: ATTACK, 1: SWITCH POKE] ')
            if int(action_index1) == 0:
                attack_index1 = input(f'Player 1, choose an attack index, or "back" to go back: ({active_pokemon1.get_attack_info()}) ')
                if attack_index1 == 'back':
                    continue
                else:
                    action_attack(active_pokemon1,active_pokemon2,int(attack_index1))
                    if active_pokemon2.hp == 0:
                        print(f'{active_pokemon2.species} faints!')
                        team2.remove(active_pokemon2)
                        if len(team2)==0:
                            print('Player 1 wins!')
                            break
                        else:
                            input_index = input(f'Player 2, select next Pokemon (your team is {", ".join([f"{i}: {mon.species}" for i, mon in enumerate(team2)])}): ')
                            active_pokemon2=team2[int(input_index)]
                            continue
                    break
            if int(action_index1) == 1:
                input_index = input(f'Player 1, select next Pokemon , or "back" to go back (your team is {", ".join([f"{i}: {mon.species}" for i, mon in enumerate(team1) if mon is not active_pokemon1])}): ')
                if input_index == 'back':
                    continue
                else:
                    active_pokemon1=team1[int(input_index)]
                break
            else:
                print("Invalid input. Please try again.")
                continue


        while True:
            action_index2 = input('Player 2, choose an option: [0: ATTACK, 1: SWITCH POKE] ')
            if int(action_index2) == 0:
                attack_index2 = input(f'Player 2, choose an attack index, or "back" to go back: ({active_pokemon2.get_attack_info()}) ')
                if attack_index2 == 'back':
                    continue
                else:
                    action_attack(active_pokemon2,active_pokemon1,int(attack_index2))
                    if active_pokemon1.hp == 0:
                        print(f'{active_pokemon1.species} faints!')
                        team1.remove(active_pokemon1)
                        if len(team1)==0:
                            print('Player 2 wins!')
                            break
                        else:
                            input_index = input(f'Player 1, select next Pokemon (your team is {", ".join([f"{i}: {mon.species}" for i, mon in enumerate(team1)])}): ')
                            active_pokemon1=team1[int(input_index)]
                            continue
                    break
            if int(action_index2) == 1:
                input_index = input(f'Player 2, select next Pokemon , or "back" to go back (your team is {", ".join([f"{i}: {mon.species}" for i, mon in enumerate(team2) if mon is not active_pokemon2])}): ')
                if input_index == 'back':
                    continue
                else:
                    active_pokemon2=team2[int(input_index)]
                break
            else:
                print("Invalid input. Please try again.")
                continue


 



        continue
    
    return