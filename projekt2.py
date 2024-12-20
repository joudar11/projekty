"""
projekt2.py: druhý projekt do Engeto Online Python Akademie

author: Kryštof Klika
email: krystofklika@pm.me
"""

import random

correct = False

#str - vraci nahodne ctyrmistne cislo k hadani hracem, ktere je unikatni a nezacina nulou
def to_guess():
    numbers = list(range(0, 10))
    increments = [1000, 100, 10, 1]
    number = 0

    for _ in range(4):
        if _ == 0:
            rand = random.randint(1, len(numbers)-1)
        else:
            rand = random.randint(0, len(numbers)-1)
        number = number + (increments[_] * numbers[rand])
        numbers.pop(rand)
    return str(number)

#bool - overi hracem zadane cislo - (delsi nebo kratsi nez 4, unikatni, zacatek 0, neciselne znaky). True, pokud je vstup v poradku, False, pokud neni
def verify(user_input):
    #kontrola zda je cislo
    if not user_input.isdigit():
        print("Input is not a valid number!")
        return False
    
    #kontrola delky
    if len(user_input) != 4:
        print("Input must be 4 digits!")
        return False
    
    #kontrola zacatku nulou
    if user_input.startswith("0"):
        print("Input must not start with 0!")
        return False
    
    #kontrola unikatnosti
    if len(set(user_input)) != 4:
        print("Each digit must only be present once!")
        return False
    
    #pozitivni return, pokud je vse ok
    return True

#oznami vyhru
def announce_win(final_guesses):
    plural = ""
    if final_guesses > 1:
        plural = "es"
    print(
        "Correct, you've guessed the right number", f"in {final_guesses} guess{plural}!", "-"*47, "That's amazing!", sep="\n")

#vrati string bull nebo bulls
def bull(n):
    if n == 1:
        return "1 bull"
    else:
        return f"{n} bulls"

#vrati string cow nebo cows
def cow(n):
    if n  == 1:
        return "1 cow"
    else:
        return f"{n} cows"

#uvitani
print(
    "Hi there!", "-"*47, "I've generated a random 4 digit number for you.", "Let's play a bulls and cows game.", "-"*47, "Enter a number:", "-"*47, sep="\n"
)

#hra
guesses = 0
secret = to_guess()
while not correct:
    bulls = 0
    cows = 0
    guess = input(">>> ")
    if verify(guess):
        guesses += 1
        if guess == secret:
            correct = True
        else:
            for i in range(len(guess)):
                if guess[i] == secret[i]:
                    bulls += 1
                elif guess[i] in secret:
                    cows += 1
            print(f"{bull(bulls)}, {cow(cows)}")
            if guesses == 10:
                print(f"\nBy the way, it is proved that any number\ncan be solved within seven turns.\nThe average minimal game length is\napproximately 5.21 turns.\n\nYou are on your {guesses}th guess. ;)\nGo on.\n")
    print("-"*47)
else:
    announce_win(guesses)