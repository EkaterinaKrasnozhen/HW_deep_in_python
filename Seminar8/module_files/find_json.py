# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import os
import pickle
import json

def json_to_pickle():
    
    file = [file for file in os.listdir() if file.endswith('.json')]
    
    for _, item in enumerate(file):
        with (
            open(item, 'rb') as f_read,
            open(f'{item.split(".")[0]}.pickle', 'wb') as f_write
        ):
            # for line in f_read:
            #     pickle.dump(line, f_write)
            pickle.dump(json.load(f_read), f_write)
    
    
if __name__ == '__main__':
    json_to_pickle()
    with open('new_user_.pickle', 'rb') as f:
        print(pickle.load(f))