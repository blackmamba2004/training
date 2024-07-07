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

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item == 'x':
            raise AttributeError('Доступ закрыт')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Нельзя обратиться к данному атрибуту')
        return super().__setattr__(self, key, value)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)

# a = pt1.x
# print(a)
