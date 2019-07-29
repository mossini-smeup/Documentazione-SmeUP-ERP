# MEMORIZZAZIONE DATI VIDEO.
# Memorizzazione dati video
Un programma interattivo normalmente deve avere la caratteristica di memorizzare i dati utilizzati l'ultima volta
dall'utente. Ciò si realizza mediante funzioni standard.
## Template RPG
Si devono inserire le seguenti copy : 
£MDVF      :     Definizione del file di memorizzazione
MEDAV01L
£MDVDS_AP  :     Definizione della DS per Applicazione che va seguita dai campi di video che si intende memorizzare.
£MDVDS_PG  :     Definizione della DS per Programma che va seguita dai campi di video che si intende memorizzare.
£MDVDS_00  :     Definizione della DS Generica che va seguita dai campi di video che si intende memorizzare.
£MDVC      :     Routine che esegue la memorizzazione ed il reperimento dei campi di video.
La routine £MDV va richiamata all'inizio del programma, per leggere i campi memorizzati dall'archivio prima di
emettere il formato del video, ed alla fine, per memorizzarli.
Si veda il TEMPLATE di esempio in QSRCGEN
## Memorizzazioni multiple per nome
E' possibile memorizzare e gestire determinate scelte del video riferite ad uno stesso programma. l'utilizzo è
consigliato quando un programma prevede scelte complesse e numerose. Qualsiasi utente può memorizzare aggiornare o
scegliere memorizzazioni.
Modalità di utilizzo
Nel programma inserire nei controlli il lancio del programma
B£MDV5 nel seguente modo : 
CALL 'B£MDV5'
PARM            £PDSNP
PARM            XXXXXX
PARM            £MDVTO
PARM '0'        YYYYYY
Dove : 
£PDSNP è il nome del programma che utilizza le scelte.
XXXXXX è il campo video lungo 8 caratteri alfanumerici.
Si consiglia di inserire questo campo sotto il nome del programma in alto a destra, inserendo nel primo campo del
formato il posizionamento del cursore.
£MDVTO
DS utilizzata dalla routine standard di memorizzazione dei dati ed è utilizzata per lo scambio dei dati.
YYYYYY è un campo alfanumerico di 1 che bisogna impostare =
'0' e che gestisce se ritornato = '1' l'errore della scelta.
Il programma B£MDV5 gestisce utilizzando il campo di richiesta le seguenti funzioni (è opportuno precisare che se il
campo di richiesta = *blanks è opportuno non lanciare il programma, comunque non succede nulla) : 
CONTROLLO
Se nella prima posizione del campo richiesta c'è un carattere diverso da  '?/!' il pgm controlla la validità della
richiesta ed esegue la ripresa se la scelta è corretta oppure imposta a '1' il campo YYYYYY.
GESTIONE
Se nella prima posizione del campo richiesta c'è il carattere '?/!' il programma emette una finestra con la quale si
gestisce la scelta (X) l'aggiornamento (2) la creazione (1) e l'annullamento (1) di scelte utilizzando i dati al
momento nei formato.
Nota Operativa : 
il Sbf eseguo un'operazione alla volta quindi la prima, riemettendo il Sbf se la prima operazione incontrata non è la
scelta.
Nota Tecnica : 
La memorizzazione fisica delle scelte avviene utilizzando MD£UTE e MD£PGM (campi chiave del file
MEDAV00F) inserendo nel primo campo '**WWWWWWWW' (dove ** è un valore fisso e WWWWWWWW è il campo del sbf gestito
dall'operatore) e nel secondo campo il nome del programma (£PDSNP).

# Default per tutti gli utenti

 NOTE SPECIFICHE PER DEFAULT UTENTE
   Il programma gestisce la lettura di due livelli di default
   utente : 
   - default di utente corrente con chiave
     Utente :  "<utente>", Ambiente :  "<ambiente>-*"
   - default di tutti gli utenti con chiave
     Utente :  "**      ", Ambiente :  "<ambiente>-*"
   l'immissione dell'impostazione di default per tutti gli
   utenti non è possibile da alcuna funzione dei programmi di mdv
   ma può essere realizzata mediante la funzione UP MDV,
   disponibile all'amministratore del sistema. che dopo aver

   Per creare un default per tutti gli utenti l'amministratore deve : 
    - creare un default utente personale.
    - duplicare tale deafult tramite UP MDV sull'utente generico **.


 FLUSSO
    Il programma riceve come parametri : 
   --->  - nome UTENTE
  <--->  - Nome programma (1-8) carattere "-" (9-9)
           variabile progressiva.
  <--->  - campo di 300 caratteri (scelte)
  <---   - indicatore di errore

   N.B :  questa funzione occupa le ultime 25 posizioni della
   stringa di memorizzazione con la descrizione della scelta : 
   sono quindi disponibili le posizioni da 1 a 275.

