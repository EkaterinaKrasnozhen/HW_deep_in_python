# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, 
# решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, 
# определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
__all__ = ['queen']

def queen(list_, n):
    x = [] # координаты по оси х
    y = [] # координаты по оси y
    game = True
    for item in list_:
        x.append(item[0])
        y.append(item[1])
        
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i]- x[j]) == abs(y[i] - y[j]):
                game = False
    
    return game

    
q = [[1, 1], [3, 4], [2, 7], [4, 6], [5, 8], [6, 2], [7, 5], [8, 3]] # True
q2 = [[4, 4], [3, 3], [2, 5], [1, 7], [5, 8], [6, 6], [7, 4], [8, 2]] # False
q3 = [[3, 4], [2, 3], [2, 5], [1, 7], [5, 8], [6, 6], [7, 4], [8, 2]] # False диагональ
n = 8
    
                    
if __name__ == '__main__':
    print(queen(q3, n))