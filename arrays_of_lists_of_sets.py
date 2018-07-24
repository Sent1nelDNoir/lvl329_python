# https://www.codewars.com/kata/arrays-of-lists-of-sets/train/python


def solve(arr):
    arr = [set(x) for x in arr]
    c = [arr.index(y) for y in arr]
    res = []
    for x in range(len(c)):
        if c.count(x) >= 2:
            res += [sum([ind for ind, y in enumerate(c) if y == x])]
    return sorted(res)
    
