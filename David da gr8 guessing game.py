# -*- coding: utf-8 -*-
"""
Chaoyi (David) Zhu

"""
# Function checking if you're right
def validate (x,n):
    if x == n:
        print ("Congratulations it's correct!")
    elif x < n:
        print ("Too small!")
    else:
        print ("Too large!")

import random
truth = random.randint(0,100)

print("Welcome to the game. You have 10 attempts to guess the score, which would between 0 and 100.")
i = 1
while i<=10:
    x = int(input('Guess how high your user scored: '))
    validate (x,truth)
    if x == truth:
        break
    print ("Lives left: ", 10-i)
    i = i+1

if i==11:
    print('Game over!')
    print('The truth score is: ', truth)