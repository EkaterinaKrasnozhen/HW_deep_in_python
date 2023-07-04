# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и 
# все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle. 
# Для дочерних объектов указывайте родительскую директорию. 
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
import os
from os.path import join, getsize


def dump_jason(dict_: dict, file_name: str) -> json:
    with open (file_name, 'a', encoding='utf-8') as f:
        json.dump(dict_, f, indent=1) 


def dump_csv(dict_: dict, file_name: str) -> csv:
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        data = []
        for key, value in dict_.items():
            data.append({'name': key, 'info': value})

        cvs_write = csv.DictWriter(f_write, fieldnames=['name', 'info'])
        cvs_write.writeheader()
        cvs_write.writerows(data)


def dump_pickle(dict_: dict, file_name: str) -> pickle:
    res = pickle.dumps(dict_)
    with open(file_name, 'wb') as f:
        pickle.dump(f'{res = }', f)


def walk_(path):
    info_dict = {}
    for root, dirs, files in os.walk(path):
        
        info_dict.setdefault('root', [])
        info_dict['root'].append({root: [[f'size = {getsize(root)}'], [f'isdir = {os.path.isdir(join(root))}']]}) 
        # тут для корневой считает размер, для вложенных = 0, для dirs тоже пробовала  - тоже 0
                  
        for file in files:
            info_dict.setdefault('files', [])
            info_dict['files'].append({file: f'size = {getsize(join(root, file))}, isfile = {os.path.isfile(join(root, file))}'})
    
    print(info_dict)
    
    dump_jason(info_dict, 'hw_sem8.json') 
    dump_csv(info_dict, 'hw_sem8.csv')
    dump_pickle(info_dict, 'hw_sem8.pickle')   
      
        
if __name__ == "__main__":
    walk_('module_files')