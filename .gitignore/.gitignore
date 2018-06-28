def nb_year(p0, percent, aug, p, year_p=0):
    if (p0 >= p):
        return year_p
    else:
        year_p += 1
        p0 = p0 + p0 * (percent / 100) + aug;
        return nb_year(p0, percent, aug, p, year_p)

def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)


def digitize(n):
    return [int(digit) for digit in str(n)][::-1]


def always(n=0):
    return lambda: n


def sum_array(a):
    return sum(a)


def multiply(a, b):
    return a * b

def get_size(w,h,d):
    a = []
    a.append( 2 * h * w + 2 * w * d + 2 * d * h)
    a.append (w * h * d)
    return a
