# Generalità
Gli schemi sono un mezzo, comune a tutto Sme.up, che permette di determinare le colonne che saranno visualizzate o stampate in una lista.

Le modalità utilizzo sono le stesse in tutto Sme.up.

Abbiamo 2 famiglie di schemi : 

- _2_Schema informazioni :  serve per la rappresentazione di informazioni alfanumeriche (codice, descrizione, caratteristiche codificate, ...)
- _2_Schema valori :  serve per la rappresentazione dei 'numeri' (quantità, valori)


# Schemi informazioni
## Gestione
Gli schemi si attivano inserendo uno dei caratteri di ricerca classici di Smeup ('!' '?') nel campo apposito che si può trovare nel formato di parzializzazione o nel formato guida di lancio delle stampe : 

![B£_02_01](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_01.png)
Viene presentata la lista degli eventuali schemi già presenti (X per selezionarne uno già creato).

### Creazione / Modifica / Cancellazione
Per creare uno schema premere il tasto F6 = Nuovo schema, viene richiesto un codice ed una descrizione del nuovo schema, il codice è lungo 1 e può essere un numero o una lettera fino alla T compresa : 

![B£_02_02](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_02.png)
ad ogni nuovo codice viene attribuito un gruppo schema (colonna G) della lista schemi, ad ogni gruppo schema appartengono 5 schemi ed in totale possiamo avere 30 gruppi schema.

Con INVIO lo schema appena creato viene presentato nella lista, per gestirlo selezionarlo con l'opzione D.

Si presenta la lista di tutte le colonne che possono essere presentate, impostando il campo sequenza si definisce l'ordine (da sinistra verso destra) con cui le colonne verranno presentate : 

![B£_02_03](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_03.png)
per togliere una colonna sbiancare la sequenza.

È possibile modificare la lunghezza o l'intestazione delle colonne agendo sui campi LC, Int Colonna 1 e Int Colonna 2 : 

![B£_02_04](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_04.png)
_2_Nota bene :  Una particolare attenzione va posta al fatto che nella definizione di uno schema le modifiche eventuali alla lunghezza del campo e alla sua intestazione agiscono su tutti gli schemi appartenenti allo stesso gruppo.

Per cancellare uno schema usare l'opzione 4 dalla lista degli schemi.

### Aggiunta attributi agli schemi
Oltre alle normali colonne previste dallo standard Sme.up si possono aggiungere nuove colonne formate da attributi (OAV) degli oggetti presenti nelle colonne standard.
- [Attributi di un oggetto](Sorgenti/MB/DOC_OPE/B£_OAV)

# Schemi valori
## Gestione
Per la creazione o modifica di uno schema valori si inserisce uno dei caratteri di ricerca classici di Smeup ('!' '?') nel campo apposito che si può trovare nel formato di impostazione delle stampe : 

![B£_02_05](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_05.png)
Viene presentata la lista degli eventuali schemi già presenti (X per selezionarne uno già creato).

### Creazione / Modifica
Per creare uno schema usare l'opzione 1 e scrivere nome e descrizione del nuovo schema, si presenta la lista di tutti i numeri che possono essere presentati (i numeri possono essere fisicamente presenti nel documento oppure calcolati dinamicamente :  es. il valore in valuta di conto), impostando nel campo '?' un numero di sequenza si stabilisce quali numeri saranno presentati ed in quale ordine (da sinistra verso destra) : 

![B£_02_06](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_06.png)
Per i campi numero selezionati è possibile inserire una descrizione (su 2 righe) e stabilire la formattazione : 

- Numero di interi
- Numero di decimali
- Numero di punti di separazione (migliaia)
- Se dividere il numero per 10 / 100 / 1000 (1 / 2 / 3)
- Le opzioni di totalizzazione, cioè quale numero presentare nella riga totali (? per i valori possibili)
- Il tipo di arrotondamento da applicare(? per i valori possibili)


![B£_02_07](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_07.png)
Con il tasto F20 viene presentata un'anteprima, con F6 si conferma l'aggiornamento.

Per modificare uno schema usare l'opzione D, si ripercorrono gli stessi passi visti per la creazione.

Per cancellare uno schema usare l'opzione 4.

_2_Caso particolare :  Impostazione tipo costo / livello utilizzato
Negli schemi valori si possono selezionare anche valori come _3_costo, _3_margine, ecc.. per determinare questi valori il sistema ha bisogno che venga indicato un tipo costo / livello.
Per impostare questi parametri è necessario andare alla lista di tutti i numero che possono essere presentati : 

![B£_02_06](http://localhost:3000/immagini/MBDOC_OPE-B£_SCH/BX_02_06.png)
a questa lista si arriva sia in inseriemnto di un nuovo schema (opzione = 1) che in manutenzione di uno schema esistente (opzione = D), quando si è in questa lista il comando funzione _3_F14 = Parametri permette l'impostazione di una serie di parametri tar cui Tipo Costo e Livello.
