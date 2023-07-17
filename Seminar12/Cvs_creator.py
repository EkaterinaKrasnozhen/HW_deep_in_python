import csv
from random import randint as rnd

MIN_SCORE = 2
MAX_SCORE = 5
MIN_TEST = 0
MAX_TEST = 100

def create_csv_lesson(*args, **kwargs):
    """ Создаем словари со случайными оценками. """
    id_ = [value for _, value in kwargs.items()][0]# нужное количество id студентов
    my_dic2 = {}
    for num in range(1, id_+1):
        for i in range(len(args)):
            my_dic2[num] = my_dic2.get(num, []) + [{args[i]: [{'оценка': rnd(MIN_SCORE, MAX_SCORE)}, {'балл': rnd(MIN_TEST, MAX_TEST)}]}]
    return my_dic2
        
def dump_to_csv(file_name, data):
    """ Запись словаря в csv файл. """
    my_data = []    
    for id_, in_dict in data.items():
        for some in in_dict:
            for lesson, score in some.items():
                my_data.append({'id': id_, 'lesson': lesson, 'оценка': score[0].get('оценка'), 'балл': score[1].get('балл')})
    with open(file_name, 'a', newline='', encoding='utf-8') as f_write:
        cvs_write = csv.DictWriter(f_write, fieldnames=['id', 'lesson', 'оценка', 'балл'])
        cvs_write.writeheader()
        cvs_write.writerows(my_data)
        
def read_csv(file):
    """ Чтения csv файла с сохранением в словарь. """
    data = {}
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, fieldnames=['id', 'lesson', 'оценка', 'балл'], 
                                 quoting=csv.QUOTE_ALL) 
        for i, line in enumerate(csv_file):
            if i != 0:
                data[line['id']] = data.get(line['id'], []) + [line['lesson'], line['оценка'], line['балл']]           
        return(data)


if __name__ == '__main__':
    res = create_csv_lesson('русский', 'литература', 'математика', id=6)
    dump_to_csv('studen2.csv', res)
    data = read_csv('studen2.csv')
    print(data['1'])