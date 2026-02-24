from services.student_service import StudentService
from database.student_database import StudentDatabase

if __name__=="__main__":
    DB= StudentDatabase(".\\data.json")
    service=StudentService()
    opzione = int(input("Scegli opzione (1 leggi, 2 modifica, 3 crea, 4 cancella): "))
    if opzione == 2 or opzione == 3:
       numero=int(input("quanti voti ha ottenuto lo studente: "))
       student= service.creazione_studente(numero)


    if opzione == 1:
      studente= service.leggi()
      print(studente)
      continuo=input("vuoi avere maggiori dettagli su uno studente? S/N: ")
      if continuo.strip().lower() == "s":
        stud_id=int(input("inserisci l'id dello studente che vuoi visualizzare: "))
        studente_specifico= service.leggi_dettaglio(stud_id)
        print(studente_specifico)


    elif opzione == 2:
        id_stud=input("inserisci id dello studente da modificare: ")
        service.modifica(student,id_stud)
        print("lo studente è stato modificato!")


    elif opzione == 3:
        service.scrivi(student)
        print("cliente inserito con successo!")

    
    elif opzione == 4:
        flag= True
        while flag:
            id_stud= int(input("inserisci l'id dello studente che vuoi eliminare: "))
            risultato= service.elimina(id_stud)
            if risultato:
                print("lo studente è stato modificato!")
                flag= False
            else:
                print("lo studente non è stato trovato, riprovare!")
        
        
