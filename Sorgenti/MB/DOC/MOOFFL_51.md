# Gestione rilevazione dati di inventario offline

## Definizione tabelle di frontiera
* Articoli (AR)
* Addetti (TA DIP)
* Area di magazzino (TA GMR)
* Ubicazioni (UB)

## Prototipazione tabelle di frontiera
Scheda di prototipazione con la produzione di una matrice per ogni tabella di frontiera : 
* Tabelle in output (il soggetto è Sme.UP), ottenute medianti semplici sql
* Tabelle in input, importabili

Per esemplificare le tabelle di frontiera, nella scheda di prototipazione vengono rappresentate delle tabelle di frontiera mediante matrici su tabelle standard di Sme.UP. Sarà a cura del delivery la realizzazione di tabelle di frontiera appropriate.

## Procedura di alimentazione tabelle di frontiera

### Esportazione (da Smeup alla tabella di frontiera)
Le tabelle di frontiera sono a cura del delivery. Il delivery definisce il numero e la definizione delle tabelle di frontiera e provvede a creare i programmi di estrazione delle stesse. Le tabelle di frontiera sono dei file as400.

Il programma di estrazione è un programma funizzato che gestisce un record alla volta.
Riceve : 
*Oggetto da estrarre (se esiste)
* Il nome della tabella di frontiera da scrivere
* L'azione richiesta

I valori possibili per l'azione richiesta sono : 
* AGG (valido sia per aggiunta che per aggiornamento)
* DEL (valido per la cancellazione).

Possibilità di estrazioni massive chiamando il programma elemento per elemento.

Supponiamo di dover estrarre la tabella della classe materiale.
Il nome della tabella di frontiera potrebbe essere XINVTACLS
I campi della tabella : 
* COD. Codice dell'elemento
* DES. Descrizione dell'elemento
* AZI. Azione da intraprendere sul record (AGG/DEL)
* DTA. Data aggiornamento record tabella di frontiera (a cura del programma di scrittura della tabella)
* HRA. Ora aggiornamento record tabella di frontiera (a cura del programma di scrittura della tabella)
* DTI. Data di invio record al webservice (a cura del servizio di comunicazione con il webservice)
* HRI. Ora di invio record al webservice (a cura del servizio di comunicazione con il webservice)
* DTR. Data ricezione record dal webservice (a cura del servizio di comunicazione con il webservice)
* HRR. Ora ricezione record dal webservice (a cura del servizio di comunicazione con il webservice)
Verificare se possibile se DTR e HRH sono ritornate da applicazione offline.

Da definire : 
* Cosa fare in caso di scritture successive dello stesso elemento : 
** Scrittura nuovo record in tabella di frontiera
*** Log delle varie scritture (che comunque se servono si potrebbero fare scrivendo il p5even)
*** Incrementi dimensioni delle tabelle di frontiera con il passare del tempo.
** Aggiornamento del record nella tabella di frontiera
*** Contenimento delle dimensioni delle tabelle di frontiera
*** Perdita log trasferimenti (possibilità comunque da scrivere con eventi)
*** Gestione della cancellazione del record : 
* Trasferisco codice (azione AGG). Cancello il record dal gestionale e rifaccio trasmissione. Occorre capire se applicazione offline può gestire DEL senza precedente AGG. Se si aggiorno e basta. Se no devo controllare DTI o DTR per decidere se cancellare il record o aggiornare con azione DEL

### Esportazione (da tabella di frontiera a webservice e viceversa)
Programmi standard che appoggia i dati in EDSEND/EDRECI, configurato tramite le definizioni delle tabelle EDT/EDR che permette di trasferire le tabelle di frontiera da e all'applicazione offline tramite webservices.



