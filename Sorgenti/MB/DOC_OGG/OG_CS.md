# Campo / Domanda di questionario
Un campo può contenere : 
 * _2_una stringa libera, quando può contenere dei caratteri alfanumerici senza riferimenti ad oggetti del data base (es. il riferimento esterno nelle testate documento, la descrizione articolo, ...), in questo caso nel dizionario e negli archivi dove viene utilizzato il campo non viene tipizzato, per evitare che i programmi di controllo lo segnalino come errore deve essere stato inserito nelle schiere del programma B£EQRY_AO senza nessuna specificazione. Esempio :   _2_V5TDOC0F  T§DSPB
 * _2_una stringa libera con possibilità di oggettizzazione, quando può contenere dei caratteri alfanumerici attualmente senza riferimenti ad oggetti del data base me che potrebbe evolvere in un oggetto oppure che può contenere oggetti in funzione di come vengono sviluppate eventuali exit nei rpgrammi di gestione dell'articolo. In questo caso nel dizionario e negli archivi dove viene utilizzato il campo viene tipizzato con "_1_**". Le gestioni particolari di questi campi sono documentate nella documentazione del file.
 * _2_un oggetto, quando il contenuto è un oggetto, in questo caso il campo viene tipizzato in modo diverso a seconda che l'oggetto sia statico (es. il tipo articolo in BRARTI0F, l'articolo in GMQUAN0F, ..... ) o dinamico quando la sua caratterizzazione può variare di record in record e dipende da valori presenti in altri campi del record (es. il campo G§COD1 di GMQUAN0F dipende dal valore del Tipo Giacenza - campo G§SOGC). Avremo quindi : 
 ** _3_ oggetto statico, tipizzato con "_1_tipo oggetto / parametro" (es. TACLS, AR, .....) questi oggetti vengono risolti dal programma di decodifica B£DEC4
 ** _3_ oggetto dinamico, tipizzato con "_1_[valore 1] [valore 2]" dove valore 1 può essere presente o assente e se presente può essere o meno racchiuso tra parentesi quadre, mentre valore 2 è sempre presente e racchiuso tra parentesi quadre (es. _1_DO[T§TDOC], CN[TAV51 : *.T40 : 3], [A§TIAR.T50 : 6.I1], .....) questi oggetti vengono risolti dal programma di decodifica B£EQRY_OD
 * _2_un numero, una quantità, un valore, tipizzato con "_1_NR". _2_Nota se il contenuto del campo numerico è una data dobbiamo comunque riferirci all'oggetto data

## Esempi caratterizzazione oggetti dinamici
Possiamo avere : 
 * _1_[A§TC01], l'oggetto dinamico è specificato dal valore di un altro campo del record, in questo caso il valore del campo A§TC01
 * _1_OG[M$TIRE], l'oggetto dinamico è un "OGGETTO", specificato dal valore del campo M$TIRE
 * _1_[M$TIRE][M$PARE], l'oggetto dinamico ha OGGETTO = M$TIRE e PARAMETRO = M$PARE
 * _1_CN[M$TIEN], è un caso particolare della notazione precedente dove l'OGGETTO è fisso = CN e il PARAMETRO = M$TIEN
 * _1_[E$CONT.T20 : 12.O], l'oggetto è definito nella tabella di E$CONT, a partire dalla posizione 20 per una lunghezza di 12 ed è un oggetto fiisato nella tabella ("O")
 * _1_[A§TIAR.T56 : 3.G1], l'oggetto è definito nella tabella di A§TIAR, a partire dalla posizione 56 per una lunghezza di 3 ed è l'oggetto 1 definito nell'elemento della tabella B£G ("G1")
 * _1_[A§TIAR.T50 : 6.I1], come il precedente con la differenza che l'elemento 1 che viene recuperato è della tabella C£I ("I1")
 * _1_[D$TROT.T41 : 01.E01], come il precedente ma il valore finale ha una gestione particolare ("E") trattata specificatamente nel programma B£EQRY_OD alla select 01
 * _1_[U§LIVE.R01 : ART_MAT], l'oggetto è il primo o il secondo campo (01 - 02) ritornato dalla gestione delle risalite (R) eseguita dalla £GRI utilizzando come parametro di lancio quanto si trova dopo i duepunti (ART_MAT)

## Attributi di un campo
Un campo ha una serie di attributi : 
 * _2_Nr Campo in Record
 * _2_Nome Campo
 * _2_Descrizione
 * _2_Tipo Oggetto
 * _2_Parametro Oggetto
 * _2_Tipo Campo
 * _2_Lunghezza Campo
 * _2_Decimali Campo
 * _2_Buffer da
 * _2_Buffer a
 * _2_Settore
 * _2_Multiplo
 * _2_Chiave
 * _2_Obbligatorio
 * _2_Non controllare
 * _2_Livello autorizzazione
 * _2_Campo tecnico

la definizione di questi attributi proviene dalla definizione dell'archivio in cui il campo si trova; per i campi riferiti ad oggetti dinamici è dinamica e deriva dall'oggetto dinamico di riferimento; per gli attributi :  _3_Chiave, Obbligatorio, Non controllare, Livello autorizzazione, Campo tecnico, la definizione è cablata nelle schiere in fondo al programma B£EQRY_AO.



