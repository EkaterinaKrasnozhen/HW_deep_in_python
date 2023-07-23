
class GetInfoUser1:
    
    def get_info():
        my_dict = {}
        while True:
            data = input('через пробел: имя, личный идентификатор и уровень доступа (от 1 до 7)')
            if not data:
                break 
            name, id_, gread = data.split(' ')
            if int(gread) not in range (1, 8):
                print(f'Вы ввели неверный уровень доступа')
                continue
            my_dict.setdefault(id_, [name, gread])
            return my_dict  
              
        
    if __name__ == '__main__':
        res_dict = get_info()   
        print(res_dict)         
            