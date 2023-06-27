#Создайте функцию генератор чисел Фибоначчи

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a + b
        
        
res = iter(fib(7))
print(*res) #0 1 1 2 3 5 8


