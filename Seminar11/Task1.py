# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


import time

class MyString(str):
    """Класс Моя строка с доступом ко всем возможностям str, хранит имя автора и время создания"""
    
    def __new__(cls, value, name):
        """Создание экз класса с наследованием от str"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time_create = time.time()
        return instance
    
    def __str__(self):
        """вывод для пользователя"""
        return f'{self.name=} текст: {super().__str__()} время: {self.time_create}'
    
    def __repr__(self):
        """вывод для программиста"""
        return f'MyString({super().__repr__()}, {self.name})'
    

if __name__ == '__main__':
    str1 = MyString('Hello my name is', 'Kate')
    print(str1.upper())
    print(repr(str1))
    print(str1.__doc__)