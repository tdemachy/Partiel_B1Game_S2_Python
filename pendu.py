# Resolution du pendu en pyhton
import random

img_file = open("pendu.txt", "r")
pendu = img_file.read().split(';')
img_file.close()

words_files = open("dict.txt", "r")
words =  words_files.read().split()
words_files.close()

nb_tries = len(pendu)
nb_errors = 0
nb_resolved = 0
game_won = False
game_lost = False

word = words[random.randrange(0,len(words))]
original_word = word # Word is destroyed in process

resolution  = ['_'] * len(word)
letters_played = ''

while not game_won and not game_lost:
    print (' '.join(resolution))
    letter = ''
    while len(letter) == 0:
        print("? ",  end='')
        letter = input()
        if len(letter) > 0 :
            letter = letter.upper()[0]
            if letter < 'A' or letter > 'Z' or letters_played.find(letter) >= 0: 
                letter = ''

    # Find and replace all occurences
    letters_played += letter
    idx = word.find(letter)
    if idx >= 0:
        while idx >= 0:
            word = word.replace(letter, '#', 1) # replace one
            resolution[idx] = letter
            idx = word.find(letter)
            nb_resolved += 1
            if nb_resolved >= len(word):
                game_won = True           
    else:
        print(pendu[nb_errors])
        nb_errors += 1
        if nb_errors >= nb_tries:
            game_lost = True

if (game_won):
    print (f"PARTIE GAGNEE AVEC {nb_errors} ERREURS. FEREZ VOUS MIEUX LA PROCHIANE FOIS ?")

if (game_lost):
    print (f"PARTIE PERDUE. LE MOT ETAIT '{original_word}' RECOMMENCEZ POUR UNE MEILLEURE CHANCE !")