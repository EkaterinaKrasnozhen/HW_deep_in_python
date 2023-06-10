# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


numberType = ""
numberCounter0 = 10
numberCounter00 = 100
result = 0
min = 0
max = 999
while True:
    number = int(input("введите число от 1 до 999: "))
    if (min < number | number < max):
        if number // numberCounter0 == 0:
            numberType = "цифра"
            result = number * number
        elif number // numberCounter00 == 0: #возможно надо было оставить 10, 100 и 1000 числами
            numberType = "двузначное число"
            result = (number%numberCounter0) * (number//numberCounter0)
        else:
            numberType = "трёхзначное число"
            num3 = (number%numberCounter0) * numberCounter00
            number = number//numberCounter0
            num2 = (number%numberCounter0) * numberCounter0
            num1 = number//numberCounter0
            result = num3 + num2 + num1     
    else:
        continue
    print(numberType, result)