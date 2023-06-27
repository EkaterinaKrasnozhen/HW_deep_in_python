# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

link = "Seminar5//txt.txt".replace(".", "//")
print(link.split("//"))


def link_split(my_str):
    (a, b, c) = my_str.split("//")
    print((a, b, c))# ('Seminar5', 'txt', 'txt')


link_split(link)