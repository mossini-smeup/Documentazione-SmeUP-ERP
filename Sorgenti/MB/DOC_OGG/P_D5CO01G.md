## Obiettivo
Attraverso questa interrogazione è possibile visualizzare i saldi dei conti bancari alle diverse date.
I dati riportati vengono aggiornati in modo automatico nel momento in cui viene effettuato il consolidamento bancario; andranno impostati manualmente solo all'attivazione  del modulo della tesoreria.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D030_027](http://localhost:3000/immagini/MBDOC_OGG-P_D5CO01G/C5D030_027.png)
All'interno del formato guida è necessario selezionare l'azienda d'interesse. Gli altri campi presenti sono facoltativi e riportano : 
 * Conti Contabili :  il codice del conto contabile di cui si voglia gestire il saldo
 * Data :  la data a cui si vuole gestire il saldo del conto indicato.

Le opzioni disponibili per questa funzione sono : 
 * 01 - Inserimento manuale di un nuovo saldo
 * 02 - Modifica di un dato presente all'interno dell'archivio saldi
 * 03 - Copia per l'inserimento di un nuovo saldo partendo dalla copia di un dato già presente
 * 04 - Cancellazione di un dato
 * 05 - Visualizzazione
 * 06 - Stampa

### Tasti funzionali
 * F03 Fine Lavoro. Esce dall'interrogazione.
 * F04 Decodifica. Permette di decodificare la data e il conto eventualmente indicati.
 * F13 Parzializzazioni. Permette di accedere alle parzializzazioni e quindi filtrare i dati presentati.

## Formato Lista

Nel caso in cui all'interno del formato guida non venga compilato ne il conto contabile ne la data dando invio verrà presentato il formato lista contenente l'elenco di tutti saldi archiviati. Se invece verrà compilato il conto contabile o la data, dando invio verranno presentati tutti i saldi presenti per quel conto o per quella data : 
 :  : IMG

All'interno del formato lista per ogni saldo archiviato sono visualizzati il relativo conto e la data.

### Opzioni

Per ogni record del formato lista sono disponibili le seguenti opzioni : 
 * 01 - Inserimento manuale di un nuovo saldo
 * 02 - Modifica del record
 * 03 - Copia per l'inserimento di un nuovo saldo partendo dalla copia di questo record
 * 04 - Cancellazione
 * 05 - Visualizzazione
 * 06 - Stampa

### Tasti funzionali

 * F05 Rivisualizzazione. Ricarica i dati presenti nel formato lista
 * F06 Aggiunta. Permette di inserire un nuovo saldo
 * F12 Uscita. Esce dal formato lista e torna al formato guida
 * F13 Parzializzazioni. Permette di filtrare i dati presentati
 * F15 Lista per codice. Posizionandosi sulla riga di un conto contabile e digitando questo tasto verranno presentati tutti e soli i record relativi al saldo di questo conto.

## Formato Dettaglio
Il formato dettaglio si presenta in questo modo : 

 :  : IMG

Al suo interno sono quindi riportati : 
 * Saldo contabile :  indica il saldo in euro per data operazione.
 * Saldo liquido :  indica il saldo in euro per data valuta.
 * Saldo contabile in divisa :  per i conti in valuta, indica il saldo in valuta per data operazione.
 * Saldo liquido in divisa :  per i conti in valuta, indica il saldo in valuta per data valuta.
 * Numero Operazioni
 * Numero Postergate
