from database.student_database import StudentDatabase
from models.studenti import Studenti
class StudentService:
    

    def leggi(db : StudentDatabase):
        tmp=[]       #calab
        db.apri()
        for stud in db.file:
            tmp.append({"id" : stud.id,"nome" : stud.nome,"cognome" : stud.cognome})
        return tmp

           


    def scrivi(db : StudentDatabase, sd : dict):      #txnzy
        db.apri()
        nuovo_studente=Studenti(sd["id"],sd["nome"],sd["cognome"],sd["eta"],sd["voti"])
        db.file.append(nuovo_studente)
        db.chiudi()


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