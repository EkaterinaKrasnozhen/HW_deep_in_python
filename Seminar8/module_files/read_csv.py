# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json

def to_json_from_csv(file_csv, file_json):
    json_dict = []
    with (
        open(file_csv, 'r', newline='', encoding='utf-8') as f_read,
        open(file_json, 'a+', encoding='utf-8') as f_write
    ):
        csv_file = csv.reader(f_read)

        for i, row in enumerate(csv_file):
            gread, id_, name = row
            if i != 0:
                json_dict.append({'gread': gread, 'id_': id_.zfill(10), 'name': name.lower(), 'hash': hash(f'{name}{id_}')})     
        json.dump(json_dict, f_write, ensure_ascii=False, indent=1)
        print(type(f_write))

          
to_json_from_csv('new_.csv', 'last_.json')
