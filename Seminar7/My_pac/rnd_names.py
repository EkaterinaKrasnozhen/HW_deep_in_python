# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import choice


def file_names():
    res = ''
    for _ in range(4, 7):        
        res += choice('bacidetamokovicuye')
    with open('names.txt', 'a', encoding='utf-8') as f:
            f.write(f'{res.title()}\n')


if __name__ == '__main__':
    file_names()