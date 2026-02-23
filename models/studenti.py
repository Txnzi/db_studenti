class Studenti:

    __id: int
    nome: str
    cognome: str
    eta: int
    voti: list[int]


    @property
    def id(self):
        return self.__id


    def __init__(self,id: int,nome:str,cognome: str,eta: int,voti: list[int]):
        self.__id= id
        self.nome= nome
        self.cognome= cognome
        self.eta= eta
        self.voti= voti