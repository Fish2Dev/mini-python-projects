import dungeonbattle as battle
from time import sleep
from sys import exit
player_coin = 0
sharp_sword = 0
resistance = 0
charm = 0
buff_heal = 0
player_reward_check = None
puzzle_solved = False
def room1():
    global player_reward_check
    global player_coin
    print("You enter the room...")
    sleep(2)
    print("The walls are gold plated with symbols & patterns...")
    sleep(3)
    print("In the center comes a hand-crafted, gold-plated structure...")
    sleep(3)
    print("But there is one problem...")
    sleep(2)
    print("This hand-crafted, gold-plated structure, with it's beaming eyes...")
    sleep(3)
    print("Sitting atop a huge pile of gold...")
    sleep(2)
    print("Is trying to kill you.")
    sleep(2)
    print(r"""
                 //||\\
              //// || \\\\
      \\     ////  ||  \\\\     //
       \\   ////   ||   \\\\   //
   <===[[[  //    ____    \\  ]]]===>
   <===[[[ //    /    \    \\ ]]]===>
   <===[[[|||   (  <O>  )   |||]]]===>
   <===[[[ \\    \____/    // ]]]===>
   <===[[[  \\            //  ]]]===>
       //   \\\\   ||   ////   \\
      //     \\\\  ||  ////     \\
              \\\\ || ////
                 \\||//
    """)
    print("The Eye Of Horizon")
    player_reward_check = battle.battle_mons(200, 24, sharp_sword, resistance, buff_heal, charm, 150)
    if player_reward_check == -1:
        return -1
    else:
        player_coin += player_reward_check
        return
def room2():
    global player_reward_check
    global player_coin
    player_fb_choice = None
    print("WARNING! This room contains the final boss.")
    while (player_fb_choice != "yes") and (player_fb_choice != "no"):
        player_fb_choice = input("If you are sure you want to proceed, type \"yes\" otherwise type \"no\" : ").lower()
    if player_fb_choice == "yes":
        print("You open the large stone door and walk down a long hallway...")
        sleep(3)
        print("The room is big with tools, armor, and materials...")
        sleep(3)
        print("You see a tunnel, your way out...")
        sleep(2.5)
        print("But there's a problem...")
        sleep(2)
        print("A giant furnace stands between you and the tunnel...")
        sleep(3)
        print("The furnace heats up and starts speaking...")
        sleep(3)
        print("\"I'm surprised...Not many have made it this far...\"")
        sleep(3)
        print("\"They all mostly died and got forged into a brand new piece of armor or tool...\"")
        sleep(3.5)
        print("\"Shall we see which one you become?\"")
        sleep(3.5)
        print(r"""
          __________

         |  🔥  🔥  |
         |___WWWW___|
        /            \
  ()===|   [ IGNIS ]  |===()
  ||   \____________/   ||
  ||      ||    ||      || 
  ||      ||    ||      ||      
 _||_    _||_  _||_    _||_

        """)
        print("Ignis The Incinerator")
        player_reward_check = battle.battle_mons(300, 32, sharp_sword, resistance, buff_heal, charm, 0)
        if player_reward_check == -1:
            return -1
        else:
            player_coin += player_reward_check
            return "WIN"
    elif player_fb_choice== "no":
        return "NO"
def room3():
    global player_coin
    global puzzle_solved
    tails_attempts = 2
    tails_room3 = {
    "1": "Tail of Regret",
    "2": "Tail of Fear",
    "3": "Tail of Hunger",
    "4": "Tail of Shame",
    "5": "Tail of Loss",
    "6": "Tail of Envy",
    "7": "Tail of Sorrow",
    "8": "Tail of Loneliness",
    "9": "Tail of Death" 
}
    if puzzle_solved == False:
        print("You enter the room...")
        sleep(2)
        print("The rooms whispers, \"The Vault Of The Nine Tail Specter\".")
        sleep(2)
        print("Then a glow appears from the corner of the room.")
        sleep(2.5)
        print("The spirit of the nine tail specter appears...")
        sleep(2.5)
        print("He moves the bricks on the floor and 9 levels appear labeled with respective numbers...")
        sleep(3)
        print("The spirit whispers...")
        sleep(2)
        print("\"Each of these levers represent the nine tails, the nine burdens I carry...\"")
        sleep(2.5)
        print("\"Find the tail of death...and I shall open the vault for you...\"")
        sleep(2.5)
        print("\"Now mortal, I'm not that forgiving, but I don't want to leave you confused...\"")
        sleep(2.5)
        print("\"I shall give you 4 clues...\"")
        sleep(2)
        print("The wind grows stronger and it whispers back...")
        sleep(2)
        print("\"The Nine Tail Specter speaks in riddles...One of these truths are a lie...\"")
        sleep(2.5)
        print("The spirit speaks back and yells \"DO NOT LISTEN TO IT...\"")
        sleep(2)
        while tails_attempts != 0:
            print("The 4 Clues:")
            print("1. The Tail Of Death's number is higher than 3.\n2. The Tail Of Death's number is odd.\n3. The Tail Of Death's number is a multiple of 3.\nThe Tail Of Death's number is NOT 9. That is the Tail Of False Hope.")
            print(f"You have {tails_attempts} attempts left.")
            player_tail_choice = input("Which tail do you pull? (1-9): ")
            if player_tail_choice == "9":
                sleep(3)
                print(f"You pull the 9th lever...The spirit reveals it is the {tails_room3["9"]}")
                sleep(3)
                print("You have exposed the Specter's lie!")
                sleep(2)
                print("The vault opens with 150 coins inside!")
                player_coin += 150
                puzzle_solved = True
                break
            elif player_tail_choice in tails_room3:
                tails_attempts -= 1
                sleep(2)
                print(f"You pull the lever labeled with the number {player_tail_choice}.")
                sleep(2.5)
                print(f"The spirit laughs and says \"You foolish mortal! You pulled the {tails_room3[player_tail_choice]}!\"")
                sleep(3)
                if tails_attempts == 0:
                    break
            else:
                sleep(2)
                print("The spirit laughs at you. \"That tail doesn't even exist!\".")
                sleep(2)
        if puzzle_solved == False:
            print("The spirit laughs and he glows and glows...")
            sleep(2.5)
            print("Suddenly, the specter appears like he has been reborn")
            sleep(2.5)
            print("\"Foolish mortal! I am reborn! Maybe defeat me again and I'll give you another chance...\"")
            sleep(3)
            print("A dark winds picks you up and takes you away to the center room (safe)")
            sleep(3)
            return "ROOM5"
        else:
            print("The spirit rises to the ceiling and starts glowing...")
            sleep(3)
            print("\"Well, mortal. You have freed me from my burdens...\"")
            sleep(3)
            print("\"In return, I shall give you this partial map.\"")
            sleep(2.5)
            print("Then, the spirit disappears and a partial map falls to the floor...")
            sleep(3.5)
            print( """
            [1] [2] [3]
            [4] [5] [-]
            [-] [-] [-]
            
            Note: If a room has a \"-\" over it, that means the map does not have information about it.
            1. Legends says The Eye Of Horizon rests here on a pile of gold...
            2. The Incinerator waits here for it's next victim... (final boss)
            3. You are resting here now...
            4. The wizard rests here with magic to trade...
            5. The center room which connects to all pathways... (safe room)
            """)
            input("Press enter once you have noted down the map, It will not show up again...")
            print("The map glows and fades away...")
            sleep(2)
            print("The winds picks you up and carries you to the center room...")
            sleep(3)
            return "ROOM5"
    if puzzle_solved == True:
        print("You enter the room...")
        sleep(2)
        print("The vault is cold and empty...")
        sleep(2)
        print("The spirit no where to be found...")
        sleep(2)
        print("The winds picks you up and carries you to the center room...")
        sleep(3)
        return "ROOM5"
def room4():
    global player_coin
    global sharp_sword
    global resistance
    global charm
    global buff_heal
    print()
    print(r"""
         /\
        /  \
       /____\
      (  o o )    /
     --[  $ ]-- <  *You've got coins? I've got magic.*
      /|    |\   \
     / |____| \
    /__________\
    """)
    while True:
        print("Items:")
        print("1. Sharpened Sword - 120 Coins (Slash Attack Deals More Damage)")
        print("2. Ruined Armor - 80 Coins (Gives 3 Resistance)")
        print("3. Steel Plated Armor - 150 Coins (Gives 5 Resistance)")
        print("4. Gold Plated Armor - 250 Coins (Gives 9 Resistance)")
        print("5. Charm Of The Blessed - 400 Coins (Has A 25% Chance to Revive You Once Per Battle At 50% Health)")
        print("6. Magma Forged Armor - 400 Coins (Gives 12 Resistance)")
        print("7. The Charm Of Vitality - 150 Coins (Buffed Healing)")
        print(f"You have {player_coin} coins.")
        player_item_choice = None
        player_item_choice = int(input("Type the number of the item you want (type \"0\" to exit the wizard's shop): "))
        if player_item_choice == 0:
            print("Safe travels wanderer!")
            break
        if player_item_choice == 1:
            if player_coin < 120:
                print("I'm sorry traveler, I can't give magic for free...")
                sleep(2)
                print(f"You need {120 - player_coin} more coins to buy this item.")
            elif player_coin >= 120:
                player_coin -= 120
                sharp_sword = 1
                print("Right away traveller!")
                sleep(2)
                print("The wizard takes your sword and puts it in his forge...")
                sleep(2)
                print("He cools it down and it looks brand new.")
                sleep(2)
                print("Your Slash attack has been upgraded.")
        if player_item_choice == 2:
            if player_coin < 80:
                print("No coins? No armor traveler!")
                sleep(2)
                print(f"You need {80 - player_coin} more coins to buy this item.")
            elif player_coin >= 80:
                player_coin -= 80
                resistance = 3
                print("Right away traveller!")
                sleep(2)
                print("The wizard looks around in his chest and finds something...")
                sleep(2)
                print("The armor is made of wood that is dark, old, and wrapped with vines.")
                sleep(2)
                print("You have gained more resistance.")
        if player_item_choice == 3:
            if player_coin < 150:
                print("Steel Plated Armor costs a lot of coins that you don't have, come back when you have them traveler.")
                sleep(2)
                print(f"You need {150 - player_coin} more coins to buy this item.")
            elif player_coin >= 150:
                player_coin -= 150
                resistance = 5
                print("Right away traveller!")
                sleep(2)
                print("The wizard looks around in his chest and finds something...")
                sleep(2)
                print("The armor is made of steel and has gray patterns etched into it...")
                sleep(2)
                print("You have gained more resistance.")
        if player_item_choice == 4:
            if player_coin < 250:
                print("You think you can get Gold Plated Armor for this low price? Go find some coins traveler!")
                sleep(2)
                print(f"You need {250 - player_coin} more coins to buy this item.")
            elif player_coin >= 250:
                player_coin -= 250
                resistance = 9
                print("Right away traveller!")
                sleep(2)
                print("The wizard looks around in his chest and finds something...")
                sleep(2)
                print("The armor is made of gold with small diamond patterns etched into it...")
                sleep(2)
                print("You have gained more resistance.")
        if player_item_choice == 5:
            if player_coin < 400:
                print("I'm giving you a deal at 400! If you don't have the coin, go find that Eye in the North; I hear it's sitting on a pile of gold.")
                sleep(2)
                print(f"You need {400 - player_coin} more coins to buy this item.")
            elif player_coin >= 400:
                player_coin -= 400
                charm = 1
                print("Right away traveller!")
                sleep(2)
                print("The wizard presses a brick in the left wall...")
                sleep(2)
                print("It opens to a steel podium holding one thing...")
                sleep(2)
                print("The Charm Of The Blessed...")
                sleep(2)
                print("The wizard hands it to you and says...")
                sleep(2)
                print("Be careful traveller, Ignis would not like to see this charm in your hands...")
                sleep(2)
                print("The Charm Of The Blessed glows in your hands...")
                sleep(2)
                print(r"You now have a 25% chance to revive once per battle at 50% health.")
        if player_item_choice == 6:
            if player_coin < 400:
                print("This armor was forged by the hands of Ignis before he became what he is today...")
                sleep(3)
                print("There is no way in this dungeon I would sell you his armor at that price! Get more coins!")
                sleep(3.5)
                print(f"You need {400 - player_coin} more coins to buy this item.")
            elif player_coin >= 400:
                player_coin -= 400
                resistance = 12
                print("Right away traveller!")
                sleep(2)
                print("The wizard walks to the back of the forge and pulls out an old steel box...")
                sleep(3)
                print("He pulls out the armor forged from Ignis himself...")
                sleep(2.5)
                print("The armor is made of obsidian with cracks of patterns filled with magma...")
                sleep(3)
                print("The wizard says, \"Be careful traveller, Ignis would not like to see you with his armor on...\"")
                sleep(3.5)
                print("You have gained more resistance.")
        if player_item_choice == 7:
            if player_coin < 150:
                print("I'm giving you a deal at 150! If you don't have the coin, I heard the Nine Tail Spector is guarding a vault full of precious coins!")
                sleep(2)
                print(f"You need {150 - player_coin} more coins to buy this item.")
            elif player_coin >= 150:
                player_coin -= 150
                buff_heal = 1
                print("Right away traveller!")
                sleep(2)
                print("The wizard presses a brick in the right wall...")
                sleep(2)
                print("It opens to a steel podium holding one thing...")
                sleep(2)
                print("The Charm Of Healing...")
                sleep(2)
                print("The wizard hands it to you and says...")
                sleep(2)
                print("Be careful traveller, Ignis would not like to see this charm in your hands...")
                sleep(2)
                print("The Charm Of Healing glows in your hands...")
                sleep(2)
                print(r"You now can heal for more health in battle...")
def room5():
    print("You enter the room...")
    sleep(2)
    print("There is a sign on the wall...")
    sleep(2)
    print("It says \"SAFE\"")
    sleep(2)
    print("Phew!")
    sleep(2)
    print("You see one more sign, and it says...")
    sleep(3)
    print("North leads to Flame, East leads to Ghosts, West leads to Trade.")
    sleep(3)
    print("You wonder what it means...")
def room6():
    global player_reward_check
    global player_coin
    print("You enter the room...")
    sleep(2)
    print("The walls are full of illusions and spirals...")
    sleep(2.5)
    print("In the center you see an altar...")
    sleep(2.5)
    print("With nine tails coming out of it...")
    sleep(2.5)
    print("Then a figure rises from the shadows...")
    sleep(2.5)
    print("It says...")
    sleep(2.5)
    print("\"One tail to trip you, three to bind you, and the ninth to brush the memory of your life away like dust on a grave. Shall we begin the count?\"")
    sleep(4)
    print(r"""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠖⣡⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⢼⣿⢃⣾⣿⠁⢀⡴⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣧⣄⣠⣤⣾⠟⠋⠉⠉⠛⢷⣌⠃⢸⣿⣇⠀⣾⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠛⠿⣯⣭⣤⣤⣴⣦⣄⡀⠀⢹⡆⠸⣿⣿⠀⢹⡿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣄⣀⠉⠙⢿⣄⢨⣿⠀⣿⣿⡇⢸⡇⢻⣷⠀⠀⠀⣴⠀⠀
⠀⢀⠀⠐⠒⠚⢛⣛⣻⣿⣷⣦⠈⣿⣾⠇⢠⣿⡿⠀⣼⠇⢀⣿⠀⠀⣸⣷⠀⠀
⠀⠈⢷⣦⣴⣾⣿⣿⠿⠛⠛⣿⢠⣿⠏⠐⠛⣉⣠⡾⠋⠀⣼⠏⠀⣰⣿⣿⡄⠀
⠀⠀⠀⠉⠉⠉⠉⠀⠀⢀⡠⢃⠾⠛⠛⠿⢿⣿⣭⣤⣴⠟⠃⣠⣼⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⢰⠀⠚⠛⠓⠲⣶⣶⣶⣶⠿⢿⣛⣛⡁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠈⢷⣄⣀⣠⣖⠈⠻⣿⣿⣷⡈⢿⣿⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⡀⢠⣇⠀⢈⡿⣿⣿⡷⠀⠘⣿⣿⣷⠈⢿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡷⢸⡿⣿⡿⠃⠸⣇⠀⠀⠀⢸⣿⡿⠀⠀⠉⠛⠿⠋
⠀⠀⠀⠀⠀⠀⡠⠾⣿⣿⠣⣾⠀⠀⠀⠀⢰⡿⠀⠀⠀⢸⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣤⣄⢸⣦⠘⢸⢣⡀⠈⠻⣦⣄⠀⠈⠁⠀⠀⠀⠊⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⠣⠏⠙⣷⡈⢼⣷⣄⠀⠙⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡏⠀⠀⣿⠇⡼⠋⠻⠆⠀⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⢳⡄⢈⡟⣠⡶⠆⠀⡆⠀⠇⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣯⣴⠏⣼⠋⠀⠀⢸⡇⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠛⠛⢁⣼⠇⠀⠀⠀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣼⡶⠟⠉⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣤⣶⡿⠋⠀⠀⠀⠀⠀⠲⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    print("The Nine Tail Specter")
    player_reward_check = battle.battle_mons(140, 17, sharp_sword, resistance, buff_heal, charm, 80)
    if player_reward_check == -1:
        return -1
    else:
        player_coin += player_reward_check
        return
def room7():
    global player_reward_check
    global player_coin
    print("You enter the room....")
    sleep(2.5)
    print("It's dark...and chilly?")
    sleep(2.5)
    print("You walk forward...You see snow and ice?")
    sleep(2.5)
    print("Then you see a monsterous ice sculpture....Spikes coming out everywhere...Eyes staring at you...")
    sleep(2.5)
    print("Luckily it's just a sculpture...right?")
    sleep(2.5)
    print("You keep walking forward as you hear a noise....")
    sleep(2.5)
    print("Then suddenly...the sculpture is gone...")
    sleep(2.5)
    print("And you realize....")
    sleep(2.5)
    print("The scuplture is right behind you...staring at you with it's chilly eyes....with breath so cold and deadly...")
    sleep(2.5)
    print(r"""
              / \
             /   \
            /^v^v^\
           /  \ /  \
       _  /  X   X  \  _
      \ \/     W     \/ /
       \ \   vvvvvv  / /
     _  \ \  \____/  / /  _
    / \  \ \________/ /  / \
   /   \  \/        \/  /   \
   \ v /  /|   /\   |\  \ v /
    \ /  / |  /  \  | \  \ /
     v  /  | /    \ |  \  v
       /  /|/      \| \  \
      /_/  V        V  \__\
    """)
    print("Mr. Icicle")
    player_reward_check = battle.battle_mons(110, 13, sharp_sword, resistance, buff_heal, charm, 50)
    if player_reward_check == -1:
        return -1
    else:
        player_coin += player_reward_check
        return
def room8():
    print("You see the broken lock on the gate. You've already commited...No going back now.")
def room9():
    global player_reward_check
    global player_coin
    print("You enter the dark room...")
    sleep(2.5)
    print("You find a torch laying on the ground. That'll be useful...")
    sleep(2.5)
    print("You walk forward...It's filled with cobwebs, dust, and...sand?")
    sleep(2.75)
    print("You see it...The walls are made of paintings from thousands of years ago...")
    sleep(2.75)
    print("In the center of it all...is an egyptian coffin...")
    sleep(2.5)
    print("You dust off the coffin...There's a lock on it...Phew...")
    sleep(2.5)
    print("CRASH...You turn to see one of the egyptian artifacts...perfectily still on it's podium...fall to the floor and shatter into pieces...")
    sleep(4.5)
    print("You turn back...and your eyes scream in horror")
    sleep(2.5)
    print("The lock is broken..the coffin in open..and what stands in front of you...")
    sleep(2.5)
    print("Is a 5000 year old mummy")
    sleep(2.5)
    print(r"""
            _________
         .-"         "-.
        /   /////////   \
       |   |  x   x  |   |
       |   |    ^    |   |
       |   |  _____  |   |
       |   | |     | |   |
       |   | |_____| |   |
       |    \_______/    |
        \      ---      /
         "-._________.-"
              ||||
          ////||||\\\\
         //// |||| \\\\
        ||||  ||||  ||||
        ||||  ||||  ||||
        ||||  ||||  ||||
        ||||  ||||  ||||
        ||||  ||||  ||||
        ||||  ||||  ||||
        ||||  ||||  ||||
        ||||  ||||  ||||
          \\  ||||  //
           \\ |||| //
            \\||||//
             \\||//
              ||||
             / || \
            /  ||  \
           /   ||   \
          /    ||    \
         /     ||     \
        /_____/  \_____\
    """)
    print("Desiccated Mummy")
    player_reward_check = battle.battle_mons(70, 9, sharp_sword, resistance, buff_heal, charm, 20)
    if player_reward_check == -1:
        return -1
    else:
        player_coin += player_reward_check
        return
