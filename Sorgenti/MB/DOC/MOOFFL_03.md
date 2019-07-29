# Sincronizzazione tabelle di frontiera
Il presente documento descrive la modalità di interscambio dati gestita dai programmi di interfacciamento con la piattaforma offline Gulliver, attualmente gestita. Nel documento si fa riferimento genericamente a "piattaforma offline", ma alcune specificità sono fissate dalla piattaforma Gulliver, in quanto dettate dalle sue caratteristiche.

## Generalità interscambio dati
Le tabelle di frontiera, sono rappresentate da un area di dati in cui depositare i records oggetto di scambio e sincronizzazione, in modalità "coda di richieste di scambio". Ciascun records che Sme.UP necessita venga inviato sulla piattaforma offline (o viceversa venga ricevuto dalla piattaforma offline), deve essere accodato come richiesta di "aggiornamento (o inserimento) / cancellazione", e viene processato a posteriori dal processo di sincronizzazione.
Il programma che si occupa del processo di sincronizzazione dei dati, legge in questa "coda" i records in attesa di essere processati, li processa, ottiene dalla piattaforma offline un esito della sincronizzazione e scrive l'esito nei records stessi nella coda. In questo modo la consultazione della coda di sincronizzazione delle tabelle di frontiera, fornisce sempre la situazione delle richieste accodate e dello stato in cui si trovano (in attesa o elaborate, con il relativo esito).
 :  : PAR F(03)
(Nella descrizione delle generalità si fa riferimento all'invio dei dati, ma la ricezione si basa su i medesimi principi, inversi)


## Invio dati verso la piattaforma offline
La gestione fisica del dato di interscambio, è basata sull'utilizzo del modulo EDI di Sme.UP, quindi le tabelle di frontiera vengono definite, ma non vengono in sostanza "riempite" dei dati da scambiare, ma vengono accodati a EDSEND0F, i dati definiti dalla struttura di ciascuna tabella di frontiera.
Le tabelle di frontiera, definite a seconda delle necessità dell'applicazione da implementare, devono rispettare i seguenti vincoli : 
* file PF definito tramite DDS in SRCWK
* campi alfanumerici o numerici zoned (non sono supportati in questo caso numerici impaccati ed a lunghezza variabile)
* il __primo campo__indicato deve essere il__campo chiave univoco__della tabella; la piattaforma offline recepisce i campi in sequenza posizionale, ed il primo campo deve essere obbligatoriamente il campo chiave univoca
* i campi di tabella gestiti dalla piattaforma offline sono in un massimo di 20 (+ il campo chiave univoco)
* elemento della tabella EDT che definisce la tabella di frontiera, con i seguenti campi valorizzati
** numeratore lotto
** tipo tracciato :  F- (in caso di tabella di frontiera definita come PF, teoricamente anche altri tipi di tracciati)
** nome tracciato :  nome del file PF o della struttura in funzione del tipo tracciato
** stato dopo l'invio
 :  : PAR F(03)
I campi tipo/nome tracciato possono anche non essere obbligatoriamente compilati, purché i records dati contengano queste caratteristiche negli appositi campi R$TTRA/R$NTRA file EDSEND0F; questa modalità è utile qualora si intenda gestire diversi tracciati con un unica tabella messaggio.
Il tipo tracciato dovrebbe essere teoricamente possibile con tutti i tipi tracciati gestiti dalla api £IR1, in quanto lo spacchettamento del buffer dati verrà fatta tramite quest'ultima. In questo modo si potrebbero gestire anche strutture di tipo configuratore o altro.


L'invio dei dati alla piattaforma offline, consiste in due momenti fondamentali : 
- accodamento dati in tabella di frontiera
- invio dati su piattaforma offline
### Accodameno dati in tabella di frontiera
L'accodamento di records da sincronizzare può essere a seconda degli eventi, di singolo record o di blocchi di records.
Ad esempio ad avvio procedura l'utilizzatore può necessitare l'invio di tutti i dati anagrafici per costituire la base dati, poi successivamente necessita di un meccanismo che garantisca l'aggiornamento automatico in tempo reale (o differito al giorno) dei dati aggiornati successivamente.
Tenendo conto che l'alimentazione delle tabelle di frontiera è in carico all'installatore presso il cliente e non fornito da programmi standard, si suggerisce di procedere nel seguente modo : 
* creare un programma in grado di elaborare il singolo record/oggetto e di accodare la singola richiesta di aggiornamento
* creare un programma che seleziona di massa tutti o un sottoinsieme di records dell'archivio da trasferire, e chiamando il programma del punto precedente (singolo oggetto), accoda le richieste per ogni oggetto selezionato
* attivare il programma singolo oggetto come flusso di oggetto (TA B£H/B£J) ad evento di inserimento/modifica/cancellazione dell'oggetto, in modo da garantire l'accodamento di tutte le richieste di modifica
L'accodamento dei records da sincronizzare termina con il deposito dei records stessi nel file EDSEND0F, in attesa di "trasmissione" mediante l'applicazione della chiusura del lotto di trasmissione EDI.
### Invio dati alla piattaforma offline
L'invio dei dati alla piattaforma offline, che consiste nell'elaborazione dei records presenti in un lotto EDI in attesa di applicazione, viene innescato mediante le funzioni native di "applicazione lotto EDI".

E' necessario configurare in modo specifico le tabelle EDI legate a questo flusso di trasmissione : 
* Tabella EDT messaggi inviati, in cui indicare tra gli altri, il parametro "metodo lista distribuzione" fisso ad uno specifico elemento della tabella EDI indirizzi, descritto nel punto seguente
![MOOFFL_03A](http://localhost:3000/immagini/MOOFFL_03/MOOFFL_03A.png)* Tabella EDI indirizzi, in cui descrivere un destinatario fisso che identifica l'instradamento verso la piattaforma offline, indicando nel campo "metodo di invio" uno specifico elemento della tabella EDC, descritto nel punto seguente
![MOOFFL_03B](http://localhost:3000/immagini/MOOFFL_03/MOOFFL_03B.png)* Tabella EDC metodi di comunicazione, in cui descrivere il punto di raccordo con la piattaforma offline, mediante il metodo *A38 (invio a webserver), ed il relativo parametro : 
** subsezione A38, in cui descrivere l'endpoint di scrittura tabelle offline
** programma specifico che esegue l'invio dei dati; se questo parametro non viene specificato, viene utilizzato il programma standard generalizzato MOED01A che genera i dati recependo la struttura specificata nei dati in trasmissione; se invece si desidera effettuare l'invio in modo specifico con delle funzionalità non coperte dal programma generalizzato, si può indicare un programma specifico creato ad hoc, utilizzando come template di partenza il programma MOED01A, rispettando il protocollo di comunicazione
![MOOFFL_03C](http://localhost:3000/immagini/MOOFFL_03/MOOFFL_03C.png)![MOOFFL_03D](http://localhost:3000/immagini/MOOFFL_03/MOOFFL_03D.png)
Da un punto di vista tecnico, tale programma esegue i seguenti passaggi : 
* riceve il nome della tabella di frontiera da trattare  (elemento della tabella EDT ricevuto come parametro di input)
* viene richiamato automaticamente dall'infrastruttura EDI su ogni record a livello 2 (non ancora inviato) e genera un file xml contenente tutto il lotto di records da trasmettere, scrivendolo in IFS (non obbligatorio ma più immediato)
** i records dati devono essere scritti in formato xml di matrice
** il file deve essere su un percorso raggiungibile dallo smeupprovider di riferimento
* identifica l'endpoint con cui comunicare, rappresentato da una subsezione A38 (classe SE SUB.A38), derivato dal metodo e parametro lista di distribuzione definito nella tabella EDT/EDI/EDC
* tramite l'api £K11 esegue la richiesta di invio al webserver
** secondo le variabili di comunicazione definite nell'endpoint
** gestendo un esito dell'invio, riaggiornando l'esito di ritorno il lotto che si è cercato di trasmettere


## Ricezione dati dalla piattaforma offline
Anche in caso di ricezione dati la gestione fisica del dato di interscambio è basata sull'utilizzo del modulo EDI di Sme.UP, quindi le tabelle di frontiera vengono "ricevute" in EDRECI0F.
Le tabelle di frontiera in ricezione devono rispettare gli stessi vincoli caratteristici sopra descritti, fatto salvo la loro descrizione che viene fatta nella tabella EDR : 
* file PF definito tramite DDS in SRCWK
* campi alfanumerici o numerici zoned (non sono supportati in questo caso numerici impaccati ed a lunghezza variabile)
* elemento della tabella EDR che definisce la tabella di frontiera, con i seguenti campi obbligatoriamente valorizzati
** tipo tracciato :  F- (in caso di tabella di frontiera definita come PF, teoricamente anche altri tipi di tracciati)
** nome tracciato :  nome del file PF o della struttura in funzione del tipo tracciato
** stato dopo applicazione
** numeratore lotto

La ricezione dei dati dalla piattaforma offline, consiste in due momenti fondamentali : 
- invio richiesta dati alla piattaforma offline (la richiesta deve sempre partire da Sme.UP) e ricezione dei dati nella tabella di frontiera
- trattamento applicativo dei dati ricevuti

### L'interfaccia tra i dati e la tabella di frontiera
L'interfaccia tra i dati dalla piattaforma offline e la tabella di frontiera deve essere definita in un programma personalizzato che indica provenienza e destinazione dei dati, nello specifico definendo le variabili per la chiamata *A38 e la schiera di correlazione per il caricamento dei dati nella tabella di frontiera. Queste informazioni verranno passate come parametri al programma standard, il cui scopo è essere una mera interfaccia tra il web service e la tabella di frontiera.

 :  : T04 Il programma personalizzato che richiama il programma standard.
Prendendo come riferimento il programma prototipo MOED02A_X, il programma personalizzato deve richiamare il programma standard MOED02A passando nei parametri : 
* l'endpoint con cui comunicare, rappresentato da una subsezione A38 (classe SE SUB.A38)
* l'elemento della tabella EDR che indica il nome della tabella di frontiera da trattare
* le variabili per la richiesta con l'api £K11
* la schiera di correlazione tra le variabili ricevute e i campi di output del tracciato definito nella tabella EDR.
Nello specifico della schiera di correlazione ($VER), ogni elemento definisce un campo di output del tracciato indicato nella tabella EDR come segue : 
* nei primi 10 caratteri ($VERFLD) va indicato il campo di output (può essere alfanumerico o numerico signed, non è gestito il packed)
* nei successivi 76 caratteri ($VERVAR) vanno inserite le eventuali verifiche da effettuare sulle variabili ricevute per validare l'importazione del campo. "*KEY" indica che è un campo chiave, pertanto al caricamento di questo campo viene scritto l'eventuale record con i campi precedentemente caricati e inizializzato un nuovo record inserendo il valore in questo campo
* negli ultimi 14 caratteri ($VERVAL) va inserita la variabile che contiene il valore da mettere nel campo.
In output il programma riceve nei parametri l'eventuale errore della £K11 o della £EDT ed il numero di lotto se non si presentano errori.

 :  : T04 Il programma standard (MOED02A)
La ricezione dei dati dalla piattaforma offline viene eseguita mediante il programma MOED02A che richiede i dati e li recepisce scrivendoli nella tabella di frontiera.

In dettaglio il programma : 
* tramite l'api £K11 invia una richiesta di ricezione dati
* verifica l'esito dell'esecuzione della richiesta ed inizia la ricezione del dato richiesto (funzione di scansione RIG della £K11)
* riceve tutti i dati e tramite la schiera di correlazione ricevuta come parametro li scrive nel tracciato definito nella tabella EDR
* scrive in EDRECI0F con identificativi della tabella di frontiera
* chiude il lotto ricevuto ed infine se definito in tabella EDR lo applica, innescando il relativo programma di applicazione.

### Trattamento applicativo dei dati ricevuti
A seconda dei casi ed a scelta dell'installatore, i dati ricevuti in EDRECI0F secondo quanto sopra descritto, possono essere immediatamente elaborati (se definito un metodo di applicazione in tabella EDR), oppure possono essere elaborati direttamente nel programma chiamante, essendo restituito nei parametri il numero di lotto dei dati resi disponibili in EDRECI0F.



