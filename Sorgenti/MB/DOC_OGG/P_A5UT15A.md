## Obiettivo

 Tramite questo programma è possibile trasferire un cespite o una lista di cespiti da una categoria ad un'altra tramite la creazione di un nuovo cespite o di una lista di nuovi cespiti.

## Formato guida

![A5CAMO_001](http://localhost:3000/immagini/MBDOC_OGG-P_A5UT15A/A5CAMO_001.png)
All'interno del formato guida le informazioni da impostare sono : 

 * Nuova categoria :  è il codice della categoria su cui si vuole trasferire il/i cespite/i.
 * Modalità :  questo campo può essere impostato con : 
 ** Vuoto - Solo stampa :  viene semplicemente eseguita una stampa di sintesi dei movimenti che verrebbero prodotti lanciando la funzione in esecuzione.
 ** 1 - Stampa ed esecuzione :  oltre alla stampa di controllo vengono eseguiti i movimenti di chiusura del cespite sulla precedente categoria e di creazione e valorizzazione del nuovo cespite sulla categoria impostata nel primo campo.
 * Data Registrazione :  riporta la data in cui eseguire il giro di categoria del cespite.
 * Tipo Applicazione :  questo campo può essere impostato con : 
 ** Vuoto - Singolo cespite :  da utilizzare nel caso in cui si voglia girare un solo cespite sulla categoria indicata sopra.
 **  1 - Lista di cespiti :  da utilizzare nel caso in cui si voglia girare una lista di cespiti sulla categoria indicata sopra.
 * Cespite :  Nel caso in cui il campo Tipo applicazione venga lasciato vuoto è necessario compilare questo campo con il codice del cespite che si desidera girare, in caso contrario questo campo è superfluo.
 * Lista Cespiti :  Nel caso in cui il campo Tipo applicazione venga compilato con 1 è necessario indicare in questo campo la lista di cespiti che si desidera girare, in caso contrario questo campo è superfluo.
 * Codice Nuovo cespite :  Nel caso in cui si stia eseguendo la funzione su un solo cespite e si voglia forzare uno specifico codice sul cespite da creare sulla nuova categoria è necessario indicare il codice in questo campo. I campi successivi consentono, invece, di ottenere una codifica automatica del/i cespite/i.
 * Lunghezza codice :  Questo campo e il successivo vanno compilati per ottenere una codifica automatica dei nuovi cespiti creati. In particolare, in questo campo deve essere inserita la lunghezza del codice cespite comprensiva di un eventuale prefisso. Pertanto ipotizzando che il codice cespite sia normalmente formato dal codice azienda + anno di acquisto  + progressivo nella forma AANNNNXXXXXX dove AA è il codice azienda, NNNN l'anno di acquisto e XXXXXX il progressivo sarà necessario indicare in questo campo 12 ovvero la lunghezza totale del codice.
 * Prefisso :  In questo campo è necessario impostare il prefisso della codifica automatica. Riprendendo l'esempio sopra sarà necessario indicare AANNNN, il sistema procederà poi a determinare il primo progressivo libero e ad attribuirlo al nuovo cespite creato.
 * Causale Chiusura :  Indicare in questo campo la causale di movimentazione da utilizzare per la chiusura del cespite sulla precedente categoria. Si sottolinea che il movimento di chiusura del cespite è ad importo nullo pertanto non genererà nessuna minus/plusvalenza ma semplicemente procederà allo storno della quota capitale e del fondo ammortamento eventualmente già registrato.
 * Causale Acquisizione Fondo :  Indicare in questo campo la causale di importazione del fondo da utilizzare per l'apertura del/i nuovo/i cespite/i sulla nuova categoria.
 * Causale Acquisizione Capitale :  Indicare in questo campo la causale di importazione del costo storico da utilizzare per l'apertura del/i nuovo/i cespite/i sulla nuova categoria.



