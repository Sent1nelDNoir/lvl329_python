#https://www.codewars.com/kata/n-th-fibonacci/train/python

def nth_fib(n):
    f1, f2 = 0, 1
    i = 2
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        while i < n:
            f1, f2 = f2, f1 + f2
            i +=1
        return f2
