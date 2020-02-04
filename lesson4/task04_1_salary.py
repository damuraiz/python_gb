# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys


def get_salary(hours, rate, bonus=0):
    return hours * rate + bonus


if __name__ == "__main__":
    working_hours = float(sys.argv[1])
    salary_rate = float(sys.argv[2])
    try:
        bonus = float(sys.argv[3])
        print(get_salary(hours=working_hours, rate=salary_rate, bonus=bonus))
    except IndexError:
        print(get_salary(hours=working_hours, rate=salary_rate))
