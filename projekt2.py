"""
projekt2.py: druhý projekt do Engeto Online Python Akademie

author: Kryštof Klika
email: krystofklika@pm.me
"""
import math
import random


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
    if not user_input.isdigit():
        print("Input is not a valid number!")
        return False
    if len(user_input) != 4:
        print("Input must be 4 digits!")
        return False
    if user_input.startswith("0"):
        print("Input must not start with 0!")
        return False
    
    set_verify = set()
    for number in range(len(user_input)):
        set_verify.add(user_input[number])

    if len(set_verify) != 4:
        print("Each digit can only be present once")
        return False

    return True