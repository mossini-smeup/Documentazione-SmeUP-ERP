## Interrogazione Movimenti
### Generalità
L'interrogazione movimenti permette, secondo varie forme, di visualizzare i movimenti di magazzino.

## Formato di lancio
L'interrogazione movimenti parte dal seguente formato di lancio : 

![GM_12_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMMO01/GM_12_01.png)Selezionando la forma si determinano i vari modi con cui interrogare i movimenti e si aprono i relativi campi di selezione : 

- _2_Numero di registrazione, presenta i movimenti in ordine di numero di registrazione (ascendente o discendente) a partire da un dato numero di registrazione
- _2_Articolo - Plant - Data Registrazione, presenta i movimenti di un articolo in un plant a partire da una data di registrazione, è possibile anche la selezione della scheda movimenti
- _2_Data di registrazione, presenta i movimenti a partire da una data di registrazione
- _2_Articolo - Lotto, presenta i movimenti di un articolo avente un determinato lotto
- _2_Tipo Ente - Ente - Tipo movimento, presenta i movimenti di un ente (es. un fornitore o un cliente) impostando il tipo ente (CLI / FOR) il codice ente ed il tipo articolo
- _2_Ubicazione - Plant - Data Registrazione, presenta i movimenti di tutti gli articoli che transitano per l'ubicazione, in un plant a partire da una data di registrazione
- _2_Collo - Data Registrazione, presenta i movimenti degli articoli contenuti in un collo a partire da una data di registrazione
- _2_Commessa - Plant - Data Registrazione, presenta i movimenti di tutti gli articoli che interessano la commessa, in un plant a partire da una data di registrazione
- _2_Causale - Plant - Data Registrazione, presenta i movimenti di tutti gli articoli con una determinata causale di movimentazione, in un plant a partire da una data di registrazione


Per ciascuna forma è possibile definire e scegliere uno schema informazioni e filtrare la lista attraverso le parzializzazioni.

Di seguito descriveremo le forme di interrogazione più significative.

### Numero di registrazione
Presenta i movimenti ordinati per numero di registrazione, che è il numeratore progressivo che viene attribuito dal sistema a ciascun movimento, si può avere un ordinamento ascendente (da una determinata registrazione in avanti) o discendente (all'indietro da una registrazione), se si inserisce un numero negativo vengono visualizzati gli ultimi n movimenti (es. -8 mostra gli ultimi 8 movimenti) : 

![GM_12_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMMO01/GM_12_02.png)Nella lista movimenti, indipendentemente dalla forma, si può interrogare il dettaglio movimento (opzione 05), oppure interrogare i movimenti collegati : 

![GM_12_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMMO01/GM_12_03.png)I movimenti collegati sono gli altri movimenti generati dal sistema e collegati in qualche maniera a quello di partenza.

Ad esempio i movimenti collegati di un versamento di produzione sono i movimento di consumo dei componenti e viceversa il movimento collegato ad un consumo componenti è il versamen to di produzione del padre.
Altri movimenti collegati sono i trasferimenti dove un movimento di scarico della giacenza di partenza è collegato al movimento di carico della giacenza di destinazione.

_3_Nota
Per vedere gli ultimi N movimenti scegliere la forma 1 e inserire N- nel campo N. di registrazione.
(Es. per vedere gli ultimi 5 movimenti inserire 5-).

### Articolo - Plant - Data Registrazione
Presenta i movimenti di un articolo in un plant a partire da una data di registrazione : 

![GM_12_04](http://localhost:3000/immagini/MBDOC_OGG-P_GMMO01/GM_12_04.png)Con questa forma è possibile anche la scheda : 

![GM_12_05](http://localhost:3000/immagini/MBDOC_OGG-P_GMMO01/GM_12_05.png)Impostando i parametri di lancio, in particolare la forma scheda e le date inizio e fine periodo presenta una scheda riassuntiva dei movimenti di un articolo : 

![GM_12_06](http://localhost:3000/immagini/MBDOC_OGG-P_GMMO01/GM_12_06.png)Da notare che  la _2_forma scheda, determina il tipo di output : 

- _3_DET / AVA, presenta il dettaglio movimenti in avanti dalla data iniziale a quella finale del periodo
- _3_DET / IND, come il precedente con presentazione all'indietro dalla data finale a quella iniziale
- _3_GIO / AVA, presenta il riepilogo giornaliero dei movimenti giornaliera in avanti dalla data iniziale a quella finale del periodo
- _3_GIO / IND, come il precedente con presentazione all'indietro dalla data finale a quella iniziale
- _3_RIE / MOV, presenta il riepilogo per tipo movimento nel periodo
- _3_RIE /  , presenta i movimenti riepilogati in entrate uscite nel periodo


## Revisione Movimenti
Si utilizzano le stesse modalità viste per l'interrogazione movimenti, con la differenza che si può passare al dettaglio per la modifica.

Quando sono state variate le informazioni, con F6 si applicano le modifiche :  il sistema storna il movimento originario e lo riscrive con i nuovi dati.

_3_NOTA; in base al valore del flag "Revisione Movimenti a Storno" verranno o meno registrati anche i movimenti di storno.
