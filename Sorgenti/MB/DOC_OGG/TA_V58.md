# V58 - Parametrizzazione delle Provvigioni
 :  : DEC T(ST) K(V58)
## OBIETTIVO
Definisce i parametri generali relativi alla Gestione delle Provvigioni.
## CONTENUTO DEI CAMPI
 :  : FLD T$V58E **Periodo di liquidazione**
Indica la periodicità in cui solitamente vengono liquidate le provvigioni. Può assumere i valori : 
 - M = mensile
 - T = trimestrale
 - A = annuale
In ogni caso poi è possibile differenziare il periodo per singolo agente.
 :  : FLD T$V58F **Tipo Provvigioni Fattura**
È un elemento TA/V5P. Indica il tipo di provvigione utilizzato di default per caricare una fattura.
 :  : FLD T$V58G **Controllo causali V56**
Attiva il controllo delle causali codificate nella tabella V56 :  le causali contabili qui codificate verranno esclude dagli importi da liquidare, pur venendo prese in considerazione per controllo della chiusura della provvigione. Il caso tipico è quello delle causali tramite cui viene rilevata una perdita :  codificando tali causali, la quota parte corrispondente non verrà mai liquidata all'agente, pur chiudendo la provvigione.
Va di fatto utilizzato obbligatoriamente in connubio con il campo T$V58N per escludere tali importi dalla liquidazione.
 :  : FLD T$V58I **Calcolo contributi mensili**
È un elemento V2SI/NO e indica se per le liquidazioni mensili (sia di provvigione, che di anticipi) devono essere calcolati i contributi.
 :  : FLD T$V58H **Tipo Liquidazione**
Indica il modo in cui generalmente viene effettuato il calcolo delle provvigioni. Può assumere i seguenti valori : 
  - " " = Sul fatturato ---> la liquidazione avviene in base a quanto viene fatturato dall'azienda al cliente dell'agente nel dato periodo;
  - "1" = Sul pagato ------> la liquidazione avviene in base a quanto viene pagato nel dato periodo;
  - "2" = Sul saldato -----> la liquidazione avviene in base a quanto viene saldato nel dato periodo.
 :  : FLD T$V58J **Piano anticipi**
È un elemento TA/V6Z. Definisce il piano anticipi usato come default nel caso non ne sia indicato uno specifico per l'agente.
 :  : FLD T$V58K **Tipo Provvigioni Note**
È un elemento TA/V5P. Indica il tipo di provvigione utilizzato di default per caricare una nota d'accredito.
 :  : FLD T$V58L **Programma Exit esecuzione liquidazione**
È un elemento V2SI/NO. Se impostato, implica l'esecuzione del programma di Exit V5PR02C_X al momento del calcolo delle provvigioni.
 :  : FLD T$V58N **Esclusione delta D/A da liquidazione**
È un elemento V2SI/NO. Se impostato, fa in modo che nella provvigione liquidata all'agente non venga imputato l'eventuale Delta D/A, presente sulla fattura, se la liquidazione avviene in base ai pagamenti effettuati. E' importante che in questo delta finiscono gli importi delle causali codificate nella tabella V56, quando l'utilizzo di tali causali è stato attivato tramite il corrispondente campo della V58.
 :  : FLD T$V58O **Piano Provvigione**
Permette di definire il calcolo delle provvigioni in modo più articolato rispetto al solo utilizzo del campo "tipo liquidazione".
Se valorizzato, il campo "tipo liquidazione" non verrà tenuto in considerazione.
Il campo può essere poi specializzato per singolo agente.
 :  : FLD T$V58P **Parzializzazioni su liquidazione definitiva**
Se impostato, permette di parzializzare su una liquidazione definitiva.
I campi di parzializzazione disponibili sono Codice intestatario, numero e data fattura.
 :  : FLD T$V58Q **Tipo periodo liquidazione**
Questo campo permette di determinare il tipo di periodicità che si vuole utilizzare per la liquidazione.
I valori possibili sono : 
- " " = standard --> sono gestiti solo i periodi fissi mensile, trimestrale e annuale
- "1" = libero ----> i periodi sono liberamente definiti dagli elementi della tabella TAV5*LQ.
 :  : FLD T$V58R **Solo divisa di conto**
Questo campo permette di determinare se, in fase di ripresa dei valori dalle fatture di vendita, le provvigioni verranno comunque imputate in divisa di conto, qualsiasi essa sia.
Questo implica che verrà letto il campo £V5FR della routine di fatturazione, mentre i campi valuta e cambio non saranno valorizzati.
 :  : FLD T$V58T  h_Liquidazione NC sul Pagato
Di norma le provvigioni da note di accredito di norma vengono liquidate con la logica del fatturato, cioè nel periodo in cui vengono create. Tramite questo flag è possibile indicare che vengano invece liquidate in funzione dei saldi della corrispondente partita contabile.
 :  : FLD T$V58U **Non Gestire flag 19**
Inserendo il valore '1' in questo campo viene disattivato,nel pgm di ripresa provvigione da fatture,
il controllo del campo R§FL19 (tipo riga in fattura).
Attualmente il pgm di gestione documento V5V5F0 **NON CONSIDERA**le righe con il campo R§FL19 (flag
19 di riga) con i valori  '1' '2' '7' '8' '9' '0', questo indipendentemente che sul record ci sia o meno
agente e provvigione. Con la disattivazione vengono considerate Tutte le righe con agente e provvigione
indipendentemente dal flag, Unica eccezione il flag R§FL19 =  '9'
 :  : FLD T$V58A
Inserendo il valore '1' in questo campo viene attivata l'obbligatorietà della Valuta (Tabella VAL) nell'inserimento manuale delle provvigioni, con assunzione automatica della valuta corrente.
Questo campo è importante se sui documenti v5 viene gestita esplicitamente la valuta corrente.
 :  : FLD T$V58B
Se attivato nel calcolo delle pagato sulle provvigioni vengono considerati anche i movimenti provvisori in base a quanto indicato. NOTA BENE :  deve essere indicato un valore che includa anche i movimenti attivi (es. " 9").
 :  : FLD T$V58C
Indica il sottosettore del listino provvigioni nelle schede del modulo provvigioni.
 :  : FLD T$V58D
Calcolo contributi su fatturato. Se valorizzato e se la liquidazione segue i criteri di pagato/saldato è possibile forzare tramite questo flag che il calcolo dei contributi venga invece effettuato tramite il criterio del fatturato.
 :  : FLD T$V58V
Le note delle provvigioni scritte, nel tipo informazione indicato, verranno riportate nella stampa della proforma.
 :  : FLD T$V58W
Se il campo viene valorizzato, viene disattiva la gestione della funzione di generazione del piano contributi e del documento attesa. Con questa impostazione diventa possibile eseguire più liquidazioni consecutive senza dover prima eseguire la generazione del piano/contributi e del documento di attesa.
 :  : FLD T$V58Y
Se il conguaglio degli anticipi viene gestito manualmente, con la specifica scheda, tramite questo campo è possibile definire il tipo provvigione da utilizzare per l'attribuzione di tale conguaglio.
 :  : FLD T$V58Z
Se il conguaglio degli anticipi viene gestito manualmente, con la specifica scheda, permette di indicare se nel conteggio degli anticipi corrisposti si vogliono escludere gli anticipi degli anni precedenti.
 :  : FLD T$V581
Al fine di contabilizzare anche il conguaglio anticipi a totale 0, tramite questo campo è possibile definire quale tipo registrazione utilizzare per tale operazione. Dovrà trattarsi in questo caso di un tipo registrazione di documento senza iva.
 :  : FLD T$V582
Al fine di contabilizzare anche il conguaglio anticipi < di 0, tramite questo campo è possibile definire quale tipo registrazione utilizzare per tale operazione. Dovrà trattarsi in questo caso di un tipo registrazione di nota d'accredito.
 :  : FLD T$V58X
L'impostazione di questo campo a forti implicazioni :  in sostanza definisce a partire da quale applicazione vengono determinati i numeri che si ritiene validi ai fini del calcolo contributi.
Di default viene presa in considerazione l'applicazione dei documenti e quindi il modulo provvigionale :  sono i dati che risultano da questo modulo da essere considerati come definitivi e certificabili. La contabilità deve esservi sempre allineata.
Viceversa se è la contabilità ad essere considerata come applicazione master, sarà il modulo provvigioni a dover adeguarsi a tali numeri.
NOTA BENE :  nel primo caso l'adeguamento/controllo è totalmente manuale, mentre nel secondo caso i dati dei contributi creati dal modulo provvigionale vengono messi in stato annullato, mentre tutte le registrazioni contabili vanno a generare dei nuovi dati costruiti a partire dalle registrazioni contabili.
Si veda la documentazione applicativa del modulo per maggiori dettagli.

 :  : FLD T$V58S
Definisce il contenitore per le note delle singole provvigioni.

 :  : FLD T$V584 Controllo Rischio
Se attivato nel pgm di calcolo degli importi da liquidare, gli incassi a rischio verranno esclusi e non verrà più richiesta la data limite insoluti.

