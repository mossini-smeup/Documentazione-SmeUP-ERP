## Obiettivo

Attraverso questa funzione è possibile analizzare le partite contabili intestate ad un soggetto o ad una lista di soggetti ed eseguire alcune azioni sulle stesse.
All'interno di Keep.UP il numero partita è dato da numero e data documento della registrazione contabile.

## Formato guida

All'interno del formato guida sono disponibili i seguenti campi : 

![C5D030_012](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORRP/C5D030_012.png)

 - Codice dell'oggetto o della lista di oggetti di cui si voglia analizzare il partitario. La compilazione di questo campo è facilitata dalla presenza dei classici caratteri di ricerca. Per maggiori informazioni su questi caratteri si veda il seguente : 

- [Ricerche](Sorgenti/MB/DOC_OPE/B£_RIC)
Per dettagli sull'utilizzo delle liste oggetti si veda invece : 
- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)

 - Funzione. Per l'analisi dei partitari questo campo deve essere impostato a P
 - Metodo. Per l'analisi dei partitari è disponibile la sola modalità A (Sintesi partite).
 - Modalità. In questo campo è necessario indicare il tipo di output desiderato. Le modalità disponibili per l'esecuzione di questa funzione sono : 
 -- 1 - Stampa :  permette di stampare il partitario del soggetto.
 -- 2 - Interrogazione (non disponibile per liste di oggetti) :  permette di visualizzare il partitario.
 -- 4 - Trasferimento PC :  permette di esportare il partitario all'interno di un file su PC.
 -- 7 - PDF :  permette di stampare il partitario all'interno di un file PDF.
 - Pertinenza. In questo campo è necessario indicare se all'interno del mastrino si vogliono visualizzare le sole registrazioni fiscali, le sole gestionali o entrambe.
 - Condizione. In questo campo è necessario indicare se all'interno del mastrino si vogliono visualizzare le sole registrazioni attive, le sole simulate o entrambe. Per maggiori dettagli sulla definizione e utilizzo della pertinenza e condizione nelle registrazioni contabili si veda il seguente : 

 :  : DEC T(MB) P(DOC_VOC) K(GLO_C5) I(Glossario Contabilità) L(1)

 - Saldo alla data :  permette di indicare una data a cui calcolare il saldo del soggetto
 - Da data documento/A data documento :  permette di visualizzare solo le partite che hanno data compresa nel range impostato in questi campi. E' possibile compilare anche uno solo dei due campi. Ad esempio, impostando il primo campo con 01/02/2010 sarà possibile visualizzare le partite con data maggiore o uguale al 01/02/2010.


### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 

![C5D010_025](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORRP/C5D010_025.png)
- Partite chiuse :  definisce il metodo di visualizzazione delle partite chiuse. Le scelte disponibili sono : 
-- 1 - Sintesi :  per le partite chiuse viene visualizzato importo dovuto e importo pagato
-- 2 - No :  le partite chiuse non vengono visualizzate
-- Default :  lasciando il campo blank viene visualizzato il dettaglio delle partite chiuse
- Partite aperte :  definisce il metodo di visualizzazione delle partite aperte. Le scelte disponibili sono : 
-- 1 - Sintesi :  per le partite aperte viene visualizzato importo dovuto e importo pagato
-- 2 - No :  le partite aperte non vengono visualizzate
-- Default :  lasciando il campo blank viene visualizzato il dettaglio delle partite aperte
- Tipo partite aperte :  è possibile utilizzare le seguenti tipologie : 
-- 1- Rischio
-- 2 - Esposizione
-- Default - Scadenzario
- Modello visualizzazione :  permette di definire le informazioni riportate per ogni record visualizzato nel formato lista. Le scelte disponibili sono : 
-- 1 - Dovuto in valuta/Pagato in valuta/descrizione/Dovuto
-- 2 - Schema utente :  permette di utilizzare uno schema personalizzato definito nel campo sotto.
-- 0 - Dovuto/Pagato/Residuo
-- Default - Dovuto/Pagato/Residuo/Descrizione
- Schema utente :  attraverso questo campo è possibile definire lo schema utente da utilizzare per la visualizzazione delle informazioni di dettaglio. Per maggiori infromazioni sull'impostazione e utilizzo di schemi utente si veda il seguente : 

- [Schemi di visualizzazione e stampa](Sorgenti/MB/DOC_OPE/B£_SCH)

- Schema utente totali :  permette di definire uno schema utente da applicare ai totali.
- Metodo dettaglio :  definisce la modalità di visualizzaione del dettaglio della partita. Le opzioni disponibili sono : 
-- Deafult - Vista per scadenza :  i record del partitario sono dettagliati per scadenza :  di conseguenza registrando un documento con 3 scadenze all'interno della stessa partita saranno visualizzati tre record di dovuto.
-- 1 - Vista per partita :   i record del partitario sono dettagliati per partita :  di conseguenza registrando un documento con 3 scadenze all'interno della stessa partita sarà visualizzato un solo record di dovuto.
-- 3 - Vista per data : 
- Tipo suddivisione. permette di definire se suddividere le partite in dovuto/pagato oppure in registrazioni relative a documenti (es. fatture)/altre registrazioni
- Limite data registrazione iniziale/finale :  attraverso questi due campi è possibile filtrare le registrazioni visualizzate impostando un range di date registrazione.
- Presenta valuta di conto. E' un campo sì/no, se impostato a 1 (sì) e l'ente è in valuta verranno visualizzate le registrazioni in euro.
- Tutte le aziende. E' un campo sì/no, se impostato a 1 (sì) verranno visualizzate anche le registrazioni delle altre aziende del gruppo.
- Gruppi partite. Permette di impostare la visualizzazione delle partite pareggiate. Le opzioni disponibili sono : 
-- 1 - SI :  al'interno della decrizione della registrazione del pareggio partite vengono riportati i riferimenti del documento con cui si esegue il pareggio (numero nota credito)
-- 2 - SI, nascondi note pareggiate :  come l'opzione 1 ma in più fa in modo che le partite relative ai documenti con cui si esegue il pareggio (tipicamente note credito) non siano più visualizzate.
-- Default - NO :  lasciando il campo vuoto verranno visualizzate entrambe le partite e come descrizione della registrazione sarà riportata la causale di pareggio partite.
- Importo netto ritenuta :  E' un campo sì/no, se impostato a 1 (sì) permette di visualizzare gli importi delle partite a netto della ritenuta d'acconto
- Ometto rate pareggio? :  E' un campo sì/no, se impostato a 1 (sì) vengono nascoste
- Note? Permette di visualizzare le diverse tipologie di note all'interno del partitario. Le opzioni disponibili sono : 
-- Default - NO :  non visualizza nessuna nota
-- 2 - Note delle rate
-- 3 - Note delle righe
-- 4 - Note delle rate e delle righe
-- 5 - Note di testata
-- 6 - Tutte le note
- Visualizza :  nel caso in cui venga richiesta la visualizzazione delle note permette di definire se queste devono essere presentate completamente, se deve essere mostrato solo un prologo oppure se è necessario evidenziarne solo la presenza.
- Note Anagrafica :  permette di visualizzare o meno le note presenti sull'anagrafica dell'ente
- Costo pagamento? Permette di visualizzare uno dei costi associabili al pagamento. Le opzioni disponibili sono : 
-- Default - Nessun :  non calcola ne riporta nessuna tipologia di costo
-- 1 - Costo pagamento : 
-- 2 - Costo ritardo pagamento :   i valori per il calcolo di questo costo sono definiti nella tabella C51
-- 3 - Costi di incasso :   i valori per il calcolo di questo costo sono definiti nella tabella PAG.
- Importo riga registrazione? E' un campo sì/no, se impostato a 1 (sì) permette di visualizzare l'importo della riga della registrazione. Ad esempio nel caso di un oagamento a fornitore che salda più rate e qiuindi chiude più partite su ogni singola rata di pagato sarà roiportato oltre all'importo della rata stessa anche l'importo totale presente nella registrazione.
- Totale riepilogativo? Permette di visualizzare o meno una sintesi riepilogativa ai piedi del partitario. Le opzioni disponibili sono : 
-- Default - Sì
-- 2- No.
-- 3 - Solo totale :  visualizza solo la sintesi riepilogativa e non il dettaglio delle partite.
- Riepilogo natura pagamento :  è un campo sì/no, se impostato a 1 (sì) permette di ottenere una sintesi per natura pagamento del partitario
- Ometto saldo intestazione :  è un campo sì/no, se impostato a 1 (sì) nasconde il saldo presente nell'intestazione del partitario
- Responsabile credito? E' un campo sì/no, se impostato a 1 (sì)
- Escludi portafoglio. E' un campo sì/no, se impostato a 1 (sì) esclude dalla visualizzazione le rate già inserite all'interno di un portafoglio.
- Fatture a zero? E' un campo sì/no, se impostato a 1 (sì) visualizza anche registrazioni di documenti sull'ente con importo nullo.
- Ometti data/utente. E' un campo sì/no, se impostato a 1 (sì) in fase di stampa vengono omessi la data e l'utente di lancio.


All'interno delle impostazioni sono disponibili le memorizzazioni video attraverso cui e' possibile salvare una specifica configurazione delle impostazioni : 

![C5C010_072](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_072.png)
Le memorizzazioni salvate saranno poi richiamabili direttamente dal formato guida attraverso l'utilizzo dei caratteri di ricerca all'interno dello specifico campo : 

![C5C010_073](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_073.png)
Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

### Parzializzazioni

Digitando il tasto F13 o il relativo pulsante è possibile accedere alle parzializzazioni : 

![C5D030_013](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORRP/C5D030_013.png)
Sono disponibili due videate di parzializzazioni; per accedere alla seconda videata è sufficiente digitare il tasto F13 dalla prima videata.

### Tasti funzionali

 * F06 :  Conferma. Permette di confermare ed eseguire la funzione
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

### Memorizzazioni

Le memorizzazioni consentono di salvare le parametrizzazioni definite all'interno della videata. Per maggiori dettagli sulla loro creazione e gestione si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

## Formato lista

All'interno del formato lista è riportato l'elenco delle rate associate all'ente raggruppate per partita, ovvero per documento che le ha generate : 

![C5D010_026](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORRP/C5D010_026.png)
Nella parte superiore della videata sono riportati i parametri impostati nel formato guida e i saldi dell'ente alla data impostata nel formato guida e ad oggi.
Per ogni partita è riportata l'indicazione del numero della partita (ovvero del numero documento) e la sua data. Immediatamente sotto queste indicazioni è riportato il dettaglio delle rate che sono associate alla partita. Le informazioni visualizzate per ogni rata variano al variare delle impostazioni definite e possono essere personalizzate in funzione delle esigenze dello specifico utente. Nell'immagine riportata sopra per ogni rata sono riportati :  data registrazione, data scadenza, importo dovuto o pagato, importo residuo, tipo e descrizione del pagamento, causale contabile e numero registrazione contabile (formato da numero di registrazione + numero di riga).

### Opzioni

Per ogni partita sono disponibili le seguenti opzioni : 
![C5D010_030](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORRP/C5D010_030.png)
 * _2_56 - Per partita :  permette di visualizzare il dettaglio della singola partita, mostra quindi una vista della sola partita raggruppando data registrazione e pagamento.
 * _2_57 - Per scadenza :  permette di aprire una vista sulla partita dettagliando per scadenza.
 * _2_58 - Per data :  mostra una vista per data, ordinando per data registrazione.

Sulle singole rate sono invece disponibili le seguenti opzioni : 
![C5D010_026](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORRP/C5D010_026.png)
 * _2_P - pareggia residuo minimo :  la "P" deve esser eposta su almeno 2 rate di dovuto per poterle pareggiare. Per esempio se ho due rate una da 100 e una da -50, mettendo la P sulle 2 rate queste vengono chiuse per il valore minimo 50.
 * _2_R - pareggia residuo massimo :  la "R" posta su almeno 2 rate di dovuto permette di pareggiarle al valore assoluto massimo, ovvero al contrario dell'opzione sopra. Quindi se riproponiamo l'esempio presentato sopra, avendo 2 rate una da 100 e una da -50 l'importo per il quale verranno chiuse le rate è il più alto (100 nel nostro esempio).
 * _2_S - scollega pagato :  questa opzione scollega la rata di pagato collegata ad una di dovuto.
 * _2_16 - Scontabilizza emissione effetto :  permette di cancellare la registrazione di contabilizzazione dell'effetto nel portafoglio effetti aziendale, ovviamente prima che sia stata fatta la distinta.
 * _2_SR - Scadenzario residuo :  permette di aprire lo scadenziario residuo relativo a quel soggetto.
 * _2_01 - Inserisci registrazione :  permette di accedere al data entry della prima nota e inserire una nuova registrazione.

 * _2_02 - Modifica registrazione :  permette di entrare in modifica della registrazione relativa alla scadenza su cui si digita l'opzione.

 * _2_04 - Cancella registrazione :  permette di cancellare la registrazione relativa alla scadenza su cui si digita l'opzione.

 * _2_05 - Interrogazione registrazione :  permette di visualizzare la registrazione relativa alla scadenza.

 * _2_06 - Stampa registrazione :  permette di stampare la registrazione relativa alla scadenza.

 * _2_10 - Anteprima estratto conto :  permette di visualizzare l'anteprima della lettera di estratto conto stampabile per il soggetto.

* _2_12 - Modifica rata :  entra direttamente in gestione della rata su cui si digita l'opzione.

 * _2_15 - Interrogazione rata :  permette di visualizzare la rata su cui viene digitata l'opzione.

 * _2_17 - Stampa lettera insoluto :  nl caso in cui si tratti di una rata insoluta attraverso questa opzione è possibile stampare una letterea da inviare al cliente insolvente.

 * _2_20 - Stampa lettera estratto conto :  permette di stampare una lettera intestata al soggetto e riportante il dettaglio delle scadenze in essere per il soggetto stesso.

 * _2_22 - Aggiungi a proposta pagamento :  permette di aggiungere il pagamento a una proposta di pagamento.

 * _2_24 - Rimuovi da proposta pagamento :  permette di eliminare la rata precedentemente assegnata ad una proposta di pagamento.

 * _2_31 - Crea nuova pratica :  permette di creare una nuova distinta includendo la rata su cui viene digitata l'opzione. Digitando l'opzione verrà richiestq la tipologia di distinta da creare, il sistema in automatico presenterà solo le tipologie di distinte compatibili con il tipo pagamento della rata su cui viene digitata l'opzione.

 * _2_32 - Aggiungi a pratica :  permette di aggiungere la rata a una distinta precedentemente creata.

 * _2_34 - Rimuovi da pratica :  per le rate già assegnate a una distinta permette di estrarle dalla distinta stessa. Il comando è disponibile solo nel caso inc ui la distinta nonsia ancora contabilizzata.

 * _2_62 - Modifica note registrazione :  permette di aprire direttamente la gestione delle note associate alla riga cntabile.

 * _2_65 - Interrogazione note registrazione :  permette di interrogare le eventuali note inserite sulla testata della registrazione.

 * _2_72 - Modifica note riga :  permette di modificare le note sulla riga della registrazione contabile.

 * _2_75 - Interrogazione note riga :  permette di visualizzare le note inserite sulla riga della registrazione contabile.

 * _2_82 - Modifica note rata :  permette di inserire o modificare le note associate alla rata su cui viene digitata l'opzione.

 * _2_85 - Interroga note rata :  permette di interrogare le note associate alla rata su cui viene digitata l'opzione.

* _2_AB - Creazione abbuono :  permette di creare, su partite aperte di limitato importo, una registrazione di abbuono. Con il comando F6 si aprirà una finestra per la creazione di questa registrazione, il conto di abbuono verrà automaticamente ripreso dagli automatismi impostati sugli abbuoni passivi e attivi.

* _2_DB - Dettaglio blocco pagamento :  permette di visualizzare il blocco eventualmente esercitato sulla rata.

 * _2_ES - Esito :  è opzionale ed è una funzione che permette di attribuire manualmente un esito agli effetti.

 * _2_MD - Mastrini dettaglio :  funzione rapida che consente di aprire in dettaglio il mastrino del soggetto.

 * _2_MM - Mastrini per mese :  è una funzione rapida per aprire il riepilogo mese per mese del mastrino del soggetto selezionato.

 * _2_MS - Mastrini dettaglio/fine mese :  permette di apire il dettaglio del mastrino con il dettaglio sui mesi, per quel soggetto.

 * _2_P - Pareggia :  permette di pareggiare rate di segno opposto. Per eseguire il pareggio è sufficiente mettere l'opzione P sulle rate da pareggiare (possono anche essere più di due) e confermare con F6.

* _2_PA - Partitario :  permette di passare direttamente all'interrogazione del partitario del soggetto.

 * _2_PG - Gruppi partite :  se la fattura è pareggiata con una nota di credito permette di visualizzare tutte le scadenze.

 * _2_RC - Scheda crediti/debiti :  permette di visualizzare la scheda crediti/debiti relativamente al soggetto.

 * _2_SC - Lettera cumulo per ente :  è una funzione applicabile ad una singola rata che se cumulata produce una stampa della lettera per il singolo ente designato.

 * _2_SP - Lettera cumulo per pratica :  stampa la lettera di cumolo per pratica, nel caso di rate cumulate per un ente anche su pratiche diverse.

 * _2_VP - Visualizzazione partita :  permette di visualizzare la partita relativa a questa scadenza.

 * _2_X1 - Modifica Scadenza : 

 * _2_XC -Campi rata :  relativamente alla rata permette di analizzare tutti i campi di quest'ultima.

 * _2_XD - Dettaglio rata :  è una funzione che permette di vedere il dettaglio della rata legata alla registrazione contabile.

* _2_YL - Controllo fatture :  permette di verificare quali documenti sono in attesa di fattura per il soggetto.


