class Point:
    """Класс, описывающий точку"""
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        print('__setattr__', key, '==', value)
        object.__setattr__(self, key, value)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.z = 5
print(pt1.z)
