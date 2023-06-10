# 4. Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000+1
count = 3
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while True:
    userNum = int(input("Угадайте число от 0 до 1000"))
    if count > 1:
        if num < userNum:
            count -= 1
            print("ваше число больше загаданного, осталось попыток: ", count)
            continue

        elif num > userNum:
            count -=1
            print("ваше число меньше загаданного, осталось попыток: ", count)
            continue

        else:
            print("Угадали!")
            break
    elif count == 1:
        print("попытки исчерпаны, вы не угадали")