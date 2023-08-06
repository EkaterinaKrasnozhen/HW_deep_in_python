# Задание №6
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
import os
from os.path import isfile, join
import logging


DirObj = namedtuple('DirObject', ['obj_name', 'ext', 'is_dir', 'parent'])
FORMAT = '{levelname} - {asctime}. {msg}' 
logging.basicConfig(format=FORMAT, style='{', filename='dir_log.log.', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__) 


def walk_dir_log(path_string: str):
    dir_objects = []

    for dirpath, dirnames, filenames in os.walk(path_string):
        for dirname in dirnames:
            dir_objects.append(DirObj(dirname, None, True, dirpath)) 
        for file in filenames:
            if isfile(join(dirpath, file)):
                f_name = file.split('.')[0]
                ext = file.split('.')[-1]
                dir_objects.append(DirObj(f_name, ext, False, dirpath))
    logger.info(dir_objects)
    return dir_objects
            

if __name__ == '__main__':
    res = walk_dir_log('Seminar8')
    print(res)