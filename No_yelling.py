#https://www.codewars.com/kata/no-yelling/train/python   
 

def filter_words(st):
    st = st.split()
    st = " ".join(st)
    st = st.capitalize()
    return st
