#https://www.codewars.com/kata/first-n-prime-numbers/train/python

import math
class Primes():
    def __init__(self):
        self.out = [2,3]
    def first(self,n):
        print(n)
        if n < (len(self.out)):
            return(self.out[0:n])
        if n == 1:
            return ([2])
        count,test = len(self.out),self.out[-1]
        while count < n:
            test += 2
            x = 0
            while x+1 < len(self.out) and test % self.out[x] != 0 and self.out[x] < math.sqrt(test):
                x += 1
            if test % self.out[x] != 0:
                count += 1
                self.out.append(test)
        #print(out)
        return self.out
Primes = Primes()
