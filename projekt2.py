"""
projekt2.py: druhý projekt do Engeto Online Python Akademie

author: Kryštof Klika
email: krystofklika@pm.me
"""
import math
import random

correct = False

#int - vraci nahodne cislo k hadani hracem
def to_guess():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    increments = [1000, 100, 10, 1]
    number = 0

    for _ in range(4):
        if _ == 0:
            rand = random.randint(1, len(numbers)-1)
        else:
            rand = random.randint(0, len(numbers)-1)
        number = number + (increments[_] * numbers[rand])
        numbers.pop(rand)
    return(number)

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
        print("Each digit can only be present once")
        return False
    
    #pozitivni return, pokud je vse ok
    return True

def announce_win(final_guesses):
    print(f"""Correct, you've guessed the right number in {final_guesses} guesses!
-----------------------------------------------
That's amazing!""")

def bull(n):
    if n > 1:
        return "bulls"
    else:
        return "bull"

def cow(n):
    if n > 1:
        return "cows"
    else:
        return "cow"
#hra

print(
    """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------"""
)

guesses = 0
secret = str(to_guess())
print(secret)
while not correct:
    bulls = 0
    cows = 0
    guess = input(">>>")
    if verify(guess):
        guesses += 1
        if guess == str(secret):
            correct = True
        else:
            for i in range(len(guess)):
                if guess[i] == secret[i]:
                    bulls += 1
                elif guess[i] in secret:
                    cows += 1
            print(f"{bulls} {bull(bulls)}, {cows} {cow(cows)}")
else:
    announce_win(guesses)