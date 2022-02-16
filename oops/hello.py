from unicodedata import name


class Hello:
    def __init__(self,name):
        self.name = name
        self.age = 10

hello1 = Hello('rohit')

print(hello1.name,hello1.age,sep="----")