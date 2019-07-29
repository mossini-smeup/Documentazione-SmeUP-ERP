# MPP - Piani
## OBIETTIVI
Permettere di definire i parametri per costruire un piano. La tabella descrive il periodo di inizio piano e la periodicità con cui vengono costruiti i periodi successivi.
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
**Definizioni**
_Impostazione_ :  Identifica il tipo di periodicità associata al piano.
**Utilizzo**
Costruzione di un piano.
**Metodo**
Partendo dalla data di inizio orizzonte, vengono costruiti n° periodi con ampiezza giornaliera, settimanale o mensile, in base al numero di periodi e alla periodicità definiti nella tabella A£Q
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrizione del codice piano
 :  : FLD T$IMPO __Impostazione__
È un elemento della tabella A£Q. Definisce l'ampiezza dei vari periodi del piano.
 :  : FLD T$DAIO __Data inizio orizzonte__
Rappresenta la data di inizio del piano.
 :  : FLD T$MAGA __Magazzino__
Individua il codice di magazzino da utilizzare nelle azioni in cui è gestito e collegate al piano.
 :  : FLD T$PREF __Prefisso tipo piano__
Rappresenta il prefisso del codice piano.
 :  : FLD T$CSCE __Codice Ambiente__

 :  : FLD T$MPPA __Livello Protezione__

 :  : FLD T$MPPB __Selezione flusso__
Rappresenta il criterio di selezione per la scelta dei flussi mediante i quali elaborare il piano.
Può essere utilizzato nel caso in cui si voglia limitare l'utilizzo di elaborazioni di flussi MPS a determinati piani.
Il programma di lancio esecuzione flusso azioni (MPAP00G) permette la scelta di gruppo azioni, il cui criterio di applicabilità flusso (specificato nella tabella B£H), coincide con il criterio di selezione flusso del piano selezionato (specificato in questo campo).
