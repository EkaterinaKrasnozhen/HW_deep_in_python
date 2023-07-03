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
    res_files = []
    res_folders = []
    for  root, dirs, files in os.walk(dir_path):
        res_files += [(name, getsize(join(root, name)), os.path.isfile(name)) for name in files]
        
        
    print(res_files)
    #     for file in files:
    #         #print(get_size(file))
    #         file_size[file] = get_size(file)
    # print(file_size)

    #     dir_dict[str(dir_path)] = {str({dir_name: os.path.isdir(dir_name)}): str({file_name: os.path.isfile(file_name)})}
        
    # print(dir_dict)
        
walk_in_path(os.getcwd())