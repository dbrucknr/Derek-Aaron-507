import random

def num_vowels(phrase):
    count = 0
    vowels = ['a','e','i','o','u']
    for character in phrase:
        if character in vowels:
            count = count + 1
    return count

#print(num_vowels('aaron'))
