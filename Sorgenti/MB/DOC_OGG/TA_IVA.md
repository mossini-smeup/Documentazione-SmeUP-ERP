## CONTENUTO DEI CAMPI
 :  : FLD T$ALIQ Aliquota iva
È la percentuale legata all'assoggettamento
 :  : FLD T$IVAA __1=non soggetta__
Immettendo '1' in questo campo, l'operazione lagata a questo assoggettamento si intende ESENTE.
 :  : FLD T$IVAB __Conto Iva Vendite__
È il conto contabile legato all'IVA C/vendite
**ATTENZIONE** :  per chi ha la contabilità SMEUP, questo non è il conto utilizzato in essa :  i conti dell'IVA in questo caso sono definiti tramite gli elementi della tabella C5U.
 :  : FLD T$IVAC __Conto Iva Acquisti__
È il conto contabile legato all'IVA C/acquisti.
**ATTENZIONE** :  per chi ha la contabilità SMEUP, questo non è il conto utilizzato in essa :  i conti dell'IVA in questo caso sono definiti tramite gli elementi della tabella C5U.
 :  : FLD T$IVA3 __2° Assoggettamento__
Indica un ulteriore assoggettamento da applicare. Questo campo è da utilizzare nei casi in cui l'imposta IVA si componga di due tassazioni separate, che devono essere esplicitamente separate. L'effetto dell'utilizzo di questo campo è quello di applicare il secondo assoggettamento agli stessi importi su cui viene applicato il primo.
_9_Esempio :  normativa fiscale spagnola.
 :  : FLD T$IVA9 __Segno 2° Assoggettamento__
Indica il segno dell'imposta ottenuta applicando il secondo assoggettamento.
NOTA BENE :  se la contabilità è smeup è importante impostare sulla tabella C5A il tipo registrazione
da utilizzare per gli omaggi. Questo perchè per effetto di questo flag non ci sarà quadratura fra
imponibili e contropartite, per cui è necessario utilizzare un tipo registrazione che non preveda il controllo di tale quadratura.
_9_Esempio :  normativa fiscale messicana.
 :  : FLD T$IVAD __% indetraibilità__
È la percentuale di indetraibilità dell'imposta. Se valorizzata, viene assunta nelle registrazioni di fattura sulle righe di costo. Il sistema è quindi in grado di eseguire le scritture contabili automatiche di rettifica.
Se invece la si lascia in bianco, si dovrà impostare la percentuale di indetraibilità sui conti di costo, durante la registrazione contabile.
Se si imposta l'indetraibilità direttamente sul formato video di IVA, la rettifica automatica non verrà eseguita.
 :  : FLD T$IVAE __Operazione IntraCee__
Questo campo indica se l'operazione eseguita interessa la gestione INTRACEE e quindi deve essere ripresa all'interno dei modleli Intrastat.
 :  : FLD T$IVAF __Codice esenzione__
Identifica (ai soli fini della trasmissione delle operazioni con operatori economici della black list) la tipologia di esenzione : 
- ES=Esente
- NI=Non Imponibile
-   =Non Soggetta
 :  : FLD T$IVAW __Gestione plafond__
Indica che tipo di rilevanza ha l'assoggettamento nel calcolo del plafond. Può assumere i seguenti valori : 
- " "--> non ha nessuna rilevanza;
- "1"--> ha rilevanza sia nel calcolo del plafond disponibile (vendite) che del plafond utilizzato (acquisti);
- "2"--> ha rilevanza solo nel calcolo del plafond utilizzato (acquisti);
- "3"--> ha rilevanza solo nel calcolo del plafond disponibile (vendite).
 :  : FLD T$IVA2 __Reverse Charge__
Se utilizzato su acquisti permette di applicare il meccanismo, dell'"inversione contabile"  alle operazioni che non sono intra. Esso, in sostanza, comporta la rilevazione sia dell'imposta a debito che dell'imposta a credito, dell'operazione posta in essere da parte dell'acquirente.
Se utilizzato su vendite da l'indicazione del fatto che la controparte applica il meccanismo dell'inversione contabile. Tale indicazione va data che sia un'operazione intra o meno e serve essenzialmente per apporre la corretta dicitura "inversione contabile" alla stampa  delle fatture di vendita.
 :  : FLD T$IVA4 __Pro-Rata__
Indica l'utilizzo delle operazioni aventi tale assoggettamento nella formula del calcolo del pro-rata.
Può assumere i seguenti valori : 
- " "--> non ha nessuna rilevanza;
- "1"--> ha rilevanza come operazione esente;
- "2"--> ha rilevanza come operazione che dà diritto a detrazione;
- "3"--> ha rilevanza sia come operazione esente che come operazione che dà diritto a detrazione;
 :  : FLD T$IVA5 __Assoggettamento prioritario__
Indica nei documenti V5 (nel caso in cui tale assoggettamento sia utilizzato come assoggettamento della testata) che l'assoggettamento deve essere utilizzato anche per tutte le righe del documento assogettate ad aliquote normali (ovvero righe che non utilizzano codici Iva di esenzione).
Questo campo deve essere impostato qualora, ad esempio, alcuni enti abbiano assoggettamenti fiscali particolari (come l'aliquota Iva del 5,50% utilizzata in Francia), che deve essere utilizzata per tutte le righe del documento, indipendentemente dall'assoggettamento di riga.
 :  : FLD T$IVA6 __Natura Operazione__
Individua la natura dell'oggetto dell'operazione.
 :  : FLD T$IVA7 __Esclusione Volume D'Affari__
Se valorizzato, questo campo indica che le operazioni relative a questo assoggettamento vanno escluse dal volume d'affari.
 :  : FLD T$IVAG __Addebito bolli__
Determina se l'assoggettamento IVA comporta l'addebito delle spese di bollo in fattura (ad esempio nel caso di presenza di lettere d'esenzione).
Se l'assoggettamento IVA con questo campo impostato è utilizzato in una testata di un documento V5, verrà automaticamente aggiunto al documento la spesa identificata nella tabella V5S con il campo Tipo spesa/Maggiorazione/sconto impostato al valore BV-Spese Bollo da tabella IVA.
NOTA BENE :  fra questi elementi viene controllato il campo metodo, per verificare la data di fine di validità dell'elemento della V5S. La data va indicata in formato AAAAMMGG.
Il campo può assumere i valori ' ','1','2'. Con il rispettivo significato : 
' ' = Nessun Addebito
'1' = Addebito in fattura e in Nota di credito (in questo ultimo caso il valore viene reso negativo)
'2' = Addebito solo in fattura
 :  : FLD T$IVAZ __Fuori Campo IVA__
Se compilato indica che l'assoggettamento è fuori campo IVA, ovvero non verrà incluso nella stampa dei registri IVA. Se si vuole comunque stampare i movimenti fuori campo IVA sui registri è necessario codificare l'assoggetamento come Non Soggetto lasciando il campo 'Fuori Campo IVA' vuoto.
 :  : FLD T$IVAM __Esc.Elenco Clienti__
Se compilato con 1=Sì permette di escludere i movimenti intestati a clienti dallo spesometro.
 :  : FLD T$IVAR __Esc.Elenco Fornit __
Se compilato con 1=Sì permette di escludere i movimenti intestati a fornitori dallo spesometro.
 :  : FLD T$IVAL __IVA Omaggi__
È un campo utilizzato in caso di contabilità NON SmeUP per indicare il valore dell'assoggettamento da utilizzare in caso di omaggio nel caso in cui questo sia diverso da quello delle operazioni non soggette ad omaggio
 :  : FLD T$IVAI __IVA Cee__
È un campo utilizzato in caso di contabilità NON SmeUP per indicare il valore dell'assoggettamento da utilizzare in caso di operazione con soggetti CEE nel caso in cui questo sia diverso da quello delle operazioni nazionali.
 :  : FLD T$IVA0 __Controllo Dichiarazioni di Intento __
Attiva in connubio con le impostazioni delle tabelle V62 e C57 il controllo della presenza
di una corrispondente dichiarazioni di intento sul documento o la registrazione nella quale viene impiegato questo assoggettamento.
 :  : FLD T$IVA1 __Escludi dall'Assoggetamento Iva Documento__
Se l'iva della spesa presente nel documento è assoggettata al riproporzionamento basato sugli imponibili iva, gli stessi, assoggettati a questa aliquota saranno esclusi dal riproporzionamento e la spesa verrà ridistribuita solo sulle restanti aliquote.
Per una documentazione sul riproporzionamento fare riferimento alla tabella V5S.
