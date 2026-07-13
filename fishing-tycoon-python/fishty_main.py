import random
from math import floor
import fishty_fishing as fish
day = 0
player_inventory = {}
player_rods = ["Old Fishing Rod"]
rod_lookup = {
    "old": "Old Fishing Rod",
    "pristine": "Pristine Fishing Rod",
    "enchanted": "Enchanted Fishing Rod",
    "lucky": "Lucky Fishing Rod",
    "twin": "Twin Hook Rod",
    "triple": "Triple Bait Rod",
    "serpent": "Serpent Catcher",
    "octo": "Octo Catcher",
    "crab": "Crab Catcher"
}
spot1_fish = {
    "Sand Crab" : {"value": 3, "rarity": "Common"},
    "Shallow Water Sardine" : {"value": 6, "rarity": "Uncommon"},
    "Shallow Water Mackerel" : {"value": 14, "rarity": "Rare"},
    "Glass Shrimp" : {"value": 30, "rarity": "Epic"},
    "Ribbon Eel" : {"value": 60, "rarity": "Legendary"},
}
spot2_fish = {
    "Rockfish" : {"value": 4, "rarity": "Common"},
    "Barbed Urchin" : {"value": 8, "rarity": "Uncommon"},
    "Neon Reef Squid" : {"value": 18, "rarity": "Rare"},
    "Lionfish" : {"value": 36, "rarity": "Epic"},
    "Peacock Mantis Shrimp" : {"value": 75, "rarity": "Legendary"},
}
spot3_fish = {
    "Slime Hagfish" : {"value": 5, "rarity": "Common"},
    "Ghost Shark" : {"value": 10, "rarity": "Uncommon"},
    "Viperfish" : {"value": 22, "rarity": "Rare"},
    "Vampire Octopus" : {"value": 45, "rarity": "Epic"},
    "Colossal Squid" : {"value": 90, "rarity": "Legendary"},
}
myth_fish1 = {
    "Moray Eel" : {"value": 22, "rarity": "Rare"},
    "Gulper Eel" : {"value": 42, "rarity": "Epic"},
    "The Leviathan" : {"value": 150, "rarity": "Mythical"},
}
myth_fish2 = {
    "Mimic Octopus" : {"value": 25, "rarity": "Rare"},
    "Dumbo Octopus" : {"value": 45, "rarity": "Epic"},
    "The Kraken" : {"value": 125, "rarity": "Mythical"},
}
myth_fish3 = {
    "Arrow Crab" : {"value": 24, "rarity": "Rare"},
    "Abyssal Hermit Crab" : {"value": 48, "rarity": "Epic"}, 
    "The Blue King Crab" : {"value": 110, "rarity": "Mythical"},
}
def dialogue(message): 
    print(message)
    input("")
print("Welcome to Fishing Tycoon!")
store_name = input("Pick a name for your fish store : ")
market_e10_sponsor = " "
market_e10_value = 0
market_events = {
    1 : "Unexpected Freeze hits the city! - Grilled Plates are now worth double.",
    2 : "International Sushi Day - Sushi plates are now worth double",
    3 : "Tourists flood the city! They're looking for some fried comfort food - Tempura plates are now worth double",
    4 : "The city is stuck in a power outage! - Cooking equipment does not work anymore but fish from last night is still preserved, can still store fish in freezer today.",
    5 : "A millionaire challenges the city! Get a fortune from legendary sea creatures!- Legendary creatures are now worth triple",
    6 : "Nothing big happening in the city today!",
    7 : "It's tax season! - 15 percent of the money that you earn today is now lost to taxes.",
    8 : "Thunderstorm incoming! - Customer volume is less today.",
    9 : f"Local food critic rates {store_name} 5 stars! - Customer volume is increased today!",
}
need_tutorial = None
market_today = None
rod_equipped = "old"
leviathan_catch = False
kraken_catch = False
bluecrab_catch = False
spot_unlocked = 1
backpack_space = 3
rod_want = None
grill_have = False
rice_cook_have = False
fryer_have = False
freezer_have = False
customer_volume = None
player_money = 0
freezer_inv = {}
while need_tutorial != "y"and need_tutorial != "n":
    need_tutorial = input("Would you like a quick tutorial? (y or n) : ")
if need_tutorial == "n":
    pass
if need_tutorial == "y":
    dialogue("With dialogue, press the enter key to continue!")
    dialogue("Your goal is to manage your fishing tycoon for 30 days while aiming for certain medals!")
    dialogue("Read the news in the morning to see what the market has affected!")
    dialogue("Head out to catch some raw fish!")
    dialogue("Go to your store and sell the raw fish, or cook it into meals if you have the equipment!")
    dialogue("Customer volumes changes day to day so not all of your fish/meals will sell.")
    dialogue("At the end of the day, remaining fish can be put in the freezer (if you bought one), or it will spoil.")
    dialogue("Also at the end of the day, use your money to go to different shops.")
    dialogue("At shops, you can buy fishing rods, backpack storage, permits for new fishing spots, cooking equipment, etc.")
    dialogue("Plus, a little secret: You can catch mythical sea creatures!")
    dialogue("Just buy the corresponding fishing rod, head to the last spot, get fishing, and hope you're lucky!")
    dialogue("Ready to go out to sea?!")
def main_fish():
    global day
    global market_today
    global market_events
    global current_rod
    global player_rods
    global rod_equipped
    global rod_want
    global rod_lookup
    global backpack_space
    global player_inventory
    global leviathan_catch 
    global kraken_catch 
    global bluecrab_catch
    global market_e10_value
    global market_e10_sponsor
    day += 1
    dialogue(f"It's a new day today! Day: {day} (Remember: Enter to continue for any dialogue!)") 
    market_today = random.randint(1, 10)
    sponsorships = ["Rainbow Trout Resorts", "Tough Bass Bait & Tackle", "Catfish's Corner", "Barracuda Banking Solutions", "Hammerhead Marketing Solutions", "The Crimson Salmon Syndicate", "Viperfish Travel Agency", "Great White Wholesale Groceries", "Nautilus Shipping & Logistics", "Squid Catering & Co.", "Octo-Travel Airlines", "Blue Crab Boats", "Mantis Shrimp Bobbers & Nets", "Clam Jam Diner Chain", "Electric Eel Energy Corp.", "Shrimp N Dip Diner", "Mackerel & Sardine Permits", "The Home Essentials: Kitchen Edition", "Sharky's Big Backpacks", "Ocean's Fishing Rods", "Hermit Crab's Abyssal Theme Park", "The Parrotfish Night Club", "Lionfish Commerical Storage", "FishMart Co.", "Eel & Crab Trader's Market"]
    sponsor_values = [0.10, 0.125, 0.15, 0.175, 0.20]
    if market_today == 10:
        market_e10_sponsor = random.choice(sponsorships)
        market_e10_value = random.choice(sponsor_values)
    dialogue("Let's read the news!")
    if market_today == 10:
        print(f"{market_e10_sponsor} has sponsored you for a {market_e10_value * 100} percent increase on all profits today!")
    else:
        dialogue(f"\"{market_events[market_today]}\"")
    dialogue("Time to head out to fish!")
    print("Owned fishing rods:")
    for current_rod in player_rods:
        print(current_rod)
    print("Example: To equip the Old Fishing Rod, type \"old\"")
    while True:
        rod_want = input("Type the first word (not case sensitive) of the rod you want to equip! : ").lower()
        try:
            if rod_lookup[rod_want] in player_rods:
                rod_equipped = rod_want
                break
        except KeyError:
            print("You do not have that rod! Pick a rod that is in your inventory.")
    if rod_equipped == "twin":
        backpack_space += 4
    if rod_equipped == "triple":
        backpack_space += 8
    dialogue("Rod equipped! (Enter to continue to fishing)")
    player_inventory, leviathan_catch, kraken_catch, bluecrab_catch = fish.phase1_fish(rod_equipped, spot_unlocked, backpack_space, spot1_fish, spot2_fish, spot3_fish, myth_fish1, myth_fish2, myth_fish3, leviathan_catch, kraken_catch, bluecrab_catch)
    if rod_equipped == "twin":
        backpack_space -= 4
    if rod_equipped == "triple":
        backpack_space -= 8
    dialogue("Let's head back to our shop!")
def main_cook():
    global player_inventory
    global grill_have
    global rice_cook_have
    global fryer_have
    global freezer_have
    global customer_volume
    global spot_unlocked
    global spot1_fish
    global spot2_fish
    global spot3_fish
    global player_money
    global freezer_inv
    if market_today == 8:
        customer_volume = random.uniform(0.35, 0.65)
    elif market_today == 9:
        customer_volume = random.uniform(0.86, 0.95)
    else:
        customer_volume = random.uniform(0.70, 0.85)
    if freezer_have == True and len(freezer_inv) > 0:
        for fish_in_freeze in freezer_inv:
            player_inventory[fish_in_freeze] = {
                "amount": freezer_inv[fish_in_freeze]["amount"],
                "value": freezer_inv[fish_in_freeze]["value"]
            }
        freezer_inv.clear()
        dialogue("Your fish has succesfully been recovered from the freezer (enter to continue)")
    dialogue("Let's head over to the shop so we can prepare food for customers! (enter to continue)")
    dialogue("NOTE: If you have any appliances, the order of which ones you use first will go like this: (Grill, Rice Cooker, Tempura).")
    if market_today == 5:
        if "The Leviathan" in player_inventory:
            player_inventory["The Leviathan"]["value"] *= 3
        if "The Kraken" in player_inventory:
            player_inventory["The Kraken"]["value"] *= 3
        if "The Blue King Crab" in player_inventory:
            player_inventory["The Blue King Crab"]["value"] *= 3
    if market_today == 4:
        print("Your appliances are not working, No cooking today!")
    else:
        if grill_have == True:
            dialogue("Let's grill some food!")
            print("This is your inventory:")
            for fish in player_inventory:
                print(f"{player_inventory[fish]['amount']} {fish}")
            while True:
                fish_want_grill = input("Type the name of the fish you want to grill (case sensitive). Type \"DONE\" when done grilling! ")
                if fish_want_grill in player_inventory:
                    if "Grilled" in fish_want_grill or "Tempura" in fish_want_grill or "Sushi" in fish_want_grill or "Sashimi" in fish_want_grill or "Onigiri" in fish_want_grill:
                        print("You have already cooked that fish!")
                    else:
                        fish_grill_amt = int(input("How many of that fish do you want to grill? "))
                        if fish_grill_amt > player_inventory[fish_want_grill]["amount"]:
                            print("You do not have that much fish to grill!")
                        elif fish_grill_amt == 0:
                            print("Error: You cannot grill zero fish")
                        else:
                            cooked_name = "Grilled " + fish_want_grill
                            if cooked_name not in player_inventory:
                                player_inventory[cooked_name] = {"amount": 0, "value": 0}
                            player_inventory[cooked_name]["amount"] += fish_grill_amt
                            if market_today == 1:
                                player_inventory[cooked_name]["value"] = round((player_inventory[fish_want_grill]["value"] * 1.25) * 2)
                            else:
                                player_inventory[cooked_name]["value"] = round(player_inventory[fish_want_grill]["value"] * 1.25)
                            player_inventory[fish_want_grill]["amount"] -= fish_grill_amt
                            if player_inventory[fish_want_grill]["amount"] == 0:
                                del player_inventory[fish_want_grill]
                elif fish_want_grill == "DONE":
                    break
                else:
                    print("You do not have that fish in your inventory, please try again!")
        if rice_cook_have == True:
            dialogue("Let's make some sushi!")
            print("This is your inventory:")
            for fish in player_inventory:
                print(f"{player_inventory[fish]['amount']} {fish}")
            while True:
                fish_want_sushi = input("Type the name of the fish you want to make into sushi (case sensitive). Type \"DONE\" when done making! ")
                if fish_want_sushi in player_inventory:
                    if "Grilled" in fish_want_sushi or "Tempura" in fish_want_sushi or "Sushi" in fish_want_sushi or "Sashimi" in fish_want_sushi or "Onigiri" in fish_want_sushi:
                        print("You have already cooked that fish!")
                    else:
                        fish_sushi_amt = int(input("How many of that fish do you want to make into sushi? "))
                        if fish_sushi_amt > player_inventory[fish_want_sushi]["amount"]:
                            print("You do not have that much fish to make into sushi!")
                        elif fish_sushi_amt == 0:
                            print("Error: You cannot make sushi with zero fish")
                        else:
                            rand_prefix_sushi = random.randint(1, 3)
                            if rand_prefix_sushi == 1:
                                cooked_name = fish_want_sushi +" Sushi"
                            elif rand_prefix_sushi == 2:
                                cooked_name = fish_want_sushi +" Sashimi"
                            elif rand_prefix_sushi == 3:
                                cooked_name = fish_want_sushi +" Onigiri"
                            if cooked_name not in player_inventory:
                                player_inventory[cooked_name] = {"amount": 0, "value": 0}
                            player_inventory[cooked_name]["amount"] += fish_sushi_amt
                            if market_today == 2:
                                player_inventory[cooked_name]["value"] = round((player_inventory[fish_want_sushi]["value"] * 1.85) * 2)
                            else:
                                player_inventory[cooked_name]["value"] = round(player_inventory[fish_want_sushi]["value"] * 1.85)
                            player_inventory[fish_want_sushi]["amount"] -= fish_sushi_amt
                            if player_inventory[fish_want_sushi]["amount"] == 0:
                                del player_inventory[fish_want_sushi]
                elif fish_want_sushi == "DONE":
                    break
                else:
                    print("You do not have that fish in your inventory, please try again!")
        if fryer_have == True:
            dialogue("Let's fry some food!")
            print("This is your inventory:")
            for fish in player_inventory:
                print(f"{player_inventory[fish]['amount']} {fish}")
            while True:
                fish_want_fry = input("Type the name of the fish you want to fry (case sensitive). Type \"DONE\" when done frying! ")
                if fish_want_fry in player_inventory:
                    if "Grilled" in fish_want_fry or "Tempura" in fish_want_fry or "Sushi" in fish_want_fry or "Sashimi" in fish_want_fry or "Onigiri" in fish_want_fry:
                        print("You have already cooked that fish!")
                    else:
                        fish_fry_amt = int(input("How many of that fish do you want to fry? "))
                        if fish_fry_amt > player_inventory[fish_want_fry]["amount"]:
                            print("You do not have that much fish to fry!")
                        elif fish_fry_amt == 0:
                            print("Error: You cannot fry zero fish")
                        else:
                            cooked_name = fish_want_fry + " Tempura"
                            if cooked_name not in player_inventory:
                                player_inventory[cooked_name] = {"amount": 0, "value": 0}
                            player_inventory[cooked_name]["amount"] += fish_fry_amt
                            if market_today == 3:
                                player_inventory[cooked_name]["value"] = round((player_inventory[fish_want_fry]["value"] * 1.55) * 2)
                            else:
                                player_inventory[cooked_name]["value"] = round(player_inventory[fish_want_fry]["value"] * 1.55)
                            player_inventory[fish_want_fry]["amount"] -= fish_fry_amt
                            if player_inventory[fish_want_fry]["amount"] == 0:
                                del player_inventory[fish_want_fry]
                elif fish_want_fry == "DONE":
                    break
                else:
                    print("You do not have that fish in your inventory, please try again!") 
    dialogue("Let's open the shop so customers can start buying food!") 
    total_fish_caught = 0
    total_profit = 0
    for caught_fish in player_inventory:
        total_fish_caught += player_inventory[caught_fish]["amount"]
    total_fish_avaliable = round(total_fish_caught * customer_volume)
    while total_fish_avaliable != 0:
        fish_want_buy = random.choice(list(player_inventory.keys()))
        if total_fish_avaliable > player_inventory[fish_want_buy]["amount"]:
            fish_want_buy_amt = random.randint(1, player_inventory[fish_want_buy]["amount"])
        else:
            fish_want_buy_amt = random.randint(1, total_fish_avaliable)
        total_profit += player_inventory[fish_want_buy]["value"] * fish_want_buy_amt
        total_fish_avaliable -= fish_want_buy_amt
        player_inventory[fish_want_buy]["amount"] -= fish_want_buy_amt
        dialogue(f"A customer has bought {fish_want_buy_amt} {fish_want_buy} for ${player_inventory[fish_want_buy]['value']} each. (enter to continue)")
        if player_inventory[fish_want_buy]["amount"] == 0:
            del player_inventory[fish_want_buy]
    if market_today == 7:
        total_profit -= round(total_profit * 0.15)
        dialogue("Unfortunately, 15 percent of your profits has been lost to taxes!")
    if market_today == 10:
        total_profit += round(total_profit * market_e10_value)
        dialogue("Your sponsorship bonus has been applied!")
    player_money += total_profit
    dialogue(f"You have made ${total_profit} today!")
    dialogue(f"You currently have a total of ${player_money} in your wallet!")
    if freezer_have == True:
        dialogue("Let's see if we can save any fish for tomorrow!")
        print("Here is your leftover fish:")
        for fish in player_inventory:
            print(f"{player_inventory[fish]['amount']} {fish}")
        fish_want_freeze = None
        while fish_want_freeze != "DONE":
            fish_want_freeze = input("Type the fish you want to freeze (case sensitive), Type \"DONE\" when done freezing: ")
            if fish_want_freeze in player_inventory:
                if "Grilled" in fish_want_freeze or "Tempura" in fish_want_freeze or "Sushi" in fish_want_freeze or "Sashimi" in fish_want_freeze or "Onigiri" in fish_want_freeze:
                    print("You cannot freeze cooked meals!")
                else:
                    fish_left_amt = player_inventory[fish_want_freeze]["amount"]
                    fish_marked_val = round(player_inventory[fish_want_freeze]["value"] * 0.80)
                    freezer_inv[fish_want_freeze] = {
                        "amount": fish_left_amt, 
                        "value": fish_marked_val
                    }
                    print("Fish stored successfully!")
            elif fish_want_freeze == "DONE":
                player_inventory.clear()
            else:
                print("You do not have that fish in your inventory")
    else:
        dialogue("Unfortunately the rest of your fish has spoiled!")
        player_inventory.clear()
    dialogue("Let's head over to the mall and buy some items!")
def rod_shop():
    global player_rods
    global player_money
    dialogue("Welcome to Ocean's Fishing Rods!")
    while True:
        rod_shop_want = ""
        dialogue("NOTE: A lot of rods will shop up on the screen! Scroll up and down to find your preferred rod! (enter to continue)")
        dialogue(f"You currently have ${player_money}. (enter to continue)")
        print("General Rods:")
        print("1. Pristine Fishing Rod - $45")
        print("\nLucky Rods:")
        print("NOTE: These rods focus on getting better and luckier fish!")
        print("2. Lucky Fishing Rod - $120")
        print("3. Enchanted Fishing Rod - $250")
        print("\nMulti Catch Rods:")
        print("NOTE: These rods focus on catching multiple of the same fish at a time! They also provide extra backpack space!")
        print("4. Twin Hook Rod (+4 backpack space) - $120")
        print("5. Triple Bait Rod (+8 backpack space) - $250")
        print("\nMythical Catchers")
        print("NOTE: These only work in the Midnight Trench, have a different fish pool, and are the only way to catch mythical creatures!")
        print("6. Serpent Catcher (Chance to catch The Leviathan) - $350")
        print("7. Octo Catcher (Chance to catch The Kraken) - $350")
        print("8. Crab Catcher (Chance to catch The Blue King Crab) - $350")
        print("\n9. Exit Fishing Rod Shop")
        while rod_shop_want != "1" and rod_shop_want != "2" and rod_shop_want != "3" and rod_shop_want != "4" and rod_shop_want != "5" and rod_shop_want != "6" and rod_shop_want != "7" and rod_shop_want != "8" and rod_shop_want != "9":
            rod_shop_want = input("Type the corresponding number of the fishing rod you want to buy! : ")
        if rod_shop_want == "1":
            if player_money >= 45:
                player_money -= 45
                player_rods.append("Pristine Fishing Rod")
                dialogue("You have unlocked the Pristine Fishing Rod! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "2":
            if player_money >= 120:
                player_money -= 120
                player_rods.append("Lucky Fishing Rod")
                dialogue("You have unlocked the Lucky Fishing Rod! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "3":
            if player_money >= 250:
                player_money -= 250
                player_rods.append("Enchanted Fishing Rod")
                dialogue("You have unlocked the Enchanted Fishing Rod! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "4":
            if player_money >= 120:
                player_money -= 120
                player_rods.append("Twin Hook Rod")
                dialogue("You have unlocked the Twin Hook Rod! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "5":
            if player_money >= 250:
                player_money -= 250
                player_rods.append("Triple Bait Rod")
                dialogue("You have unlocked the Triple Bait Rod! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "6":
            if player_money >= 350:
                player_money -= 350                
                player_rods.append("Serpent Catcher")
                dialogue("You have unlocked the Serpent Catcher! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "7":
            if player_money >= 350:
                player_money -= 350            
                player_rods.append("Octo Catcher")
                dialogue("You have unlocked the Octo Catcher! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        elif rod_shop_want == "8":
            if player_money >= 350:
                player_money -= 350            
                player_rods.append("Crab Catcher")
                dialogue("You have unlocked the Crab Catcher! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this fishing rod! (enter to continue)")
        if rod_shop_want == "9":
            return
def backpack_shop():
    global backpack_space
    global player_money
    dialogue("Welcome to Sharky's Big Backpacks!")
    dialogue(f"You currently have ${player_money}. (enter to continue)")
    while True:
        backpack_want = ""
        print("Backpacks:")
        print("1. Pristine Backpack (6 slots) - $45")
        print("2. Duffel Bag (12 slots) - $110")
        print("3. Specialized Crate (18 slots) - $225")
        print("4. Exit Backpack Shop")
        while backpack_want != "1" and backpack_want != "2" and backpack_want != "3" and backpack_want != "4":
            backpack_want = input("Type the corresponding number of the backpack you want to buy! : ")
        if backpack_want == "1":
            if player_money >= 45:
                player_money -= 45
                backpack_space = 6
                dialogue("You have unlocked the Pristine Backpack! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this backpack! (enter to continue)")
        if backpack_want == "2":
            if player_money >= 110:
                player_money -= 110
                backpack_space = 12
                dialogue("You have unlocked the Duffel Bag! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this backpack! (enter to continue)")
        if backpack_want == "3":
            if player_money >= 225:
                player_money -= 225
                backpack_space = 18
                dialogue("You have unlocked the Specialized Crate! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this backpack! (enter to continue)")
        if backpack_want == "4":
            return
def kitchen_shop():
    global grill_have
    global rice_cook_have
    global fryer_have
    global freezer_have
    global player_money
    dialogue("Welcome to The Home Essentials: Kitchen Edition!")
    dialogue(f"You currently have ${player_money}. (enter to continue)")
    while True:
        cook_equipment_want = ""
        print("Cooking Equipment:")
        print("1. Seafood Grill (Unlocks Grilled Plates) - $70")
        print("2. Rice Cooker (Unlocks Sushi) - $110")
        print("3. Industrial Fryer (Unlocks Tempura) - $90")
        print("4. Deep Sea Freezer (Can Freeze Leftover Fish But At A Cost Of A 20% Markdown) - $120")
        print("5. Exit Cooking Equipment Shop")
        while cook_equipment_want != "1" and cook_equipment_want != "2" and cook_equipment_want != "3" and cook_equipment_want != "4" and cook_equipment_want != "5":
            cook_equipment_want = input("Type the corresponding number of the cooking equipment you want to buy! : ")
        if cook_equipment_want == "1":
            if player_money >= 70:
                player_money -= 70
                grill_have = True
                dialogue("You have unlocked the Seafood Grill! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this cooking equipment! (enter to continue)")
        if cook_equipment_want == "2":
            if player_money >= 110:
                player_money -= 110
                rice_cook_have = True
                dialogue("You have unlocked the Rice Cooker! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this cooking equipment! (enter to continue)")
        if cook_equipment_want == "3":
            if player_money >= 90:
                player_money -= 290
                fryer_have = True
                dialogue("You have unlocked the Industrial Fryer! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this cooking equipment! (enter to continue)")
        if cook_equipment_want == "4":
            if player_money >= 120:
                player_money -= 120
                freezer_have = True
                dialogue("You have unlocked the Deep Sea Freezer! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this cooking equipment! (enter to continue)")
        if cook_equipment_want == "5":
            return
def permit_shop():
    global spot_unlocked
    global player_money
    dialogue("Welcome to Mackerel & Sardine Permits! (enter to continue)")
    dialogue("NOTE: When you buy a permit you are limited to that spot. You cannot go back to a pervious spot! (enter to continue)")
    dialogue(f"You currently have ${player_money}. (enter to continue)")
    while True:
        permit_want = ""
        print("Permits:")
        print("1. Coral Reef Permit - $80")
        print("2. Midnight Trench Permit - $175")
        print("3. Exit Permit Shop")
        while permit_want != "1" and permit_want != "2" and permit_want != "3":
            permit_want = input("Type the corresponding number of the permit you want to buy! : ")
        if permit_want == "1":
            if player_money >= 80:
                player_money -= 80
                spot_unlocked = 2
                dialogue("You have unlocked the Coral Reef! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this permit! (enter to continue)")
        if permit_want == "2":
            if player_money >= 175:
                player_money -= 175
                spot_unlocked = 3
                dialogue("You have unlocked the Midnight Trench! (enter to continue)")
            else:
                dialogue("You do not have enough money to buy this permit! (enter to continue)")
        if permit_want == "3":
            return
def main_shop():
    while True:
        shop_selected = ""
        print("Shops:")
        print("1. Ocean's Fishing Rods")
        print("2. Sharky's Big Backpacks")
        print("3. The Home Essentials: Kitchen Edition ")
        print("4. Mackerel & Sardine Permits")
        print("5. Exit Mall")
        while shop_selected != "1" and shop_selected != "2" and shop_selected != "3" and shop_selected != "4" and shop_selected != "5":
            shop_selected = input("Type the corresponding number of the shop you want to go to! : ")
        if shop_selected == "1":
            rod_shop()
        if shop_selected == "2":
            backpack_shop()
        if shop_selected == "3":
            kitchen_shop()
        if shop_selected == "4":
            permit_shop()
        if shop_selected == "5":
            return
while day <= 31:
    main_fish()
    main_cook()
    main_shop()
dialogue("Congrats! You made it to the end of the 30 days. Let's see how you did! (enter to continue)")
if player_money >= 25000 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 3:
    print("🌑 Obsidian Medal Achieved! You accumlated more than 2500 bucks and catched 2 different mythical sea creatures!")
    print("The town looks at you like a legend now. Your shop has turned into a full on mall and you live in a mansion right by the beach. You've retired with your son managing the mall and are filthy rich. If dad were here, he would hold you in his arms, and tell you he proud of you. If only if it were that easy.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 15000 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 3:
    print("♦️ Ruby Medal Achieved! You accumlated more than 2500 bucks and catched 2 different mythical sea creatures!")
    print("The town looks at you like a legend now. Your shop has turned into a full on mall and you live in a mansion right by the beach. You've retired with your son managing the mall and are filthy rich. If dad were here, he would hold you in his arms, and tell you he proud of you. If only if it were that easy.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 10000 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 3:
    print("❇️ Emerald Medal Achieved! You accumlated more than 2500 bucks and catched 2 different mythical sea creatures!")
    print("The town looks at you like a legend now. Your shop has turned into a full on mall and you live in a mansion right by the beach. You've retired with your son managing the mall and are filthy rich. If dad were here, he would hold you in his arms, and tell you he proud of you. If only if it were that easy.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 7500 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 3:
    print("⭐ Platinum II Medal Achieved! You accumlated more than 2500 bucks and catched 2 different mythical sea creatures!")
    print("The town looks at you like a legend now. Your shop has turned into a full on mall and you live in a mansion right by the beach. You've retired with your son managing the mall and are filthy rich. If dad were here, he would hold you in his arms, and tell you he proud of you. If only if it were that easy.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 7500 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 2:
    print("⭐ Platinum I Medal Achieved! You accumlated more than 2500 bucks and catched 2 different mythical sea creatures!")
    print("The town looks at you like a legend now. Your shop has turned into a full on mall and you live in a mansion right by the beach. You've retired with your son managing the mall and are filthy rich. If dad were here, he would hold you in his arms, and tell you he proud of you. If only if it were that easy.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 5000 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 2:
    print("💎 Diamond III Medal Achieved! You accumlated more than 1500 bucks!")
    print("Well look at you! You made enough money to clear the massive debt you owe from the bank. The shop went from selling fish out of dad's old shack to a full running business. You hand the keys over to your aspiring son and visit dad one last time at the cemetary before officialy retiring.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 5000 and sum([leviathan_catch, bluecrab_catch, kraken_catch]) >= 1:
    print("💎 Diamond II Medal Achieved! You accumlated more than 1500 bucks!")
    print("Well look at you! You made enough money to clear the massive debt you owe from the bank. The shop went from selling fish out of dad's old shack to a full running business. You hand the keys over to your aspiring son and visit dad one last time at the cemetary before officialy retiring.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 5000:
    print("💎 Diamond I Medal Achieved! You accumlated more than 1500 bucks!")
    print("Well look at you! You made enough money to clear the massive debt you owe from the bank. The shop went from selling fish out of dad's old shack to a full running business. You hand the keys over to your aspiring son and visit dad one last time at the cemetary before officialy retiring.")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 3000:
    print("🥇 Gold Medal Achieved! You accumlated more than 750 bucks!")
    print("Congrats, you've made enough money to clear your debt. The shop is running well and you've been able to hire a small team. If you work a few more months, you'll be able to live a comfortable livestyle. Dad would be proud of you...")
    dialogue("Enter to continue to ending screen:")
elif player_money >= 1000:
    print("🥈 Silver Medal Achieved! You accumlated more than 250 bucks!")
    print("It's not much but it's not little. You used the money to upgrade dad's old shack into something better. It might take a few more months to clear the massive debt, but...there's hope.")
    dialogue("Enter to continue to ending screen:")
else:
    print("🥉 Bronze Medal Achieved! You ran a shop for 30 days!")
    print("You didn't make as much as you were hoping. The bank keeps sending letters every week talking about the massive debt you owe them. You'll have to go through a few more harsh winters and hot summers before you can relax.")
    dialogue("Enter to continue to ending screen:")

print("\n" * 100)
print("If you ever want to go for a higher medal, close the terminal and run the play command again!")
print("\n Thank you for playing!🐟🐟\n")