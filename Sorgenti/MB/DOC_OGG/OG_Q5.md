## Cos'è un Q5

L'oggetto Q5 identifica i programmi che permettono di costruire delle query (si veda il modulo) B£EQRY.

La fonte dati rappresenta l'origine dei dati in cui ricercare gli oggetti, fornisce delle query che è possibile eseguire per lo specifico contenitore. La query fornisce una sequenza di oggetti da restituire. Lo schema imposta le proprietà dell'oggetto che arricchiscono il record restituito. Il filtro parzializza i record da restituire. L'ordinamento sequenzia i record.

Per ogni oggetto sono quindi disponibili delle fonti in cui può essere ricercato, ogni fonte mette a disposizione delle query, ogni query mette a disposizione schemi, filtri e ordinamenti caratteristiche della ricerca.

## La codifica delle fonti
Le fonti standard sono codificate nelle schiere definite a pgm B£IQRS. Ad ognuna di esse tecnicamente corrisponde un programmi di tipo V3PQR (B£IQR_xx).

 :  : DEC T(OJ) P(*PGM) K(B£IQRS) L(1)
 :  : DEC T(MB) P(SMESRC) K(B£IQR_)(1)

Fa esse di particolare importanza ricoprono le fonti che vengono assunte come default per query : 
* Se l'oggetto appartiene ad un archivio viene assunta la fonte *FIL (da file) che permette di sfruttare le possibilità del motore SQL
* Viceversa viene assunta la fonte *INT (da interfaccia)

A fianco delle fonti standard possono essere definite delle fonti apposite per l'ambiente cliente.

Queste fonti vengono definite all'interno di uno script nel file SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).
Il nome dello deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Tipo Oggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro CNCLI e quindi il CN.
Quando si vuole quindi implementare un nuovo schema sarà innanzitutto necessario : 
* Verificare se esiste già uno file sorgente SCP_QRY nella libreria di personalizzazione dell'ambiente.
** In caso contrario crearlo (copia ad esempio quello della DEV)
** In caso affermativo verificando la presenza del sorgente corrispondente alla classe interessata (facendo le dovute considerazioni sul tipo/parametro)
** Se opportuno prendere in considerazione la possibilità di sfruttare le istruzioni dello script INC.SCP per includere in differenti script le stesse istruzioni

Fatto questo si può passare alla compilazione dello script. In questo senso è' importante notare che all'interno di questi script possono essere definiti, non solo gli schemi, ma anche tutte quelle informazioni utilizzabili poi nella costruzione di query in ambiente cliente. Nel wizard di questi script sussistono quindi vari tag non tutti immediatamente correlati alla definizione di uno filtro. Possono essere catalogati come tali i tag SRC.

In particolare il tag SRC permette di definire la fonte, stessa, mentre la parametrizzazione avviene tramite vari altri tag aggiuntivi, la cui composizione è abbastanza particolareggia e per questo, si rimanda direttamente alla documentazione specifica.

 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.REC) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.RE2) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.ALS) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.FLT) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.DST) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.GRP) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.JOI) L(1)
 :  : DEC T(RE) P(S-) K(EDT_QRY/SRC.PAR) L(1)

