# Introduzione
Il calcolo e il trattamento dei tempi sono la base della schedulazione :  nel seguito viene descritto in dettaglio il processo, dal calcolo, all'utilizzo fino alla memorizzazione dei risultati.

# Determinazione dei componenti di carico
Si passano alla routine BRT i dieci tempi del ciclo, il tipo tempo e il codice di carico (V2/BR*CR (in modo esplicito o, in assenza, ricavato dalla risorsa).
Essa calcola le 10 componenti di carico (V2/BR*CA)
02 - Attrezzaggio
03 - Carico

# Costruzione S5IRIS
Memorizza sempre l'efficienza della risorsa principale (S6EF01).
Copia tutti i tempi del ciclo nei campi corrispondenti (S6TE01 - 10).
Copia tutti i componenti di carico nei campi corrispondenti  (S6CC01 - 10).
Copia il componente di carico 03 nelle ore totali (S6HTOT) e. se previsto nello scenario, le incrementa dell'effcienza memorizzata in precedenza.
Se l'impegno non è iniziato e se previsto nello scenario, copia il componente di carico 03 nelle ore attrezzagglio (S6HATR), e le  incrementa dell'effcienza memorizzata in precedenza (sempre se previsto nello scenario).
Calcola la quantità residua dell'operazione (S6QTOR) e la copia nella quantità schedulata (S6STSC)
Calcola le ore unitarie S5HUNI come rapporto tra le ore totali (S6HTOT) e quantità scehedulata  (S6QTSC)

# Schedulzione BCD
## Impostazioni
Le ore totali S6HTOT vengono copiate in XIHTOT e in XAHTOT.
Le ore di attrezzaggio S6HATR vengono copiate in XIHATR e in XAHATR
Se è il caso XAHTOT e XAHATR vengono nettificate dell'efficienza della risorsa generale e ricalcolate con quella della risorsa specifica (in base alle impostazioni di scenario e di parametri BCD).
Le ore di attrezzaggio XAHATR (nettificate)  vengono poi copiate in XGHATR (ore attrezzaggio effettive).

## Aggiustamento attrezzaggio
Le ore di attrezzaggio effettive XGHATR vengono passate al programma di aggiustamento attrezzaggio che le può modificare.
Attenzione :  nel pgm di aggiustamento, se lo si vuole, bisogna riapplicare l'efficienza.

## Schedulazione
Si parte dall'istante in cui la risorsa si libera (istante di inizio schedulazione) e, avazando di XGHATR (dopo l'aggiustamento) se l'operazione non è iniziata,  e delle ore totali XAHTOT, si determina l'istante di fine schedulazione.
Se si è scelto di calcolarlo, sempre partendo dall'istante di inizio schedulazione, e avazando di XGHATR, si determina l'istante di fine attrezzaggio.

## Memorizzazione in S5IRIS
Data - ora inizio e fine schedulata
Data - ora al più presto
Data - ora fine attrezzaggio (in S6ID01 e S65IH01), se valorizzati.
Ore attrezzaggio effettive (in S6HL01)

# Rifasatura di S5IRIS
I seguenti campi sono ripristinati in automatico : 
