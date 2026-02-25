from services.student_service import StudentService
from database.student_database import StudentDatabase

if __name__=="__main__":
    DB = StudentDatabase("./data/student.json")
    DB.apri()
    service = StudentService()
    opzione = 1
    possibili_opz = {1, 2, 3, 4}
    while opzione in possibili_opz:
        opzione = int(input("Scegli opzione (1 leggi, 2 modifica, 3 crea, 4 cancella): "))
        if opzione == 2 or opzione == 3:
            numero=int(input("quanti voti ha ottenuto lo studente: "))
            student= service.creazione_studente(numero)

        if opzione == 1:
            studente= service.leggi(DB)
            print(studente)
            continuo=input("vuoi avere maggiori dettagli su uno studente? S/N: ")
            if continuo.strip().lower() == "s":
                stud_id=int(input("inserisci l'id dello studente che vuoi visualizzare: "))
                studente_specifico= service.leggi_dettaglio(DB,stud_id)
                print(studente_specifico)

        elif opzione == 2:
            id_stud=input("inserisci id dello studente da modificare: ")
            service.modifica(student,DB, id_stud)
            print("lo studente è stato modificato!")

        elif opzione == 3:
            service.scrivi(DB,student)
            print("Studente inserito con successo!")

        elif opzione == 4:
            flag= True
            while flag:
                id_stud= int(input("inserisci l'id dello studente che vuoi eliminare: "))
                risultato= service.elimina(DB,id_stud)
                if risultato:
                    print("lo studente è stato modificato!")
                    flag= False
                else:
                    print("lo studente non è stato trovato, riprovare!")
    DB.chiudi()
        
