https://www.codewars.com/kata/interactive-dictionary/train/python

class Dictionary():
    def __init__(self):
        self.main_dict = {}
        
    def newentry(self, word, definition):
        self.main_dict[word] = definition
        
    def look(self, key):
        return self.main_dict.get(key, "Can't find entry for {}".format(key))
