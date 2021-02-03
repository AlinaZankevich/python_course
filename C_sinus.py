
# класс итерируемых объектов,
# которые возвращают генератор вместо итератора
import math
import time


class SinusIterableWithGenerator:
    def __init__(self, steps, width):
        # запоминаем растянутость синусоиды по высоте и ширине
        self.steps = steps
        self.width = width

    # метод получения итератора
    def __iter__(self):
        # локальная переменная внутри метода (не класса)
        # для хранения состояния
        x = 0.0
        # в данном случае - бесконечный цикл,
        # но мог бы быть с условием окончания последовательности
        while True:
            x += math.pi * 2 / self.steps
            length = self.width / 2 + self.width / 2 * math.sin(x) + 1
            # вместо return используется yield
            # для создания генератора - объекта, который
            # сохраняет переменные (х) и логику (цикл while)
            # текущего метода (__iter__); логика выполняется
            # при вызове метода __next__ у созданного генератора;
            # преимущества:
            # 1. не надо писать метод __next__ самим;
            # 2. не надо хранить переменные в классе, дописывая self.
            yield '#' * int(length)


if __name__ == '__main__':
    generator = SinusIterableWithGenerator(64, 32)
    for item in generator:
        print(item)
        time.sleep(0.25)