# Creazione foto giacenza

## Generalità
La foto giacenza è una immagine della giacenza che viene salvata per usi di carattere gestionale o fiscale.

La foto può : 
 * essere valorizzata con un tipo / livello costo
 * essere memorizzata senza costi e valorizzata successivamente
 * essere valorizzata dinamicamente in fase di stampa.
Nel creare una foto prima di tutto occorre inserire un elemento (codice della foto) nella tabella GMW, la data foto sarà libera o bloccata a seconda che in tabella sia stata inserita o meno la data.
Se la data è libera sarà possibile memorizzare diverse foto con lo stesso codice e data diversa.
Se è selezionata la "_2_Costruzione" e se la foto / data già esiste il sistema sovrascrive altrimenti ci sarà solo un completamento di dati (es. valorizzazione).
Scegliendo la funzione opportuna è possibile creare la foto in diversi modi (da giacenza attuale, con ricostruzione movimenti, da altra foto, ....)
In fase di costruzione foto è possibile inibire la stampa che esce di default e decidere se memorizzare o meno anche le giacenze = 0, come pure se memorizzare il costo o le classificazioni (sintesi 1, sintesi 2, valore di ordinamento) che sono state stabilite nella tabella GMW.

### Particolarità
Compilando opportunamente la tabella GMY - sottosettore è possibile applicare regole di valorizzazione diverse per : 
 * Area / Tipo giacenza / OAV articolo
 * Area / Tipo giacenza
 * Area
 * **
_2_Nota Bene; per garantire la congruenza dei dati è opportuno costruire la foto in un momento in cui non vengono registrati movimenti di magazzino.

## Creazione foto - formato di lancio
La creazione della foto parte dal seguente formato di lancio : 

![GMFOTO_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMFO01/GMFOTO_01.png)
Con lo stesso formato si può fare : 

- Creazione della foto e memorizzazione in archivio
- Completamento (valorizzazione e scrittura codici di raggruppamento) di una foto creata in precedenza con l'azione 1
- Entrambe le azioni ( 1+ 2 )


### Descrizione dei campi
_2_Foto; è il nome della foto (la chiave con cui sarà scritta nell'archivio), il nome della foto deve essere presente nella tabella GMW.

_2_Data; è la data a cui si vuole congelare la giacenza (la data può essere già presente nella tabella GMW, in questo caso il campo è visualizzato ma non modificabile, se in tab. GMW la data è assente allora si può inserire manualmente in fase di lancio della funzione).

_2_Esecuzione funzione; se si sceglie SI allora il sistema congela la giacenza, altrimenti si intende un'azione di completamento dove la giacenza è già stata congelata in precedenza e si vuole solo completare la foto con la valorizzazione e/o i codici di raggruppamento.

_2_Totalizza magazzini; se selezionato, a parità di chiave giacenza somma le quantità presenti dei vari magazzini (plant).

_2_Funzione; definisce come calcolare le quantità da congelare nella foto, sono possibili : 

| 
| .COL Txt="Cod." A="L" |
| ---|----|
| 
| .COL Txt="Funzione" A="L" |
| 
| .COL Txt="Azione eseguita" LunAut="1" A="L" |
| - A | Dalla fine all'indietro| Parte dalla giacenza attuale e ricostruisce, elaborando i movimenti a ritroso, la giacenza alla data. |
| - B | Dall'inizio in avanti| Parte da zero e ricostruisce la giacenza alla data elaborando in avanti tutti i movimenti dall'inizio fino alla data. |
| - C | A partire da una foto| Chiede la foto e data di partenza e calcola la nuova foto applicando i movimenti. |
| - D | Differenza tra due foto| Chiede 2 foto e data di partenza e calcola la nuova foto come differenza tra le altre due. |
| - E | Differenza tra foto e giacenza| Chiede la foto e data di partenza e calcola la nuova foto come differenza tra la foto e la giacenza corrente. |
| - F | Differenza tra giacenza e foto| Come la precedente invertendo i fattori. |
| - G | Direttamente da giacenza| Congela direttamente la giacenza. |
| - H | Differenza tra foto e LIFO| Chiede la foto e data di partenza ed Esercizio, Scenario e Magazzino fiscale e calcola la nuova foto come differenza tra la foto e magazzino fiscale. |
| - I | Copia del LIFO| Congela una copia del magazzino fiscale. |
| - L | Cancellazione foto| Cancella la foto in input |
| 


_2_No stampa; se selezionato inibisce la stampa di controllo che altrimenti viene creata.

_2_Mantieni giacenze 0; se selezionato congela anche i record con giacenza = 0.

_2_Costi; se selezionato valorizza la giacenza secondo le regole definite negli elementi della tabella GMY il cui sottosettore è nella tabella GMW, è possibile applicare regole di valorizzazione diversa in base a giacenze diverse (es. il magazzino può essere valorizzato al costo pieno, mentre il magazzino obsoleti può essere valorizzato al 30%).

_2_Sintesi 1  Sintesi 2; se selezionati valorizza anche i campi di raggruppamento utilizzando gli attributi definiti nella tabella GMW.

_2_Valorizzazione ordinamento; se selezionato valorizza il campo di ordinamento definito nella tabella GMW.

## Stampa foto
Questa funzione serve per stampare le foto create in precedenza, è possibile anche la stampa di una foto dinamica (quando il campo Foto resta in bianco) creata al momento e che poi non resta memorizzata nell'archivio. Dinamicamente è possibile anche la valorizzazione con tipo costo / livello diversi da quelli utilizzati in fase di creazione, la stessa cosa è possibile anche per i codici di raggruppamento.

La stampa foto utilizza il seguente formato di lancio : 

![GMFOTO_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMFO01/GMFOTO_02.png)
_2_Nota bene, se il campo foto non è compilato il sistema calcola dinamicamente una foto alla data di input partendo dalla giacenza attuale e poi la stampa utilizzando le impostazioni di lancio (parzializzazioni, schema, valorizzazioni e raggruppamenti solo se questi ultimi sono stati richiesti come "dinamici").
