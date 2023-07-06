# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
# Для тестированию возьмите pickle версию файла из предыдущей задачи. 
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle

def from_pickle_to_csv(pickle_file, new_csv_file):
    with (
            open(pickle_file, 'rb') as f_read,
            open(new_csv_file, 'a') as f_write
        ):
            data_pickle = pickle.load(f_read)

            cvs_write = csv.DictWriter(f_write, fieldnames=['gread', 'id_', 'name', 'hash'])
            cvs_write.writeheader()
            cvs_write.writerows(data_pickle)
            

if __name__ == "__main__":
    from_pickle_to_csv('last_.pickle', 'last_.csv')