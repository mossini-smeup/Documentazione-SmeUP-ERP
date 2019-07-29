## Obiettivo
Controllare lo stato di contabilizzazione delle informazioni del piano contributi (e di tutte le informazioni ad esso correlate :  provvigioni, documenti, registrazioni).
E' importante notare che complementare a questa funzione c'è la scheda "controllo ripresa dati coge" che svolge una funzione simile, ma partendo dalla contabilità invece che dal piano contributi.

## Parametri di lancio
* Agente :  permette di limitare l'analisi ad un singolo agente
* Anno :  è l'anno di riferimento, se vuoto assume l'anno corrente
* Mese :  permette di limitare l'analisi ad un singolo mese
* Stato provvigioni :  determina in base allo stato dei valori delle provvigioni, quali righe verranno analizzate. Le possibili scelte sono fra : 
** " "  :  vengono letti i record che hanno le provvigioni ancora da contabilizzare o già  contabilizzate.
** "A"  :  vengono letti i record in stato annullato. NOTA BENE :  quando la contabilità è l'applicazione master tutti i dati calcolati dal piano provvigioni vanno in stato annullato.
** "C"  :  vengono letti i record in stato contabilizzato.
** "I"  :  vengono letti i record in stato ancora da contabilizzare.
** "P"  :  vengono letti i record in stato ancora da contabilizzare o annullati.
** "V"  :  vengono letti i record che non sono ancora stati calcolati definitivamente (creati dall'esecuzione in modalità provvisoria dalla procedura di generale del piano contributi).
* Stato enasarco :  determina in base allo stato dei valori enasarco, quali righe verranno analizzate. Le possibili scelte sono fra : 
** " "  :  vengono letti i record che hanno l'enasarco ancora da contabilizzare o già  contabilizzato.
** "C"  :  vengono letti i record in stato contabilizzato.
** "I"  :  vengono letti i record in stato ancora da contabilizzare.
* Stato firr :  determina in base allo stato dei valori firr, quali righe verranno analizzate. Le possibili scelte sono fra : 
** " "  :  vengono letti i record che hanno il firr ancora da contabilizzare o già  contabilizzato.
** "C"  :  vengono letti i record in stato contabilizzato.
** "I"  :  vengono letti i record in stato ancora da contabilizzare.
* Stato isc :  determina in base allo stato dei valori isc, quali righe verranno analizzate. Le possibili scelte sono fra : 
** " "  :  vengono letti i record che hanno l'isc ancora da contabilizzare o già  contabilizzato.
** "C"  :  vengono letti i record in stato contabilizzato.
** "I"  :  vengono letti i record in stato ancora da contabilizzare.

## Dettaglio informazioni
* Dettaglio segnalazioni :  evidenzia la presenza di qualche incongruenza. Al click verrà aperta una finestra che le documenterà.
* Agente :  agente intestatario della riga
* Stato provvigioni :  indica lo stato di contabilizzazione degli importi provvigionali
* Data liquidazione provvigioni :  data in cui le provvigioni sono state liquidate
* Importo provvigioni liquidate :  recuperato dall'archivio delle liquidazioni effettuate
* Mese piano :  data competenza del piano contributi
* Importo provvigioni piano :  recuperato dall'archivio del piano contributi
* Tipo documento :  tipo documento della pro-forma collegata al piano
* N° documento :  n° documento della pro-forma collegata al piano
* Registrazione :  registrazione contabile della fattura del fornitore
* Importo provvigioni registrazione :  recuperato dalla registrazione contabile
* Condizione registrazioni :  viene evidenziato se la registrazione è provvisoria
* Data registrazione :  data di registrazione della fattura del fornitore
* Data fattura fornitore
* Segnalazioni :  testo indicativo del tipo delle eventuali segnalazioni presenti

## Funzioni Disponibili
* Modifica piano :  solo per utenti gestori, permette di andare a rettificare manualmente il piano provvigioni
* Interroga piano :  permette di andare ad interrogare nel dettaglio la riga del piano provvigioni
* Cancella piano :  solo per utenti gestori, permette di andare a cancellare manualmente il piano provvigioni
* Dettaglio provvigioni :  permette di andare ad interrogare il dettaglio delle provvigioni che hanno generato il piano
* Scheda registrazione fattura fornitore :  permette di andare ad interrogare la registrazione della fattura del fornitore
* Dettaglio ritenute :  permette di andare ad interrogare il dettaglio delle ritenute collegate alla registrazione della fattura del fornitore
* Scheda del documento :  permette di andare ad interrogare il documento di proforma corrispondente
* Elenco righe documento collegate :  permette di andare ad interrogare le righe del documento di proforma corrispondente

