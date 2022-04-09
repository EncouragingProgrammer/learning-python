# Getting started with Python 3!
# Following Bill Weinman's LinkedIn Learning course, "Python Essential Training"
# Author Ryan Gustafson

# import modules from the library
import platform

# hello-world
name = 'Ryan'

def main():
    print('Hello, {}'.format(name))     # alternatively:      print(f'Hello, {x}')
    print('How are you doing today?')
    message()

#   Python History
#       Created by Guido van Rossum (Benevolent Dictator for Life - BDFL) in 1989
#       Name inspired by Monty Python
#
#   Python Philosophy (not complete list)
#       Beautiful is better than ugly
#       Explicit is better than implicit
#       Simple is better than complex
#       Complex is better than complicated
#       Readability counts

# Version number variable
version = platform.python_version()

# Display Python Version
def message():
    print('This is python version {}'.format(version))

if __name__ == '__main__': main()

# Looking at blocks and scope
# x = int(input('Please enter a value for x: '))
# y = int(input('Please enter a value for y: '))

# if x < y:
#     z = 1112
#     print('x < y: x is {} and y is {}'.format(x, y))
# elif x == y:
#     z = 112
#     print('x == y: x is {} and y is {}'.format(x, y))
# else:
#     z = 12
#     print('x > y: x is {} and y is {}'.format(x, y))

# Notice that blocks do not define scope in python, z is still defined
# print('z is {}'.format(z))

# Loops
words = ['one', 'two', 'three', 'four', 'five']

n = 0
# while loops
while n < 5:
    print(words[n])
    n += 1

print()
print('Fibonacci numbers!')
a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print()
print()

# For loops
for i in words:
    print(i)

# Functions
def function(n = 1):    # default value of 1
    print(n)
    return n * 2

x = function(47)
print(x)

# Prime numbers function
def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range(100):
        if is_prime(n):
            print(n, end = ' ', flush = True)
    print()

n = 5

if is_prime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')

list_primes()

print()

# classes and objects
class Duck:
    sound = 'Quaaack!'
    walking = 'waddle, waddle!'
    def quack(self):
        print(self.sound)
    
    def walk(self):
        print(self.walking)

donald = Duck()
donald.quack()
donald.walk()