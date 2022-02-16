print("Hello! What is your name?")
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
print("Take a guess.")
k = int(input())

import random
s = random.randint(1, 20)
b = []
def game(k):
    if k != s:
        b.append(1)
        print('Your guess is too low.')
        print('Take a guess.')
        a = int(input())
        return game(a)
    else:
        print('Good job, '+ name +'! You guessed my number in '+ str(len(b) + 1) + ' guesses!')
        
game(k)
