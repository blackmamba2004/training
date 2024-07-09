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

    def __getattr__(self, item):
        return False


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.yy)
