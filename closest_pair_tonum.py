https://www.codewars.com/kata/the-sum-and-the-rest-of-certain-pairs-of-numbers-have-to-be-perfect-squares/train/python


def closest_pair_tonum(upper_lim):
    m = upper_lim-1
    while m > 0:
        for n in range(m-1, 0, -1):
            if ((n + m) ** 0.5) % 1 == 0 and ((m-n) ** 0.5) % 1 == 0:
                return (m, n)
        m -= 1
    return (m, n)
