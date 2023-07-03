# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
import os

def add_id(file_json):

    with open(file_json, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
    # else:
    # my_dict = {str(i):{} for i in range(1, 8)}
    
    
    while True:
        data = input('через пробел: имя, личный идентификатор и уровень доступа (от 1 до 7)')
        if not data:
            break
        name, id_, gread = data.split(' ')
        if int(gread) in range(1, 8):
            my_dict.setdefault(gread, {id_: name})[id_] = name
        
        else:
            print('Введите идентификатор от 1 до 7')
            continue
        
    with open ('new_user_.json', 'a', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False)
        
        

        
add_id('new_user_json')