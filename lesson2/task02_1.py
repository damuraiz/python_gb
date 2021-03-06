# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 1.0, complex(0, 1), "1", [1], (1, 1), {1}, {1: 1},
           True, b'1', bytearray(b'1'), None, ValueError(), print, range(1)]

for value in my_list:
    print(f"Элемент {value} имеет тип - {type(value)}")
