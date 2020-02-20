# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NotIntError(Exception):
    def __init__(self, txt):
        self.txt = txt

class IntList(list):
    def append_from_str(self, item):
        if not isinstance(item, str) or not item.isnumeric():
            raise NotIntError("Это не число!")
        super().append(int(item))


print("Заполняем список числами. Для завершения введи stop")
inp = input("Введите число: ")
result = IntList()
while inp != "stop":
    try:
        result.append_from_str(inp)
    except NotIntError as err:
        print(err)
    inp = input("Введите число: ")

print(result)