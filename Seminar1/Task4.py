# 4. Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 3
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count :
    userNum = int(input("Угадайте число от 0 до 1000"))
    if num < userNum:
        count -= 1
        print("ваше число больше загаданного, осталось попыток: ", count)

    elif num > userNum:
        count -=1
        print("ваше число меньше загаданного, осталось попыток: ", count)

    else:
        print("Угадали!")
        break

else:
    print("попытки исчерпаны, вы не угадали")