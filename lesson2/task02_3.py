# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# через list
month = int(input('Введите месяц (1-январь, 12-декабрь): '))
month_seasons = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
print(f"Введенный вами месяц({month}) относится к сезону: {month_seasons[month - 1]}")

# через dict
month = int(input('Введите месяц (1-январь, 12-декабрь): '))
seasons = {"зима": {12, 1, 2}, "весна": {3, 4, 5}, "лето": {6, 7, 8}, "осень": {9, 10, 11}}
for k, v in seasons.items():
    if month in v:
        print(f"Введенный вами месяц({month}) относится к сезону: {k}")