# https://www.codewars.com/kata/will-you-make-it/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump<=(mpg * fuel_left):
        return (True)  
    return (False)    
	
#https://www.codewars.com/kata/jennys-secret-message

name = input("enter name")
if name == "John":
    print ("Welcome John Snow")
elif  name == "Alice":
    print ("Goodbay, Alice")
elif name == "Jane":
    print("How are you doing, Jane?")
else:
    print("Not authorized")
	
#https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

def bool_to_word(bool):
     if bool:
         return "Yes"
     return "No"
	 
#https://www.codewars.com/kata/are-you-playing-banjo

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#https://www.codewars.com/kata/counting-sheep-dot-dot-dot

def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
  
#https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits

def digitize(n):
    return [int(digit) for digit in str(n)][::-1]
	
#https://www.codewars.com/kata/a-needle-in-the-haystack/train/python

def find_needle(haystack):
    for word in haystack:
        if word == 'needle':
            return "found the needle at position " + str(haystack.index('needle'))
			
#https://www.codewars.com/kata/a-function-within-a-function

def always(n=0):
    return lambda: n
	
#https://www.codewars.com/kata/sum-arrays

def sum_array(a):
    return sum(a)
	
#https://www.codewars.com/kata/multiply

def multiply(a, b):
    return a * b
	
#https://www.codewars.com/kata/surface-area-and-volume-of-a-box

def get_size(w,h,d):
    a = []
    a.append( 2 * h * w + 2 * w * d + 2 * d * h)
    a.append (w * h * d)
    return a

	
#https://www.codewars.com/kata/rock-paper-scissors


#https://www.codewars.com/kata/formatting-decimal-places-number-0/train/python


def two_decimal_places(n):
    num = round (n, 4)
    n1 = str(num)
    if n1[-1] == '5':
        n1 = n1[:-1] + '6'
        return round(float((n1)),2)
      
    else:
        return round(n,2) 
		
#https://www.codewars.com/kata/formatting-decimal-places-number-1/train/python


def two_decimal_places(number):
    a = round (number, 4)
    a1 = str(a)
    if a1[-4] == '.':
        return float((a1)[:-1])
    else:
        a = round (number, 4)
        a2 = a1[:-2]
        return float(a2)
		
#https://www.codewars.com/kata/stringy-strings

def stringy(size):
    if size == 0:
        return ''
    elif (size == 1):
        return "1"
    elif (size == 2):
        return "10"
    elif (size % 2 == 0):
        return "10" * (size / 2)
    else:
        return ("10" * ((size  - 1) / 2) + "1")
		
#https://www.codewars.com/kata/find-count-of-most-frequent-item-in-an-array/train/python

def most_frequent_item_count(collection):
    s = 1
    if collection == []:
        return 0 
    elif len(collection)== 1:
            return 1
    else:    
        for  i in collection:
            if s < collection.count(i):
                s = collection.count(i)
    return s
	
	
#https://www.codewars.com/kata/the-if-function/train/python

def _if(bool, func1, func2):
    func1() if bool else func2()


def truthy():
    print('True')


def falsey():
    print('False')

#https://www.codewars.com/kata/dollars-and-cents/train/python

def format_money(amount):
     return "${:.2f}".format(amount)
	 
	 
#https://www.codewars.com/kata/is-it-a-number/train/python

def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False
		

#https://www.codewars.com/kata/get-planet-name-by-id/train/python


def get_planet_name(id_):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id_, None)
	
#https://www.codewars.com/kata/unfinished-loop-bug-fixing-number-1/train/python

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
        if i != 1:
            continue
    return res
	
#https://www.codewars.com/kata/grasshopper-debug/train/python

def weather_info(temp):
    celsius = (temp - 32) * (5 / 9.0)
    if celsius > 0:
        return '{} is above freezing temperature'.format(celsius)
    return '{} is freezing temperature'.format(celsius)	
	
#https://www.codewars.com/kata/unexpected-parsing/train/python

def get_status(is_busy):
    return {"status": "busy" if is_busy else "available"}
	
	
# https://www.codewars.com/kata/squash-the-bugs/train/python

def find_longest(string):
    return max(len(a) for a in string.split())
	
#https://www.codewars.com/kata/is-this-my-tail/python

def correct_tail(body, tail):
    return body[-1] == tail	
	
#https://www.codewars.com/kata/grasshopper-combine-strings

def combine_names(first, last):
    return first + " " + last
	
#https://www.codewars.com/kata/grasshopper-if-slash-else-syntax-debug

def checkAlive(health):
    if(health > 0):
        return True
    else:
        return False
		
#https://www.codewars.com/kata/grasshopper-grade-book/train/python

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    return 'F'
	
#https://www.codewars.com/kata/comfortable-words/train/python

def comfortable_word(word):
    Left = "qwertasdfgzxcvb"
    Right = "yuiophjklnm"
    last = None
    for l in word:
        if l in Left:
            if last == "L": return False
            last = "L"
        elif l in Right:
            if last == "R": return False
            last = "R"
    return True	

	

