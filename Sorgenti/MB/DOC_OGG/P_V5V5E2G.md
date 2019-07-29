## Obiettivo

Attraverso la ripresa dai documenti commerciali è possibile estrarre tutte le informazioni e i dati da riportare all'interno dei modelli Intrastat.

## Formato guida

Il formato guida si presenta nel seguente modo : 

![C5C090_013](http://localhost:3000/immagini/MBDOC_OGG-P_V5V5E2G/C5C090_013.png)
Vediamo nello specifico il significato dei campi visualizzati : 
 * Tipo cessione :  definisce la tipologia di scambi da estrarre. Le scelte disponibili sono : 
 ** ' '= Acquisti e vendite
 ** A = Acquisti
 ** V = Vendite
 * Modalità esecuzione :  definisce il modo in cui viene eseguita la scrittura dei dati. Le scelte disponibili sono : 
 ** ' '= Scrivi solo mancanti :  ad ogni scritturà verranno solamente scritti i record mancanti e non verranno modificati i dati già presenti ed eventualmente modificati.
 ** S = Scrivi solo automatici : 
 ** V = Scrivi tutti :  riscrive completamente il file cancellando i record appartenenti al periodo indicato e riscrivendoli a partire dai documenti inseriti. Quindi nel caso in cui siano state apportate modifiche o immissioni manuali di record intrastat, lanciando la funzione in questa modalità verranno perse.
 * Periodo competenza :  delimita l'ambito temporale entro il quale verranno estratti i dati.
 * Numero documento :  permette di limitare in funzione del numero documento i record estratti
 * Stampa log :  l'esecuzione stampa normalmente un elenco di errori (articoli senza nomenclatura combinata e/o inesistente), richiedendo il log si produrrà anche una stampa di documentazione e quadratura tra movimento contabile e documento.

### Tasti funzionali
 * F06 Conferma. Permette di confermare l'estrazione delle informazioni
 * F11 Parametri esecuzione.  Permette di impostare i parametri per l'esecuzione dell'estrazione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.


