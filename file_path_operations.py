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
