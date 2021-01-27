

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
        length = ((point1[0] - point1[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
        return length

    def coordinates(self):
        print(self.point1)
        print(self.point2)
        print(self.point3)


t = Triangle([0, 1], [1, 2], [3, 10])
print(t.get_perimeter())
