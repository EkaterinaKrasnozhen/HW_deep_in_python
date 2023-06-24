# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа 
# и списком с доходами и расходами (3-10 чисел) в качестве значения. 
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании 
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

dict_company = {'Ромашка': [3000, -3000, 1000], 'Сатурн':[4000, -4000, 1000, 1000], 'Тойота':[6000, -5000]}


def balance(some_dict: dict) -> dict:
    """баланс по значениям

    Args:
        some_dict (dict): словарь {str:[int, ]}

    Returns:
        dict:
    """
    res ={}
    for key, num in some_dict.items():
        res.setdefault(key, sum([int(n) for n in num]))
    return(res)

result = balance(dict_company)
print(result) # {'Ромашка': 1000, 'Сатурн': 2000, 'Тойота': 1000}
print(all(map(lambda x: result[x] > 0, result)))#True
    

