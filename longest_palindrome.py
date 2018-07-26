https://www.codewars.com/kata/longest-palindrome/train/python


def longest_palindrome(s):
    if len(s) == 1 or s == '':
        return len(s) 
    else:
        if s == s[::-1]:
            return len(s)
        else:
            for i in range(len(s)-1, 0, -1):
                for j in range(len(s)-i+1):
                    poly = s[j:j+i]
                    if poly == poly[::-1]:
                        return len(poly)
