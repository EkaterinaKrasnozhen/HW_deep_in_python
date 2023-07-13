from Animals import Animals


class Dogs(Animals):
    def __init__(self, wool, *args, **kwargs):
        self.wool = wool
        super().__init__(*args, **kwargs)
        
    def get_unique(self):
        if self.wool == 'короткая':
            return 'коротко-шерстная'
        elif self.wool == 'короткая':
            return 'коротко-шерстная'
        elif self.wool == 'длинная':
            return 'длинно-шерстная'
        return 'голая'
    
    def get_info(self):
        return f'"класс" = {Dogs}, "особенность" = {self.get_unique()}, "имя" = {self.name}, "возраст" = {str(self.age)}'
    
    
if __name__ == '__main__':
    dog = Dogs('без шерсти', 'Kate', 3)
    print(dog.get_unique())