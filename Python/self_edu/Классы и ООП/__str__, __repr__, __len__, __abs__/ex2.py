class Point:
    def __init__(self, *args):
        self.coordinates = args

    def __len__(self):
        return len(self.coordinates)

    def __abs__(self):
        return list(map(abs, self.coordinates))


p = Point(1, -2, -5)
print(len(p))
print(abs(p))

