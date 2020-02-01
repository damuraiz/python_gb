# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user(name, surname, birth_year, city, email, phone):
    print(f'Пользователь - {name.title()} {surname.title()}, год рождения - {birth_year}, '
          f'город проживания - {city}, email - {email}, модель телефона - {phone}')


print_user(birth_year=1970, city='Gotham', email="iambatman@waynecorp.com", phone="waynePhone Pro", name="bruce",
           surname="wayne")
