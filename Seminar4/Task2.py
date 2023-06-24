#Напишите функцию для транспонирования матрицы

def transpon_matrix(matrix):
    trans_Matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_Matrix

matrix = [[1, 3], [2, 4], [5,7]] 
result = transpon_matrix(matrix)
print(result)#[[1, 2, 5], [3, 4, 7]]

