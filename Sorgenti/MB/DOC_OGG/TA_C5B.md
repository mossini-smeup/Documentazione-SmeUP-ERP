# C5B - Conti contabili
 :  : DEC T(ST) K(C5B)
## OBIETTIVO
Definire i conti contabili a cui si intestano le registrazioni.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive il conto contabile
 :  : FLD T$C5BA **Categoria**
È un elemento TA/C5O :  è una classificazione libera del conto, che assegna al conto stesso una tipologia (conto patrimoniale, economico o ordine) e una natura (conto attività, passività, costi, ricavi o riclassifica). Il campo ha puramente valore statistico e le informazioni riportate in questa tabella sono riprese nei campi successivi della C5B.
 :  : FLD T$C5BB **Pertinenza**
È un elemento V2/C5PER che dichiara il tipo di utilizzo che si vuole fare del conto :  la scelta è tra contabile, gestionale o entrambe (comune). Se questo campo viene compilato all'atto dell'inserimento della registrazione viene controllato che la pertinenza del conto e della registrazione (viene ripresa dai flag di testata) coincidano.
 :  : FLD T$C5BC **Condizione**
È un elemento V2/C5COR che riporta il tipo di registrazione a cui è possibile associare il conto :  può essere attiva, sospesa o simulata. Se impostato, all'atto dell'inserimento di una registrazione, viene controllato che la condizione del conto e della registrazione (viene ripresa dai flag di testata) coincidano.
 :  : FLD T$C5BD **Validità esercizio (da/a)**
Sono elementi TA/PER :  se impostati, viene assegnato un periodo all'interno del quale il conto è valido. All'inserimento del conto in una registrazione viene controllato che il range di validità sia congruente con il periodo della registrazione.
 :  : FLD T$C5BF **Riclassifica CEE**
È un elemento TA/C5N (sottosettore CE) :  definisce la linea di bilancio CEE a cui appartiene questo conto, in modo da riclassificarlo secondo le direttive europee.
 :  : FLD T$C5BH **Tipo conto**
È un elemento V2/C5TCO :  definisce la tipologia del conto (patrimoniale, economico, d'ordine).
 :  : FLD T$C5BI **Natura del conto**
È un elemento V2/C5NCO :  definisce la natura del conto (attività, passività, costi, ricavi o riclassifica) all'interno della sua tipologia. Il campo è facoltativo :  se viene definito veicolerà la sezione di bilancio in cui il conto verrà visualizzato, se non è definito il sistema in automatico deciderà in che sezione collocare il conto analizzando la tipologia di conto e il suo saldo. Quindi, se ad esempio imponiamo su un conto patrimoniale la natura attività, questo conto sarà sempre visualizzato nelle attività indipendentemente dal suo saldo, mentre lasciando il campo blank il sistema collocherà il conto nelle attività se il suo saldo è in dare e nelle passività se è in avere.
 :  : FLD T$C5BJ **Tipo contatto**
È un elemento TA/BRE :  se impostato, significa che il conto è collegato a questo tipo di ente. In fase di interrogazione del conto verranno visualizzate tutte le registrazioni che abbiano come partita un ente dello stesso tipo riportato nel campo :  ad esempio, se compilo il campo con CLI interrogando il mastrino del conto visualizzerò tutte le registrazioni che abbiano come partita un CLI.
In fase di attribuzione del conto in manutenzione enti, si controlla che il tipo ente che si sta trattando sia uguale al corrispondente valore del conto.
Se utilizzato nella contabilizzazione delle pratiche nel conto di portafoglio, ne scatena la contabilizzazione dettagliata per ente.
Questo conto inoltre non può essere usato autonomamente in una registrazione contabile.
 :  : FLD T$C5BK **Valuta se in valuta**
È un elemento TA/VAL :  se impostato, viene controllato che le registrazioni in cui si inserisce il conto abbiano questa valuta. In questo modo è possibile ottenere rendiconti (mastrini e bilanci) nella valuta qui impostata. Se impostato il programma di immissione della prima nota chiederà obbligatoriamente anche il valore del cambio.
 :  : FLD T$C5BG **Gestito in analitica**
È elemento V2/SI/NO :  se impostato, significa che il conto è gestito in contabilità analitica (la riga di registrazione a cui appartiene il conto deve svilupparsi in righe di analitica).
La definizione della modalità con la quale si gestisce il dettaglio di analitica è specificata nella tabella C6B. A risalita può contenere : 
1) conto contabile della C5B;
2) categoria del conto contabile della C5B;
3) elemento di default '**'.
 :  : FLD T$C5BL **Gestione a documenti**
Se il conto è gestito a documenti verranno richiesti numero e data documento all'inserimento di ogni registrazione. Il campo può assumere vari valori : 
-' ' indica che il conto NON è gestito a documenti.
-'1' indica che il conto è gestito a documenti e che i riferimenti (data e numeor documento) vengono ripresi dalla testata della registrazione o imputati manualmente.
-'2' indica, invece, che il conto è gestito a documenti, ma che i riferimenti vengono ripresi in base all'OAV dell'oggetto riga indicato nei parametri del conto contabile.
-'3' indica che il campo è libero e non è soggetto alle forzature dovute ai campi di testata.
-'4' indica che per il conto sono attivate le interrogazioni per partita ma che in sede di gestione la partita non è obbligatoria.
 :  : FLD T$C5BM **Segno registrazione proposto**
È un elemento V2/C5DAAV. Se impostato, in immissione della registrazione viene proposto all'atto della digitazione del conto (se il campo non è già stato valorizzato). Questa impostazione, che vale solo per registrazioni non IVA, prevale su quanto eventualmente definito nella causale.
 :  : FLD T$C5BN **Obbligatoria data valuta**
È un elemento V2/SI/NO. Se impostato, nelle righe di questo conto la data valuta è obbligatoria; è generalmente impostato per i conti-banca.
 :  : FLD T$C5BO **Rilevanza cespiti**
È un elemento V2/SI/NO. Se impostato, le registrazioni contabili su questo conto, se con una causale con corrispondenza cespiti, saranno comprese nella funzione di ripresa movimenti contabili nell'applicazione cespiti.
 :  : FLD T$C5BP **Rapporto bancario**
È un elemento TA/C5J (eventualmente con il sottosettore dell'azienda). La sua presenza caratterizza il conto come conto bancario.
 :  : FLD T$C5BQ **Rilevanza Competenza**
Indica la rilevanza che il conto ha per gli stanziamenti. Può assumere i seguenti valori : 
- "1" il conto ha sempre rilevanza.
- "2" il conto non ha mai rilevanza.
- "3" il conto ha rilevanza solo se la competenza è differnte dal punto di vista fiscale (esercizio)
- " " il conto ha rilevanza solo per le registrazioni in cui è previsto lo stanziamento immediato in presenza di una data competenza diversa dalla data registrazione.
 :  : FLD T$C5BR **Rilevanza Controllo Fatture**
È un elemento V2SI/NO, se impostato implica che il conto potrà essere utilizzato solo in una registrazione con attivato il controllo fatture
 :  : FLD T$C5BS **Rilevanza Intercompany**
Indica la rilevanza del conto ai fini dell'analisi dei movimenti intercompany. I riferimenti vengono cmq riportati ma in funzione di questo flag è possibile operare dei filtri in fase di spunta.  Se indicato valore 1 il campo è semplicemente rilevante, mentre con il valore 2 va attivato se il conto rappresenta sempre una società ben precisa (es. Clienti/Fornitori Consociati) in funzione dell'ente  compilato o del codice indicato nel campo società intercompany (T$C5BV)
 :  : FLD T$C5BU **Rilevanza Valuta**
Indica se un conto patrimoniale multivaluta deve riportato nella registrazione di apertura per ogni singola valuta per il quale risulta aperto.
 :  : FLD T$C5BV **Società Intercompany**
Indica che il conto identifica sempre una particolare società intercompany. In questo caso è necessario indicare sempre anche il campo T$C5BS (Rilevanza Intercompany) pari a 2 per ottenere il comportamento corretto.
 :  : FLD T$C5BW **Conto Non Anagrafico**
Per i conti di mastro su soggetti, se indicato permette di forzare il suo utilizzo su soggetti che hanno un differente mastro indicato in anagrafica.
 :  : FLD T$C5BX **Cambio Traduzione Valuta**
Questo conto ha rilevanza solo qualora per l'ambiente, da tabella C57, sia prevista la gestione del bilancio in una valuta di traduzione.
Nel qual caso attraverso questo è campo è possibile specificare un metodo di traduzione specifico per il conto, che fa eccezione rispetto al criterioni indicato nella tabella C57 (es. in tabella indico che sui patrimoniali applicao il cambio corrente, ma su un conto di patrimonio netto lascio il cambio storico). Valori possibili solo : 
* 1. Cambio corrente :  forza per il conto la traduzione del saldo al cambio corrente
* 2. Cambio storico :  forza per il conto l'utilizzo del saldo calcolato dalla somma dei singoli  movimenti calcolati al cambio della data dell'operazione (data documento o data registrazione)
* 3. Cambio medio :  forza per il conto la traduzione del saldo al cambio medio (attraverso il il tipo cambio indicato nella tabella C57).
 :  : FLD T$C5BZ **Rilevanza provvigioni**
Se attivo e se utilizzato in una registrazione di fattura fornitore, se l'intestatario risulta esse un agente, nel modulo provvigioni, la registrazione verrà presa in considerazione per il controllo di quadratura coge/provvigioni.
 :  : FLD T$C5B1 **Costo/Ricavo Bancario**
Se impostato significa che il conto contabile indica un costo/ricavo bancario.
Questo viene utilizzato in tesoreria per analisi costi/ricavi per banca aziendale

