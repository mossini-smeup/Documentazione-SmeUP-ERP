# Obiettivo
La routine è necessaria per gestire i valori di un documento V5, recupera i valori dal listino e calcola tutte le sue componenti.
In definitiva per recuperare il listino di una riga, decodificare i singoli valori e calcolare il prezzo della riga è necessario utilizzare questa routine

# Funzioni e metodi
_1_Funzioni e _5_Metodi
 * _1_DP, Oltre alla funzione CA (alla quale rimandiamo) effettua la decodifica dei singoli valori,i metodi possibili sono gli stessi della funzione CA
 * _1_DPE, Oltre alla funzione CAE (alla quale rimandiamo) effettua la decodifica dei singoli valori,i metodi possibili sono gli stessi della funzione CAE (che ha sua volta sono gli stessi della funzione CA)
 * _1_CAE, Vedi la documentazione della CA, unica differenza è che tramite questa funzione è possibile recuperare anche gli sconti virtuali non presenti sulla riga ma scritti sulla testata
 * _1_CA, Esegue il calcolo dei valori (passati tramite la DS £V5PDS).Lo scopo principale della routine è ritornare la schiera dei valori. Da notare che la schiera di output £5W è composta di 10 elementi, i primi 5 sono i valori presenti nel documento ed hanno un significato specifico definito tramite il flag 4 di riga (col quale vengono definiti sia il significato che il comportamento), i secondi 5 (dal 6 al 10) sono calcolati e quindi ritornati al richiedente dalla routine ed hanno significato fisso e precisamente : 
 ** (06) Prezzo netto in UM esterna
 ** (07) Prezzo netto in UM interna (di magazzino)
 ** (08) Prezzo effettivo (da fattura) in UM interna
 ** (quindi gli eventuali programmi di exit per la gestione di valori specifici "utente" devono TENERE conto di quest'ultimo vincolo)

I metodi delle funzioni CA, CAE e quindi anche della funzione DP e DPE sono : 
 * _5_      ,  Ritorna i valori nella valuta del documento
 * _5_CAMBIO, Ritorna i valori nella valuta corrente dell'azienda
 * _5_VALALT, Ritorna i valori nella valuta alternativa specificata nella tabella B£2
 * _5_EURO  , Ritorna i valori in EURO  (questo metodo è stato utilizzato durante l'introduzione della nuova moneta è rimasta ma andato in disuso quindi non è + da utilizzare)

 * _1_GE, Emette un formato che da la possibilità di interrogare Metodo _5_VIS, oppure modificare _5_MOD, i 5 valori base (dal 1 al 5) passati al programma
 * _1_SC, La funzione non prevede metodi e da la possibilità di scegliere un singolo valore dei 10 del tipo prezzo richiesto e ritorna la decodifica del campo prezzo scelto nel primo elemento della schiera £5I ed il numero dell'elemento della schiera valori passata (£5W) nel primo elemento della schiera
 * _1_RV, La funzione non prevede metodi ed è la funzione che recupera i prezzi dal listino, passato un listino ed una sezione ritorna i 5 valori base recuperandoli tramie la routine £C£L

# Input
I dati di input oltre alla funzione e metodo sono passati tramite la DS £V5PDS, la quale contiene tutti i valori significativi della riga documento in elaborazione e i dati principali della testata, e la schiera £5W con i valori della riga (quindi saranno valorizzati in input solo i valori dal 1 al 5)
**DA NOTARE** che per i richiami della routine con i record del V5RDOC e V5TDOC già in linea è disponibile la routine **£V5VF** che esegue il riempimento della ds e della schiera in automatico


# Output
La routine restituisce al programma chiamante le schiere £5I con la decodifica dei valori presenti nella schiera £5W

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£V£VE
£FUNDS1
£V5PDS

# Esempio di chiamata
Con in linea i record V5TDOC e V5RDOC : 
>       C                  EVAL  £FUNFU='CA'
       C                  EVAL  £FUNFU='CA'
       C                  EXSR  £V5VF
       C                  EXSR  £V5V

Altrimenti sono da riempire tutti i valori necessari della ds £V5PDS e la schiera £5Q



# Note particolari
E' consigliabile usare sempre questa routine se si desidera elaborare il prezzo netto di una riga di V5 che quindi è l'unico posto in cui si può intervenire per modificare o condizionare specifici calcoli.
