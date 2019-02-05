# -*- coding: utf-8 -*-

"""
Author: Scott Burgert
Contact me at: https://github.com/quantumech3/
Date written: 2/5/2019

Project name: PLTW 1.3.7
Purpose: 
   Code written for section 1.3.7 of PLTW
"""

import matplotlib.pyplot as plt
from random import randint


def roll_hundred_pair():
    '''
    Displays a histogram showing the all the values resulting from 100 rolls of a 6 sided dice.

    :returns: None
    '''

    results = [randint(1, 6) for i in range(100)]  # Generate results from 100 dice rolls

    # Display results on histogram
    plt.hist(results)
    plt.show()


def dice(n=0):
    '''
    Rolls 'n' dice and returns the sum of their values
    :param n: Int: Amount of dice to roll
    :return: Int
    '''

    dice_sum = 0
    for i in range(n):
        dice_sum += randint(1, 6)

    return dice_sum


def hangman_display(guessed="", secret=""):
    '''
    Returns the string a hangman player would see.

    :param guessed: Str
    :param secret: Str
    :return: Str
    '''

    hangStr = ''

    for i in secret:
        if i in guessed:
            hangStr += i
        else:
            hangStr += '-'

    return hangStr


def matches(ticket, winner):
    '''
    Returns an integer that says how many numbers the two lists have in common.

    :param ticket:
    :param winner:
    :return:
    '''

    accm = 0
    for i in ticket:
        if i in winner:
            accm += 1

    return accm


def report(guess, secret):
    '''
    Takes two lists and returns a 2-element list [number_right_ place, number_wrong_place].

    :param guess:
    :param secret:
    :return: list
    '''

    duo_accm = [0, 0]

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            duo_accm[0] += 1
            secret[i] = ''
        elif guess[i] in secret:
            duo_accm[1] += 1
            secret[secret.index(guess[i])] = '' 

    return duo_accm

guess = ['red', 'red', 'red', 'green', 'yellow']
secret = ['red', 'red', 'yellow', 'yellow', 'black']
print(report(guess, secret)) # 2 in place, 1 out of place
