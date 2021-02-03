import time


class RangeIterableIterator:
    def __init__(self, size):
        self.x = size

    # раз сам себе итератор - сам себя и возвращает
    def __iter__(self):
        return self

    def __next__(self):
        self.x -= 1
        if self.x <= 0:
            raise StopIteration
        return '#' * self.x

# 8. В файле «B_decrease.py» повторите главную программу
# из файла «A_increase.py» с итерируемым объектом нового
# класса RangeIterableIterator.


if __name__ == '__main__':
    for item in RangeIterableIterator(10):
        print(item)
        time.sleep(0.25)

# 9. Запустите написанную в файле «B_decrease.py» программу,
# полюбуйтесь рисунком в консоли.
#
# 10. Дальнейшим упрощением работы с итерируемыми объектами является
# применение генераторов вместо итераторов. Для работы с генераторами
# создайте новый файл «C_sinus.py».
#
# 11. В файле «C_sinus.py» создайте для бесконечных последовательностей
# строк из решеток длиной, определяемой функцией синус, класс
# SinusIterableWithGenerator, который будет итерируемым объектом,
# возвращающим в методе __iter__ генератор с помощью оператора yield:

# 12. В файле «C_sinus.py» повторите главную программу
# из файла «A_increase.py» с итерируемым объектом нового класса
# SinusIterableWithGenerator.
#
# 13. Запустите написанную в файле «C_sinus.py» программу,
# полюбуйтесь рисунком в консоли.
# Для остановки используйте кнопку с изображением красного квадрата.
#
