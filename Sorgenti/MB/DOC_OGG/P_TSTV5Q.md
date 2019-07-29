# Obiettivo
La routine è necessaria per gestire le quantità di un documento V5, Calcola gestisce e visualizza tutte le quantità legate ad una riga.

# Funzioni e metodi
_1_Funzioni e _5_Metodi
 * _1_DC, Oltre alla funzione CA (alla quale rimandiamo) effettua la decodifica delle singole quantità presenti, i metodi sono gli stessi della funzione CA
 * _1_CA, Esegue il calcolo delle quantità (passati tramite la DS £V5PDS).Lo scopo principale della routine è ritornare la schiera delle quantità. La schiera di input/output £5Q è composta di 20 elementi, divisi in 2, dall'elemento 01 al elemento 10 sono gestite le quantità in UM interna (di magazzino) dall'elemento 11 all'elemento 20 quelle in UM esterna (acquisto o vendita). Le 2 parti sono divise a loro volta in 2, le prime 5 quantità sono di input (quindi dal 01 alla 05 e dall 11 al 15) le seconde (dal 06 al 10 e dal 16 al 20) sono di output. La funzione ritorna le qtà calcolate al richiedente con i significati delle quantità con significato fisso : 
 ** (06/16) Quantità residua
 ** (07/17) Quantità extraspedita ( o ricevuta in caso di acquisto)
 ** (10/20) Quantità in attesa di collegamento (se richiesto metodo AT viene impostata la quantità presente in documenti collegati alla riga non ancora collegati,e quindi confermati, legati alla riga
 * _1_GE, Emette un formato che da la possibilità di modificare le 5 quantità base (dal 1/5,11/15) passati dal/al programma. da notare che se viene passato il flag 6 nel campo £V5PQM è manutenzionabile solo il campo richiesto altrimenti tutti e 5 le qtà.
 * _1_VI, Emette un formato che da la possibilità di visualizzare le 5 quantità base (dal 1/5,11/15) passati dal programma.
 * _1_SC, La funzione non prevede metodi e da la possibilità di scegliere un singolo valore dei 10 del tipo quantità richiesto e ritorna la decodifica del campo qtà scelto nel primo elemento della schiera £5S ed il numero dell'elemento della schiera qtà passata (£5Q) nel primo elemento della schiera

I metodi per tutte le funzioni (SC a parte) sono : 
 * _5_      , Normale :  elabora le qtà presente nelle cinquine senza colcoli aggiuntivi
 * _5_AT    , Al netto dell'attesa spe/ric :  se passato nei campi £V5PTD/ND/NR i campi della riga controlla, per calcolare il residuo riga, anche i documenti legati alla riga e non ancora collegati.

# Input
I dati di input oltre alla funzione e metodo sono passati tramite la DS £V5PDS, la quale contiene tutti i valori significativi della riga documento in elaborazione e i dati principali della testata, e la schiera £5Q con le quantità della riga (quindi saranno valorizzati in input solo i valori dal 1/5 11/15)

**DA NOTARE**, che per i richiami della routine con i record del V5RDOC e V5TDOC già in linea è disponibile la routine **£V5QF** che esegue il riempimento della ds e della schiera in automatico


# Output
La routine restituisce al programma chiamante le schiere £5I con la decodifica dei valori presenti nella schiera £5W

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£V£QE
£FUNDS1
£V5PDS

# Esempio di chiamata
Con in linea i record V5TDOC e V5RDOC : 
>       C                  EVAL  £FUNFU='CA'
       C                  EVAL  £FUNFU='CA'
       C                  EXSR  £V5QF
       C                  EXSR  £V5Q

Altrimenti sono da riempire tutti i valori necessari della ds £V5PDS e la schiera £5Q



# Note particolari
E' consigliabile usare sempre questa routine se si desidera elaborare le qtà residua di una riga di V5 che quindi è l'unico posto in cui si può intervenire per modificare o condizionare specifici calcoli.
