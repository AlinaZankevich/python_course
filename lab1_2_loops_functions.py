# Инфа отсюда
# http://pythonicway.com/python-functinal-programming


# import numpy
#
# for x in numpy.arange(0.0, 0.6, 0.1):
#     y = 2**x
#     print(y)

# x = 0 # так как нет range, работает без nympy
# while x <= 0.5:
#     y = 2 ** x
#     print(y)
#     x += 0.1

import random
# # ввод
# n = int(input("Введите размер списка:\n"))
# A = []
# for i in range(n):
#     a = random.random()   # генерация случайного числа дробного
#     A.append(a)           # добавление числа в список
# # вывод
# for i in range(n):
#     print(A[i])

# for a in A:  # то же самое
#     print(a)

# n = int(input("Введите размер списка:\n"))
# A = []
# for i in range(n):
#     a = random.randint(1, 9)   # генерация случайного числа целого, включает 1 и 9
#     A.append(a)           # добавление числа в список
# # обработка
# s = sum(A)       # сумма элементов
# l = len(A)       # количество эл
# a = s/l          # среднее ариф элементов



# вывод
#
# mas = [23, 5, 67, -65, 34, 21]
# point = 34
# l = len(mas)
# for i in range(l):
#     if mas[i] == point:
#         print('содержит')
#         break
#     else:
#         print('не содержит')

# Поиск максимального знач в списке
# mas = [4, 5, 9, 90, 4, 43]
# maximum = mas[0]
# for i in range(1,len(mas)):
#     if mas[i] > maximum:
#         maximum = mas[i]
# print(maximum)

# mas = [random.randint(0, 100) for i in range(20)]
# print(mas)
# # нвчиная со второго элемента списка mas[1]  и до предпоследнего сравниваем элементы списка со своими соседями
# for i in range(1, len(mas)-1):
#     if mas[i-1] < mas[i] > mas[i+1]: #выводим индексы подходящих элементов на экран в строку
#         print(i, end=" ")

# Functions Лекция 2

# def person(name, age):
#     print(name, "is", age, "years old")
# person(age=23, name='John')

# def space (planet_name, center="Star"):
#     print(planet_name, "is orbitting a", center)
    #можно вызвать функцию так:
#space("Mars")
    #в результате получим: Mars is orbitting a Star

    #а можно вызвать иначе:
#space("Mars", "Black Hole")
    # в результате получим: Mars is orbitting a Black Hole
    # и еще вызовем
#space("Mercury")
    # Mercury is orbitting a Star


# Аргументы произвольной длины
# def unknown(*args):
#     for argument in args:
#         print(argument)
# unknown("hello", "world") #напечатает оба слова, каждое с новой строкм


#Return

# def bigger(a, b):
#     if a > b:
#         return a
#     return b #незачем использовать else, если мы дошли до жтой строки, то b точно не меньше
# num = bigger(23,42) # мы переменной присвоили вызов функции
# print(bigger(23,42))


#lambda - фунции в Python - это анонимная или несвязная фунция, довольно ограниченная


# f = lambda x: x * x
# print(f(5))
#
# sum = lambda a,b: a+b
# print(sum(2,3))


# import math
#
# def sqroot(x):
#     return math.sqrt(x) #обычная фунция
#
# square_rt = lambda x: math.sqrt(x) # лямбда выражение
# print(sqroot(49))
# print(square_rt(64))

# Рекурсия -фунция вызывает саму себя
# факториал
# def fact(num):
#     if num == 0:
#         return 1 # по договоренности факториал 0 равен 1
#     else:
#         return num * fact(num-1) #возвращаеи результат
#         # произв num и результата возвразенного фунцией
#     #fact(num-1)


# Functional programming has patterns wich we can use
# there are built- in functions:

# Map

# old_list =['1','2','3']
# new_list = list(map(int, old_list))
# print(new_list)

# #или циклом

# old_list =['1','2','3']
# new_list = []
# for item in old_list:
#     new_list.append(int(item))
# print(new_list)

# Функция map применяет функцию к каждому элементу последовательности и возвращает итератор с результатами.
#
# Например, с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:
# Конвертация в числа:
#
# In [3]: list_of_str = ['1', '2', '5', '10']
#
# In [4]: list(map(int, list_of_str))
# Out[4]: [1, 2, 5, 10]


# Лямбда-функция и map
#
# Распространенная операция со списками в Python —
# применение операции к каждому элементу.
#
# map() — это встроенная функция Python,
# принимающая в качестве аргумента функцию и
# последовательность. Она работает так, что применяет
# переданную функцию к каждому элементу.
#
# Предположим, есть список целых чисел, которые
# нужно возвести в квадрат с помощью map.

# L = [1, 2, 3, 4]
# L1 = list(map(lambda x: x**2, L))
# print(L1)

# Filter()

# mixed = ['mak', 'proso', 'mak', 'goroh', 'mak']
# zolushka = list(filter(lambda x: x == 'mak', mixed))
# print(zolushka)

# filter() — это еще одна встроенная функция,
# которая фильтрует последовательность итерируемого
# объекта.
#
# Другими словами, функция filter отфильтровывает
# некоторые элементы итерируемого объекта
# (например, списка) на основе какого-то критерия.
# Критерий определяется за счет передачи функции
# в качестве аргумента. Она же применяется
# к каждому элементу объекта.
#
# Если возвращаемое значение — True, элемент остается.
# В противном случае — отклоняется.
# Определим, например, простую функцию,
# которая возвращает True для четных чисел и False —
# для нечетных:

# def even_fn(x):
#   if x % 2 == 0:
#     return True
#   return False
#
# print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))


#Reduce()
# Функция reduce принимает 2 аргумента:
# функцию и последовательность. reduce()
# последовательно применяет функцию-аргумент к элементам
# списка, возвращает единичное значение.
# Обратите внимание в Python 2.x функция reduce доступна
# как встроенная, в то время, как в Python 3 она была
# перемещена в модуль functools.
# Вычисление суммы всех элементов списка при помощи
# reduce:

# from functools import reduce
#
# items = [1, 2, 3, 4, 5]
# sum_all = reduce(lambda x, y: x + y, items)
#
# print(sum_all)


# Функция zip объединяет в кортежи элементы
# из последовательностей переданных в качестве аргументов.
# a = [1, 2, 3]
# b = "xyz"
# c = (None, True)
#
# res = list(zip(a, b, c))
# print(res)


# libraries: NumPy, SkiPy, Pandas, Matplotlib (график)
# SciKit-Learn








