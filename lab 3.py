# Primer nasledovania

'''class Table:
    def__init__(self, l, w, h):
        self.length = l
        self.width = w
        self.high = h

class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p

class DeskTable(Table):
    def square(self):
        return self.width * self.length

class ComputerTable(DeskTable):
    def square(self,e):
        return self.width * self.length - e

from test import ComputerTable
ct = ComputerTable(2, 1, 1)
ct.square(0.3)'''

#Primer polimorfizma
'''class T1:
    n = 10
    def total(self, N):
        self.total = int(self.n) + int(N)

class T2:
    def total(self,s):
        self.total = len(str(s))

t1 = T1()
t2 = T2()
t1.total(45)
t2.total(45)
print(t1.total)
print(t2.total)

#metod __str__() возвращает строкуб которую будет выводить функция print()

class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __str__(self):
        return str(self.field1)
            return f"{self.field1} {self.field}"

a = A(3, 4)
print(a)'''

#Kvadrat iz simvolov
# class Rectangle:
#     def __init__(self, width, height, sign):
#         self.w = int(width)
#         self.h = int(height)
#         self.s = str(sign)
#
#     def __str__(self):
#         rect = []
#         for i in range(self.h): # kolichestvo strok
#             rect.append(self.s * self.w) #znak povtoriaetsa w raz
#         rect = '\n'.join(rect) #prevrashaem spisok v stroku
#         return rect
# b = Rectangle(10, 5, '*')
# print(b)


'''class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * 3.1415 * self.radius


class Rect:
    def __init__(self, pa, pb):
        self.ma = pa    # pa - это параметр..создали атрибут(ma) по имени ma у обхкета(self) класса Rect
        self.mb = pb
        

    def get_perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rect):
    def __init__(self, size):
        super().__init__(size, size)


# t = Triangle(Point(0, 1), Point(1, 2), Point(3, 10))
c = Circle(5)
r = Rect(3, 7)
sq = Square(4)
..
figures = [c, sq, r]
for f in figures:
    print(f.get_perimeter())'''

# Инкапсуляция
# class B:
#     count = 0
#
#     def __init__(self):
#         B.count += 1
#         self.count_2 = 1
#
#     def __del__(self):
#         B.count -= 1
#
# a = B() # создалa обйукт класса B
# b = B()
# print(B.count)
# del a
# print(B.count)
#
# class B:
#     __count = 0
#
#     def __init__(self):
#         B.__count += 1
#         self.count_2 = 1
#
#     def __del__(self):
#         B.__count -= 1

# a = B()
# print(B.__count)



'''class RegularClass:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

obj1 = RegularClass() # sozdali obect klassa regular class
obj2 = RegularClass()

obj1.increment() # vizvali metod pod nazvaniem increment
obj1.increment()

print(obj1.count)
print(obj2.count)



# a = B() # создалa обйукт класса B
# print(B.count)
# del a
# print(B.count)'''












