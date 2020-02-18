# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_number_date(cls, date):
        # просто предполагаю что из условий задачи, экземпляр нам зачем-то нужен
        return tuple(map(int, cls(date).date.split('-')))

    @staticmethod
    def validate_date(date):
        date_tuple = Date.get_number_date(date)
        #не стал проверять дату на 30дневные месяцы, особенности февраля и високосных годов
        if date_tuple[0] < 1 or date_tuple[0] > 31:
            print("неправильное число")
        elif date_tuple[1] < 1 or date_tuple[1] > 12:
            print("неправильный месяц")
        else:
            print("все хорошо")


print(Date.get_number_date('10-04-1985'))
Date.validate_date('10-04-1985')
Date.validate_date('10-30-1985')
Date.validate_date('50-30-1985')
