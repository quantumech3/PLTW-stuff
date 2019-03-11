# -*- coding: utf-8 -*-

"""
Author: Scott Burgert
Contact me at: https://github.com/quantumech3/
Date written: 1/31/2019

Project name: guess_letter
Purpose: 
   Generates and returns a random letter of the alphabet as a character object
"""

from random import choice

def guess_letter():
	#print(tuple(chr(i) for i in range(65, 90))) Only chumps type in every letter...
	#...the alphabet by hand MUAHAHAHAHA!
	alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y')

	return choice(alphabet)