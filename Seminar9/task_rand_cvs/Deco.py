# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import os
from typing import Callable


# передача аргументов в функцию из файла
def start_quadro_fromcsv(func: Callable):
    def wrapper(*args):
        with open('rand_int.csv', 'r', newline='', encoding='utf-8') as f_read:
            res = []
            csv_file = csv.reader(f_read)
            for i, line in enumerate(csv_file):
                if i != 0:
                    a,b,c = map(int, line)
                    res = func(a,b,c)
            return res
    return wrapper


# логирование аргументов и результатов работы функции
def cache_to_json(func: Callable):
    def wrapper(*args):
        file_name = func.__name__+ '.json'
        result = func(*args)
        
        if os.path.exists(file_name):
            with open (file_name, 'r+', encoding="utf-8") as file:
                my_dict = json.load(file)
        else:
            my_dict = []

        my_dict.append({
            'args': args,
            'result': f'{result}'
            }) 
        with open(file_name, 'w', encoding='utf-8') as writer:
            json.dump(my_dict, writer, indent=1, ensure_ascii=False)    
        return my_dict
    return wrapper
               
