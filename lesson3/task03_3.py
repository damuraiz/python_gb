# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def my_func(arg1, arg2, arg3):
    args = sorted([arg1, arg2, arg3])
    return args[1] + args[2]


print(my_func(30, 20, 10))
