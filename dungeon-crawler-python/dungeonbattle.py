import random
from time import sleep
from sys import exit
def battle_mons(mons_health, mons_atk, better_sword, resist, heal_buff, charm_have, coins_earned):
    monster_health = mons_health
    player_health = 100
    revive = 1
    while monster_health > 0:
        print(f"\nMonster Health: {monster_health}")
        print(f"Player Health: {player_health}")
        if better_sword == 1 and heal_buff == 0:
            print("1. Slash (9-12, 1)\n2. Special Attack (17-23, 2)\n3. Heal(16-24, 1)")
        if better_sword == 0 and heal_buff == 0:
            print("1. Slash (7-10, 1)\n2. Special Attack (17-23, 2)\n3. Heal(16-24, 1)")
        if better_sword == 1 and heal_buff == 1:
            print("1. Slash (9-12, 1)\n2. Special Attack (17-23, 2)\n3. Heal(19-27, 1)")
        if better_sword == 0 and heal_buff == 1:
            print("1. Slash (7-10, 1)\n2. Special Attack (17-23, 2)\n3. Heal(19-27, 1)")
        player_atk_choice = 0
        while (player_atk_choice != 1) and (player_atk_choice != 2) and (player_atk_choice != 3):
            player_atk_choice = int(input("Choose your attack (dmg, number of attack turns monster gets) Type number of attack you want to do: "))
        if player_atk_choice == 1:
            if better_sword == 1:
                player_dmg = random.randint(9, 12)
                monster_health -= player_dmg
                sleep(1.5)
                print(f"\nYou have dealt {player_dmg} damage.")
            if better_sword == 0:
                player_dmg = random.randint(7, 10)
                monster_health -= player_dmg
                sleep(1.5)
                print(f"\nYou have dealt {player_dmg} damage.")
            mons_turns = 1
        if player_atk_choice == 2:
                player_dmg = random.randint(17, 23)
                monster_health -= player_dmg
                sleep(1.5)
                print(f"\nYou have dealt {player_dmg} damage.")
                mons_turns = 2
        if player_atk_choice == 3:
            if heal_buff == 1:
                player_heal = random.randint(19, 27)
            if heal_buff == 0:
                player_heal = random.randint(16, 24)
            if player_health + player_heal >= 100:
                print("You may not heal as you will exceed the health limit.")
                sleep(1.5)
                mons_turns = 0
            else:
                player_health += player_heal
                sleep(1.5)
                print(f"\nYou have healed {player_heal} health.")
                mons_turns = 1
        for _ in range(mons_turns):
            player_health -= (mons_atk - resist)
            sleep(1.5)
            print(f"The monster has dealt {mons_atk - resist} damage to you.")
        if player_health == 0 or player_health < 0:
            if charm_have == 1 and revive == 1:
                if random.random() < 0.25:
                    print("\nThe Charm Of The Blessed Has Saved You...")
                    player_health = 50
                    revive = 0
            else:
                print("\nI'm sorry, your journey has officialy ended...maybe?")
                sleep(2)
                print("You may be given a second chance (you will keep all items)...")
                sleep(2)
                print("Type \"quit\" if you want to end your journey.")
                print("Type \"retry\" if you would like to try and continue your journey.")
                player_retry = None
                while (player_retry != "quit") and (player_retry != "retry"):
                    player_retry = input("\nMake your choice: ").lower()
                if player_retry == "quit":
                    print("Your journey shall end here traveller...")
                    sleep(2)
                    print("Come back again if you want to challenge the dungeon once more...")
                    sleep(1)
                    exit(0)
                elif player_retry == "retry":
                    print("Well traveler...you just don't give up...")
                    sleep(2)
                    print("The dungeon shall give you another chance...")
                    sleep(2)
                    print("Don't waste it.")
                    sleep(2)
                    print("Note: You will spawn in the center room (safe room).")
                    sleep(1)
                    return -1
    print("You have defeated the monster!")
    print(f"You have earned {coins_earned} coins.")
    return coins_earned     
