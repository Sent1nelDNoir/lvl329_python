#https://www.codewars.com/kata/interactive-dictionary/train/python#   

class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        return self.my_dict.get(key, "Can't find entry for {}".format(key))

    def newentry(self, key, value):
        self.my_dict[key] = value 
