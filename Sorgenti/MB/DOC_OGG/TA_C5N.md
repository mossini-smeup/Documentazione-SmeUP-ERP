# C5N - Linee di riclassifica
 :  : DEC T(ST) K(C5N)
## OBIETTIVO
Definire i modi in cui un conto può essere aggregato per ottenere rappresentazioni sintetiche.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Contiene la descrizione di questa linea di riclassifica.
 :  : FLD T$C5NA Descrizione aggiuntiva
Con questo campo è possibile descrivere in modo più completo questo elemento.
 :  : FLD T$C5NB Dare/Avere
È un elemento V2/C5DAV :  definisce la natura intrinseca di questa linea. Se impostato, all'interno di questa linea dovranno finire solo conti che abbiano saldo concorde a quanto indicato in questo campo.
 :  : FLD T$C5NC Linea se inverso
È un altro elemento di questa tabella (dello stesso sottosettore) :  se il segno del saldo non è concorde con quanto impostato nel dare/avere, si assegna il saldo, cambiato di segno, a questa nuova linea, che dovrà avere il campo dare/avere opposto a quello della linea di origine. La situazione si verifica spesso per le banche :  potrei avere, infatti, la necessità di assegnare il conto a una linea di classifica se è in dare (ad esempio la linea delle banche attive) e ad un'altra se è in avere (ad esempio la linea delle banche passive) :  in questo caso dovrei mettere che la linea delle banche attive è in dare e nel campo 'Linea se inverso' dovrei mettere la linea delle banche passive.
 :  : FLD T$C5ND Linea di destinazione
È un altro elemento di questa tabella (dello stesso sottosettore) :  è un campo utilizzato nel caso in cui la linea venga poi totalizzata all'interno di un'altra macro-linea. In questo campo dovrò inserire il codice della linea del totale.
 :  : FLD T$C5NE Segno di destinazione
Si imposta insieme alla linea di destinazione :  specifica se gli importi vanno sommati o sottratti nella linea di destinazione.
 :  : FLD T$C5NF Linea calcolata
È un elemento V2/SI/NO :  viene compilato nel caso in cui si tratti di una macro-linea, ovvero di una linea totalizzatrice che, di conseguenza, non ha associati conti propri (sarà la destinazione di altre linee).
 :  : FLD T$C5NG Costruzione livelli superiori
Per le linee calcolate si richiede di costruire anche i livelli superiori. Se ad esempio la linea contiene l'utile, si può richiedere di sommare l'utile nel totale delle passività per quadrare con le attività.
 :  : FLD T$C5NH Linea Fittizzia
Indica che la linea non verrà riprodotta in output. I valori 1 e 2 hanno effetto solo sulle considerazioni relative alla linea inversa : 
* "1" :  con questo valore i conti vengono invertiti solo se l'intera sommatoria della linea risulta inversa
* "2" :  con questo valore l'inversione viene applicata conto per conto. Vengono quindi girati tutti i singoli conti che risultano avere valore inverso.
 :  : FLD T$C5NI Grassetto in stampa
È un elemento V2SI/NO :  indica se la riclassifica nel pgm di stampa standard (C5NAC1L) deve essere stampata in grassetto.
 :  : FLD T$C5NL Salto pagina in stampa
È un elemento V2SI/NO :  indica se la riclassifica nel pgm di stampa standard (C5NAC1L) deve essere stampata dopo aver eseguito il salto pagina.
 :  : FLD T$C5NO Riclass. CEE
Riclassifica CEE del conto
