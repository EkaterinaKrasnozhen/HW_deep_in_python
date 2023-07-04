# Прочитайте созданный в прошлом задании csv файл 
# без использования csv.DictReader. Распечатайте его как pickle строку.
import csv
import pickle


def read_csv(file_name):
    
    with open(file_name, 'r', newline='') as f:
        csv_file = csv.reader(f, dialect='excel-tab')
        for line in csv_file:
            print(pickle.dumps(line))
            

if __name__ == '__main__':
    read_csv('last_.csv')