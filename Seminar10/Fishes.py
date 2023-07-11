from Animals import Animals


class Fishes(Animals):
    def __init__(self, area, *args, **kwargs):
        self.area = area
        super().__init__(*args, **kwargs)
        
    def get_unique(self):
        if self.area == 'океан':
            return 'океаническая'
        elif self.area == 'море':
            return 'морская'
        return 'речная'
    
    def get_info(self):
        return f'"класс" = {Fishes}, "особенность" = {self.get_unique()}, "имя" = {self.name}, "возраст" = {str(self.age)}'


if __name__ == '__main__':
    fish = Fishes('океан', 'Kate', 3)
    print(fish.get_unique())