class Persona():
    def __init__(self,nome,cognome):
        self.__nome__ = nome
        self.__cognome = cognome
        
    def __str__(self):
        print(f"Nome: {self.__nome} Cognome:{self.__cognome}")
        
    def Info(self):
        print(f"ciao mi chiamo {self.__nome}")