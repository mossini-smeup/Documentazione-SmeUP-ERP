## Obiettivo
Attraverso questa funzione è possibile analizzare l'evoluzione futura del saldo dei rapporti bancari.

## Formato guida

Il formato guida si presenta nel seguente modo : 

![C5D030_016](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXS0/C5D030_016.png)
All'interno del formato guida è prima di tutto necessario selezionare l'azienda d'interesse e la modalità di esecuzione della funzione :  le modalità disponibili sono Interrogazione , Stampa, Trasferimento a PC e PDF. Le prime due modalità restituiscono lo stesso risultato rispettivamente in formato video e in spool di stampa mentre la terza permette di esportare i dati sul proprio PC all'interno di un file che può essere in formato txt o xls. L'ultima modlaità permetterà, invece, di visualizzare i dati all'interno di un file PDF.
I campi 'Pertinenza' e 'Condizione' devono essere compilati in funzione della tipologia di registrazioni che si vogliono considerare per l'analisi dell'evoluzione del saldo dei rapporti. In particolare nel campo Pertinenza è necessario indicare se considerare solo registrazioni gestionali, solo contabili o entrambe mentre nel campo Condizione è possibile indicare se considerare solo registrazioni attive, solo simulate o entrambe.
La 'Data partenza' rappresenta l'inizio del periodo all'interno del quale analizzare l'evoluzione dei saldi.
Nel campo 'Periodicità' è necessario definire la periodicità con cui si voglia siano restituiti i dati. La periodicità è definita nella tabella A£Q e caratterizza dal punto di vista temporale le colonne in cui saranno esposti i dati. E' possibile utilizzare periodi con durata fissa (es. giorni, settimane, mesi,ecc.) o variabile (es. 10 giorni con analisi giornaliera, successivamente analisi settimanale per 3 settimane e infine analisi mensile).
Nel campo 'Tipo rapporto' è possibile specificare quale tipologia di rapporto visualizzare (es. solo salvo buon fine o solo conto corrente).
Il campo 'Codice banca' viene compilato nel caso in cui si vogliano visualizzare solamente i rapporti di una specifica banca.

### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Ometto dettaglio :  attraverso questo campo è possibile visualizzare o meno il dettaglio per rapporto bancario. Omettendo il dettaglio, quindi, verranno resituite solamente le informazioni a livello di banca e non a livello di rapporto bancario.
 * Ordinamento :  permette di definire l'ordinamento di visualizzazione dei record; le scelte disponibili sono per tipo rapporto/banca oppure per banca/tipo rapporto.
 * Solo valorizzati :  permette di visualizzare solamente i rapporti con valori non nulli.
 * Separazione simulati :  attraverso questo campo è possibile vedere le informazioni suddivise tra registrazioni simulate e registrazioni definitive :  sarà, quindi, possibile visualizzare l'evoluzione dei saldi che considera le sole registrazioni definitve, quella che considera solo le simulate e quella totale.
 * Separazione stimati :  permette di visualizzare su due righe il saldo imputabile a sole registrazioni attive e il saldo imputabile sia a registrazioni attive che simulate.
 * Data trattata :  permette di impostare come data analizzata la data valuta o la data operazione
 * Saldo disponibile :  consente di visualizzare sia il saldo liquido che quello disponibile (ovvero la somma tra fido e saldo liquido).
 * Presenta interessi :  consente di visualizzare per ogni rapporto bancario il valore degli interessi impostato nell'anagrafica del rapporto stesso.
 * Conto fronteggiato :  permette di visualizzare il rapporto bancario collegato a quello visualizzato in lista. Ad esempio se nella tabella C5J ho indicato su un rapporto di conto corrente il rapporto di salvo buon fine collegato potrò visualizzare sia l'evoluzione dei saldi del rapporto di conto corrente che quella del salvo buon fine.
 * Divisore :  permette di definire se dividere i dati visualizzati in migliaia o milioni oppure se vederli interi.

### Tasti funzionali

- F11 Parametri di esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
- F17 Impostazioni. Permette di accedere alla schermata delle impostazioni


Confermando il formato guida è possibile accedere al formato lista.

## Formato lista
All'interno del formato lista è possibile visualizzare per ogni rapporto bancario (oppure per ogni banca se si è deciso di omettere il dettaglio) l'evoluzione del suo saldo : 

![C5D030_017](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXS0/C5D030_017.png)
Come mostrato dall'immagine, per ogni rapporto bancario è visualizzata l'evoluzione del suo saldo nel tempo. La periodicità delle colonne è definita all'interno del formato guida e per ogni periodo sono riportati il fido, il saldo liquido e il saldo disponibile (nel caso in cui all'interno delle impostazioni si sia richiesto di visualizzare anche il saldo disponibile).
Se all'interno delle impostazioni viene richiesto di visualizzare le registrazioni simulate separatamente da quelle attive, per ogni rapporto bancario saranno riportate tre righe :  la prima identificata con una D riporta le registrazioni definitive, la seconda identificata con una S quelle simulate e la terza identificata da una T la somma delle due precedenti : 

![C5D030_020](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXS0/C5D030_020.png)
Se invece viene richiesto di visualizzare i valori stimati in modo separato nel formato lista saranno riportate due righe :  la prima che considera le sole registrazioni attive e la seconda che considera sia le attive che le simulate : 

![C5D030_021](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXS0/C5D030_021.png)
In fondo alla schermata è riportato anche il totale per azienda.
Attraverso il tasto F1 è possibile effettuare una ricerca all'interno della lista :  digitando una stringa questa verrà, infatti, ricercata all'interno dell'elenco e verrà restituita la prima istanza trovata. Attraverso i tasti F9 e F10 sarà poi possibile passare all'istanza precedente o successiva.

## Formato dettaglio
Per ognuno dei rapporti bancari visualizzato nel formato lista sono disponibili alcune opzioni : 

 * 02 Modifica elemento tabella :  permette di accedere in modifica all'elemento della C5J che definisce il rapporto bancario
 * 05 Interrogazione elemento tabella :  permette di accedere in visualizzazione all'elemento della C5J che definisce il rapporto bancario
 * 22 Gestione parametri :  visualizza e permette di modificare i parametri dell'elemento della C5J che definisce il rapporto bancario
 * 32 Gestione condizioni :  visualizza il formato guida per la gestione delle condizioni del rapporto selezionato
 * CS Castelletto :  sui rapporti di salvo buon fine permette di visualizzare l'evoluzione del castelletto
 * MC Estratto conto :  consente di visualizzare il mastrino del conto contabile associato al rapporto bancario ordinato per data registrazione
 * MI Scalare interessi :  se per il rapporto bancario selezionato sono impostati i parametri per il calcolo dello scalare interessi questo viene visualizzato alla selezione di questa opzione.
 * MV Proiezione in valuta :  consente di visualizzare il mastrino del conto contabile associato al rapporto bancario ordinato per data valuta
