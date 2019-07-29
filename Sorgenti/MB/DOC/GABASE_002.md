# Premessa
E' stata introdotta la gestione delle "Richieste d'Offerta (RdO)" partendo dalle RdA e generando opportunamente due documenti di V5, rispettivamente la "GARA e la Richiesta d'OFFERTA".
Il modulo creato permette di generare in automatico le Gare, sfruttando l'immissione delle Rda e generando un insieme di Richieste d'offerta in modo libero verso qualunque fornitore.
Il processo guida l'azienda nella gestione / archiviazione di tutti i documenti tipicamente gestiti in modo cartaceo.

 * Gara
E' un documento di V5 intestato all'Azienda, indica l'apertura di un progetto di cui si vuole tenere tracciabilità tra la Richiesta d'acquisto origine e le Offerte chieste agli enti preposti :  i fornitori (Sinonimo di Contratto da stipulare).

 * Offerta
E' un documento di V5 intestato ai fornitori dal quale ci si aspettano le informazioni utili per la fase di applicazione della Vittoria, cioè la scelta di un'Offerta rispetto alle altre (Sinonimo di Preventivo).
I passi sono i seguenti : 
  **a -** Immissione della Richiesta d'Acquisto
  **b -** Generazione della Gara
  **c -** Generazione della/e Offerta/e (con stampa/invio mail)
  **d -** Gestione/Immissione dei prezzi,mod.pagamento,... sui documenti di V5
  **e -** Applicazione del concetto di vincita di un'Offerta
  **f -** Chiusura della Gara

# Tabelle dell'applicazione
Le tabelle indicate servono come traccia, in modo da lasciare le impostazioni ad ogni singolo caso aziendale.
Nella tabella GA2 si riportano il tipo documento per la gara, il tipo documento per l'Offerta e il relativo pgm di aggiustamento (Utile per pilotare la scrittura del V5RDOC).
 :  : DEC T(ST) K(GA2)
 :  : DEC T(ST) K(V5D)
 :  : DEC T(ST) K(V5A)
 :  : DEC T(ST) K(V5B)

## Classe di Autorizzazioni
Nel caso della generazione della Gara, per le Richieste d'Acquisto valgono le Autorizzazioni del modulo GA, mentre per i documenti interessati quelle legate ai V5.
La classe standard di gestione dei documenti (in particolare per il tipo T$GA2B e T$GA2C) dev'essere gestita per abilitare utenti e/o gruppi di utenti nel cruscotto principale.
Vedi con  "UP AUT"
Classe :  V5DO01
Utente :  **
Funzione :  **

Classe :  GARDATB per funzione RC di Richiesta d'Offerta
Utente :  **
Funzione :  **

## Default
Stato / Livello : 
Per quanto riguarda la gestione degli Stati / Livelli si usa la Copy £SAG e, nel caso vada in errore, si assume lo stato / livello di chiusura uguale a "80/8".

>N.B. : 
Per quanto riguarda la gestione delle Note, si assume che il contenitore tra Gare e Offerte sia comune, cioè la stessa NSIxx per entrambe i modelli.

Contratto : 
Nelle Offerte, in testata documento, è utilizzato il campo "Numero Contratto" per riportare il numero della gara origine.

# Cruscotto di Gestione
 :  : INI Come gestire il cruscotto delle Gare   : 
 :  : CMD  CALL GAV5RDO
 :  : FIN
###
Si vedano in dettaglio le opzioni disponibili
       02=Modifica riga
       05=Visualizza riga
       GO=Genera Ric.Offerta
       ST=Stampa Ric.Offerta
       IC=Interroga Commenti
       GC=Gestione  Commenti
       AV=Assegna Vittoria Gara
       CG=Chiude riga Gara

# Passi descrittivi del processo
In questo paragrafo si vuole dare una traccia di comportamento della gestione delle Rdo : 
 - Immissione della Rda
Non è necessario compilarla in ogni parte, se è attiva (nella tabella GA2) la funzione di aggiornamento da Rdo su Rda in fase di assegnazione della vincita
 - Generazione, da Rda, della Gara nel menù della Validazione
 - Generazione delle Rdo, partendo dalle Gare, utilizzando il cruscotto di cui sopra
 - Generazione di documenti cartacei (stampe o mail) da inviare ai Fornitori
 - Aggiornamento delle Rdo con i dati di ritorno dai fornitori
 - Applicazione della Vincita e relativa chiusura delle righe di Rdo/Gare
 - Generazione dell'ordine di acquisto da Rda con funzione relativa
 - .. .. ..

##  In sospeso
 * Nel cruscotto di gestione si deve riportare il campo T§DEDO come informativa sulla tipologia della gara (consiglio :  usare questo campo per identificare la Gara in questione)
 * Concetto di Data di Validità della Gara e della Richiesta d'Offerta
 * Chiusura della Gara (testata) gestita in modo manuale
