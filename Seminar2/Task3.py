#Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction

a = '1/3'
b = '1/3'
summ = ""
# num_a = input("Введите дробь A типа 1/2")
# num_b = input("Введите дробь B типа 1/2")

index_numerator = 0
index_denominator = 2
x1 = int(a[index_numerator])
x2 = int(a[index_denominator])
y1 = int(b[index_numerator])
y2 = int(b[index_denominator])

n = x2 / y2
m = y2 / x2

k = x2 * y2
l = x1 * y2
c = y1 * x2

#сложение дробей
def summ_(x1,y1,y2):
    summ = str(x1+y1) + "/" + str(y2)
    return summ

if n > m and (m*10) % 10 == 0:
    y2 *= int(n)
    y1 *= int(n)

elif m > n and (m*10) % 10 == 0:
    x1 *= int(m)

elif x2 == y2:
    print(summ)

else:
    x1 = l
    y1 = c
    x2 = k
    y2 = k

summ = summ_(x1,y1,y2)
print(summ) # 2/3

print(Fraction(1,3)+Fraction(1,3)) #2/3