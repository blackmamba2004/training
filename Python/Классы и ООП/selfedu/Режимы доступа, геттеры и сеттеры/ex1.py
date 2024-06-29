class Point:
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise TypeError('Invalid arguments')

    def get_coord(self):
        return self.__x, self.__y


pt = Point()
print(pt.__dict__)
print(Point.__dict__)
pt.set_coord(10, 20)
print(pt.get_coord())
