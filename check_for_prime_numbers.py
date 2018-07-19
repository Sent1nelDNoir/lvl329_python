#https://www.codewars.com/kata/check-for-prime-numbers/train/python


import math
def is_prime(n):
  if n < 2:
      return False
  elif n ==2:
     return True
  i = 2
  limit = int(math.sqrt(n))
  while i<=limit:
      if n% i == 0:
         return False
      i += 1
  return True
  
