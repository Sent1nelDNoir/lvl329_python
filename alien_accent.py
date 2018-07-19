#https://www.codewars.com/kata/alien-accent/train/python


from string import maketrans
def convert(st):
    in_str = "ao"
    out_str = "ou"
    convert_str = maketrans(in_str, out_str)
    return st.translate(convert_str)
