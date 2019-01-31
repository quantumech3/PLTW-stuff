# -*- coding: utf-8 -*-

"""
Author: Scott Burgert
Contact me at: https://github.com/quantumech3/
Date written: 1/31/2019
PLTW lesson 1.3.6

Project name: roll_two_dice
Purpose: 
   Simulates the rolling of 2 six sided dice and outputs the sum of their values as an integer.
"""

from random import randint

def roll_two_dice():
    dice1 = randint(1, 6) #Computing each dice instead of generating a number from 2-12 beccause...
    dice2 = randint(1, 6) #...the requirements are to 'simulate' the die, not just calculate the sum.

    return dice1 + dice2