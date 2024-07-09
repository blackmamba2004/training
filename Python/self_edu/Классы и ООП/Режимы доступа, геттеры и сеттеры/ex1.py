# from accessify import private, protected


class Point:
    def __init__(self, x=None, y=None):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)
    
    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise TypeError('Invalid arguments')

    def get_coord(self):
        return self.__x, self.__y


pt = Point()
pt.set_coord(10, 20)
print(pt.get_coord())
print(dir(pt))
print(pt._Point__x)