class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x, self.y = 0, 0
        if self.validate(x) and self.validate(y):

            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x ** 2 + y ** 2


v = Vector(1, 2)
res = Vector.get_coord(v)
res2 = Vector.norm2(5, 6)
print(res2)
print(Vector.validate(5))
print(res)