from task_queen import queen

q = [[1, 1], [3, 4], [2, 7], [4, 6], [5, 8], [6, 2], [7, 5], [8, 3]] # True
q2 = [[4, 4], [3, 3], [2, 5], [1, 7], [5, 8], [6, 6], [7, 4], [8, 2]] # False
q3 = [[3, 4], [2, 3], [2, 5], [1, 7], [5, 8], [6, 6], [7, 4], [8, 2]] # False диагональ
n = 8

print(queen(q, n))