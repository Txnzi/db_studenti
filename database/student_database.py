import json
from models.studenti import Studenti
class StudentDatabase:
    __path: str
    file: list[Studenti] | None

    @property
    def path(self):
        return self.__path


    def __init__(self, path: str, file = None):
        self.__path = path
        self.file = file
    

    def apri(self):
        appoggio=[]
        with open(self.path, "r") as F:
            tmp = json.load(F)
        for el in tmp:
            appoggio.append(Studenti(el["id"],el["nome"],el["cognome"],el["eta"],el["voti"]))
        self.file=appoggio


    
    def chiudi(self):
        with open(self.path, "w") as f:
            json.dump(self.file,  f)
        self.file = None