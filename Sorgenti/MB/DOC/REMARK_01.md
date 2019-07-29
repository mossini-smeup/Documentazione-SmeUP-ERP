# Campagne
## Definizione
 :  : I.INC.MBR Fil(DOC_VOC) Mem(REBASE_GLO) Sec( :  : VOC) SAt(006)

## Schema relazioni
![X1MARK04A](http://localhost:3000/immagini/REMARK_01/X1MARK04A.png)
## Dati
* Codice identificativo
* Date apertura / chiusura
* Budget previsto
* Tipo (telemarketing, evento, fiera, newsletter, commerciale, ...)
* Programma di vendita
* Lista destinatari
* Responsabile campagna
* Elenco attività previste

![X1MARK0402](http://localhost:3000/immagini/REMARK_01/X1MARK0402.png)
## Funzioni
### Definizione degli obiettivi
Identificare account/referenti target di una particolare campagna.

### Creazione di una nuova campagna
Dalla scheda campagne esiste la funzione Gestione > Nuova campagna, oppure lanciare la funzione "Nuovo" dal menù "UP" di una qualsiasi scheda, altrimenti digitare "nuova campagna" nello spotlight.
Compilare i campi del formato di input (se il campo responsabile è blank il programma assume il codice utente).
Premere il bottone "Conferma"

![X1MARK0401](http://localhost:3000/immagini/REMARK_01/X1MARK0401.png)
controllare eventuali messaggi di errore quindi proseguire con "Conferma inserimento", il programma crea la campagna e la propone per eventuali modifiche o compilazioni di altre informazioni (es. budget) : 

![X1MARK0402](http://localhost:3000/immagini/REMARK_01/X1MARK0402.png)
F6 per confermare le modifiche. Dopo la conferma è possibile, attraverso il tab "Inviti" passare direttamente alla selezione degli account / referenti a cui la campagna è indirizzata.

### Sviluppo di una campagna verso una lista di account/referenti
La funzione di costruzione inviti permette di assegnare ad una campagna una lista di destinatari. Per la stessa campagna la funzione può essere richiamata n. volte in modo che possiamo associare alla campagna liste di destinatari anche a più riprese.
La funzione può essere richiamata direttamente appena conclusa la creazione della campagna (dal tab. Inviti della sk inserimento campagna) oppure successivamente partendo dalla SK navigazione.

Inizialmente si presenta la scheda di costruzione della lista : 

![X1MARK0403](http://localhost:3000/immagini/REMARK_01/X1MARK0403.png)gli inviti possono essere costruiti in diversi modi che sono attivabili dai tab. della prima sottoscheda (1) : 
* dagli inviti a campagne precedenti :  viene mostrata la lista delle compagne, il click su una campagna mostra nella sezione sottostante la lista dei referenti collegati
* dall'elenco referenti che accettano un tipo di mailing list :  viene mostrata la lista dei tipi mailing list, il click su una mailing mostra nella sezione sottostante la lista dei referenti collegati
* filtrando i referenti con il drill down della navigazione
* selezionando dall'elenco completo dei referenti
* partendo da una lista di account (2) :  inserire una lista account nel campo di input, eventualmente compilare anche la funzione aziendale ed il tipo di mailing che verranno usati come filtri aggintivi e premere il bottone "Conferma". Nella sezione sottostante vengono mostrati gli accounti ed i relativi referenti che soddisfano i criteri di filtro.

![X1MARK0404](http://localhost:3000/immagini/REMARK_01/X1MARK0404.png)selezionare i referenti da invitare ed usare il drag'n drop trascinandoli nella sezione di destra (1), è possibile trascinare selezioni multiple (click sul primo - tenere premuto il maiuscolo e fare click sull'ultimo - tenere premuto il click e trascinare il puntatore nella sezione di destra).
Per eliminare dalla lista un referente basta trascinarlo nel cestino (2).

Il tab. "Crea eventi" (3) permette di avere una visione completa (dei dati dell'account e di quelli del referente) di chi si sta invitando : 

![X1MARK0405](http://localhost:3000/immagini/REMARK_01/X1MARK0405.png)
prima di presentare la lista degli inviti porre attenzione a compilare i campi superiori (1) : 
* azione, stabilisce che tipo di azione dovrà essere fatta successivamente (es. telefonata, invio mail, ..)
* data / ora, dell'azione
* responsabile, di eseguire l'azione (se blank si assume l'utente)
completate le impostazioni si preme "conferma" (2) e appare la lista, si possono cambiare le impostazioni (es. cambiare la data o il responsabile, ..) e premere nuovamente "conferma" e la lista si aggiorna.

Quando le attività sono completate premere il bottone "Crea eventi" (3) per concludere l'attività.
Nel tab. "Storico eventi" possono essere interrogati tutti gli eventi generati per la campagna.

### Scadenzario / promemoria

### Generazione newsletter

### Export to social malier

### Import da social mailer

### Drill down sulle attività di marketing e vendita successive o derivate : 
- telefonate, inviti ad eventi o fiere, invio di newsletter
- lead, opportunità
- offerte, ordini, fatture

### Generazione lead
Normalmente è possibile derivare una o più lead da un evento associato ad una campagna (es. una telefonata oppure un eventodi tipo mailing), quando questo succede in fase di creazione la lead eredita dall'evento :  campagna, account, referente, responsabile. In ogni casi si può derivare direttamente una lead da una campagna, attraverso il Tab. "Nuova lead" presente nella scheda campagna.

### Analisi risultati della campagna
* conto economico di commessa (costi diretti e margini delle commesse cliente derivate)
* numeri significativi : 
** numero lead generate
** n. opportunità, (vinte e perse)





## Implementazione
Le campagne sono sull'archivio BRCOMM0F ed hanno tipo commessa = '£R1'

### Campi utilizzati
M$COMM as "Campagna;CM£R1",
M$DECM,
M$STAT,
M$CDRE as "Responsabile;CNCOL",
M$COEN as "Account;CNNOM",
M$DT01 as "Data apertura",
M$DT02 as "Data chiusura",
M$QI02 as "Valore budget",
M$COD2 as "Programma vendita;REE",
M$COD4 as "Target campagna;TAREH",
M$STCM as "Tipo campagna;TABSE£1",


