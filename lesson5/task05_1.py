# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task05_1.temp.txt", "w") as f:
    line = input("Введите строку: ")
    while line != "":
        f.write(line + '\n')
        line = input("Введите строку: ")