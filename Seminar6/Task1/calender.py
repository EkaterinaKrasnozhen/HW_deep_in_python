# Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv

MIN_YEAR = 1
MAX_YEAR = 10000

# проверка на високосный год
def _visokos(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
 # високосный

# возможна ли такая дата    
def calend(day, month, year):
    set_monthes = {1: 31,
                   2: 28,
                   3: 31,
                   4: 30,
                   5: 31,
                   6: 30,
                   7: 31,
                   8: 31,
                   9: 30,
                   10: 31,
                   11: 30,
                   12: 31}

    day, month, year = map(int, (date.split('.')))
    if (MIN_YEAR <= year < MAX_YEAR) and (month in set_monthes.keys()):
        if month == 2 and (_visokos(year)):
            set_monthes[month] = 29    
        if day in range(1, set_monthes[month]+1):    
            return True
    return False


if __name__ == '__main__':
    _, date = argv
    my_list = ''
    for chr in date:
        my_list += str(chr)
    print(calend(*map(int, (my_list.split(".")))))



    