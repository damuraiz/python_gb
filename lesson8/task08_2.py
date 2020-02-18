# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):

    def __init__(self, text):
        self.text = text




def div(num_1, num_2):
    try:
        print(f'trying to divide {num_1} to {num_2}')
        if num_2 == 0:
            raise MyZeroDivisionError("Не хорошо пытаться делить на 0")
        else:
             print(f'Результат - {num_1/num_2}')
    except MyZeroDivisionError as err:
        print(err)


div(10, 10)
div(10, 0)
