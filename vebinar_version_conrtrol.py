class Point:
    # points = []

    # def __new__(cls, *args, **kwargs):
    #     print(1)
    #     point = super().__new__(cls)
    #     cls.points.append(point)
    #     return point

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])

    def __radd__(self, other):
        print(1)
        return self.__add__(other)

    def __iadd__(self, other):
        print(1)
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1.x, p1.y, p1)
print(p2)
# print(Point.points)
print((1, 2) + p1)
p1 += p2
print(p1)


class A:
    def __str__(self):
        return "A"

    def __repr__(self):
        return "A"


print(A())
print([A()])