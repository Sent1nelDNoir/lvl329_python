#https://www.codewars.com/kata/simple-pig-latin/train/python		
def pig_it(text):
    words = text.split(' ')
    pig_latin = []
    for word in words:
        if word.isalpha():
            if len(word) > 1:
                pig_latin.append(word[1:]+word[0]+'ay')
            else:
                pig_latin.append(word + 'ay')
        else:
            pig_latin.append(word)
    pig_text = ' '.join(pig_latin)
    return pig_text
	
#https://www.codewars.com/kata/pig-atinlay/train/python

def pig_latin(word):
    return word if len(word) < 4 else word[1:] + word[0] + 'ay'
