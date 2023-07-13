# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

#  Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle():
    def __init__(self, length, width = None):
        self.length = length
        if width == None:
            self.width = length
        else:
            self.width = width
        
    def perimeter(self):
       return (self.length + self.width) * 2
   
    def s(self):
        return self.length * self.width
    
    def __str__(self):
        return f'{self.length = } {self.width = }'
    
    def __add__(self, other):
        perim = self.perimeter() + other.perimeter()
        new_rect = Rectangle(perim / 2 / 2, perim / 2 / 2)
        return new_rect
    
    def __sub__(self, other):
        if self.perimeter() > other.perimeter():
            perim = self.perimeter() - other.perimeter()
        else:
            return f'Первый прямоугольник меньше или равен второму, их вычитание = 0'      
        new_rect = Rectangle(perim / 2 / 2, perim / 2 / 2)
        return new_rect
    
    def __eq__(self, other):
        return self.perimeter() == other.perimeter()

    def __gt__(self, other):
        return self.perimeter() > other.perimeter()
    
    def __lt__(self, other):
        return self.perimeter() < other.perimeter()
    
    def __ge__(self, other):
        return self.perimeter() >= other.perimeter()
    
    def __le__(self, other):
        return self.perimeter() <= other.perimeter()

rect1 = Rectangle(4, 6)
rect2 = Rectangle(4, 5)

print(rect1.perimeter(), rect2.perimeter())
new_rect = rect1 + rect2
print(new_rect)
print(rect1 - rect2)
print(rect1 == rect2)
print(rect1 > rect2)
print(rect1 < rect2)