Tale componente è utilizzato dalla £G87 per stampare un file pdf (già esistente) su una coda di
stampa (remota) AS400 (RMTOUTQ).

## Cosè SmePD?
Si tratta di un prodotto che viene installato su un PC Windows e basato su protocollo LPD. Consente di definire delle code di stampa virtuali accessibili da AS400 e associate ad altrettante stampanti fisiche. In pratica il server SmePD si comporta come una stampante virtuale con funzionalità di stampa PDF verso la quale è possibile inviare degli stream in formato PDF affinchè vengano stampati. Il processo operativo è semplice : 

Dopo aver installato e configurato il prodotto, la stampa di un documento PDF si ottiene
copiando (attraverso la funzione CPYTOSPLF della /copy G87) il contenuto di un file PDF presente nel IFS (o in qualsiasi altra directory accessibile da AS400) al'interno di una delle code di stampa virtuali definite in fase di configurazione. In questo modo il contenuto del file PDF viene inviato al server SmePD che lo elabora e lo stampa sulla stampante fisica associata alla coda.  Da notare che per ora il server SmePD può interpretare solo stream in formato PDF ma è predisposto per l'elaborazione di stream di dati di ogni tipo;

### Test di stampa di file pdf con Looc.Up
Per stampare un file .pdf utilizzando Looc.Up si utilizza la seguente applicazione : 
B£ - BASE_up Basic Functions
X3 :  Prova stampa PDF

Descrizione dei campi della scheda : 

Numero Richiesta :  indica una richiesta di movimentazione, cioè l'oggetto da stampare. Per visualizzare l'elenco degli oggetti disponibili digitare il carattere ! seguito da Invio e inserire una X a fianco dell'oggetto da stampare.
Stampante :  nome della stampante fisica su cui stampare il file .pdf.
Numero di Copie :  numero delle copie del documento da stampare.

Il nome della stampante ed il numero di copie sono obbligatori.

E' possibile memorizzare valori di default per i campi descritti, richiamando ogni configurazione da "Memorizzazione dati video" in alto a sinistra.

## Installazione e configurazione del componente : 
- [Installazione&-x2f;configurazione SmePD](Sorgenti/MB/DOC/NSPRNT_02I)
## Possibili malfunzionamenti con SmePD, troubleshooting, etc. : 
- [Possibili malfunzionamenti con SmePD](Sorgenti/MB/DOC/NSPRNT_02E)

