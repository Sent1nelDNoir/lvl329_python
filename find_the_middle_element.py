# https://www.codewars.com/kata/find-the-middle-element

def gimme(input_array):
    number = sorted(input_array)[1]    
    return input_array.index(number)
