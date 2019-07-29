Attraverso le impostazioni è possibile definire i seguenti parametri : 
 * Livello massimo :  permette di definire a che livello di riclassifica visualizzare il bilancio. Ad esempio impostando il codice 01 si vedrà solo il primo livello di riclassifica, impostando 10 si vedrà il dettagliod ei conti contabili mentre impostando lasciando il campo vuoto si vedrà anche il dettaglio clienti /fornitori.
 * Omettere i conti a 0 :  permette di includere o meno i conti con valori nulli per tutte le colonne.
 * Struttura :  può essere impostata : 
 ** Ascendente :  vedrò prima i totalizzatori e in seguito i dettagli
 ** Discendente :  vedrò prima i dettagli e in seguito i totalizzatori
 ** Discendente con rottura :  vedrò i totalizzatori sia prima che doppo i dettagli e la loro valorizzazione nuemrica verrà fatta sotto i dettagli.
 * Separa livelli 1 e 2 :  permette di inserire delle righe di separazione tra i vari livelli delle riclassifiche.
 * Salto Pagina Livello 1 :  permette di stampare una nuova pagina ogni volta in cui cambia il livello 1 della riclassifica.
 * Visualizzazione :  permette di visualizzare gli importi interi o con i decimali.
 * Visualizz. desc. agg. :  permette di visualizzare la descrizione aggiuntiva della linea di riclassifica.
 * Stampa del piede :  permette di personalizzare il piede presentato in fase di stampa o generazione PDF.
 * Ver.Allin.Saldi Lv.Max
 * Note aggiuntive? permette di visualizzare le note riportate sulle linee di riclassifica
 * Modello Colonne :  permette di richiamare le valorizzazioni di colonne salvate nella Gestione colonne.
 * Gestione colonne :  questo è il parametro più significativo perchè permette di gestire le informazioni visualizzate nelle 6 colonne disponibili in fase di stampa (l'interrogazione, invece, mostrerà solo le prime 4 colonne). Il valore restituito all'interno di ciascuna colonna è definito attraverso una stringa costituita a sua volta da 5 sottostringhe. Impostando questo campo con 1 verrà visualizzata un'ulteriore videata in cui impostare i valori resituiti in ciascuna colonna : 
![C5E010_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5NAC11/C5E010_007.png)Digitando '!' all'interno di ciascuna colonna partirà la costruzione guidata del valore restituito all'interno della colonna stessa. Vediamo le scelte proposte dal sistema : 


 * DI - Diretto dell'esercizio in esame :  questo parametro permetterà di visualizzare valori dell'esercizio impostato nel formato guida. Quindi se nel formato guida avrò impostato esercizio 2013, scegliendo DI vedrò i valori dell'esercizio 2013.
 * CO - Costruito da periodi precedenti :  questo parametro permetterà di visualizzare valori di un periodo diverso da quello impostao nel formato guida. Quindi se nel formato guida avrò impostato data 31/03/2013, ma vorrò visualizzare i valori di Febbraio 2013, scegliendo CO e indicando dat 28/02/2013 vedrò i valori di Febbraio 2013.

Scegliendo una di queste due opzioni verrà presentata la scelta tra questi valori : 
 * PE - Relativo al periodo in esame :  restituisce i valori relativi del mese in esame. Pertanto se avrò impostato nel formato guida la data 31/03/2013 visualizzerò i movimenti con data dal 01/03/2013 al 31/03/2013
 * PR - Progressivo nell'esercizio in esame :  restituisce i valori progressivi del mese in esame. Pertanto se avrò impostato nel formato guida la data 31/03/2013 visualizzerò i movimenti con data dal 01/01/2013 al 31/03/2013, includendo anche il saldo al 01/01/2013 se presente.
 * MO - Movimenti dell'esercizio in esame :  restituisce i valori movimenti dell'esercizio in esame. Pertanto se avrò impostato nel formato guida la data 31/03/2013 visualizzerò i movimenti con data dal 01/01/2013 al 31/03/2013, escludendo il saldo al 01/01/2013 se presente.

A questo punto la scelta sarà tra : 

 * DA - Dare :  permette di analizzare i soli movimenti in dare.
 * AV - Avere :  permette di analizzare i soli movimenti in avere.
 * SA - Saldo :  permette di analizzare i saldo dei movimenti.

 * FI - Fiscale :  permette di analizzare i soli movimenti fiscali.
 * GE - Fiscale + Gestionale :  permette di analizzare i movimenti fiscali e gestionali.
 * GS - Gestionale :  permette di analizzare i soli movimenti gestionali.



 * AT - Attivo :  permette di analizzare i soli movimenti attivi.
 * SI - Simulato :  permette di analizzare i soli movimenti simulati.
 * AS - Attivo e Simulato :  permette di analizzare i movimenti attivi e simulati.

La scelta inziale, oltra ai valori DI e CO presenterà queste due opzioni : 

 * PE - Costruito da un range di periodi :  questo parametro permetterà di visualizzare valori di più periodi. In questo caso il periodo impostato nel formato guida non sarà signifcativo poichè sarà necessario indicare la data di partenza e il numero di periodi da analizzare
 * OP- Operazione su colonne valori :  questo parametro permetterà di costruire operazioni (differenze, analisi di incidenza) sui valori riportati nelle precedenti colonne
