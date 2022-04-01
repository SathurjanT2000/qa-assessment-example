from math import sqrt, gcd

from pyparsing import alphanums
    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
    
def endsPy(input):
    outcome = 0
    if type(input) is str:
        if input[-2:].lower() == "py":
            outcome = True
        else:
            outcome = False
    else:
        outcome = "Please enter a string" 
    return outcome

    
# <QUESTION 2>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter

# <EXAMPLES>

# one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) → {'apple':3, 'orange':2, 'banana':1}
# one(['tic', 'tac', 'toe']) → {'tic':1, 'tac':1, 'toe':1}
    
def one(items):
    if type(items) is list:
        items_set = set(items) #set only stores unique items
        item_dict = dict() #dict to refer to later
        for i in items_set:
            item_dict[i] = items.count(i) #counts items in the list
        return item_dict
    else: 
        return "Please enter a list"

# <QUESTION 3>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

# <EXAMPLES>

# two(2, 4, '+') → 6
# two(7, 3, '-') → 4
# two(3, 1.5, '*') → 4.5
# two(-5, 2, '/') → -2.5

def two(a, b, operator):
    if type(a) and type(b) is int or float:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b 
        elif operator == '*':
            return a*b
        elif operator == '/':
            return a/b
        else:
            return "please enter the correct operator"
    else:
        return "Please enter integers"
    
# <QUESTION 4>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <EXAMPLES>

# three(7) → 4          # 4 is the square of 2
# three(64) → 64        # 64 is the square of 8 already
# three(32) → 25

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):
    if type(num) is int and num >= 0: 
        sqrt_num = 0
        while sqrt_num == 0:
            if (num**0.5)%1 == 0:
                sqrt_num = (num**0.5)
                return int(sqrt_num)
            else:
                num = num - 1


# <QUESTION 5>

# Given two integers, return the greatest common factor of the two numbers

# <EXAMPLES>

# four(32, 24) → 8
# four(18, 11) → 1
# four(10, 50) → 10

def four(a, b):
    a_factors = []
    b_factors = []
    highest_number = 1
    for i in range(1, a):
        if a%i == 0:
            a_factors.append(i)
    for j in range(1, b):
        if b%j == 0:
            b_factors.append(j)
    for k in a_factors:
        if k in b_factors:
            if k > highest_number:
                highest_number = k
    return highest_number
    


# <QUESTION 6>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

# <EXAMPLES>

# five('wxyz') → 'vwxy'
# five('abc') → 'zab'
# five('aAbB') → 'zZaA'
# five('hello world') → 'gdkkn vnqkc'
# five('54321') → '54321'

def five(string):
    alpabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in string:
        if i in alpabets:
            previous_letter = alpabets[alpabets.index(i)-1]
            string = string.replace(i, previous_letter, 1)
        elif i.upper() in alpabets:
            previous_letter = alpabets[alpabets.index(i.upper())-1]
            string = string.replace(i.lower(), previous_letter.lower(), 1)
    return string


