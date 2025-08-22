# guess number by python (source code)

import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 to 20.')

#ask the player to guess 6 times.
for guessestaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is to low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break  #this condition is the correct guess!
if guess == secretNumber:
        print('good job!, you guessed my number in ' + str(guessestaken) + ' guesses!')
else:
        print('Nope. the number I was thinking of was' + str(secretNumber))
