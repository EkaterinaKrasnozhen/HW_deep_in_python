# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from pathlib import Path
import typing


def read_line(file: typing.TextIO):# если при записи закончились строки в читаемом файле, переносим курсор в начало
    line = file.readline()
    if line == '':
        file.seek(0)
        line = file.readline()
    return line[:-1] #убрать последнюю пустую строку


def my_func():

    with (
            open('1.txt', 'r', encoding='utf-8') as fnums,
            open('names.txt', 'r', encoding='utf-8') as fnames,
            open('res.txt', 'a+', encoding='utf-8') as fres
    ):
        len1 = sum(True for _ in fnums) #количество строк в файле
        len2 = sum(True for _ in fnames)
        
        for _ in range(max(len1, len2)): 
            names = read_line(fnames)
            nums = read_line(fnums)
            res_sum = int(nums.split("|")[0]) * float(nums.split("|")[1])
            if res_sum > 0:
                fres.write(f'{str(names.lower())}, {int(res_sum)}\n')
            else:
                fres.write(f'{str(names.title())}, {str(res_sum)}\n')


if __name__ == '__main__':
    my_func()