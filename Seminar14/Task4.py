# Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, 
# личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей
import GetInfouser1 as get

class User1:
    def __init__(self, id, name, level=None):
        self.id = id
        self.name  = name
        self.level = level
        
    def set_level(self, level):
        self.level = level
        
    def get_level(self):
        return f'{self.level = }'
            
    def __str__(self):
        return f'{self.id = }, {self.name = }, {self.level=}'
    
    def __eq__(self, other):
        if self.id == other.id and self.name == other.name:
            return True
        return False


if __name__ == '__main__':    
    user1 = User1(1, 'Kate')
    print(user1)
    user1.set_level(3)
    print(user1.get_level())

    
    
