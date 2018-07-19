#https://www.codewars.com/kata/will-there-be-enough-space/train/python


def enough(cap, on, wait):
    pas = cap - on
    if wait < pas:
        return 0
    else:
        return wait - pas
