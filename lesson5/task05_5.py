# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random as r

with open("task05_5.temp.txt", "w+") as f:
    text = " ".join([str(r.randint(0, 9)) for _ in range(r.randint(1, 10))])
    print(text, file=f)
    f.seek(0)
    text = f.read()
    numbers = [int(num) for num in text.split()]
    print(f"Среднее значение - {sum(numbers)/len(numbers)}")




