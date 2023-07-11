from Birds import Birds
from Dogs import Dogs
from Fishes import Fishes


class Fabrique():
    def __init__(self, class_, *args, **kwargs):
        
        if class_ == 'Birds':
            self = Birds(*args, **kwargs)
        elif class_ == 'Dogs':
            self =  Dogs(*args, **kwargs)
        elif class_ == 'Fishes':
            self = Fishes(*args, **kwargs)
        
        print(self.get_info())
             
            
if __name__ == '__main__':
    animal1 = Fabrique('Birds', 'летающая', 'Снегирь', 3)
    animal2 = Fabrique('Dogs', 'короткая', 'Такса', 5)
    animal3 = Fabrique('Fishes', 'река', 'Ерш', 1)
