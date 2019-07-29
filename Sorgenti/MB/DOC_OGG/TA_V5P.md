# V5P - Tipo Provvigione
 :  : DEC T(ST) K(V5P)
## OBIETTIVO
Definire le tipologie di movimenti provvigionali.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrive il tipo di provvigione
 :  : FLD T$V5PA  Livello Nascita
Definisce il livello di nascita del record
 :  : FLD T$V5PB  Gruppo Flag
E'un elemento TA/B£Y. Definisce il gruppo di flag che viene assunto all'atto dell'inizializzazione del record
 :  : FLD T$V5PC  Parametri Impliciti
E'un elemento TA/C£I. Caratterizza i campi liberi presenti nell'archivio che sono a disposizione dell'utente
 :  : FLD T$V5PD  Contenitore Note
E' un valore TA/NSC :  se impostato, indica il contenitore delle note relative ai record
 :  : FLD T$V5PE  Tipo Doc.Fat.Agente
E' un valore TA/V5D :  se impostato definisce il tipo documento da utilizzare per la generazione del documento di attesa fattura dell'agente
 :  : FLD T$V5PF  Mod.Fat.Agente
E' un valore TA/V5A :  se impostato definisce il modello di documento da utilizzare per la generazione del documento di attesa fattura dell'agente
 :  : FLD T$V5PH  Tipo Destinatario
E' un valore TA/*CNTT :  definisce in concomitanza al campo T$V5PI il tipo oggetto a cui viene intestata la provvigione
(normalmente TAAGE)
 :  : FLD T$V5PI  Param.Destinatario
Definisce in concomitanza al campo T$V5PH il tipo oggetto a cui viene intestata la provvigione (normalmente TAAGE).
 :  : FLD T$V5PL  Tipo Riga Fat.Agente
E' un valore TA/V5B :  se impostato definisce il tipo riga da utilizzare per la generazione del documento di attesa fattura dell'agente
 :  : FLD T$V5PG  Num.Fat.Manuale
E' un valore TA/CRNV5 :  se impostato, fa si che in inserimento manulae venga omaticamente attribuito come n° fattura
il numero ottenuto da tale numeratore
 :  : FLD T$V5PJ  Tipo imponibile
E' un valore V2/V5TPR. Definisce il significato del record provvigionale
Questo campo è molto importante in quanto alcuni valori attivano un trattamento particolare della provvigione corrispondente : 
* 1 Provvigione :  va utilizzato quando la provvigione è originata da una particolare fattura clienti
* 2 Minimo garantito :  individua un anticipo che potrà essere conguagliato solo se le provvigioni saranno di importo superiore
* 6 Note credito :  va utilizzato quando la provvigione è originata da una particolare nc clienti
* 7 Note debito :  va utilizzato quando la provvigione è originata da una particolare nota addebito
* 9 Anticipo :  individua un anticipo che dovrà essere conguagliato o restituito
* 0 Fisso :  individua un importo corrisposto che originato da documenti, che non verrà mai congualiato
I restanti valori possono essere considerati a scopo puramente descrittivo.
 :  : FLD T$V5PK  Desc.Fissa Pro-Forma
E' un valore V2/SI/NO. Se impostato fa si che nella generazione delle righe del documento di attesa fattura dell'agente venga forzata come descrizione di riga la descrizione del tipo provvigione (solo se il livello di dettaglio previsto è l'agente e non un livello più basso).
 :  : FLD T$V5PM  Esente Enasarco
E' un valore V2/SI/NO. Se impostato fa si che tale record non venga preso in considerazione per la determinazione dell'imponibile su cui viene calcolato l'enasarco.
 :  : FLD T$V5PN  Esente F.I.R.R.
E' un valore V2/SI/NO. Se impostato fa si che tale record non venga preso in considerazione per la determinazione dell'imponibile su cui viene calcolato il Firr.
 :  : FLD T$V5PO  Esente I.S.C.
E' un valore V2/SI/NO. Se impostato fa si che tale record non venga preso in considerazione per la determinazione dell'imponibile su cui viene calcolato l' I.S.C.
 :  : FLD T$V5PP  Suff.Pgm Aggiustamento
Viene Richiamato il pgm V5V6B0_X dove X è il contenuto di questo campo.
Il programma viene richiamato con le stesse funzioni/metodi della £V6B, quindi : 
CLEAR :  inizializzazione nuovo record
DERIV :  derivazione record da esistente
UPD :  Aggiornamento record
WRI :  Scrittura record
DEL :  Cancellazione record
 :  : FLD T$V5PQ  Conto Contabile
Se indicato determina il conto che verrà attribuito sulla riga del documento di attesa della fattura dell'agente.
 :  : FLD T$V5PU  Conto Contabile Fatture da Ricevere
Solo se indicato determina il conto che verrà attribuito sulla riga del documento di attesa della fattura dell'agente, qualora la provvigione liquidata si riferisca ad esercizi precedenti a quello di liquidazione.
 :  : FLD T$V5PR  Assoggettamento Iva
Se indicato determina l'assoggettamento iva che verrà attribuito sulla riga del documento di attesa della fattura dell'agente.
 :  : FLD T$V5PV  Esclusione Conguaglio Anticipi
Qualora si gestisca il conguaglio anticipi manuale, tramite la specifica scheda, attraverso questo campo è possibile escludere tale provvigione dagli importi previsti dalla succitata scheda.

