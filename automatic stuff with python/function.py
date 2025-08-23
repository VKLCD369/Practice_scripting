# functions 
"""
def hello():
    print('howdy')
    print('howdy!')
    print('how are you : ')

hello()
hello()
"""
"""

def hello(name):
    print('hello, ' + name)

hello('alice')
hello('bob')
"""

"""
def sayhello(name):
    print('hello, ' + name)

sayhello('al')
"""

def a():
    print('a() starts')
    b()
    c()
    print("a() return")

def b():
    print('b() starts')
    c()
    print("b() returns")

def c():
    print('c() start')
    print('c() returns')
            
def d():
    print('d() starts')
    print('d() returns')

a()

