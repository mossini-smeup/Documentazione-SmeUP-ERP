## Scheda Analisi di due valori nel tempo
La scheda permette si analizzare l'andamento nel tempo di una o due serie di valori. La scheda è generica e quindi può essere applicata a fenomeni diversi :  uno degli utilizzi possibili è collegato all'analisi delle statistiche V5 a cui faremo riferimento nel seguito della spiegazione.

## La scheda
All'apertura la scheda si presenta nel modo seguente : 


![LOA02_001](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_001.png)
 * Nella sezione denominata _2_vista vengono elencati i tipi di valori disponibili per l'interrogazione, quando viene selezionato un valore nella parte di destra viene emesso il corrispondnete report. Le viste hanno la seguente classificazione : 
 ** _3_Valori base, sono le due serie passate, più la somma, calcolata, dei valori della prima e della seconda serie
 ** _3_Medie, sono le medie e la numerosità, calcolate, dei valori delle due serie
 ** _3_Aumenti, mostra l'incremento (qtà o percentuale) rispetto al periodo precedente (il periodo è quello della riga precedente, es. se in orizzontale i periodi sono gli anni questa funzione mostra gli aumenti rispetto all'anno precedente)
 ** _3_Incidenze, calcola l'incidenza percentuale del valore rispetto a : 
 *** _1_totale, gran totale (colonne / righe)
 *** _1_colonna, totale di colonna
 *** _1_riga, totale di riga
 * Nelle sezioni denominate _2_verticale e orizzontale ci sono gli sviluppi temporali (tutti gli attributi delle date presenti nei dati in input) che possono essere utilizzati nelle analisi. Se non vengono effettuate selezioni il programma propone l'anno come sviluppo verticale e il trimestre come sviluppo orizzontale.
 * Nella sezione di destra, _2_gestione di un piano vengono presentati i vari report disponibili. Le stesse visualizzazioni sono visibili cliccando il tab. "Gestione di un piano" della scheda.

## Gestione di un piano
Questa sezione della scheda è preposta alla visualizzazione, nei vari formati, del risultato della selezione eseguita su Vista, Verticale, Orizzontale.

### Visualizzazione Valore scelto
Mostra il valore selezionato in Vista secondo gli assi verticale / orizzontale scelti : 
![LOA02_002](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_002.png)
Nell'esempio viene visualizzato l'importo netto mensile nei vari anni presenti nelle statistiche.

### Visualizzazione Grafico
Riporta i valori precedenti in una forma grafica.
![LOA02_003](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_003.png)
### Visualizzazione Dettaglio per data
Mostra i record in dettaglio, ordinati per data di riferimento : 
![LOA02_004](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_004.png)
Nell'esempio viene visualizzato l'importo netto mensile nei vari anni presenti nelle statistiche.

### Visualizzazione Dettaglio dei valori
Riporta i valori precedenti in froma di matrice dove nella prima colonna ci sono i valori dell'ordinamento verticale, nella seconda colonna quelli dell'ordinamento orizzontale, nella taerza il valore selezionato in "Vista" : 
![LOA02_005](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_005.png)
### Visualizzazione Andamento
Mostra il grafico dell'andamento dei valori nei vari periodi. Sono calcolati e visualizzati anche la media mobile e la media aritmetica : 
![LOA02_007](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_007.png)
La visualizzazione tabellare mostra i valori del grafico in forma di matrice : 
![LOA02_006](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_006.png)
### Visualizzazione Forme di dettaglio
Mostra i valori della vista.
La visualizzazione "una riga" richiede che venga selezionato un elemento del raggruppamento verticale : 
![LOA02_008](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_008.png)La visualizzazione "una colonna" richiede che venga selezionato un elemento del raggruppamento orizzontale : 
![LOA02_009](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_009.png)La visualizzazione "tabella completa" presenta i dati di tutti i raggruppamenti verticali e orizzontali : 
![LOA02_010](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_010.png)La visualizzazione "dettaglio dei valori" presenta i dati di dettaglio in  forma di matrice : 
![LOA02_011](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_011.png)
### Visualizzazione Analisi della serie
Esegue una serie di analisi statistiche che possono venire rappresentate graficamente oppure in forma tabellare, tra queste abbiamo : 


- _2_Analisi, mostra il grafico

![LOA02_012](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_012.png)

- _2_Gaussiana, rappresenta graficamente la curva gaussiana che più si avvicina ai dati presenti

![LOA02_013](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_013.png)

- _2_Previsione - Regressione lineare, esegue una previsione sui periodi futuri con il metodo della regressione lineare

![LOA02_014](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_014.png)

- _2_Previsione - Holt Winters, esegue una previsione sui periodi futuri con il metodo di Holt Winters

![LOA02_015](http://localhost:3000/immagini/MBDOC_OGG-V2LOCOSA02/LOA02_015.png)