# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

person_name = 'Damir'
person_surname = 'Yunusov'
person_age = 34

is_married = input(f'{person_name}, вас есть муж/жена? (True/False): ')
print(f'Имя: "{person_name}", фамилия: "{person_surname}", возраст: {person_age}, женат: {is_married}')

python_grade = int(input('Введите свою оценку по курсу python (1-5): '))
devops_grade = int(input('Введите свою оценку по курсу devops (1-5): '))
english_grade = int(input('Введите свою оценку по английскому языку (1-5): '))
math_grade = int(input('Введите свою оценку по высшей математике (1-5): '))

average_grade = (python_grade + devops_grade + english_grade + math_grade) / 4

print(f"На основании введеных вами оценок по отдельным дисциплинам, Ваш средний балл - {average_grade:.2f}")
