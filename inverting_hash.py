https://www.codewars.com/kata/inverting-a-hash/train/python

def invert_hash(dictionary):
    return {dictionary[key]:key for key in dictionary.keys()}
