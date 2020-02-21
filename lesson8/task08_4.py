# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class ItemNotFoundError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.inventory_counter = 0
        self.items = {}
        self.sended_items = {}

    def add(self, item):
        self.inventory_counter += 1
        self.items[self.inventory_counter] = item

    def send(self, number, department):
        if self.sended_items.get(department) is None:
            self.sended_items[department] = {}
        if number not in self.items.keys():
            raise ItemNotFoundError("Оргтехника с таким инвентарным номером не найдена")
        self.sended_items[department][number] = self.items.pop(number)

    def __str__(self):
        result = '\n'.join([f'Инвентарный номер {num} - {str(item)}' for num, item in self.items.items()])
        for dep in self.sended_items.keys():
            result += '\n' + dep + '\n'
            result += '\n'.join(
                [f'Инвентарный номер {num} - {str(item)}' for num, item in self.sended_items[dep].items()])
        return result


class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return str(self.__dict__)


class Printer(OfficeEquipment):
    def __init__(self, brand, model, is_color):
        OfficeEquipment.__init__(self, brand, model)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, scan_res):
        OfficeEquipment.__init__(self, brand, model)
        self.scan_res = scan_res


class Copier(Printer, Scanner):

    def __init__(self, brand, model, is_color, scan_res, copy_speed):
        Printer.__init__(self, brand, model, is_color)
        Scanner.__init__(self, brand, model, scan_res)
        self.copy_speed = copy_speed


warehouse = Warehouse()

warehouse.add(Printer("HP", "LJ300", False))
warehouse.add(Printer("HP", "LJ300", False))
warehouse.add(Printer("HP", "LJ300", False))
warehouse.add(Scanner("Epson", "SD300", "4800x4800"))
warehouse.add(Scanner("Epson", "SD300", "4800x4800"))
warehouse.add(Scanner("Epson", "SD300", "4800x4800"))
warehouse.add(Copier("HP", "DJ5400", True, "4600x4600", 26))
warehouse.add(Copier("HP", "DJ5400", True, "4600x4600", 26))

warehouse.send(1, "Python Development")
warehouse.send(2, "Java Development")
warehouse.send(4, "Python Development")
warehouse.send(5, "Java Development")
warehouse.send(8, "Reception")

try:
    warehouse.send(2, "Reception")
except ItemNotFoundError as err:
    print(err)

print(warehouse)
