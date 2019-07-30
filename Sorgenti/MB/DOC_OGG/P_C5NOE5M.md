## Obiettivo

Attraverso questa funzione è possibile analizzare il mastrino contabile di un oggetto che può essere un conto contabile, un cliente, un fornitore, un agente, ecc. Attraverso questa funzione è anche possibile analizzare il mastrino di una lista di oggetti.

Per mastrino intendiamo l'elenco cronologico delle registrazioni contabili che possono essere ordinate secondo criteri che variano al variare dell'oggetto analizzato :  ad esempio per un conto bancario potremmo avere un ordinamento per data registrazione o per data valuta mentre per un ente l'ordinamento standard è quello per data registrazione.

## Formato guida

Il formato guida si presenta nel seguente modo : 

![C5C010_069](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE5M/C5C010_069.png)
All'interno del formato guida è necessario specificare i seguenti campi : 

 - Codice dell'oggetto o della lista di oggetti di cui si voglia analizzare il mastrino. La compilazione di questo campo è facilitata dalla presenza dei classici caratteri di ricerca. Per maggiori informazioni su questi caratteri si veda il seguente : 

- [Ricerche](Sorgenti/MB/DOC_OPE/B£_RIC)
Per dettagli sull'utilizzo delle liste oggetti si veda invece : 
- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)

 - Funzione. Per l'analisi dei mastrini questo campo deve essere impostato a M
 - Metodo. Sono disponibili diversi metodi per l'analisi dei mastrini : 
 -- D - Dettaglio. Consente di ottenere il dettaglio delle registrazioni contabili
 -- S - Detaglio + Fine mese.  Consente di ottenere oltre al dettaglio delle registrazioni contabili un totale mensile.
 -- M - Riepilogo Fine mese. Consente di ottenere il solo totale mensile delle registrazioni contabili.
 -- P - Per documento (disponibile solo per i conti contabili). Visualizza le registrazioni contabili ordinate per numero e data documento. Si tratta di una sorta di partitario del conto contabile; per essere visualizzato è necessario che il conto contabile sia gestito a documenti.
 -- C - Estratto conto (disponibile solo per i conti contabili). Visualizza le registrazioni contabili ordinate per data operazione bancaria.
 -- I - Scalare interessi (disponibile solo per i conti contabili). Visualizza lo scalare interessi del conto contabile.
 -- V - Proiezione in valuta (disponibile solo per i conti contabili). Visualizza le registrazioni contabili ordinate per data valuta bancaria.
 - Modalità. In questo campo è necessario indicare il tipo di output desiderato. Le modalità disponibili per l'esecuzione di questa funzione sono : 
 -- 1 - Stampa :  permette di stampare il mastrino contabile.
 -- 2 - Interrogazione (non disponibile per liste di oggetti) :  permette di visualizzare il mastrino.
 -- 4 - Trasferimento PC :  permette di esportare un file su PC contenente il mastrino.
 -- 7 - PDF :  permette di stampare il mastrino all'interno di un file PDF.
 - Pertinenza. In questo campo è necessario indicare se all'interno del mastrino si vogliono visualizzare le sole registrazioni fiscali, le sole gestionali o entrambe.
 - Condizione. In questo campo è necessario indicare se all'interno del mastrino si vogliono visualizzare le sole registrazioni attive, le sole simulate o entrambe. Per maggiori dettagli sulla definizione e utilizzo della pertinenza e condizione nelle registrazioni contabili si veda il seguente : 

 :  : DEC T(MB) P(DOC_VOC) K(GLO_C5) I(Glossario Contabilità) L(1)

 - Esercizio. In questo campo è necessario indicare l'esercizio contabile per il quale si voglia analizzare il mastrino contabile. All'interno delle impostazioni è poi possibile definire un range di più esercizi che si vogliano analizzare.
 - Da data registrazione / A data registrazione. In questi campi è possibile definire un range temporale all'interno del quale visualizzare le registrazioni contabili. E' possibile compilare anche uno solo dei due campi. Ad esempio, impostando il primo campo con 01/02/2010 sarà possibile visualizzare le registrazioni con data maggiore o uguale al 01/02/2010.
 - Saldo alla data. Attraverso questo campo è possibile ottenere il valore del saldo dell'oggetto a una specifica data.


### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
![C5C010_070](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE5M/C5C010_070.png)
 - Mostra apertura/chiusura. Permette di mostrare ed eventualmente sommare il saldo dell'apertura/chiusura dell'oggetto all'interno del valore progressivo. I valori disponibili sono : 
 -- Default :  se il campo non viene compilato verranno visualizzati gli importi del saldo di apertura e chiusura. Inoltre, il valore progressivo sarà calcolato considerando anche questi valori.
 -- 2 - Mostra ma non sommare in progressivo :  i saldi di apertura e chiusura verranno mostrati ma non considerati per il calcolo del valore progressivo. In questo modo l'importo progressivo riporterà il progressivo dell'esercizio, senza considerare gli importi derivanti da esercizi precedenti.
 -- 3 - No apertura/chiusura :  i saldi di apertura/chiusura non verranno mostrati ne considerati per il calcolo del valore progressivo.
 -- 4 - Registrazioni contabili :  permette di visualizzare le registrazioni contabili di apertura e chiusura dell'esercizio contabile.
 -- 5 - Mostra solo apertura e chiusura :  permette di visualizzare solo le registrazioni contabili di apertura e chiusura dell'esercizio contabile.
 -- 6 - Mostra registrazioni chiusura :  permette di visualizzare oltre alle registrazioni contabili la registrazione di chiusura dell'esercizio contabile.
 -- 7 - Mostra registrazioni apertura :  permette di visualizzare oltre alle registrazioni contabili la registrazione di apertura dell'esercizio contabile.
 - Ometti saldo iniziale. E' un campo sì/no, se impostato a 1 (sì) non verrà visualizzato ne conteggiato nel valore progressivo il saldo iniziale del mastrino.
 - Causali. Se impostata verranno visualizzate le sole registrazioni contabili la cui causale sia presente all'interno della lista. Per l'impostazione di una lista di valori si veda il seguente : 

- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)

 - Escludi gestionali stornate. E' un campo sì/no, se impostato a 1 (sì) non verranno visualizzate le registrazioni gestionali stornate.
 - Tipo ente intestatario. Permette di visualizzare le sole registrazioni che abbiano in testata un ente della tipologia impostata in questo campo.
 - Codice ente intestatario. Permette di visualizzare le sole registrazioni che abbiano in testata l'ente indicato in questo campo.
 - Lista ente intestatario. Permette di definire una lista di enti; se impostata la lista verranno visualizzate le sole registrazioni che abbiano in testata uno degli enti della lista. Per l'impostazione di una lista di valori si veda il seguente : 

- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)

 - Solo intercompany. E'un campo sì/no, se impostato a 1 (sì) verranno visualizzate le registrazioni intercompany.
 - Singola contropartita. Indicando il codice di un conto contabile permette di eseguire un filtro sulle registrazioni contabili al cui interno sia riportato come contropartita il conto indicato.
 - Numero esercizi precedenti. Impostando questo campo con un numero X oltre all'esercizio impostato nel formato guida verrà presentato il mastrino degli X esercizi precedenti. Quindi, se ad esempio nel formato guida è impostato l'esercizio 2009 e questo campo viene impostato con 2 verranno visualizzati i mastrini degli esercizi 2007, 2008 e 2009.
 - Analisi esercizi precedenti. In questo campo viene definita la tipologia di analisi desiderata per gli esercizi precedenti; i valori possibili sono : 
 -- Default - Solo saldo. Per gli esercizi precedenti viene visualizzato solo il saldo finale.
 -- 2 - Completa da data a data. Viene presentato il mastrino dettagliato degli esercizi precedenti; inoltre se nel formato guida vengono impostati i campi 'Da data registrazione/A data registrazione' questi vengono considerati anche per l'analisi degli esercizi precedenti.
 -- 3 - Completa - Esercizio. Viene presentato il mastrino dettagliato degli esercizi precedenti; se nel formato guida vengono impostati i campi 'Da data registrazione/A data registrazione' questi non vengono considerati per l'analisi degli esercizi precedenti per i quali viene mostrato l'intero esercizio.
 - Fatture a zero? E' un campo sì/no, se impostato a 1 (sì) verranno visualizzate anche le registrazioni con importo 0.
 - Impostazioni generali.
 - Metodo dettaglio. Permette di definire alcune informazioni di dettaglio visualizzate all'interno del mastrino; le opzioni disponibili sono : 
 -- Default - D/A 1 colonna + Saldo + Contropartita. Viene visualizzata una colonna  con l'importo e il segno della registrazione, una colonna con il valore del saldo progressivo e nell'ultima colonna sarà riportata la contropartita della registrazione contabile (nel caso in cui fossero presenti più contropartite viene definito nei campi sotto quale sia visualizzata).
 -- 2 - D/A in 2 colonne + Saldo. Viene visualizzata una colonna  con gli importi in dare, una colonna con gli importi in avere e una colonna con il valore del saldo progressivo.
 -- 3 - Saldo + D/A in due colonne. Viene visualizzata una colonna con il valore del saldo progressivo, una colonna con gli importi in dare e una colonna con gli importi in avere.
 -- 4 - D/A in una colonna + Saldo + Controvaluta. Viene visualizzata una colonna  con l'importo e il segno della registrazione, una colonna con il valore del saldo progressivo e nell'ultima colonna sarà riportato il controvalore in euro della registrazione contabile.
 -- 5 - D/A in una colonna + Saldo + Registrazione.  Viene visualizzata una colonna  con l'importo e il segno della registrazione, una colonna con il valore del saldo progressivo e nell'ultima colonna sarà riportato il numero della registrazione contabile.
 -- 6 - Schema. Permette di personalizzare le informazioni visualizzate attraverso la definizione di uno schema utente. Lo schema da utlizzare sarà impostato nel campo subito sotto.
 - Schema. Attraverso questo campo è possibile definire lo schema utente da utilizzare per la visualizzazione delle informazioni di dettaglio. Per maggiori infromazioni sull'impostazione e utilizzo di schemi utente si veda il seguente : 

- [Schemi di visualizzazione e stampa](Sorgenti/MB/DOC_OPE/B£_SCH)

 - Valuta di conto. E' un campo sì/no, se impostato a 1 (sì) e il conto è in valuta verranno visualizzate le registrazioni in euro.
 - Note. Permette di visualizzare o meno le note delle registrazioni contabili. Le opzioni disponibili sono : 
 -- Default - No. Se il campo viene lasciato bianco non verranno visualizzate le note.
 -- 2 - Note delle righe. Vengono visualizzate le note scritte sulle righe delle registrazioni contabili.
 -- 3 - Note delle testate. Vengono visualizzate le note scritte sulle testate delle registrazioni contabili.
 -- 4 - Note delle testate e delle righe. Vengono visualizzate sia le note scritte sulle testate che quelle riportate sulle righe delle registrazioni contabili.
 - Dettaglio analitica. E' un campo sì/no, se valorizzato con sì viene visualizzato anche il dettaglio analitico delle registrazioni contabili.
 - Dettaglio rate. E' un campo sì/no, se valorizzato con sì viene visualizzato anche il dettaglio delle rate associate alle registrazioni contabili.
 - Informazioni aggiuntive. Attraverso questo campo è possibile richiedere la visualizzazione di alcune informazioni aggiuntive relative alla registrazione contabile. Le opzioni disponibili sono : 
 -- Default - Nessuna. Se il campo viene lasciato bianco non viene visualizzata nessuna informazione agguntiva della registrazione contabile.
 -- 2- Descrizione e protocollo/Soggetto. Vengono visualizzati data e numero protocollo oltre al codice e alla descrizione dell'ente intestario che compare sui mastrini dei conti contabili. Oltre a queste informazioni compare la descrizione aggiuntiva riportata sulla registrazione contabile.
 -- 3 - Protocollo/Soggetto. Vengono visualizzati data e numero protocollo oltre al codice e alla descrizione dell'ente intestario che compare sui mastrini dei conti contabili.
 -- 4 - Descrizione. Permette di visualizzare la descrizione aggiuntiva riportata sulla registrazione contabile.
 - Sintesi. Permette di ottenere in coda al mastrino una sintesi dei valori presentati. Le sintesi disponibili sono : 
 -- Default - Nessuna. Se il campo non viene compilato non viene presentata nessuna sintesi.
 -- 2 - Data/Numero documento.
 -- 3 - Contropartita.
 -- 4 - Causale.
 -- 5 - Valuta.
 -- 6 - Soggetto.
 -- 7 - Società Intercompany.
 -- 8 - Società origine.
 -- 9 - Conto.
 -- A - Attributo soggetto. E' possibile ottenere una sintesi per un attributo del soggetto che viene definito nel campo immediatamente sotto.
 -- Attributo oggetto. Nel caso in cui si sia scelta una sintesi per attributo soggetto in questo campo è necessario indicare l'attributo scelto (es. categoria contabile, nazionalità, ecc.)
 - Solo sintesi? E' un campo sì/no, se compilato con sì viene visualizzata solo una sintesi impostata nei campi sopra.
 - Ordinamento sintesi. E' possibile definire se visualizzare la sintesi per codice oppure per importo.
 - Contropartita. Permette di visualizzare la/e contropartita/e della registrazione contabile
 - Più contropartite. se sono presenti più contropartite all'interno della registrazione contabile permette di definire quali e quante contropartite visualizzare. Le opzioni disponibili sono : 
 -- Default - Contropartita importo maggiore. Visualizza solo la contropartita con il valore maggiore.
 -- 2 - Diverse. Mostra le diverse contropartite della registrazione contabile.
 -- 3 - Tutte le contropartite. Mostra tutte le contropartite della registrazione contabile (nel caso in cui siano presenti più righe con una stessa contropartita questa verrà ripetuta più volte).
 -- 4 - Tutte le righe. Mostra tutte le righe della registrazione contabile e non solo le contropartite.
 - Saldo giornaliero. E' un campo sì/no, se compilato con sì viene visualizzato il saldo contabile giornaliero.
 - Ometti data/utente. E' un campo sì/no, se compilato con sì in fase di stampa vengono omessi la data e l'utente di lancio.
 - Saldo alla data. Definisce se il saldo deve essere visualizzato alla mattina o alla sera del giorno indicato. Visualizzando il saldo alla mattina, quindi non verranno inclusi i movimenti aventi data uguale a quella impostata; al contrario visualizzandolo alla sera questi movimenti verranno inclusi nella valorizzazione del saldo.
 - Ometto saldo intestazione.


All'interno delle impostazioni sono disponibili le memorizzazioni video attraverso cui e' possibile salvare una specifica configurazione delle impostazioni : 

![C5C010_072](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_072.png)
Le memorizzazioni salvate saranno poi richiamabili direttamente dal formato guida attraverso l'utilizzo dei caratteri di ricerca all'interno dello specifico campo : 

![C5C010_073](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_073.png)
Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OPE) Mem(C5BASE_01) Tag(Parzializazioni)

### Tasti funzionali

 * F06 :  Conferma. Permette di confermare ed eseguire la funzione
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

### Memorizzazioni

Le memorizzazioni consentono di salvare le parametrizzazioni definite all'interno della videata. Per maggiori dettagli sulla loro creazione e gestione si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)


## Formato lista

All'interno del formato lista è possibile visualizzare l'elenco delle registrazioni contabili in cui sia coinvolto l'oggetto in analisi : 

![C5C010_074](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE5M/C5C010_074.png)
Nella parte superiore della videata sono riportate alcune informazioni generali relative all'oggetto in analisi e alle opzioni definite nel formato guida; in particolare abbiamo : 
 * Codice e descrizione azienda
 * Codice e descrizione divisione
 * Saldo alla data iniziale del mastrino; quindi interrogando un mastrino dal 01/07/200X vedrò il saldo al 01/07/200X
 * Esercizio impostato nel formato guida
 * Estremi impostati nel formato guida relativamente alla data registrazione; se non viene impostato nessun limite il sistema in automatico imposta dal primo gennaio dell'esercizio indicato nel formato guida al 31/12/9999
 * Valore del saldo alla data impostata nel formato guida; se non viene impostata una specifica data di saldo viene evidenziato il saldo al 31/12/9999

Le informazioni visualizzate per ogni record del mastrino sono divisibili in due gruppi :  informazioni descrittive e valori. Le informazioni descrittive sono fisse e riportano : 
 * Pertinenza e condizione della registrazione contabile
 * Società intercompany associata alla registrazione
 * Data Registrazione
 * Data documento
 * Numero documento per mastrini di enti/Causale contabile per mastrini di conti

Per quanto riguarda i valori questi variano in funzione delle impostazioni definite come documentato all'interno di questo mauale.

Nel caso in cui la freccia in basso presente nella barra inferiore della videata sia evidenziata in giallo significa che non tutte le registrazioni sono state caricate e quindi visualizzate, per farlo è necessario premere sulla freccetta o digitare il tasto Page Down da tastiera : 

![C5C010_075](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE5M/C5C010_075.png)
Ai piedi della lista delle registrazioni contabili è riportato il saldo finale del mastrino.

### Opzioni

Per ognuna delle registrazioni presenti all'interno del mastrino sono disponibili le seguenti opzioni : 


 - 01 - Crea registrazione :  presenta il data entry per l'inserimento di una nuova registrazione contabile.
 - 02 - Modifica registrazione
 - 03 - Copia registrazione
 - 04 - Cancellazione registrazione :  permette di cancellare la registrazione contabile (viene prima richiesta una conferma).
 - 05 - Interrogazione registrazione
 - 06 - Stampa registrazione
 - 07 - Storno della registrazione
 - 08 - Gestione note testata :  permette di accedere alle note di testata della registrazione contabile ed eventualmente modificarle.
 - 09 - Controllo fatture
 - 12 - Modifica rate :  permette di accedere direttamente alle rate collegate alla registrazione contabile ed eventualmente modificarle.
 - 15 - Interrogazione rate :  permette di visualizzare le rate collegate alla registrazione contabile.
 - 18 - Gestione note riga :  permette di accedere alle note di riga della registrazione contabile ed eventualmente modificarle.
 - 22 - Modifica analitica :  permette di accedere ed eventualmente modificare l'analitica associata alla registrazione contabile.
 - 25 - Interrogazione analitica :  permette di visualizzare l'analitica associata alla registrazione contabile.
 - 26 - Passaggio a simulata :  nel caso in cui la registrazione sia attiva (condizione 6) permette di modificarne la condizione e farla diventare simulata.
 - 27 - Passaggio a attiva :  nel caso in cui la registrazione sia simulata (condizione inferiore a 3) permette di modificarne la condizione e farla diventare attiva.
 - 62 - Modifica note registrazione
 - 65 - Interrogazione note registrazione :  permette di visualizzare le note di testata della registrazione contabile.
 - 72 - Modifica note riga
 - 75 - Interrogazione note riga :  permette di visualizzare le note di riga della registrazione contabile.
 - A1 - Registrazione :  permette di visualizzare una sintesi dell'intera registrazione contabile che riporta informazioni di testata e contropartite presenti.
 - A2 - Registrazioni utente :  permette di visualizzare le registrazioni contabili inserite dall'utente.
 - MD - Mastrini Dettaglio :  permette di visualizzare il mastrino in modalità Dettaglio.
 - MS - Mastrini Dettaglio fine mese :  permette di visualizzare il mastrino in modalità Dettaglio+ Fine mese.
 - MM - Mastrini per mese :  permette di visualizzare il mastrino in modalità Riepilogo Fine mese.
 - PA - Partitario :  permette di accedere al partitario dell'oggetto (se si tratta di un conto contabile è possibile visualizzarne il partitario solo se il conto è gestito a partita).
 - XC - Campi testata :  permette di visualizzare le informazioni di dettaglio della testata della registrazione riportate su file.
 - XD - Dettaglio testata :  permette di visualizzare la testata della registrazione contabile.
 - X1 - Dettaglio riga :  permette di visualizzare il dettaglio della riga della registrazione contabile.
 - X2 - Campi riga :   permette di visualizzare le informazioni di dettaglio della riga della registrazione riportate su file.


### Tasti funzionali

 * F01 :  Permette di ricercare una stringa all'interno della videata
 * F05 :  Esegue l'aggiornamento della videata
 * F09 :  Permette di posizionarsi sulla prima pagina del mastrino
 * F10 :  Permette di posizionarsi sull'ultima pagina del mastrino
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.


