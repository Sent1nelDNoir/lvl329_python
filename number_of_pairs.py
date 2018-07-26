https://www.codewars.com/kata/pair-of-gloves/train/python

def number_of_pairs(gloves):
    unique = set(gloves)
    return sum(gloves.count(i)//2 for i in unique)
