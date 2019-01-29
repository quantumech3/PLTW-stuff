from __future__ import print_function # must be first in file
import random

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
        returns True if good, returns False and prints error if not
        good
        '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')

    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()')
        # Add tests so that all lines of code are visited during test

    if food_id('potato') != 'Starchy, NOT Fruit':
        works = False
        print("potato bug found in food_id()")

    if food_id('carrot') != 'NOT Starchy, NOT Fruit':
        works = False
        print("carrot bug found in food_id()")

    if works:
        print('food_id passed all tests')
        return works

#PLTW told us to make a function 'f(x)' but its flowchart refers to the variable being tested as 'n'.
#I am going to choose to interpret that as the following code.
def f(x):
    if int(x) == x:
        if x % 2 == 0:
            if x % 3 == 0:
                print("x is a multiple of 6")
            else:
                print("x is even")
        else:
            print("x is odd")

    else:
        print("x is not an integer")

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(input('Guess: '))
    if guess < secret:
        print("Too low - my number was", secret, '!')
    elif guess > secret:
        print("Too high - my number was", secret, '!')
    else:
        print('Right, my number is', guess, '!')

def quiz_decimal(low, high):
    userInput = float(input("Type a number between " + str(low) + " and " + str(high)))

    if userInput > high:
        print("No, ", userInput, "is too high!")
    elif userInput < low:
        print("No,", userInput, "is too low!")
    else:
        print("Good!", low, '<', userInput, '<', high)
