# Задание №6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print
counterOriginal = 4
counterMillenium = 100
counterLeap = 400
result = ""
year = int(input("введите год уууу"))

if year % counterOriginal != 0:
    result = "обычный"
elif year % counterMillenium == 0:
    if year % counterLeap == 0:
        result = "високосный"
    else:
        result = "обычный"
else:
    result = "Високосный"
    
print(result)