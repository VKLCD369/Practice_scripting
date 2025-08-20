# This program says hello and asks for my name

print('Hello!') #print function out the string
print('what is your name? ') #ask for their name

myname = input() #variable input
print('It is good to meet you, ' + myname)
print(f"Length of your name: " + str(len(myname)))
print('what is your age? ') #ask for their age
myage = input()
print('you will be ' + str(int(myage) + 1) + ' in a year.')
