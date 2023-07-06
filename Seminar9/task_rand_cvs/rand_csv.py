# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import random
import csv


MIN = -4
MAX = 6
NUM_OF = 3
IN_RANGE = 101


def rand_():
    """запись в файл csv 100 строк по 3 случайных значения int
    """
    my_list = []
    for _ in range(IN_RANGE):
        a, b, c = random.sample(range (MIN, MAX), NUM_OF)
        my_list.append((a, b, c))
    
    pos_a = 0
    pos_b = 1
    pos_c = 2
    with open('rand_int.csv', 'a', newline='') as writer:
        
        data = []
        csv_write = csv.DictWriter(writer, fieldnames=["a", "b", "c"], dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for i in range(len(my_list)):
            data.append({"a": my_list[i][pos_a], "b": my_list[i][pos_b], "c": my_list[i][pos_c]}) 
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    rand_()

