# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path

file_name = Path().cwd() / 'Seminar7' / 'res.txt'

def file_json(file_name):
    with (
        open(file_name, 'r', encoding='utf-8') as f,
        open('file_json', 'w', encoding='utf-8') as j
    ):
        #print(list(f))
        my_dict = {}
        for row in f:
            key, value = row.replace('\n', '').split(',')
            my_dict[key.capitalize()] = value
        json.dump(my_dict, j, ensure_ascii=False, indent=1)
    
file_json(file_name)