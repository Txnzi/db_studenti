import json
class StudentDatabase:
    __path: str
    file: dict[str, int | str | list[int]] | None

    @property
    def path(self):
        return self.__path


    def __init__(self, path: str, file = None):
        self.__path = path
        self.file = file
    

    def apri(self):
        with open(self.path, "r") as F:
            self.file = json.load(F)

    
    def chiudi(self):
        with open(self.path, "w") as f:
            json.dump(self.file,  f)
        self.file = None