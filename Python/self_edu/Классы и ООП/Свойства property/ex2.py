class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('Symon', 20)
p.__dict__['old'] = 'old object'
p.old = 35
del p.old
print(p.old, p.__dict__)