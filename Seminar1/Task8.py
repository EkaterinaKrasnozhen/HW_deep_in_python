# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

number = int(input("Введите количество рядов у елки: "))
count = 1
SPACE = " "
spaceCount = number-1
for i in range(number):
    print((SPACE * spaceCount) + ("*" * count))
    count += 2
    spaceCount -= 1