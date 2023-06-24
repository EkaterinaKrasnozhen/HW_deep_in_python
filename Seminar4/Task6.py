# Задание №6
# ✔ Функция получает на вход список чисел и два индекса. 
# ✔ Вернуть сумму чисел между между переданными индексами. 
# ✔ Если индекс выходит за пределы списка, сумма считается 
# до конца и/или начала списка.


def get_from_user(text: str) -> list:
    """
    Получаем ответ от пользователя
    """
    answer = list(map(int, input(text).strip().split()))
    return answer


START_INDEX = 0
FINISH_INDEX = 1


def find_sum(nums_list: list, index_list: list) -> int:
    """
    Сумма элементов списка в указанных грницах индексов
    """
    if   0 > index_list[START_INDEX]: 
        index_list[START_INDEX] = 0
    elif index_list[FINISH_INDEX] > len(nums_list):
        index_list[FINISH_INDEX] = len(nums_list)
    
    for _ in my_list:
        res = sum([int(n) for n in nums_list[index_list[START_INDEX]:index_list[FINISH_INDEX]+1:]])
    return res


my_list = get_from_user('Введите список чисел через пробел: ') # 0 2 3 4 10 1 2
list_index = get_from_user('Введите два индекса через пробел: ')# 2 4

result = find_sum(my_list, list_index)
print(result)# 17