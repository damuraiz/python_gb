# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self):
        self.inventory_counter = 0
        self.items = []

    def add(self, item):
        self.inventory_counter += 1
        self.items.append((self.inventory_counter, item))

    def __str__(self):
        return '\n'.join([f'Инвентарный номер {num} - {str(item)}' for num, item in self.items])


class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return str(self.__dict__)


class Printer(OfficeEquipment):
    def __init__(self, brand, model, is_color):
        OfficeEquipment.__init__(self, brand, model)
        self.is_color=is_color


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

printer = Printer("HP", "LJ300", False)
scanner = Scanner("Epson", "SD300", "4800x4800")
copier = Copier("HP", "DJ5400", True, "4600x4600", 26)

warehouse.add(printer)
warehouse.add(scanner)
warehouse.add(copier)

print(warehouse)
