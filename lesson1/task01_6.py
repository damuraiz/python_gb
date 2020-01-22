# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

init_distance = float(input('Введите начальный результат: '))
wish_distance = float(input('Введите желаемую дистанцию: '))

# Первое решение что приходит в голову требует логарифмов.
# На уроке их не было, но с другой стороны модуль math был в рекомендованном видеокурсе.
import math
day = int(math.log(wish_distance/init_distance, 1.1))+2
print(f"На {day}-й день спортсмен достиг результата — не менее {wish_distance} км.")

# Второе решение, только на основе материалов урока
day = 1
distance = init_distance
while distance < wish_distance:
    day+=1
    distance *= 1.1
print(f"На {day}-й день спортсмен достиг результата — не менее {wish_distance} км.")




