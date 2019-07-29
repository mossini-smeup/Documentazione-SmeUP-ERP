# A£Q - Periodicità
 :  : DEC T(ST) K(A£Q)
## OBIETTIVO
La tabella serve per costruire uno schema di periodi (intervalli di giorni) di ampiezza omogenea o mista (es. 20 periodi giornalieri + 10 periodi settimanali + 24 periodi mensili) da utilizzare quando si vogliono rappresentare dei fenomeni che si sviluppano nel tempo (es. statistica qtà da produrre nel tempo).
Il TST per la costruzione dei periodi è il programma B£DIRV (CALL B£DIRV).
## CONTENUTO DEI CAMPI
 :  : FLD T$A£QA **Tipo risorsa di default**
Rappresenta la tipologia di calendario da utilizzare per la costruzione della periodicità
 :  : FLD T$RIS **Codice risorsa di default**
Rappresenta il codice risorsa (Centro di lavoro, Centro di costo) il cui calendario si utilizza per la costruzione della periodicità
 :  : FLD T$NGIO **Numero giorni**
Numero di periodi a giorni che si vogliono considerare
 :  : FLD T$FGIO **Flag giorni**
- Se indicato ' ' oppure '+' nel caso in cui l'ultimo periodo a giorni non coincida con l'inizio di una settimana, costruisce n. periodi di raccordo fino ad arrivare all'inizio della settimana successiva
- Se indicato '-' nel caso in cui l'ultimo periodo a giorni non coincida con l'inizio di una settimana, arretra di n. periodi fino ad arrivare all'inizio della settimana corrente
 :  : FLD T$NSET **Numero settimane**
Numero di periodi a settimane che si vogliono considerare
 :  : FLD T$FSET **Flag settimane**
Stesso significato del flag giorni :  se indicato ' ' o '+' costruisce n. periodi di raccordo fino a inizio mese successivo, se indicato '-' arretra fino a inizio mese corrente
 :  : FLD T$NMES **Numero mesi**
Numero di periodi a mesi che si vogliono considerare
 :  : FLD T$FMES **Flag mesi**
Non usato.
 :  : FLD T$FSCA **Costruzione periodo scaduto**
Se impostato costruisce un periodo con data inizio 0 e data fine antecedente alla data di partenza della costruzione del calendario
 :  : FLD T$A£Q1 **Presentazione settimane**
Se impostato presenta al posto delle date del periodo il Numero/Anno della settimana
 :  : FLD T$A£Q2 **Presentazione numero giorno IBM**
Non più usato
 :  : FLD T$A£Q3 **Presentazione periodo contabile**
Se impostato presenta al posto delle date il periodo contabile (tab. PER)
 :  : FLD T$A£QP **Assegnazione pesi manuale**
Per ciascun periodo con ampiezza superiore al giorno il sistema calcola di default il numero di giorni lavorativi da utilizzare come peso nelle funzioni i distribuzione (es. la distribuzione di una qtà mensile nelle sue settimane avviene in base al n. di giorni lavorativi di ciascuna settimana). Se questo flag
è impostato i pesi vengono assegnati manualmente
 :  : FLD T$A£QE **Tipo risorsa calendario periodo**
3
 :  : FLD T$A£QB **Tipi periodi omogenei**
Se impostato, vengono costruiti periodi del tipo impostato in questo campo.
In questo caso la periodicità ha unicamente lo scopo di costruire una griglia di periodi (n° coppie di date inizio e fine) da usare nelle proiezioni per data (£G14, £G27), mentre non vengono costruiti i pesi per la suddivisione di quantità settimanali o mensili.
 :  : FLD T$A£QC **Numero periodi omogenei**
È significativo in presenza del campo tipo periodi omogenei ed è il numero di periodi costruiti (se non impostato si assume 120)
 :  : FLD T$A£QD **Primo periodo omogeneo**
È significativo in presenza del campo tipo periodi omogenei e rappresenta il modo di trattare la parte del primo periodo scaduta : 
- Se non impostato, l'inizio del primo periodo è costuito dall'inizio del periodo scelto a cui appartiene la data ricevuta. Ad esempio se essa vale 12/05/2003, e se i periodi sono trimestri, la data inizio periodo è 01/04/2003 :  il primo giorno del secondo trimestre dell'anno. Il primo periodo è quindi 01/04/2003 - 30/06/2003
- Se impostato '1', il primo periodo inizia con la data ricevuta.
Nel caso dell'esempio precedente, il primo periodo è quindi 12/05/2003 - 30/06/2003
- Se impostato '2', il primo periodo viene suddiviso in un periodo scaduto, dall'inizio periodo al giorno precedente la data ricevuta, ed in un secondo dalla data ricevuta alla data di fine periodo.
Nel caso dell'esempio precedente, il primo periodo è 01/04/2003 - 11/05/2003, mentre il secondo è  12/05/2003 - 30/06/2003
- Se impostato '3', per i periodi con durata > al mese e < all'anno, il primo periodo viene impostato a partire dall'inizio del mese cui appartiene la data ricevuta. Ad esempio se essa vale 12/05/2003, e se i periodi sono trimestri, il primo periodo andrà dal 01/05/2003 al 31/07/2003 e così via.
 :  : FLD T$A£QF **Periodi omogenei discendenti**
Se impostato questo flag, in concomitanza con l'utilizzo dei periodi omogenei, fa sì che i periodi non vengano calcolati dalla data passata in avanti bensì dalla data passata indietro.
 :  : FLD T$A£QH **Periodo finale**
Se impostato, viene aggiunto un periodo finale con partenza al giorno successivo alla fine dell'ultimo periodo, e con arrivo al 31.12.2099.
Questo periodo si aggiunge al numero di periodi (a differenza del periodo iniziale).
Ad esempio, se si sono impostati 12 periodi, è il tredicesimo.
Unica eccezione, se sono impostati 120 periodi, considera l'ultimo periodo come "oltre periodo" impostando nella data fine il 31.12.2099.
