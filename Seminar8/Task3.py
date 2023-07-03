# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def to_csv(file_name):
    
    with (
        open(file_name, 'r', newline='', encoding='utf-8') as f_read,
        open('new_.csv', 'w', newline='', encoding='utf-8') as f_write
    ):
        json_dict = json.load(f_read)
        print(json_dict)
        data = []
        for gread, in_dict in json_dict.items():
            for id_, name in in_dict.items():
                data.append({'gread': gread, 'id':id_, 'name': name})

        cvs_write = csv.DictWriter(f_write, fieldnames=['gread', 'id', 'name'])
        cvs_write.writeheader()
        cvs_write.writerows(data)

        
to_csv('new_user_json')