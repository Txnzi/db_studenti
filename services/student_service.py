from database.student_database import StudentDatabase
from models.studenti import Studenti
class StudentService:
    

    def creazione_studente(n: int):
        valutazioni=[ int(input("inserisci voto: ")) for _ in range(n) ]

        student = {
          "nome" : input("inserisci nuovo nome: "),
          "cognome" : input("inserisci nuovo cognome dello studente:  "),
          "eta" : input("inserisci nuova eta studente: "),
          "voti" : valutazioni
        }
        return student

    def leggi(db: StudentDatabase):
        tmp=[]       #calab
        db.apri()
        for stud in db.file:
            tmp.append({"id" : stud.id,"nome" : stud.nome,"cognome" : stud.cognome})
        return tmp

           


    def scrivi(db: StudentDatabase, sd: dict[str, str | int | list[int]]):      #txnzy
        db.apri()
        tmp = {stud.id for stud in db.file}
        if sd["id"] in tmp or not isinstance(sd["voti"], list):
            return False
        
        nuovo_studente=Studenti(sd["id"], sd["nome"].strip(), sd["cognome"].strip(), int(sd["eta"]), sd["voti"])
        db.file.append(nuovo_studente)
        db.chiudi()
        return True


    def modifica(student : dict, db : StudentDatabase, id_stud : int):   #txnzy
        db.apri()
        for el in db.file:
            if el.id == id_stud:
                el.nome=student["nome"]
                el.cognome=student["cognome"]
                el.eta=student["eta"]
                el.voti=student["voti"]
        db.chiudi()




    def elimina(db : StudentDatabase, id_stud : int):    #calab
        db.apri()
        for stud in db.file:
            if stud.id == id_stud:
                del stud
                return True
        return False

  
    def leggi_dettaglio(db : StudentDatabase, id_stud : int):   #calab
        db.apri()
        for stud in db.file:
            if stud.id == id_stud:
                studente_cercato={"id" : stud.id, "nome" : stud.nome, "cognome" : stud.cognome, "eta" : stud.eta, "voti" : stud.voti}
                return studente_cercato
        return None