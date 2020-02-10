# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position):
        self.name, self.surname, self.position = name, surname, position
        self._income = {"wage": 0, "bonus": 0}

    def set_wage(self, wage):
        self._income["wage"] = wage

    def set_bonus(self, bonus):
        self._income["bonus"] = bonus

    def get_income(self):
        return self._income

class Position(Worker):
    def __init__(self, name, surname, position, wage=0, bonus=0):
        super().__init__(name, surname, position)
        self.set_bonus(bonus)
        self.set_wage(wage)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return 12*self.get_income()["wage"]+self.get_income()["bonus"]

ceo = Position(name="Dam", surname="Yun", position="CEO", wage=300, bonus=600)
head_dev = Position(name="Alex", surname="Bel", position="Department of Development")
head_dev.set_wage(200)
head_dev.set_bonus(400)
developer = Position("Ed", "Sady", "Senior Developer")
developer.set_wage(150)

print(f'{ceo.get_full_name()} total year income - {ceo.get_total_income()}')
print(f'{head_dev.get_full_name()} total year income - {head_dev.get_total_income()}')
print(f'{developer.get_full_name()} total year income - {developer.get_total_income()}')

