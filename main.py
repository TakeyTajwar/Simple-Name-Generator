from random import choice
from random import randint

starter_consonants = ['L', 'C', 'J', 'P', 'D', 'B', 'M', 'El', 'Er', 'Iv']
starter_vowels = "aeiouy"
ending_consonants = ['sh', 'ck', 'm', 'l', 'd', 'ce', 'se']
ending_vowels = "aeiouy"

for _ in range(10):
    print(choice(starter_consonants)+choice(starter_vowels)+choice(ending_consonants)+choice(ending_vowels))

input("Press Enter to exit...")