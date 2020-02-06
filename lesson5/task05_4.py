# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

en_ru = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def translate(line, dictionary=en_ru):
    for word_en, word_ru in dictionary.items():
        line = line.replace(word_en, word_ru)
    return line


with open("task05_4.txt") as in_f:
    lines = in_f.readlines()
    with open("task05_4.temp.txt", "w") as out_f:
        for line in lines:
            print(translate(line), file=out_f, end='')
