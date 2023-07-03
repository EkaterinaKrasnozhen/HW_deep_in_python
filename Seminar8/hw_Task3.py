# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и 
# все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle. 
# Для дочерних объектов указывайте родительскую директорию. 
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


import os
from os.path import join, getsize
from pathlib import Path


# def get_size(file) -> int:
#     return os.path.getsize(file)



def walk_in_path(dir_path):
    dir_dict = {}
    file_size = {}
    # my_list = os.listdir()
    # print(my_list)
    res_dict = {}
    res_dict2 = {}
    res_files = []
    res_folders = []
    # for  root, dirs, files in os.walk(dir_path):
    #     res_files += [(name, getsize(join(root, name)), os.path.isfile(name)) for name in files]
    total_size = os.path.getsize(dir_path)
    #print(dir_path, total_size)
    for item in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, item)):
            res_dict.setdefault(os.path.join(dir_path), [])
            res_dict[os.path.join(dir_path)].append([item, os.path.getsize(os.path.join(dir_path, item))])
            #res_files += [os.path.join(dir_path), item, os.path.getsize(os.path.join(dir_path, item))]
        elif os.path.isdir(os.path.join(dir_path, item)):
            res_dict2 = walk_in_path(os.path.join(dir_path, item))
        
    return(res_dict, res_dict2)

        
print(walk_in_path('Seminar8'))