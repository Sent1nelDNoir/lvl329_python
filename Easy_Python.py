# https://www.codewars.com/kata/will-you-make-it/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump<=(mpg * fuel_left):
        return (True)  
    return (False)  
	
#https://www.codewars.com/kata/interactive-dictionary/train/python#   

class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        return self.my_dict.get(key, "Can't find entry for {}".format(key))

    def newentry(self, key, value):
        self.my_dict[key] = value 
		
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
	
#https://www.codewars.com/kata/smart-traffic-lights/train/python


class SmartTrafficLight():
    def __init__(self, st1, st2):
        self.st1 =  st1
        self.st2 = st2 
        
    def turngreen(self):
        if self.st1[0] < self.st2[0]:
            self.st2[0] = 0
            return self.st2[1]
        elif self.st2[0] < self.st1[0]:
            self.st1[0] = 0
            return self.st1[1]
			
# https://www.codewars.com/kata/reversing-words-in-a-string/train/python


def reverse(st):
        rev_words =' '.join (st.split(' ')[::-1]) 
        return rev_words
		
		
#https://www.codewars.com/kata/file-path-operations/train/python


class FileMaster():
    def __init__(self, filepath):
        self.path = filepath

    def extension(self):
        return self.path.split('.')[-1]

    def filename(self):
        return self.path.rsplit('/',1)[-1].split('.')[0]

    def dirpath(self):
        return self.path.rsplit('/', 1)[0] + '/'
		
#https://www.codewars.com/kata/how-much-will-you-spend		
def get_total(costs, items, tax):
    return round(sum(costs.get(item, 0) for item in items) * (1 + tax), 2)
	
#https://www.codewars.com/kata/noob-debug-1-fix-the-string-sum/train/python

def add(s1, s2):
    return sum(ord(x) for x in s1+s2)
	
	
#https://www.codewars.com/kata/make-a-square-box/train/python	

		
def box(n):
    side = ["-" * n]
    side += ["-" + (' '*(n-2)) + "-"] * (n-2)
    side += ["-" * n]
  return side
  
  #https://www.codewars.com/kata/21-sticks/train/python


def makeMove(sticks):
    print(sticks)
    return sticks % 4 if sticks % 4 != 0 else 1
	
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
	
#https://www.codewars.com/kata/alien-accent/train/python


from string import maketrans
def convert(st):
    in_str = "ao"
    out_str = "ou"
    convert_str = maketrans(in_str, out_str)
    return st.translate(convert_str)

	
#https://www.codewars.com/kata/will-there-be-enough-space/train/python


def enough(cap, on, wait):
    pas = cap - on
    if wait < pas:
        return 0
    else:
        return wait - pas
		
#https://www.codewars.com/kata/no-yelling/train/python   
 

def filter_words(st):
    st = st.split()
    st = " ".join(st)
    st = st.capitalize()
    return st
	
# https://www.codewars.com/kata/esolang-minibitmove/train/python

def interpreter(tape, array):
    if '0' not in tape:
        return
    
    i, j = 0, 0
    array = list(array)
    while i < len(array):
        if tape[j] == '1':
            array[i] = '0' if array[i] == '1' else '1'
        else:
            i += 1
        j = (j + 1) % len(tape)
    return ''.join(array)
	
	
#https://www.codewars.com/kata/plotting-points-on-a-grid/train/python

class Grid:

    def __fill_grid(self):
        self.grid = "\n".join(list(("".join(str(el) for el in line) for line in self.matrix)))

    def __init__(self, width, height):
        self.matrix = [[0] * width for _ in range(height)]
        self.__fill_grid()

    def plot_point(self, x, y):
        self.matrix[y - 1][x - 1] = 'X'
        self.__fill_grid()

    def __repr__(self):
        return self.grid
		
#https://www.codewars.com/kata/string-templates-bug-fixing-number-5/train/python


def build_string(*args):
    return "I like {}!".format(", ".join(args))
    
		
# https://www.codewars.com/kata/the-modulo-3-sequence

def sequence(n):
    if n == 1: 
	    return 0
    n1, n2 = 0, 1
    n = (n-2) % 8
    for i in range(n):
        n1, n2 = n2, (n1+n2)%3
    return n2
	
	
#https://www.codewars.com/kata/esolang-tick/train/python	
from collections import defaultdict
def interpreter(tape):
    memory, potr, res = defaultdict(int), 0, []
    for cmd in tape:
        if cmd == '+':
            memory[potr] += 1
        elif cmd == '*':
            res.append(chr(memory[potr] % 256))
        elif cmd == '>':
            potr += 1
        elif cmd == '<':
            potr -= 1
    return ''.join(res)
	
# https://www.codewars.com/kata/which-are-in/train/python


def in_array(array1, array2):
    sort_ar = []
    for a in array1:
        for b in array2:
            if a in b and not a in sort_ar:
                sort_ar.append(a)
    sort_ar.sort()
    return sort_ar
	
	
#https://www.codewars.com/kata/simple-find-the-distance-between-two-points/train/python	
import math 
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return round(dist, 2)
	

