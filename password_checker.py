"""
Mallory Rich
IS 303

Password Checker - Evaluates password strength based on multiple criteria

Inputs:
- password (str)

Processes:
- check_length (password): return 1 point if password is at least 8 characters in length
- check_uppercase (password): return 1 point if password has at least 1 uppercase letter
- check_digits (password): return 1 point if password has at least 1 number
- calc_score (password): calls all check functions, returns score as integer
- display_results (password, score): prints password, overall password strength score (weak, moderate, strong)

Outputs:
- password
- score
- strength label
"""

import re

# FUNCTIONS

def check_length (password):
    """ return 1 point if password is at least 8 characters in length """
    if len(password) >= 8:
        return 1
    return 0
    
#while True:
#   try:  
#   except EOFError:
#       print("No input was received.")

def check_uppercase (password):
    """ return 1 point if password has at least 1 uppercase letter """
    if re.search(r"[A-Z]", password):
        return 1
    return 0

def check_digits (password):
    """ return 1 point if password has at least 1 number """
    if re.search(r"[0-9]", password):
        return 1
    return 0

def calc_score (password):
    """ calls all check functions, returns score as integer """

    length_score = check_length(password)
    upper_score = check_uppercase(password)
    digit_score = check_digits(password)
    
    total = length_score + upper_score + digit_score
    return total

def display_results (password):
    """ prints password, overall password strength score (weak, moderate, strong) """

    try:
        if password == "":
            raise ValueError("Password cannot be blank.")
    except ValueError as error:
        print(error)

    total = calc_score(password)
    if total == 3:
        strength = "excellent"
    elif total == 2:
        strength = "strong"
    elif total == 1:
        strength = "moderate"
    else:
        strength = "weak"
   
    print(f"Your password: {password}")
    print(f"Your password strength: {strength}")


# MAIN FLOW

password = input("What is your password? ")



results = display_results(password)