# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
from random import randint as rnd
from random import uniform as uf

START = -1000
STOP = 1000


def mk_file(num_rows, name_file):
    
    with open(name_file, 'a', encoding='utf-8') as f:
        for _ in range(num_rows):
            f.write(f'{rnd(START, STOP+1)} | {uf(START, STOP+1)}\n')

     
if __name__ == '__main__':
    mk_file(3,'1.txt')        