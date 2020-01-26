"""
*Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    "название": ["компьютер", "принтер", "сканер"],
    "цена": [20000, 6000, 2000],
    "количество": [5, 2, 7],
    "ед": ["шт."]
}
"""
idx = 1
commands = ('add', 'analytics', 'exit')
goods = []


print("Работа с товарами! \nВведите команду:")
print(f"{commands[0]} - добавить товар\n{commands[1]} - показать аналитику\n{commands[2]} - выход")
while True:
    command = input()
    if command == commands[2]:
        break
    elif command == commands[1]:
        analytics = {}
        all_attr_names = set(sum([list(g[1]) for g in goods], []))
        all_attr_items = sum([list(g[1].items()) for g in goods], [])
        for name in all_attr_names:
            analytics[name]=list({t[1] for t in all_attr_items if name == t[0]})
        print(analytics)
    elif command == commands[0]:
        product = idx, {}
        print("Добавление характеристик товара\n Введите команду:")
        print(f'{commands[0]} - добавить характеристику\n{commands[2]} - закончить ввод характеристик')
        while True:
            add_command = input()
            if add_command == commands[0]:
                attribute_name = input("Введите название характеристики: ")
                attribute_value = input("Введите значение характеристики: ")
                if attribute_value.isnumeric():
                    attribute_value = int(attribute_value)
                product[1][attribute_name]=attribute_value
                print("Характеристики добавлены")
                print(product)
            elif add_command == commands[2]:
                print("Ввод характеристик закончен")
                break
            else:
                print('Команда не найдена!')
        goods.append(product)
        idx += 1
    else:
        print("команда не найдена!")

