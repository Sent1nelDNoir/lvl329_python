# https://www.codewars.com/kata/reversing-words-in-a-string/train/python


def reverse(st):
        rev_words =' '.join (st.split(' ')[::-1]) 
        return rev_words
