class UserException(Exception):
    pass

class MatrixLenException(UserException):

    def __init__(self, len1, len2):
        self.len1 = len1
        self.len2 = len2
        
    def __str__(self):
        return f'Длина первой матрицы = {self.len1}, не равна длине второй матрицы = {self.len2}.'
    
class MatrixException(UserException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        
    def __str__(self):
        return f'Размер матрицы {self.matrix1} и {self.matrix2} не совпадают, сложение невозможно.'