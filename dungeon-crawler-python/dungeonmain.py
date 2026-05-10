from time import sleep
import dungeonrooms as dr
# this is the map with position numbers
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]
game_running = True
player_retry_check = None
fb_progress = ""
print("Welcome to the Dungeon!")
sleep(1.5)
current_pos = 2
while game_running == True:
    if current_pos == 1:
        dr.room1()
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [.] [] []
        [] [] []
        [] [] []
        The dot represents where you are on the map right now!

    """)
        while (path_choice != "right") and (path_choice != "back"):
            path_choice = input("Which path shall you take? Right or Back? : ").lower()
            if path_choice == "back":
                current_pos = 2
            elif path_choice == "right":
                current_pos = 4
    elif current_pos == 2:
        fb_progress = dr.room2()
        if fb_progress == "NO":
            current_pos = 5
        if fb_progress == "WIN":
            print("Ignis falls to the ground...")
            sleep(3)
            print("Cracks upon cracks appear on the furnace...")
            sleep(3.5)
            print("Ignis screams in agony as he crumbles into a pile of pebbles...")
            sleep(3.5)
            print("\"You did it...\"The wizard says from behind you...")
            sleep(3.5)
            print("\"Now we are finally free...\"")
            sleep(3)
            print("You dig through what remains of Ignis...")
            sleep(3)
            print("And you find it...You found what you were looking for...")
            sleep(4)
            print("The Solar Ember")
            sleep(2)
            print("The wizard looks at the artifact and says, \"So that's why you came here...\"")
            sleep(4)
            print("And for the first time in months...You speak")
            sleep(3)
            print("\"Our world has been in a great freeze for centuries...The sun never rises...\"")
            sleep(4)
            print("\"Legend said this artifact could warm up our planet...With this, now we don't have to live in fear\"")
            sleep(4.5)
            print("Before you walk to the tunnel...Th wizard says one more thing...")
            sleep(3.5)
            print("\"You know... when you first walked in here with that Ruined Armor, I didn't think you'd make it past the Mummy. But you've got more fire in you than Ignis ever did. Go on now. The world has been waiting for that light.\"")
            sleep(10)
            print("You smile and walk through the tunnel...")
            sleep(3)
            print("You hold The Solar Ember up to the ceiling...")
            sleep(3)
            print("And for the first time in centuries...")
            sleep(3)
            print("You see a light at the end of the tunnel...")
            sleep(3)
            print("\n" + "="*40)
            print("THE END")
            print("="*40)
            print("Thank you for playing!")
            print("Press ENTER to exit the dungeon...")
            input()
            exit()
    elif current_pos == 3:
        dr.room3()
        current_pos = 5
    elif current_pos == 4:
        dr.room4()
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [] [] []
        [.] [] []
        [] [] []
        The dot represents where you are on the map right now!

    """)
        while (path_choice != "right") and (path_choice != "forward") and (path_choice != "back"):
            path_choice = input("Which path shall you take? Right, Forward? or Back? : ").lower()
            if path_choice == "back":
                current_pos = 7
            elif path_choice == "forward":
                current_pos = 1
            elif path_choice == "right":
                current_pos = 5
    elif current_pos == 5:
        dr.room5()
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [] [] []
        [] [.] []
        [] [] []
        The dot represents where you are on the map right now!

    """)
        while (path_choice != "right") and (path_choice != "forward") and (path_choice != "back") and (path_choice != "left"):
            path_choice = input("Which path shall you take? Right, Left, Forward? or Back? : ").lower()
            if path_choice == "back":
                current_pos = 8
            elif path_choice == "forward":
                current_pos = 2
            elif path_choice == "right":
                current_pos = 6
            elif path_choice == "left":
                current_pos = 4
    elif current_pos == 6:
        dr.room6()
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [] [] []
        [] [] [.]
        [] [] []
        The dot represents where you are on the map right now!

    """)
        while (path_choice != "forward") and (path_choice != "back") and (path_choice != "left"):
            path_choice = input("Which path shall you take? Left, Forward? or Back? : ").lower()
            if path_choice == "back":
                current_pos = 9
            elif path_choice == "forward":
                current_pos = 3
            elif path_choice == "left":
                current_pos = 5
    elif current_pos == 7:
        player_retry_check = dr.room7()
        if player_retry_check == -1:
            current_pos = 5
            continue
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [] [] []
        [] [] []
        [.] [] []
        The dot represents where you are on the map right now!

    """)
        while (path_choice != "right") and (path_choice != "forward"):
            path_choice = input("Which path shall you take? Right or Forward? : ").lower()
            if path_choice == "right":
                current_pos = 8
            elif path_choice == "forward":
                current_pos = 4
    elif current_pos == 8:
        dr.room8()
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [] [] []
        [] [] []
        [] [.] []
        The dot represents where you are on the map right now!
    """)
        while (path_choice != "left") and (path_choice != "right") and (path_choice != "forward"):
            path_choice = input("Which path shall you take? Left, Right, or Forward? : ").lower()
            if path_choice == "left":
                current_pos = 7
            elif path_choice == "right":
                current_pos = 9
            elif path_choice == "forward":
                current_pos = 5
    elif current_pos == 9:
        player_retry_check = dr.room9()
        if player_retry_check == -1:
            current_pos = 5
            continue
        path_choice = input("The path ahead still waits for you...Choose your fate. (enter to continue)")
        print( """
        [] [] []
        [] [] []
        [] [] [.]
        The dot represents where you are on the map right now!

    """)
        while (path_choice != "left") and (path_choice != "forward"):
            path_choice = input("Which path shall you take? Left or Forward? : ").lower()
            if path_choice == "left":
                current_pos = 8
            elif path_choice == "forward":
                current_pos = 6