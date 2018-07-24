# https://www.codewars.com/kata/dictionary-of-factors/train/python

def factorsRange(n, m):
    d = dict()
    for i in range(n,m+1):
        d[i] = []
        for x in range(2, i):
            if i%x == 0:
                d[i].append(x)
        if len(d[i]) == 0:
            d[i] = ['None']
    return d
