# class A:
#     pass
#
#
# obj_a = A()  # создаем объект класса А
#
#
# obj_a.hello = "world"  # создаем атрибут hello со значением world.
# Отличие от переменной только в том, что то, что идет после точки(атрибут) присобачен
# к обьекту obj_a
# print(obj_a.hello)
#
#
# obj_aa = A()
# print(obj_aa.hello)

class User:
    def __init__(self, i):
        self.id = i
        self.first_name = f"Alina_{i}"
        self.last_name = "Zankevich"
        self.age = None

    def print_user(self):
        print('+-------------+')
        print(f'id: {self.id}')
        print(f'first name: {self.first_name}')
        print(f'last name: {self.last_name}')
        if self.age:
            print(f'age: {self.age}')
        print('+-------------+')

    def set_age(self, age):
        self.age = age


user = User(0)
user.set_age(42)
user.print_user()

user2 = User(0)
user2.set_age(11)
user2.print_user()

# all_users_list = []
# for i in range(10):
#
#     a = User(i)
#
#     all_users_list.append(a)  # добавляются объекты со своими атрибутами
#
#
# all_users_list[2].age = 34
# all_users_list[2].print_user()

