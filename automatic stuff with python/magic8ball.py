# return value with return statement in functions

import random

def getanswer(answerNumer):
    if answerNumer == 1:
        return 'it is certain'
    elif answerNumer == 2:
        return 'it is decidedly so'
    elif answerNumer ==3:
        return 'yes'
    elif answerNumer ==4:
        return 'reply hazy try again'
    elif answerNumer == 5:
        return 'ask agin later'
    elif answerNumer == 6:
        return 'concentrate and ask again'
    elif answerNumer == 7:
        return 'my reply is no'
    elif answerNumer == 8:
        return 'outlook not so good'
    elif answerNumer == 9:
        return 'very doubtful'
    
r = random.randint(1,9)
fortune = getanswer(r)
print(fortune)

   