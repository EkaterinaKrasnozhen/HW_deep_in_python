# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

class Archiv:
    """ Класс Архив, хранящий в списке чисел - числа, в списке строк -строки."""
    list_num = []
    list_str = []
    
    def __init__(self, number, string):
        """ Создание экзмепляра класса Архив со свойства (втч списки)."""
        self.number = number
        self.string = string
        self.list_num.append(self.number)
        self.list_str.append(self.string)
        
    def __str__(self):
        lst = 'список чисел: ' + str(self.list_num) + ', ' + 'список строк: ' + str(self.list_str)
        return lst
    
    def __repr__(self):
        return f'список чисел {self.list_num}, список строк {self.list_str}'
        
obj = Archiv(3, 'da')
print(obj.list_num, obj.list_str)#[3] ['da']
print(obj.__doc__)
print(obj)
print(repr(obj))
