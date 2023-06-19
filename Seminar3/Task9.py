# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [1, 3, 3, 5, 7, 7 , 9]
res_list = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in res_list:
            res_list.append(item)
        
print(res_list) #[3, 7]