# Gestione automatica mancata consegna

E' stato predisposto il programma V5FE15 schedulabile che permette di gestire in modo automatico i messaggi di mancata consegna.
Il risultato dell'esecuzione di questo programma è l'invio della mail al cliente e il passaggio dello stato della fattura a 'Notificata da mancata consegna' (T§FL12='X') o 'Notificata da impossibilità di recapito' (T§FL12='Y')
Il programma legge i documenti del ciclo attivo con T§FL12 uguale a 3 'Mancata consegna a ufficio PA ' o 8 'Impossibilità recapito'.
Come parametri di input sarà necessario indicare : 
1- Codice identificativo dell'EMAIL da cercare che potrà essere : 
a) l'identificatico utilizzato all'interno dell'estensione £16 del BRESCO oppure
b) il parametro legato all'oggetto £RN (ovvero l'elemento della tabella REM) nel caso in cui siano gestiti i referenti con REREFE0F
2- Il PATH della configurazione (di solito una PEC), se questo parametro è BLANKS assume il path di default (ovvero la PEC aziendale)

Il testo della mail inviata è il seguente : 
'Spett.le XXXX,
Vi comunichiamo che abbiamo ricevuto dal Sistema di Interscambio una notifica di
mancata consegna per la fattura Nr NNNN del GG/MM/AAAA.
Vi segnaliamo, quindi, che il documento è disponibile all'interno della vostra area riservata del
portale Fatture e Corrispettivi messo a disposizione dall'Agenzia delle Entrate e che da lì potete
procedere al download del documento per la sua gestione contabile.
Cordiali saluti.'

Dove XXXX è la ragione sociale del cliente per cui è stata ricevuta la mancata consegna.          

L'elaborazione del programma produce l'invio di un file csv all'utente che ha sottomesso il lavoro con il riasunto dell'invio effettuato (mail mandate e mail non inviate con relativa causa)
