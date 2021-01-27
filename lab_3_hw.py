
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def get_perimeter(self):
        return (self.get_length(self.point1, self.point2) +
                self.get_length(self.point2, self.point3) +
                self.get_length(self.point1, self.point3))

    def get_length(self, point1, point2):
        length = ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
        return length

    def coordinates(self):
        print(self.point1.x, self.point1.y)
        print(self.point2.x, self.point2.y)
        print(self.point3.x, self.point3.y)


t = Triangle(Point(0, 1), Point(1, 2), Point(3, 10))
print(t.get_perimeter())
