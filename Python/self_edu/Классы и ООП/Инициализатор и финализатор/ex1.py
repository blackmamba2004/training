class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра: " + str(self))
    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()