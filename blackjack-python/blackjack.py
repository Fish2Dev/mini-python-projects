from time import sleep
from sys import exit
import random
all_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_ace_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# used for testing ace card cases
#ace_cards = ["A","A","A","A","A","A","A","A","A","A"]
def play_bot():
    bot_cards.append(no_ace_cards[random.randint(0, 8)])   
    bot_cards.append(all_cards[random.randint(0, 9)])
    if "A" in bot_cards:
        bot_cards[1] = 11
    bot_value_func = sum(bot_cards)
    bot_index_track = 1
    while bot_value_func < 21:
        bot_cards.append(all_cards[random.randint(0, 9)])
        bot_index_track += 1
        if "A" in bot_cards:
            bot_cards[bot_index_track] = 1
        bot_value_func = sum(bot_cards)
    del bot_cards[-1]
    bot_value_func = sum(bot_cards)
    return bot_value_func

def check_ace():
    if "A" in player_cards:
        print(f"Your cards are {player_cards[0]} and {player_cards[1]}.")
        user_ace_value = int(input("Would you like the ace to equal 1 or 11? : "))
        while user_ace_value != 1 and user_ace_value != 11:
            print("That is not a valid answer")
            user_ace_value = int(input("Would you like the ace to equal 1 or 11? : "))
        ace_track = 0
        for ace_index, ace_value in enumerate(player_cards):
            if ace_value == "A" and ace_track == 0:
                player_cards[ace_index] = user_ace_value
                ace_track += 1
            elif ace_value == "A" and ace_track == 1:
                user_ace_value = int(input("You got another ace! Would you like the ace to equal 1 or 11? : "))
                while user_ace_value != 1 and user_ace_value != 11:
                    print("That is not a valid answer")
                    user_ace_value = int(input("You got another ace! Would you like the ace to equal 1 or 11? : "))
                player_cards[ace_index] = user_ace_value
print("Welcome to Blackjack!")
print("Dealing Cards...")
sleep(2)
player_cards = []
bot_cards = []
player_value = 0
bot_value = 0
for _ in range(2):
    player_cards.append(all_cards[random.randint(0, 9)])
    check_ace()
print(f"Your cards are {player_cards[0]} and {player_cards[1]}.")
player_value = sum(player_cards)
while True:
    player_choice = input("Would you like to \"hit\" or \"stand\" : ").lower()
    if player_choice == "hit":
        player_cards.append(all_cards[random.randint(0, 9)])
        check_ace()
        player_value = sum(player_cards)
        if player_value > 21:
            print("You busted!")
            exit(0)
        print("Your cards are: ")
        for card in player_cards:
            print(card)
    if player_choice == "stand":
        print(f"You have stood with {player_value} points!")
        sleep(0.5)
        bot_value = play_bot()
        print("Dealing Cards To Bot...")
        sleep(2)
        print("Waiting For Bot To Finish Playing...")
        sleep(2)
        if (player_value > bot_value) or (player_value == 21 and bot_value != 21):
            print("You Win!")
            show_bot_cards = input("Would you like to see the bot's cards? : ")
            if show_bot_cards == "no":
                print("Run this program to play another game!")
                exit(0)
            elif show_bot_cards == "yes":
                for bot_card in bot_cards:
                    print(bot_card)
                print("Run this program to play another game!")
                input("Type anything to quit : ")
                exit(0)
        if (bot_value > player_value) or (bot_value == 21 and player_value != 21):
            print("Bot Wins!")
            show_bot_cards = input("Would you like to see the bot's cards? : ")
            if show_bot_cards == "no":
                print("Run this program to play another game!")
                exit(0)
            elif show_bot_cards == "yes":
                for bot_card in bot_cards:
                    print(bot_card)
                print("Run this program to play another game!")
                input("Type anything to quit : ")
                exit(0)

