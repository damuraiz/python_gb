#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

with open('task05_2.txt') as f:
    lines = f.readlines()
    print(f'В файле {f.name} обнаружено - {len(lines)} строк')
    for i, line in enumerate(lines, 1):
        print(f'{i}: обнаружено {len(line.split())} слов')