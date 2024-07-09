class Integer:
    @classmethod
    def verify_coordinates(cls, coord):
        if not isinstance(coord, int):
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):

        self.name = '_' + name

        print(owner, name, self.name)

    def __get__(self, instance, owner):
        print(instance)
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coordinates(value)
        setattr(instance, self.name, value)


class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__, p.x)
