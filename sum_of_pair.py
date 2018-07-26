https://www.codewars.com/kata/sum-of-pairs/train/python

def sum_pairs(ints, s):
    nums = set()
    for i in ints:
        if s - i in nums:
            return [s - i, i]
        nums.add(i)
