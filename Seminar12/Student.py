# Создайте класс студента. 
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
# Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы. 
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). 
# Также экземпляр должен сообщать средний балл по тестам для каждого 
# предмета и по оценкам всех предметов вместе взятых.
import Cvs_creator

class TextDescriptor:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.param(value): 
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'ФИО должно состоять только из букв, первая буква заглавная, пример Иван Иванович Иванов')


class Student:
    name = TextDescriptor(str.isalpha) # не смогла объединить несколько проверок
    name = TextDescriptor(str.istitle)
    surname = TextDescriptor(str.isalpha)
    surname = TextDescriptor(str.istitle)
    middle_name = TextDescriptor(str.isalpha)
    middle_name = TextDescriptor(str.istitle)
    
    def __init__(self, id_, name, middle_name, surname):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.id = id_
        data = Cvs_creator.read_csv('studen2.csv')# например оценки зв 2ое полугодие
        data2 = Cvs_creator.read_csv('studen.csv')# оценки за 1ое полугодие
        self.student_data = []
        self.student_data.append(data[str(id_)])
        self.student_data.append(data2[str(id_)])
        
    def __repr__(self):
        """ Вывод экз. """
        return f'Student(id = {self.id}, name={self.name}, middle_name={self.middle_name}, surname={self.surname})'
        
    def get_score(self):
        """ Получаем средние оценки и средний балл. """
        self.res_average_score = {}
        for i in range(0, len(self.student_data[0])-2, 3):
            self.res_average_score[self.student_data[0][i]] = [{'средняя оценка': (int(self.student_data[0][i+1]) + int(self.student_data[1][i+1])) / 2},{'средний балл': (int(self.student_data[0][i+2]) + int(self.student_data[1][i+2])) / 2}]
        return self.res_average_score
    

if __name__ == '__main__':
    student1 = Student(1, 'Kate', 'Leonidovna', 'Krasnozhen')
    print(student1.student_data)
    res = student1.get_score()
    print(res)
    print(repr(student1))
