"""
projekt_1.py: Textový analyzátor pro Engeto Online Python Akademie
author: Josef Lučan
email: peposh1@seznam.cz
discord: Josef Lučan#98945
"""

# Import potřebných knihoven
import sys
import matplotlib.pyplot as plt
from collections import Counter

# Uživatelská databáze
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

if username not in users or users[username] != password:
    print("Unregistered user, terminating the program..")
    sys.exit()
else:
    print(f"Welcome to the app, {username}")

# Nabídka textů
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

print("We have 3 texts to be analyzed.")
choice = int(input("Enter a number between 1 and 3 to select: "))
if choice not in [1, 2, 3]:
    print("Invalid choice, terminating the program..")
    sys.exit()

selected_text = TEXTS[choice - 1]

# Analýza vybraného textu
words = selected_text.split()
word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper())
lowercase_count = sum(1 for word in words if word.islower())
numbers = [int(word) for word in words if word.isdigit()]
numbers_count = len(numbers)
sum_of_numbers = sum(numbers)

print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numbers_count} numeric strings.")
print(f"The sum of all the numbers is {sum_of_numbers}")

# Grafické zobrazení četnosti délek slov
word_lengths = Counter(len(word) for word in words)
plt.bar(word_lengths.keys(), word_lengths.values())
plt.xlabel('Length of Words')
plt.ylabel('Frequency')
plt.title('Word Lengths in the Selected Text')
plt.show()
