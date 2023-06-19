# Задание №6
# Пользователь вводит строку текста. 
# Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = input("Введите текст: ").split(' ')
text = sorted(text)
for i, word in enumerate(text, start=1):        
    print(f"{str(i)} {word.rjust(len(word)):>1}\n") #не получается по правому краю