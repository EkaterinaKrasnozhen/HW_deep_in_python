# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 

# * При переименовании в конце имени добавляется порядковый номер.

# * принимать в качестве аргумента расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.

# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
from pathlib import Path
import os


def rename_file(new_name, exten_old, exten_new):
    
    for i, files in enumerate(os.listdir(), start=1):
        if files.split(".")[1] == exten_old:
            Path(files).rename(f'{files.split(".")[0]}{new_name}{i}.{exten_new}')
            

if __name__ == '__main__':
    rename_file('new_file', 'txt', 'bin')