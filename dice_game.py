"""
Mallory Rich
IS 303

A simple dice game where the player rolls against the computer

Inputs
- how many rounds player wants to play

Processes
- get_valid_input(): prompt how many times to play, verify input as int between 1 and 5
- roll_dice(): random library, roll 2 dice, return values of dice
- determine_winner(): determine which value is higher, return winner
- show_scoreboard(): print results 

Outputs 
- scoreboard

"""

import random

# FUNCTIONS

def get_valid_input (prompt):
    while True:
        try:
            num_of_rounds = int(input(prompt))
            if num_of_rounds > 5 or num_of_rounds < 1:
                raise TypeError
            return num_of_rounds
        except ValueError:
            print("Invalid input. Please enter a number.")
        except TypeError:
            print("Invalid input. Please enter a number between 1 and 5.")
    
    
def roll_dice ():
    return random.randint(1,6)

def determine_winner (user_num, comp_num):
    if user_num > comp_num:
        print("You won!")
        return "user_win"
    elif comp_num > user_num:
        print("Computer won!")
        return "comp_win"
    else:
        print("You tied!")
        return "tie"

def show_scoreboard (user_score, comp_score):
    print(f"\nYou won {user_score} rounds!")
    print(f"Computer won {comp_score} rounds!")
    if user_score > comp_score:
        print("You won the game!")
    elif comp_score > user_score:
        print("Computer won the game!")
    else:
        print("You tied!")


# MAIN FLOW

"""
get input from player about how many rounds to play

roll dice

show winner for round

continue until all rounds are played

show final results with ultimate winner

"""

user_score = 0
comp_score = 0

total_rounds = get_valid_input("How many rounds do you want to play? (1-5): ")

for round_number in range(total_rounds):
    user_roll_dice = roll_dice()
    comp_roll_dice = roll_dice()
    print(f"\nYou rolled {user_roll_dice}. Computer rolled {comp_roll_dice}.")
    round_winner = determine_winner(user_roll_dice, comp_roll_dice)
    if round_winner == "user_win":
        user_score += 1
    elif round_winner == "comp_win":
        comp_score += 1

show_scoreboard(user_score, comp_score)