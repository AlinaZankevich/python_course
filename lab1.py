
def task1():
    # Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.

    n = int(input("Type in 'n' "))
    m = int(input("Type in 'm' "))
    p = int(input("Type in 'p' "))
    neg_count = 0
    list_num = [n, m, p]
    for num in list_num:
        if num < 0:
            neg_count += 1
    print(neg_count)


def task2():
    def ticket_is_lucky(ticket):
        sum_of_num = 0
        for num in str(ticket):
            sum_of_num += int(num)
        if sum_of_num % 7 == 0:
            return True
        else:
            return False

    first_ticket = 100000
    last_ticket = 999999
    for ticket in range(first_ticket, last_ticket + 1):
        if ticket_is_lucky(ticket) and ticket_is_lucky(ticket + 1):
            print(f'{ticket} and {ticket + 1} are lucky')


task2()

