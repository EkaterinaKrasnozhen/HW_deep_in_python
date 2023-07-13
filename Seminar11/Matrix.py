# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения мат

class Matrix:
    """ Класс Матрица. """
    def __init__(self, matrix):
        """ Инициализация экземпляра. """
        self.matrix = matrix
        
    def __str__(self):
        """ Выводя для пользователя. """
        return f'{[self.matrix[i] for i in range(len(self.matrix))]}'
    
    def __repr__(self):
        """ Вывод для программиста. """
        return f'Matrix({self.matrix})'
    
    def __eq__(self, other):
        """ Сравнение 2 матриц по длине. """
        if len(self.matrix) == len(other.matrix): 
            return all([len(el1) == len(el2) for el1 in self.matrix for el2 in other.matrix])
        return False
    
    def __add__(self, other):
        """ Сложение двух матриц. """
        if len(self.matrix) == len(other.matrix) and len([el for el in self.matrix]) == len([el for el in other.matrix]):
            result = self.matrix
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            return f'длины матриц разные, сложение невозможно'


m1 = Matrix([[1,2,3], [3,4,5], [2,6,4]])
m2 = Matrix([[5,2,3], [7,5,6], [7,5,6]])
m3 = Matrix([[5,2,3], [7,6], [7,5,6]])
m4 = Matrix([[5,2,3], [7,5,6]])


if __name__ == '__main__':
    print(m1)#[[1, 2, 3], [3, 4, 5], [2, 6, 4]]
    print(repr(m1))# Matrix([[1, 2, 3], [3, 4, 5], [2, 6, 4]])
    print(m1 == m2) # True
    print(m1 == m4) # False
    print(m2 == m3) # False
    print(m1+m2)#[[6, 4, 6], [10, 9, 11], [9, 11, 10]]
    print(m1+m4)#длины матриц разные, сложение невозможно