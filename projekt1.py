"""
projekt1.py: první projekt do Engeto Online Python Akademie

author: Kryštof Klika
email: krystofklika@pm.me
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


#prihlaseni
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = str(input("Enter username: "))
password = str(input("Enter password: "))
if user in users.keys():
    if users[user] == password:
        print("Welcome to the app, ", user)
    else:
        print("Pasword and username don't match!")
        exit()
else:
    print("User not registered! Exiting the program.")
    exit()

print("We have", len(TEXTS), "to be analyzed.")

#kontrola, ze na vstupu je cislo:
text_n = input("Please, select a text to analyze. Entere a number between 1 and 3: ")
if not text_n.isdigit():
    print("The input is not a number!")
    exit()

#kontrola, ze zadany text je v listu:
text_n = int(text_n)
if text_n > len(TEXTS):
    print("Text not found.")
    exit()


#zalozeni listu slov:
words = TEXTS[text_n-1].split()

#zalozeni promennych s vysledky:
count = 0
capitals = 0
uppers = 0
lowers = 0
numbers = 0
sum = 0
alnum = 0

#odstraneni znaku:

for i in range(len(words)):
    words[i] = words[i].strip(",.!?")

#graf
longest = 0
lengths_set = set()

for i in range(len(words)):
    lengths_set.add(len(words[i]))
lengths = dict.fromkeys(list(lengths_set), 0)
#analyza:

for i in range(len(words)):
    if words[i].isdigit():
        numbers = numbers + 1
        sum = sum + int(words[i])
    elif words[i].isalpha():
        count = count + 1
        if words[i].islower():
            lowers = lowers + 1
        elif words[i].isupper():
            uppers = uppers + 1
        elif words[i][0].isupper():
            capitals = capitals + 1
    elif words[i].isalnum():
        count = count + 1
        alnum = alnum + 1
    lengths[len(words[i])] = lengths[len(words[i])] + 1

#soucet slov a cisel
count_all = count + numbers

#vysledek analyzy
print("There are", count_all, "words in the selected text.")
print("There are", capitals, "titlecase words.")
print("There are", uppers, "uppercase words.")
print("There are", lowers, "lowercase words.")
print("There are", numbers, "numeric strings")
print("There are", alnum, "alphanumeric string.")
print("The sum of all numbers is", sum)

#graph


word_lens = list(lengths.items())
print("LEN - OCCURENCES - NR")
for i in range(len(word_lens)):
    print(word_lens[i][0], "-", "*"*word_lens[i][1], "-", word_lens[i][1] )