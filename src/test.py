import random
from colorama import Fore, Back, Style
import os
from trap import Trap
from rooms import Rooms
rooms = Rooms.rooms
reset = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

header = f"""{red}

                                                    ██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗
                                                    ██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║
                                                    ██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║
                                                    ██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║
                                                    ██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║
                                                    ╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝
{reset}"""


# Define the player's starting stats
os.system('clear')
print(header)
player_name = input(f"                                                                           {green}Enter your name:{Fore.CYAN}")

player_health = 10000
player_damage = 10
player_gold = 1000
player_weapon = "Dagger"
player_anger = 195
player_xp = 0
player_defense = 0
os.system('clear')

# Define the available weapons and their prices
weapons = {
    "Dagger": 0,
    "Sword": 50,
    "Axe": 100,
    "Bow": 150
}

potions = {
    "Potion": 10,
}

perks = {
    "Defense1" : 50,
    "Defense2" : 150,
    "Defense3" : 250
}

defense = {
    "Defense1" : 10,
    "Defense2" : 15,
    "Defense3" : 20
}

damage = {
    "Dagger:": 10,
    "Sword": 15,
    "Axe" : 20,
    "Bow": 25
}

# Define the monsters and their stats
monsters = {
    "Goblin": {"health": 20, "damage": 5, "gold": 10},
    "Troll": {"health": 50, "damage": 10, "gold": 25},
    "Dragon": {"health": 100, "damage": 20, "gold": 50}
}

# Define the boss and its stats
boss = {
    "name": "The Dark Lord",
    "health": 200,
    "damage": 30,
    "gold": 1003
}

# Define the game loop
while True:
    print(header)
    # Display the player's stats
    print(f"{reset}Char: {green}{player_name}{reset}")
    print(f"Health: {green}{player_health}{reset}")
    print(f"Knowledge: {green}{player_xp}{reset}")
    print(f"Damage: {red}{player_damage}{reset}")
    print(f"Gold: {yellow}{player_gold}{reset}")
    print(f"Weapon: {blue}{player_weapon}{reset}")
    print(f"Defense: {blue}{player_defense}{reset}")
    print(f"Boss Anger: {red}{player_anger}{reset}")

    # Ask the player what they want to do
    print("\nWhat would you like to do?")
    print(f"1. {blue}Explore{reset}")
    print(f"2. {yellow}Shop{reset}")
    print(f"3. {red}Quit{reset}")
    choice = input("> ")
    os.system('clear')
#
    if choice == "1":
        if player_anger <= 199:
            print(header)
            curr_room = random.choice(list(rooms))
            # Generate a random monster
            monster_name = random.choice(list(monsters.keys()))
            monster_health = monsters[monster_name]["health"]
            monster_damage = monsters[monster_name]["damage"]
            monster_gold = monsters[monster_name]["gold"]

            traps = Trap.traps
            trap_name = random.choice(list(traps.keys()))
            trap_dmg = traps[trap_name]["damage"]
            print(f"\nYou have entered {red}{curr_room}{reset}")
            print("\nDo you want to:")
            print(f"\n1. {blue}look around{reset}")
            print('\nOr')
            print(f"\n2. {blue}go back!{reset}")
            choice = input('> ')
            if choice == "1":
                os.system('clear')
                print(f"\nYou encounter a {red}{monster_name}{reset}!")
                if random.random() < 0.2:
                    print(f'You walked into a trap type: {red}{trap_name}{reset} and your health went down by {red}{trap_dmg}{reset}')
                    player_health -= trap_dmg

                # Fight the monster
                while monster_health > 0 and player_health > 0:
                    print(header)
                    print(f"\n: {red}{monster_name}{reset}")
                    print(f"Health: {green}{monster_health}{reset}")
                    print(f"Damage: {red}{monster_damage}{reset}")
                    print(f"\n: {green}{player_name}{reset}")
                    print(f"Health: {green}{player_health}{reset}")
                    print(f"Damage: {red}{player_damage}{reset}")

                    print("\nWhat would you like to do?")
                    print(f"1. {red}Attack{reset}")
                    print(f"2. {blue}Run{reset}")
                    choice = input("> ")

                    if choice == "1":
                        # Player attacks
                        monster_health -= player_damage
                        os.system('clear')
                        print(f"You hit the {monster_name} for {player_damage} damage!")
                        
                        # Monster attacks
                        if monster_health > 0:
                            player_health -= monster_damage - player_defense 
                            os.system('clear')
                            print(f"The {red}{monster_name}{reset} hits you for {red}{monster_damage}{reset} damage!")
                            print(f'Your {blue}armour{reset} absorbed {blue}{player_defense}{reset} of the {red}damage{reset}')
                    elif choice == "2":
                        # Player runs away
                        os.system('clear')
                        print(f"You run away from the {red}{monster_name}{reset}!")
                        break
            elif choice == 2:
                break
            # Boss Fight
        elif player_anger == 200:
            monster_name = boss["name"]
            monster_health = boss["health"]
            monster_damage = boss["damage"]
            monster_gold = boss["gold"]

            print(f"{red}OH! NO! The Dark Lord is Hangry and Seeking Revenge{reset}")
            print("""
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠘⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⠏⣠⡂⠙⣿⣷⠘⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⡼⠃⢨⠟⠁⠀⠈⠻⢧⡈⠻⣆⠻⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⣷⣶⣤⣤⣄⠀⠀⠀⣤⣿⣷⣿⣯⡁⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⢿⣿⣧⣀⣐⡿⠟⠻⠟⠛⠙⣦⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⡄⠀⠉⠁⠀⠀⣹⠀⢸⡀⠀⠀⠀⠀⠀⡼⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠱⣄⡀⠀⢀⣴⠃⠀⠀⠳⣄⡀⠀⣀⠴⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠉⠉⠁⠸⣀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢀⡀⠀⠉⠃⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢰⡀⠀⠀⠉⠉⠭⠭⠉⠉⠀⠀⣠⣾⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⢿⣶⣄⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠿⢿⣷⣶⣶⡶⠟⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣀⣼⣿⣶⣶⣦⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⣠⣾⢻⣿⣿⣿⡿⠟⠛⠋⠉⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠼⠛⠁⢸⣿⣿⣿⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⣸⣿⣿⣿⣧⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⡆⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿1
            """)

            # Fight the monster
            while monster_health > 0 and player_health > 0:
                print(f"\n: {red}{monster_name}{reset}")
                print(f"Health: {green}{monster_health}{reset}")
                print(f"Damage: {red}{monster_damage}{reset}")
                print(f"\n: {green}{player_name}{reset}")
                print(f"Health: {green}{player_health}{reset}")
                print(f"Damage: {red}{player_damage}{reset}")

                if monster_health >=200:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 175:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{red}⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 150:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{red}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 125:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿{red}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 100:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿{red}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 75:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{red}⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 50:
                    print(f"                            [{green}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{red}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 25:
                    print(f"                            [{green}⣿⣿⣿{red}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                elif monster_health >= 5:
                    print(f"                            [{green}⣿{red}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}]")
                print("""
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠘⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⠏⣠⡂⠙⣿⣷⠘⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⡼⠃⢨⠟⠁⠀⠈⠻⢧⡈⠻⣆⠻⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⣷⣶⣤⣤⣄⠀⠀⠀⣤⣿⣷⣿⣯⡁⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⢿⣿⣧⣀⣐⡿⠟⠻⠟⠛⠙⣦⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⡄⠀⠉⠁⠀⠀⣹⠀⢸⡀⠀⠀⠀⠀⠀⡼⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠱⣄⡀⠀⢀⣴⠃⠀⠀⠳⣄⡀⠀⣀⠴⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠉⠉⠁⠸⣀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢀⡀⠀⠉⠃⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢰⡀⠀⠀⠉⠉⠭⠭⠉⠉⠀⠀⣠⣾⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⢿⣶⣄⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠿⢿⣷⣶⣶⡶⠟⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣀⣼⣿⣶⣶⣦⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⣠⣾⢻⣿⣿⣿⡿⠟⠛⠋⠉⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠼⠛⠁⢸⣿⣿⣿⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⣸⣿⣿⣿⣧⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⡆⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿1
            """)

                print("\nWhat would you like to do?")
                print(f"1. {red}Attack{reset}")
                print(f"2. {blue}Run{reset}")
                choice = input("> ")

                if choice == "1":
                    # Player attacks
                    monster_health -= player_damage
                    print(f"You hit the {red}{monster_name}{reset} for {red}{player_damage}{red} damage!")
                    
                    # Monster attacks
                    if monster_health > 0:
                        player_health -= monster_damage - player_defense
                        os.system('clear')
                        print(f"The {red}{monster_name}{reset} hits you for {red}{monster_damage}{reset} damage!")
                        print(f'Your {blue}armour{reset} absorbed {blue}{player_defense}{reset} of the {red}damage{reset}')
                elif choice == "2":
                    # Player runs away
                    os.system('clear')
                    print(f"You run away from the {red}{monster_name}{reset}!")
                    break
        # Check if the player won the fight
        if player_health > 0:
            if monster_health <= 0:
                print("\nYou defeated the {0}!".format(monster_name))
                print(f"{red}Dark Lord is getting Hangry!{reset}")
                print(f"You found {yellow}{monster_gold}{reset} gold!")
                player_gold += monster_gold
                player_anger += 5
                xp = random.randint(1, 10)
                player_xp += xp
                print(f"You Gained {green}{xp}{reset} Knowledge!") 
                if random.random() < 0.2:
                    # Player finds a random weapon
                    new_weapon = random.choice(list(weapons.keys()))
                    wp_dmg = damage[new_weapon]
                    if weapons[new_weapon] > weapons[player_weapon]:
                        player_damage = wp_dmg
                        player_weapon = new_weapon
                        print(f"{green}You found a New Weapon{reset}")
                    else:
                        print(f"{Fore.YELLOW}You found a Weapon, but it's worse than your current weapon.{reset}")
        else:
            print("\nYou were defeated by the {0}...".format(monster_name))
            break

    elif choice == "2":
        print(header)
        # Display the available weapons and their prices
        print("\nAvailable Weapons:")
        for weapon, price in weapons.items():
            print(f"{blue}{weapon}{reset}: {yellow}{price}{reset}")
        
        print("\nAvaliable Potions")
        for potion, price in potions.items():
            print(f"{blue}{potion}{reset}: {yellow}{price}{reset}")

        print("\nAvaliable Perks")
        for perk, price in perks.items():
            print(f"{blue}{perk}{reset}: {yellow}{price}{reset} XP")

        # Ask the player what they want to buy
        print("\nWhat would you like to buy?")
        choice = input("> ")

        if choice in weapons.keys():
            price = weapons[choice]
            if player_gold >= price:
                if choice in damage.keys():
                    dmg = damage[choice]
                    player_damage = dmg
                # Player buys the weapon
                player_gold -= price
                player_weapon = choice
                os.system('clear')
                print(f"You bought a {blue}{choice}{reset}!")
            else:
                os.system('clear')
                print(f"You don't have enough gold to buy a {blue}{choice}{reset}!")
        elif choice in potions.keys():
            price = potions[choice]
            if player_gold >= price:
                player_gold -= price
                player_health += 15
                os.system('clear')
                print(f"You bought a {blue}{choice}{reset}!")
        elif choice in perks.keys():
            price = perks[choice]
            if player_xp >= price:
                player_xp -= price
                if choice in defense.keys():
                    player_defense = defense[choice]
                os.system('clear')
                print(f"You bought a {blue}{choice}{reset}!")  
        else:
            os.system('clear')
            print("Invalid choice.")

    elif choice == "3":

        # End the game
        os.system('clear')
        print(header)
        print(f"{Fore.MAGENTA}Thanks for playing!{reset}")
        break

    else:
        print("Invalid choice.")
