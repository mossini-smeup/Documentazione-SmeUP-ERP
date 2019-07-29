# Operatività
## Ruoli principali del processo Richieste di acquisto => ordine di acquisto
Con la premessa che ogni azienda può darsi un processo di acquisto diverso in funzione di N parametri, nel processo proposto dal modello contenuto in SMEUPFIL, si identificano 4 ruoli principali  : 

1-Il richiedente l'acquisto, colui il quale compila una richiesta di acquisto, identificato come REQUESTER
2-Il manager (MGR) che si occupa di preapprovare la richiesta di acquisto e di identificare l'acquisitore (detto anche BUYER, ossia appartenente all'organizzazione responsabile degli acquisti)
3-Il Buyer che si occupa di trovare/confermare il fornitore proposto ed il costo di acquisto
4-Il responsabile dell' amministrazione (ADM) che si occupa di approvare dal punto di vista AFC (amministrazione, finanza e controllo) l'acquisto.

Essi vengono coinvolti nel processo descritto dalla figura qui di seguito : 

![V5RIDA_01](http://localhost:3000/immagini/V5RIDA_04/V5RIDA_01.png)
Questo processo dove si vedono le transizioni di approvazione che coinvolgono i 4 ruoli principali, mostra anche i luoghi di revisione che possono essere indirizzati sia dal Buyer che dal richiedente, quando ritengono che la RDA debba essere rimaneggiata.
Ad ogni passaggio di luogo viene inviata una mail al destinatario dell'impegno che si è attivato :  questo indirizzo mail è quello che si trova sull'ente referenziato nella tabella B£U dell'utente dell'impegno.
Per ogni transizione sono attivi gli utenti di Back up e  l'annullamento della dichiarazione..
Ad ogni transizione viene modificato lo stato del documento RA, secondo la tabella stati

 :  : DEC T(LI) P(TAB£WRA) K(*) R(1)
## Punti importanti della gestione.

Il documento di tipo RA si intesta all'azienda; sul dettaglio di riga c'è l'indicazione del fornitore da cui si pensa di acquistare.

Il passo finale del processo è ad opera del buyer che estrae dalla richiesta l'ordine di acquisto intestato al fornitore riporato sulla riga di richiesta

Il rifiuto dell'approvazione della richiesta da parte del Manager o dell'amministrazione porta all'annullamento della richiesta, in toto, ossia della testata della richiesta. Quindi conviene separare le righe di una richiesta se non strettamente correlate allo stesso acquisto.
