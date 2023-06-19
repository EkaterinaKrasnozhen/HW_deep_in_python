#Напишите программу, которая получает целое число и возвращает его 
#шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

num = 189
def func_hex(num):
    result = []
    letters = ['a', 'b', 'c', 'd', 'i', 'f']
    
    while num > 0:
        x = num % 16
        
        if x >= 10:
            x = letters[int(x-10)] 
            result.append(str(x))
        else:
            result.append(str(x))
        num = num // 16
    result.reverse()
    return 'ответ = %s' % ''.join(result)
  

print(func_hex(num))
    