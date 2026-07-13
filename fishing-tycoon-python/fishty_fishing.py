from random import randint
from time import sleep
def define_rarity(rarity_num, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    if rarity_num >= num1 and rarity_num <= num2:
        return "Common"
    if rarity_num >= num3 and rarity_num <= num4:
        return "Uncommon"
    if rarity_num >= num5 and rarity_num <= num6:
        return "Rare"
    if rarity_num >= num7 and rarity_num <= num8:
        return "Epic"
    if rarity_num >= num9 and rarity_num <= num10:
        return "Legendary"
def phase1_fish(rod, spot, space, s1, s2, s3, m1, m2, m3, catch_m1, catch_m2, catch_m3):
    inventory = {}
    fish_rarity = None
    fish_caught = None
    multiplier = None
    if rod == "twin":
        multiplier= 2
    elif rod == "triple":
        multiplier= 3
    else:
        multiplier= 1
    print("Fishing...")
    sleep(3)
    while space > 0: 
        if multiplier > space:
            multiplier = 1
        for _ in range(multiplier):                                                                                                                                                                   
            fish_rarity_num = randint(1, 100)
            if rod == "old":
                if fish_rarity_num >= 1 and fish_rarity_num <= 70:
                    fish_rarity = "Common"
                if fish_rarity_num >= 71 and fish_rarity_num <= 90:
                    fish_rarity = "Uncommon"
                if fish_rarity_num >= 91 and fish_rarity_num <= 98:
                    fish_rarity = "Rare"
                if fish_rarity_num >= 99 and fish_rarity_num <= 100:
                    fish_rarity = "Epic"
            if rod == "pristine":
                fish_rarity = define_rarity(fish_rarity_num, 1, 55, 56, 80, 81, 94, 95, 99, 100, 100)
            if rod == "lucky":
                fish_rarity = define_rarity(fish_rarity_num, 1, 35, 36, 65, 66, 85, 86, 96, 97, 100)
            if rod == "enchanted":
                fish_rarity = define_rarity(fish_rarity_num, 1, 15, 16, 40, 41, 72, 73, 91, 92, 100)
            if rod == "twin":
                fish_rarity = define_rarity(fish_rarity_num, 1, 48, 49, 76, 77, 92, 93, 98, 99, 100)
            if rod == "triple":
                fish_rarity = define_rarity(fish_rarity_num, 1, 32, 33, 62, 63, 83, 84, 95, 96, 100)
            if rod == "serpent" or rod == "octo" or rod == "crab":
                if fish_rarity_num >= 1 and fish_rarity_num <= 60:
                    fish_rarity = "Rare"
                if fish_rarity_num >= 61 and fish_rarity_num <= 98:
                    fish_rarity = "Epic"
                if fish_rarity_num >= 99 and fish_rarity_num <= 100:
                    fish_rarity = "Mythical"
            if spot == 1:
                for item in s1:
                    if fish_rarity == s1[item]["rarity"]:
                        fish_caught = item
            elif spot == 2:
                for item in s2:
                    if fish_rarity == s2[item]["rarity"]:
                        fish_caught = item
            elif spot == 3 and (rod != "serpent" and rod != "octo" and rod != "crab"):
                for item in s3:
                    if fish_rarity == s3[item]["rarity"]:
                        fish_caught = item
            elif spot == 3 and rod == "serpent":
                if fish_rarity == "Mythical":
                    catch_m1 = True
                for item in m1:
                    if fish_rarity == m1[item]["rarity"]:
                        fish_caught = item
            elif spot == 3 and rod == "octo":
                if fish_rarity == "Mythical":
                    catch_m2 = True
                for item in m2:
                    if fish_rarity == m2[item]["rarity"]:
                        fish_caught = item
            elif spot == 3 and rod == "crab":
                if fish_rarity == "Mythical":
                    catch_m3 = True
                for item in m3:
                    if fish_rarity == m3[item]["rarity"]:
                        fish_caught = item
            if fish_caught in inventory:
                inventory[fish_caught]["amount"] += multiplier
                if spot == 1:
                    inventory[fish_caught]["value"] = s1[fish_caught]["value"]
                elif spot == 2:
                    inventory[fish_caught]["value"] = s2[fish_caught]["value"]
                elif spot == 3 and (rod != "serpent" and rod != "octo" and rod != "crab"):
                    inventory[fish_caught]["value"] = s3[fish_caught]["value"]
                elif spot == 3 and rod == "serpent":
                    inventory[fish_caught]["value"] = m1[fish_caught]["value"]
                elif spot == 3 and rod == "octo":
                    inventory[fish_caught]["value"] = m2[fish_caught]["value"]
                elif spot == 3 and rod == "crab":
                    inventory[fish_caught]["value"] = m3[fish_caught]["value"]
            else:
                if spot == 1:
                    inventory[fish_caught] = {
                        "amount" : multiplier,
                        "value" : s1[fish_caught]["value"]
                    }
                elif spot == 2:
                    inventory[fish_caught] = {
                        "amount" : multiplier,
                        "value" : s2[fish_caught]["value"]
                    }
                elif spot == 3 and (rod != "serpent" and rod != "octo" and rod != "crab"):
                    inventory[fish_caught] = {
                        "amount" : multiplier,
                        "value" : s3[fish_caught]["value"]
                    }
                elif spot == 3 and rod == "serpent":
                    inventory[fish_caught] = {
                        "amount" : multiplier,
                        "value" : m1[fish_caught]["value"]
                    }
                elif spot == 3 and rod == "octo":
                    inventory[fish_caught] = {
                        "amount" : multiplier,
                        "value" : m2[fish_caught]["value"]
                    }
                elif spot == 3 and rod == "crab":
                    inventory[fish_caught] = {
                        "amount" : multiplier,
                        "value" : m3[fish_caught]["value"]
                    }
            space -= multiplier   
    print("Here is what you caught:")
    if spot == 1:
        for inv_item in inventory:
            print(f"{inventory[inv_item]["amount"]} {s1[inv_item]["rarity"]} {inv_item} worth ${s1[inv_item]["value"]} each.")
    if spot == 2:
        for inv_item in inventory:
            print(f"{inventory[inv_item]["amount"]} {s2[inv_item]["rarity"]} {inv_item} worth ${s2[inv_item]["value"]} each.")
    if spot == 3 and (rod != "serpent" and rod != "octo" and rod != "crab"):
        for inv_item in inventory:
            print(f"{inventory[inv_item]["amount"]} {s3[inv_item]["rarity"]} {inv_item} worth ${s3[inv_item]["value"]} each.")
    if spot == 3 and rod == "serpent":
        for inv_item in inventory:
            print(f"{inventory[inv_item]["amount"]} {m1[inv_item]["rarity"]} {inv_item} worth ${m1[inv_item]["value"]} each.")
    if spot == 3 and rod == "octo":
        for inv_item in inventory:
            print(f"{inventory[inv_item]["amount"]} {m2[inv_item]["rarity"]} {inv_item} worth ${m2[inv_item]["value"]} each.")
    if spot == 3 and rod == "crab":
        for inv_item in inventory:
            print(f"{inventory[inv_item]["amount"]} {m3[inv_item]["rarity"]} {inv_item} worth ${m3[inv_item]["value"]} each.")
    input("Enter to continue: ")
    return inventory, catch_m1, catch_m2, catch_m3