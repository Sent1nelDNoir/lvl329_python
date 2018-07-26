https://www.codewars.com/kata/range-extraction/train/python


def solution(args):
    result = ''
    i = 0
    while i < len(args[:-1]):
        result += str(args[i])
        next = i + 1
        if args[next] == args[i] + 1:
            while next < len(args) - 1 and args[next] + 1 == args[next + 1]:
                next += 1
            if next >= i + 2:
                result += '- {},'.format(str(args[next]))
                i = next
            else:
                result += ','
        else:
            result += ','
        i += 1
        
    if i < len(args):
        result += str(args[-1])
        return result
    else:
        return result[:-1]
