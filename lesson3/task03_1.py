# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def silent_division(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        return "NaN"


dividend = float(input("Введите делимое: "))
divider = float(input("Введите делитель: "))

print(f'Результат деления - {silent_division(dividend, divider)}')
