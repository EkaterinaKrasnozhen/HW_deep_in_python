# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

my_str = 'Ветер с моря дул, ветер с моря дул, ветер, ветер, ветер, ветер, ветер, ветер, ветер, ветер, ветер, десять, моря, с, с, с, с, с, с, с, с, с, с, с,'\
    .replace(',', '').replace('.', '').replace('!', '').replace('?', '').lower().split(' ')
print(my_str)
res_list = []
my_dic = {}
for item in my_str:
    my_dic[item] = my_dic.get(item, my_str.count(item))
    if my_str.count(item) >= 10:
        if item not in res_list:
            res_list.append(item)
            
print(f'{res_list=}\n{my_dic=}')