#Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

input_sec = int(input("Введите количество секунд: "))

hours = input_sec // 3600
input_sec %= 3600

minutes = input_sec // 60
seconds = input_sec % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

