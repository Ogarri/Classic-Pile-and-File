class Pile:
    def __init__(self):
        self.__pile = []
    
    def empile(self, x):
        self.__pile.append(x)
    
    def depile(self):
        return self.__pile.pop()
    
    def est_vide(self):
        return len(self.__pile) == 0
    
    def __str__(self):
        return str(self.__pile)
    
    def get_first(self):
        return self.__pile[-1]
    
    def __len__(self):
        return len(self.__pile)

    def get_pile(self):
        return self.__pile

class File:
    def __init__(self):
        self.__file = []
    
    def enfiler(self, x):
        self.__file.append(x)
    
    def defiler(self):
        return self.__file.pop(0)
    
    def est_vide(self):
        return len(self.__file) == 0
    
    def __str__(self):
        return str(self.__file)
    
    def get_first(self):
        return self.__file[0]
    
    def __len__(self):
        return len(self.__file)

    def get_file(self):
        return self.__file
