# Доработаем задачи 3 и 4. Создайте класс Project, 
# содержащий атрибуты – список пользователей проекта и админ проекта. 
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. 
# Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта. Если в списке его нет, 
# то вызывается исключение доступа. Если пользователь присутствует в списке пользователей проекта, 
# то пользователь, который входит получает его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. 
# Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

import json
import Task4 as us
from ExceptionTask5 import EnterError, LevelError


class Project:
    
    def __init__(self, users, admin=None):
        self.users = users
        self.admin = us.User1(4321, 'Pi', 1)
        
    def __str__(self):
        return str(self.users)
        
    @classmethod
    def load(cls, file_name):
        data = []
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                my_dict = json.load(f)
            for level, value in my_dict.items():
                for  id, name in value.items():
                    data.append(us.User1(id, name, level))
            return Project(data)        
                
        except FileNotFoundError as e:
            print(e)
        
    def enter():
        my_dict = {}
        while True:
            data = input('через пробел: имя, личный идентификатор')
            if not data:
                break 
            name, id_ = data.split(' ')
            my_dict.setdefault(id_, name)
            return my_dict 
    
    def create_new_user(dictionary):
        for key, value in dictionary.items():
            new_user = us.User1(key, value)
        return new_user
    
    def check(self, user):
        if user not in self.users:
            raise EnterError(user.id)
        for old_user in self.users:
            if user == old_user:
                user.level = old_user.level
                self.admin = old_user
                #print(self.admin)
            return self.admin
    
    def add_new_user(self, new_level, new_name, new_id):
        if int(self.admin.level) > new_level:
            raise LevelError(self.admin.level, new_level)
        self.users.append(us.User1(new_id, new_name, new_level))
        return f'в список пользователей добален пользователь {us.User1(new_id, new_name, new_level)}'  
    
          
if __name__ == '__main__':
    project = Project.load('users.json')# загружаем новый проект со списком пользователей из файла
    project.add_new_user(3, 'Olya', 4321)
    # new_user_info = Project.enter() # вводим данные нового пользователя
    # print(new_user_info)
    # new_user = Project.create_new_user(new_user_info)# создаем нового пользователя на основе введенных данных
    # res = project.check(new_user)# проверяем есть ли новый пользователь в списке пользователей
    # print(res)
    # project.add_new_user(2, 'Leo', 987)# добавляем нового пользователя в список с проверкой чтобы admin.level < new_user.level
    # print(*project.users)
    
 
