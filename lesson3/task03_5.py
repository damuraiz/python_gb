"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
result = 0

def new_result(in_str):
    return sum([int(s) for s in in_str.split()])+result

while True:
    input_string = input()
    if input_string.find('q') == -1:
        result = new_result(input_string)
        print(result)
    elif input_string.find('q') == 0:
        break
    else:
        input_string = input_string[:input_string.find('q')]
        result = new_result(input_string)
        print(result)
        break
