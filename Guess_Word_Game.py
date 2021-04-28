
"""fun game using Python where you need 
to guess the word based on the hint."""



import random

words = ['apple', 'oracle', 'amazon', 'orange', 'cat', 'dog', 'canada',
         'texas', 'kentucky', 'london']
guessed_word = random.choice(words)
hint = guessed_word[0], guessed_word[-1]

store_guessed_letter = []
attempt = 6
a = input('Enter your name: ')
print('Welcome to the Game world', a)
print('We are going to give you 6 attempts for the guessing')
print('The length of word is', len(guessed_word))

for guess  in range(attempt):
    while True:
        letter = input('Guess the letter: ').lower()
    
        if len(letter) == 1:
            break
        else:
            print('Oops! Please Guess a letter!')
    
    if letter in guessed_word:
        print('Yes!')
        store_guessed_letter.append(letter)
    else:
        print('No!')
    
    if guess == 3:
        print()
        clue_request = input('Would you like a clue? ')
        if clue_request.lower().startswith('y'):
            print()
            print('CLUE: The first and last letter of the word is: ', hint)
        else:
            print('You\'re very confident!')
        
print()
print('''Now Let's see what have you guessed so far. You have guessed: ''',
      len(store_guessed_letter), 'letters correctly.')
print('These letters are:', store_guessed_letter)


word_guess = input('Guess the whole word: ')
if word_guess.lower() == guessed_word:
    print('Congrats! you are correct')
else:
    print('Sorry! The answer was,', guessed_word)

print()
input('Please press Enter to leave the program')
    


