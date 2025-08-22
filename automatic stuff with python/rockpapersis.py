# rock paper scissors with python

import random, sys  #import random and sys modules

print('ROCK, PAPER, SCISSORS')

#thes variables keep track of the number of wins losses and ties.
wins = 0
losses = 0
ties = 0

while True: # the main game loop.
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    while True: #the player input loop.
        print('Enter you move: (r)rock (p)paper (s)scissor or (q)quit')
        playermove = input()
        if playermove == 'q':
            sys.exit() #quit the program.
        if playermove == "r" or playermove == 'p' or playermove == 's':
            break #break out of the player input loop.
        print('Type one of r, p, s, or q')

    #display what the player chose:
    if playermove == 'r':
        print('Rock versus...')
    elif playermove == "p":
        print('Paper versus...')
    elif playermove == 's':
        print('Scissors versus...')

    #display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print ('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('scissor')
    
    #display and record the win/loss/tie
    if playermove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playermove == 'r' and computerMove == 's':
        print('you win!')
        wins = wins + 1
    elif playermove == 'p' and computerMove == 'r':
        print('you win!')
        wins = wins + 1
    elif playermove == 's' and computerMove == 'p':
        print('you wins!')
        wins = wins + 1
    elif playermove == 'r' and computerMove == 'p':
        print('you lose!')
        losses = losses + 1
    elif playermove == 'p' and computerMove == 's':
        print('you lose!')
        losses = losses + 1
    elif playermove == "s" and computerMove == 'r':
        print('you lose!')
        losses = losses + 1