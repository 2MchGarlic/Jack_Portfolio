import random

# The import is how we are able to have a random choice through the list.

# This is the variable containing the amount of lives available
lives = 9

# this is the secret word list
words = ['pizza','candy','pumpkin','prunes','chocolate','dog','cat','chip']

# This is the random module choice function selecting a word
secret_word = random.choice(words)
clue = list("?" * len(secret_word))
heart_symbol = u'\u2764'
guessed_word_correctly = False
# The variable heart_symbol makes the lives into hearts.
# The variable clue makes it to where you are abel to guess a letter or the whole word if you can.
# The variable secret_word goes into the list and randomly chooses a word

# This helps update the clues to show if a letter was guessed or not
def update_clue(guessed_letter, sectret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

# This is for if you guessed a letter in the secret word correctly or not
while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print('You are incorrect. You will lose a life.')
        lives = lives - 1

# This is for if you have either guessed the secret word correctly or not
if guessed_word_correctly:
    print('Congrats! You won! The secret word is ' + secret_word)
else:
    print('Sorry. You lost. The secret word is ' + secret_word)






        
