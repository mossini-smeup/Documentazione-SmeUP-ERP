# Attivazione dell'integrazione
Per attivare le ceazione delle richieste di movimentazione è necessario : 
_4_Documenti
 * _2_definire il Tipo di documento di movimentazione
 :  : DEC T(TA) K(V55)
 * _2_attivare il flag 23 di testata dei documenti
 :  : DEC T(TA) K(B£Y)
_4_Ordini di produzione
 * _2_definire il Tipo di documento di movimentazione impegni
 :  : DEC T(TA) K(P55)
 * _2_attivare il flag 09 dell'ordine di produzione
 :  : DEC T(TA) K(B£Y)

## Funzionamento
_4_Documenti
Il documento che deve essere integrato con la logistica deve essere abilitato tramite l'apposito
flag di testata (23).
Le righe del documento, se appartenenti all'oggetto AR, saranno inviate alla logistica a meno
della loro disabilitazione tramite il flag (45).

Le Richieste di movimentazione sono generate al livello di disattivo, una volta che la logistica
le ha prese in carico, attivandole, la riga del documento non sarà più annullabile mentre la
quantità non sarà modificabile.

Le Richieste di movimentazione sono generate durante la fase di collegamento del documento.
Le Richieste di Movimentazione se non processate dalla logistica verranno annullate a seguito della
modifica o cancellazione della riga.

_4_Documenti di Conto Lavoro
Il documento che deve essere integrato con la logistica deve essere abilitato tramite l'apposito
flag di testata (23).
Le righe del documento, se appartenenti all'oggetto AR, saranno inviate alla logistica a meno
della loro disabilitazione tramite il flag (45).

Le Richieste di movimentazione sono generate al livello di disattivo, una volta che la logistica
le ha prese in carico, attivandole, la riga del documento non sarà più annullabile mentre la
quantità e la distinta base non saranno modificabili.

Le Richieste di movimentazione sono generate durante la fase di creazione degli impegni di conto
lavoro.
Le Richieste di Movimentazione se non processate dalla logistica verranno annullate a seguito della
modifica o cancellazione della riga.

_4_Ordine di produzione
L'ordine di produzione che deve essere integrato con la logistica deve essere abilitato tramite
l'apposito flag (09).

Le Richieste di movimentazione sono generate al livello di disattivo, una volta che la logistica
le ha prese in carico, attivandole, la riga del documento non sarà più annullabile mentre la
quantità e la distinta base non saranno modificabili.

Le Richieste di movimentazione sono generate durante la fase di creazione degli impegni di
produzione.
Le Richieste di Movimentazione se non processate dalla logistica verranno annullate a seguito della
modifica o cancellazione dell'ordine.

## Attenzione
_4_Documenti
Per mantenere aggiornata l'integrazione delle righe del documento con la logistica si consiglia
l'attivazione dello scollegamento/collegamento automatico del documento.
In alternativa devono essere impostati i passi di flusso necessari all'inytegrazione del documento.
_4_Ordine di produzione
Non sono stati attivati automatismi, deve essere predisposto il relativo flusso per l'esecuzione
dell'integrazione.
