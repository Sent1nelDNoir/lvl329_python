# https://www.codewars.com/kata/the-modulo-3-sequence

def sequence(n):
    if n == 1: 
	    return 0
    n1, n2 = 0, 1
    n = (n-2) % 8
    for i in range(n):
        n1, n2 = n2, (n1+n2)%3
    return n2
