# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

import re
#text = input("Введите текс: ").replace(" ", "").replace("?","").replace("(","").replace(")","")\
#                              .replace(",", "").replace(".", "").replace("''","").replace("[","")\
#                              .replace(";", "").replace(":", "").replace("!", "").replace("]","")


text2 = input("Введите текст: ")
reg = re.compile('[^a-zA-Z ]')
result_text = reg.sub('', text2)
result_text = result_text.replace(' ', '')

my_dict = {}

for char in result_text:
    if  char in my_dict:
        my_dict[char] = my_dict.get(char, 0) + 1

    
my_dict2 = {}
for item in result_text:
    my_dict2[item] = result_text.count(item)
print(f'{my_dict} \n{my_dict2}')