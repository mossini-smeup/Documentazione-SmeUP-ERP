# Esempi di configurazione
Di seguito mostriamo un esempio di configurazione orizzontale ed uno di configurazione verticale, la spiegazione non intende in alcun modo essere esaustiva, si vogliono solo dare degli spunti per chi ha la necessità di attivare delle configurazioni.

## Configurazione orizzontale
Si abbia un articolo A01 che ha la caratteristica di essere colorato, quindi definiamo una tabella di colori (tabella XCO) ed un modello di configurazione BRC orizzontale con riferimento alla tabella colori (XCO).
![BRCONF_12](http://localhost:3000/immagini/BRCONF_091/BRCONF_12.png)![BRCONF_13](http://localhost:3000/immagini/BRCONF_091/BRCONF_13.png)
In anagrafico articoli all'articolo A01 si assegna il modello di configurazione COL01 : 
![BRCONF_14](http://localhost:3000/immagini/BRCONF_091/BRCONF_14.png)
Nella distinta tecnica prevediamo, oltre agli altri componenti, tutti i vari tipi di vernice : 
![BRCONF_15](http://localhost:3000/immagini/BRCONF_091/BRCONF_15.png)
ciascun legame configurato ha un criterio di selezione (elemento della tabella BRS che contiene il programma BRSCOGN)
![BRCONF_17](http://localhost:3000/immagini/BRCONF_091/BRCONF_17.png)
per ogni legame configurato esiste il riferimento ad un colore specifico
![BRCONF_16](http://localhost:3000/immagini/BRCONF_091/BRCONF_16.png)
Nella distinta il criterio di selezione così impostato permette di rendere valido il legame in base a determinati valori contenuti nel codice configurazione, quindi la distinta di produzione di A01sarà diversa a seconda del valore posto in configurazione : 
![BRCONF_18](http://localhost:3000/immagini/BRCONF_091/BRCONF_18.png)
Inoltre, per come è stato impostato l'elemento della tabella BRC (Obbligatoria = 2) il campo configurazione viene chiesto obbligatorio nel documenti del ciclo esterno : 
![BRCONF_19](http://localhost:3000/immagini/BRCONF_091/BRCONF_19.png)ed è possibile inserire solo uno dei colori presenti nella tabella XCO.

## Liminti della configurazione orizzontale
La configurazione orizzontale permette solo poche possibilità di descrivere varianti (il campo è lungo 20). Quando le necessità della configurazione sono molto più ampie allora si utilizza la configurazione verticale.

## Configurazione verticale
Un esempio di configurazione verticale prevede l'utilizzo di parametri di condizionamento delle varie caratteristiche della distinta.

Abbiamo una distinta generica con componenti reali ed altri generici : 
![BRCONF_20](http://localhost:3000/immagini/BRCONF_091/BRCONF_20.png)Nell'esempio i componenti generici sono quelli con sequenza 0010 e 0015.

Per ciascuno di questi legami di distinta si richiama un elemento della tabella BRS che utilizza il programma BRSCOP1 e i parametri seguenti che prevedono la sostituzione dell'articolo generico con il valore contenuto nel parametro / categoria qui indicati : 

![BRCONF_21](http://localhost:3000/immagini/BRCONF_091/BRCONF_21.png)
Per ogni componente generico è presente un parametro Cxx nella categoria ROA : 
![BRCONF_22](http://localhost:3000/immagini/BRCONF_091/BRCONF_22.png)ciascun parametro punta ad una tabella dove sono contenuti gli articoli effettivi che possono sostituire l'articolo generico.

Poiché la categoria parametri è collegata alle righe documenti di vendita, quando viene inserita / modificata una riga ordine di vendita, un apposito flusso di inserimento/modifica lancia la manutenzione parametri dove viene chiesto di inserire gli articoli prescelti per la configurazione della riga di vendita in questione : 
![BRCONF_23](http://localhost:3000/immagini/BRCONF_091/BRCONF_23.png)
La distinta di produzione dell'articolo sarà sensibile alla configurazione alla riga del documento : 
![BRCONF_24](http://localhost:3000/immagini/BRCONF_091/BRCONF_24.png)