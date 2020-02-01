# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

import time, itertools, sys

start_time = time.time()
init_num = int(sys.argv[1])

for num in itertools.count(init_num):
    if time.time() - start_time < 5:
        print(num)
    else:
        break
