from database.student_database import StudentDatabase
from models.studenti import Studenti
class StudentService:
    

    def leggi(db : StudentDatabase):
        tmp=[]       #calab
        db.apri()
        for stud in db.file:
            tmp.append({"id" : stud.id,"nome" : stud.nome,"cognome" : stud.cognome})
        return tmp

           


    def scrivi(db : StudentDatabase, nuovo_studente : Studenti):      #txnzy
        pass


    def modifica(studente : Studenti, db : StudentDatabase, id : int):   #txnzy
        pass


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