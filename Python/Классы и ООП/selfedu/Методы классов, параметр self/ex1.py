class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()
pt2 = Point()
pt.set_coords(1, 2)
pt2.set_coords(2, 3)
print(pt.__dict__)
print(pt2.__dict__)
print(pt.get_coords())
f = getattr(pt, 'get_coords')
print(f())