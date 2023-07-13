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
    

str1 = MyString('Hello my name is', 'Kate')
print(str1, str1.name, str1.time_create)
print(str1.__doc__)