# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

my_dict = {'Video': ['mp4', 'dvd', 'avi'],
           'Img': ['png', 'jpg', 'jpeg'],
           'Text': ['txt', 'pdf']}


def sort_files(dict):

    files = [file for file in os.listdir() if os.path.isfile(file)]
    for folder, ext in  dict.items():
        if not os.path.isdir(folder):
            os.mkdir(folder)
        for file in files:
            if str(file.split(".")[1]) in ext:
                os.replace(file, os.path.join(os.getcwd(), folder, file))
    


if __name__ == '__main__':
    sort_files(my_dict)