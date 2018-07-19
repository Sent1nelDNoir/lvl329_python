#https://www.codewars.com/kata/make-a-square-box/train/python	

		
def box(n):
    side = ["-" * n]
    side += ["-" + (' '*(n-2)) + "-"] * (n-2)
    side += ["-" * n]
  return side
