# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_list = [1, 1, 4, 4, 3, 3, 7, 8, 9]
new_list = []
for i, item in enumerate(my_list, start=1):
    if item % 2 != 0:
        new_list.append(i)

print(new_list) #[1, 2, 5, 6, 7, 9]