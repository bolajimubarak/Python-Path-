import random
from hangman_words import word_list
from hangman_art import logo, stages

# Random word selection from list of words
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
print(logo)
#print(chosen_word)

# a list the dashes of the same length as the chosen word
show = []
for _ in range(word_len):
    show += '_'


live_count = 6      # Declaration of number of maximum guesses 
game_over = False

while not game_over:
    letter_guess = input('Please input your guess: ').lower()

    # If the letter has been guessed 
    if letter_guess in show:
        print('Letter already exist')

    # Determining the position of the rightly guessed letter and repalcing the dashes with the guessed letters 
    for place in range(word_len):
        letter = chosen_word[place]
        if letter == letter_guess:
           show[place] = letter
    
    # Chance reduction for the wrong guesses
    if letter_guess not in chosen_word:
        print(f'Wrong guess, {letter_guess} is not in the chosen word.')
        live_count -= 1
        print(stages[live_count])
        if live_count == 0:
            game_over = True
            print('Game over')

    print(f"{''. join(show)}")

    # Determinating the game after seccessful guesses 
    if '_' not in show:
        game_over = True
        print('Great job. You win!')