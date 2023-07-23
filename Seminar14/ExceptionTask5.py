class UserException(Exception):
    pass

class EnterError(UserException):

    def __init__(self, id_):
        self.id = id_
        
    def __str__(self):
        return f'Пользователя с id {self.id} нет в списке пользователей.'
    
class LevelError(UserException):
    def __init__(self, level, other_level):
        self.level = level
        self.other_level = other_level
        
    def __str__(self):
        return f'Ваш уровень {self.level} больше, чем уровень нового пользователя {self.other_level}.'