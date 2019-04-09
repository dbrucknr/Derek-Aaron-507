import random #this imports random module
import json #this imports json module

def num_vowels(phrase): #these lines create a new function num_vowels, which takes a string as an argument
    count = 0 #this starts an accumulator for the function
    vowels = ['a','e','i','o','u'] #this is a list of vowels for an accumulator
    for character in phrase:
        if character in vowels:
            count = count + 1
    return count #this returns the total count of vowels

#print(num_vowels('aaron'))
