# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, color = "white", name="noname"):
        self.speed=0
        self.color=color
        self.name=name
        self.is_police=False

    def show_speed(self):
        print(f'{self.name} - текущая скорость - {self.speed} км/ч')

    def go(self, speed):
        self.speed=speed
        print(f'{self.name} поехала')

    def stop(self):
        self.speed=0
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} свернула {direction}')

class WorkCar(Car):
    legal_speed = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > WorkCar.legal_speed:
            print(f'Превышение скорости! Разрешенная скорость не более {WorkCar.legal_speed} км/ч')

class TownCar(Car):
    legal_speed = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > TownCar.legal_speed:
            print(f'Превышение скорости! Разрешенная скорость не более {TownCar.legal_speed} км/ч')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, color = "white", name="noname"):
        super().__init__(color=color, name=name)
        self.is_police=True

def check_car(car):
    print(f"---------{car.name}---------")
    print(f'Атрибуты - цвет:{car.color}, полиция:{car.is_police}')
    car.show_speed()

    car.go(50)
    car.show_speed()

    car.stop()
    car.show_speed()

    car.go(100)
    car.show_speed()

    car.turn("в ад")



check_car(WorkCar(name="Газель"))
check_car(TownCar(name="Лада"))
check_car(SportCar(name="KalinaSport", color="yellow"))
check_car(PoliceCar(name="УАЗ"))