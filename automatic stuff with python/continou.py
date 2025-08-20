# continue statements

while True:
    print('who are you')
    name = input()
    if name != 'joe':
        continue
    print('Hello, joe. what is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')