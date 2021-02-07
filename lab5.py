#Exeptions
# x = int(input())
# y = int(input())
#
# try:
#     result = x/y
# except ZeroDivisionError:
#     print("Вы ввели 0")
#     res = 0
# print(result)

# Unit testing

def calc_add(a, b):
    return a + b

# import calc  - импорт файл с предыдущими функциями

def test_add():
    if calc.add(1, 2) == 3:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is Fail")

test_add()



