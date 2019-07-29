## Obiettivo
Attraverso questa funzione è possibile analizzare l'evoluzione futura del castelletto aziendale.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D030_018](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXS0C/C5D030_018.png)
All'interno del formato guida è prima di tutto necessario selezionare l'azienda d'interesse e la modalità di esecuzione della funzione :  le modalità disponibili sono Interrogazione , Stampa e Trasferimento a PC. Le prime due modalità restituiscono lo stesso risultato rispettivamente in formato video e in spool di stampa mentre la terza permette di esportare i dati sul proprio PC all'interno di un file che può essere in formato txt o xls.
I campi 'Pertinenza' e 'Condizione' devono essere compilati in funzione della tipologia di registrazioni che si vogliono considerare perl'analisi dell'evoluzione del saldo del castelletto. In particolare nel campo Pertinenza è necessario indicare se considerare solo registrazioni gestionali, solo contabili o entrambe mentre nel campo Condizione è possibile indicare se considerare solo registrazioni attive, solo simulate o entrambe.
La 'Data partenza' rappresenta l'inizio del periodo all'interno del quale analizzare l'evoluzione dei saldi. Nel caso in cui non venga indicata nessuna data viene considerata la data odierna come partenza per l'analisi dei dati.
Nel campo 'Periodicità' è necessario definire la periodicità con cui si voglia siano restituiti i dati. La periodicità è definita nella tabella A£Q e caratterizza dal punto di vista temporale le colonne in cui saranno esposti i dati. E' possibile utilizzare periodi con durata fissa (es. giorni, settimane, mesi,ecc.) o variabile (es. 10 gironi con analisi giornaliera, successivamente analisi settimanale per 3 settimane e infine analisi mensile).
Il campo 'Tipo rapporto' non è significativo per questa interrogazione in quanto vengono considerati validi solo i rapporti di salvo buon fine.
Il campo 'Codice banca' viene compilato nel caso in cui si voglia visualizzare solamente il castelletto di una specifica banca.

Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Ometto dettaglio :  attraverso questo campo è possibile visualizzare o meno il dettaglio per rapporto bancario. Omettendo il dettaglio, quindi, verranno resituite solamente le informazioni a livello di banca e non a livello di rapporto bancario.
 * Ordinamento :  permette di definire l'ordinamento di visualizzazione dei record; le scelte disponibili sono per tipo rapporto/banca oppure per banca/tipo rapporto.
 * Solo valorizzati :  permette di visualizzare solamente i rapporti con valori non nulli.

Confermando il formato guida è possibile accedere al formato lista.

## Formato lista
All'interno del formato lista è possibile visualizzare per ogni rapporto bancario di salvo buon fine (oppure per ogni banca se si è deciso di omettere il dettaglio) l'evoluzione del castelletto : 

![C5D030_019](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXS0C/C5D030_019.png)
## Formato dettaglio
Per ognuno dei record visualizzato nel formato lista sono disponibili alcune opzioni : 

 * 02 Modifica elemento tabella :  permette di accedere in modifica all'elemento della C5J che definisce il rapporto bancario
 * 05 Interrogazione elemento tabella :  permette di accedere in visualizzazione all'elemento della C5J che definisce il rapporto bancario
 * 22 Gestione parametri :  visualizza e permette di modificare i parametri dell'elemento della C5J che definisce il rapporto bancario
 * 32 Gestione condizioni :  visualizza il formato guida per la gestione delle condizioni del rapporto selezionato
 * CS Castelletto :  sui rapporti di salvo buon fine permette di visualizzare l'evoluzione del castelletto
 * MC Estratto conto :  consente di visualizzare il mastrino del conto contabile associato al rapporto bancario ordinato per data registrazione
 * MI Scalare interessi :  se per il rapporto bancario selezionato sono impostati i parametri per il calcolo dello scalare interessi questo viene visualizzato alla selezione di questa opzione.
 * MV Proiezione in valuta :  consente di visualizzare il mastrino del conto contabile associato al rapporto bancario ordinato per data valuta
