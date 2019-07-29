# GESTIONE DATI CLIENTE

La schermata iniziale permette di effettuare diverse operazioni per la gestione clienti quali : 
 * 01 :  Aggiunge
 * 02 :  Modifica
 * 03 : Copia
 * 04 :  Cancella
 * 05 :  Interroga
 * 06 :  Stampa
 * 07 :  Sostituzione
 * X : Scelta
Inserire  **CLI**  nel riquadro "Tipo Contatto" .

Lo "Scenario" indica a che Ditta il cliente si riferisce  : 
 * **FX : ** Fox Bompani
 * **ML : ** Emmelle
 * **FF : ** FinFox
 * **FB  : ** Bompani Italia  (l'Azienda non esiste più però è ancora presente nel Sistema)

 IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_1.PNG) A(C)
## MODIFICA DEL CLIENTE :  VARIAZIONE AGENTI E/O ZONA
Un codice cliente, una volta inserito, non è possibile cancellarlo.
Un cliente può essere soggetto a : 
 * __ cambiamento agente__
 * __ annullamento del cliente__

### Cambiare agente : 
Nel caso in cui un cliente cambi _Zona_ e di conseguenza cambi _Agente_, non verrà ricreato un nuovo cliente ma è necessario STORICIZZARE LA ZONA.
Selezionare con X la Zona.
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_2.PNG) A(C)
Viene visualizzata una maschera dove è presente lo storico dei cambi di zona del cliente.
Il simbolo ***** indica lo stato attuale del cliente.
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_3.PNG) A(C)
Per Inserire la nuova area bisogna : 
 * Inserire al posto dell' *****  la data di chiusura vecchia Zona.
 * Inserire la nuova Zona nella successiva riga.
 * Inserire l' * in S$DATF e premere  INVIO.
### Annullamento del cliente
Annullamento del cliente implica che il cliente stesso venga classificato come obsoleto. Ovviamente il processo comporta anche la fase inversa, cioè il reinserimento da cliente obsoleto a cliente attivo.
Per rendere un cliente obsoleto bisogna : 
Selezionare con X la Zona.
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_2.PNG) A(C)
Viene visualizzata una maschera dove è presente lo storico dei cambi di zona del cliente.
Il simbolo ***** indica lo stato attuale del cliente.
IMG P(\\SRVMODC1\LOOCU\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_3.PNG) A(C)
Per annulare il cliente bisogna : 
 * Inserire in S$DATI la data di inizio obsolescenza e  nella sezione _CLI00088_ digitare : 
 ** **01 : ** **(Obsoleta)** nel caso di cliente ITALIA
 ** **02 : ** **(Vecchi codici Esteri)** nel caso di cliente ESTERO
 * Inserire l' * in S$DATF e premere  INVIO.
#  INSERIMENTO NUOVO CLIENTE
L'immissione di un nuovo cliente comporta la selezione se quest'ultimo è di nazionalità **italiana (XCE)** o **estera  (XCI)**.
La selezione avviene digitando  X sulla casella di sinistra della relativa sezione.
IMG P(\\SRVMODC1\LOOCUP$\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_5.PNG) A(C)
__ NB : **i clienti che fanno parte dell' anagrafica **ITALIA** iniziano con il codice anagrafica **0xxxxx**, mentre i clienti **ESTERO** iniziano con il codice anagrafica **2xxxxx**
##  _2_ CLIENTE ITALIA 
Una volta scelto il cliente Italia viene visualizzata una successiva maschera, in cui si seleziona il cliente in funzione del rapporto fiscale.
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_6.PNG) A(C)
### __Persona fisica ITALIA
Nella schermata compaiono diversi campi in rosso :  **tali parametri devono essere obbligatoriamente inseriti per concludere correttamente l'inserimento del cliente._
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_7.PNG) A(C)
Tali parametri sono : 

 **Ragione sociale : ** nel momento in cui viene inserita la ragione sociale, comparirà una nuova matrice "Gestione cliente" che obbliga l'inserimento di tutti i dati anagrafici (dati descrittivi, di residenza, di nascita..)

IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_8A.PNG) A(C)
__NB : Dati di residenza__
 * Come  primo step per la  compilazione dei dati di residenza è **OBBLIGATORIO il riempimento del dato Comune. Utilizzando ! o ?  si riesce ad ottenere la lista dei possibili Comuni (es. ?BO per ottenere la lista dei Comuni che iniziano per BO oppure ! per avere la lista completa dei Comuni ).  Tale selezione guidata  comporta la  compilazione automatica di tutti i relativi dati come Cap, Provincia,Regione,Nazione.
 * La nazionalità, se è Italia, lasciarla blank
**Rapporto fiscale : ** compilato automaticamente
**Zona**
**Codice Pagamento**
**Codice Listino**
**Agente : ** viene preimpostato nel momento in cui si digita la Zona (es. zona 15 agente 015, zona BB agente 0BB)
**Altri Dati (F8)**

> Altri Dati (F8)

Selezionare _"Parametri scenario"_ dove appare il formato
IMG P(\\SRVMODC1\LOOCU\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_9.PNG) A(C)
Le fonti in rosso devono essere compilate obbligatoriamente : 
 * __Tipo invio fattura : __può assumere due valori distinti che influenzano direttamente la compilazione della schermata principale di inserimento nuovo cliente
 ** **E : **indica che la fattura verrà inviata via e-mail. Ciò comporta la necessità di inserimento della e-mail nella schermata principale
 ** **F : **indica che la fattura verrà inviata via fax. Ciò comporta la necessità di inserimento del fax nella schermata principale
 * __Canale di vendita : __
 ** inserisce automaticamente 090 (clienti occasionali) per i clienti Italia (0xxxxx)
 ** inserisce automaticamente 000 (senza gruppo) per i clienti Estero    (2xxxxx)
 * __Classificazione ABCD : __ in tutti i casi viene inserito automaticamente il valore D. Eventualemnte può essere modificato.

_1_IMPORTANTE : Alla fine del processo di inserimento del nuovo cliente, nel caso in cui il Sistema rilevasse P.Iva o Codice Fiscale (duplicazione) già presente nel database, compare una nuova matrice che chiede di confermare la duplicazione cliente. Nel caso ITALIA, il sistema permette di duplicare il cliente mentre impedisce la duplicazione nel caso di cliente ESTERO.
### __ Persona giuridica ITALIA
Il processo di inserimento di una nuova _"Persona giuridica ITALIA"_ è uguale all'inserimento della _"Persona fisica ITALIA" _. (Ovviamente cambieranno alcune variabili dipendenti dal tipo di rapporto fiscale)
## _2_ CLIENTE ESTERO
Una volta selezionato il cliente Italia viene visualizzata una successiva maschera, in cui si seleziona la nazionalità.
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_10.PNG) A(C)ù
IMG P(\\SRVMODC1\LOOCUP\IMMAGINI_DOCUMENTAZIONE\SCH_CLIENTE_11.PNG) A(C)
**Le fasi successive alla sezione nazionalità, sono uguali a quelle di "INSERIMENTO CLIENTE ITALIA".
_1_IMPORTANTE : Alla fine del processo di inserimento del nuovo cliente, nel caso in cui il Sistema rilevasse P.Iva o Codice Fiscale (duplicazione) già presente nel database, compare una nuova matrice che chiede di confermare la duplicazione cliente. Nel caso ITALIA, il sistema permette di duplicare il cliente mentre impedisce la duplicazione nel caso di cliente ESTERO.
