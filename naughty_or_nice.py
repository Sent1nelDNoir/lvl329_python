#https://www.codewars.com/kata/naughty-or-nice-2/train/python	

def whatListAmIOn(actions):
    naughty = 0
    nice = 0

    for a in actions:
        if a[0] in 'bfk':
            naughty += 1
        elif a[0] in 'gsn':
            nice += 1

    return 'naughty' if naughty >= nice else 'nice'
