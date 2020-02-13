# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.

# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, length, width):
        """Длина и ширина в метрах"""
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def calculate_mass(self, default_mass, depth):
        """Масса - килограммы на 1кв м на 1см толщины. Толщина в см. Результат в тоннах"""
        return self._length * self._width * default_mass * depth/1000

road = Road(length=5000, width=20)
default_mass = 25
depth = 5

print(f'Масса асфальта для дороги длиной - {road.get_length()} м. и шириной  {road.get_width()} м. '
      f'при толщине асфальта - {depth} см. составит {road.calculate_mass(25, 5)} т.')