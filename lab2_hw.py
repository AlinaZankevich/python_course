def select_sort(A):
    N = len(A)
    for i in range(N - 1):
        m = i
        for j in range(i, N):
            if A[j] < A[m]:
                m = j
        A[m], A[i] = A[i], A[m]


# a = [3, 1, 0, 7, 9, 12]
# select_sort(a)

#  1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на
# каждом этапе стороной. Выведите длины ребер получаемых квадратов и кол-
# во полученных квадратов.

def slice_rect(a, b):
    if a > b:
        long_side = a
        short_side = b
    else:
        long_side = b
        short_side = a

    square_count = long_side // short_side
    print(f'{square_count} squares of size {short_side}')

    reminder = long_side - square_count * short_side
    if reminder != 0:
        slice_rect(reminder, short_side)

slice_rect(139, 7)
