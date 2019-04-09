import random

def num_vowels(phrase):
    count = 0
    vowels = ['a','e','i','o','u']
    for character in phrase:
        if character in vowels:
            count = count + 1
            if count > 2:
                truth_value =  True
            else:
                truth_value = False
    return truth_value

print(num_vowels('aaron'))
