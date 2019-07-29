# V51 - Parametri ciclo esterno
 :  : DEC T(ST) K(V51)
## OBIETTIVO
Definisce i parametri generali relativi al ciclo attivo.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$DESC Note
 :  : FLD T$V51A **Gestione rate in fattura**
Se questo campo è diverso da blank, viene effettuato il calcolo delle rate relative al codice di pagamento sul totale fattura.
 :  : FLD T$V51B **Stampa controllo fattura**
Se questo campo è diverso da blank, viene lanciata insieme alla stampa della fattura anche quella di controllo.
 :  : FLD T$V51D **Tipo contatto**
È un elemento della tabella BRE. È il tipo ente che viene utilizzato nella contabilizzazione.
 :  : FLD T$V51E **Programma commenti aggiustamento fatture**
Nome del programma che permette di definire dei commenti aggiuntivi a livello di riga nella stampa della fattura.
 :  : FLD T$V51F **Ambiente contabilizzazione**
È un parametro tipico dell'applicazione contabile interfacciata.
_9_Esempio :  se l'applicazione è sotto modulo base, se in questo campo si inserisce il sistema informativo d'arrivo, viene eseguito, dopo la scrittura degli archivi di transito, anche il passaggio agli archivi finali dei movimenti contabili.
Per le Installazioni che prevedono come ambiente di contabilizzazione l'Azienda è possibile
lasciare bianco questo campo ed impostare il campo T$V62D (della tabella V62) che riempie questo
campo con l'azienda. Questa opzione è utile per le installazioni multi azienda in cui la tabella
V51 non contiene dati differenti tra un'azieda e l'altra. Si può lasciare la tabella V51 tra le
tabelle di gruppo
 :  : FLD T$V51G **Non imp.Data Fattura**
Se impostato a '1' il programma di acquisizioni dati per stampa fattura (V5FA01A e V5FA02A) non impostano la
data fattura con "oggi".
Lasciando non valorizzato (blank) i programmi continuano a impostare il default nella data fattura

 :  : FLD T$V51H **Data Val.List.TEST.**
È un valore compreso tra 1 e 5 ed indica la data da utilizzare per controllare la validità del codice listino, inserito nella testata documenti. Il significato dei valori è il seguente : 
- 1=Data documento;
- 2=Data ordine cliente;
- 3=Data inserimento;
- 4=Data consegna richiesta;
- 5=Data consegna confermata.
 :  : FLD T$V51I **Data Val.List. C.A.**
È un valore compreso tra 1 e 5 ed indica la data da utilizzare per controllare la validità del listino inserito nelle RIGHE documenti DEL CICLO ATTIVO.
Il significato dei valori è il seguente : 
- 1=Data documento;
- 2=Data ordine cliente;
- 3=Data inserimento;
- 4=Data consegna richiesta;
- 5=Data consegna confermata.
 :  : FLD T$V511 **Data Val.List. C.P.**
È un valore compreso tra 1 e 5 ed indica la data da utilizzare per controllare la validità del listino, inserito nelle RIGHE documenti DEL CICLO PASSIVO.
Il significato dei valori è il seguente : 
- 1=Data documento;
- 2=Data ordine cliente;
- 3=Data inserimento;
- 4=Data consegna richiesta;
- 5=Data consegna confermata.
Se non inserito viene assunto il parametro del ciclo attivo.
 :  : FLD T$V51L **Cost.Conto articolo**
Individua quale classe dell'articolo definisce i conti contabili.
È possibile scegliere una tra le seguenti classi : 
-    Tipo Articolo            (BRA);
-    Classe materiale         (CLS);
-    Classe programmazione    (BRO);
-      Classe gestione          (BRH);
-      Calsse contabile         (BRB);
-      Calsse fiscale           (BRF);
-    Classe valore            (BRV);
-    Riclassifica xx          (CLRxx).
Gli elementi di questa classe dovranno essere codificati nella tabella COA, sottosettore AR, dove si inseriranno i conti contabili.
 :  : FLD T$V51M **Tipo Ente Vettori**
È un elemento della tabella BRE. È il tipo ente che definisce i vettori nell'applicazione.
 :  : FLD T$V51N **Ass.Fis. Cli assunto**
È il codice di assoggettamento fiscale assunto per il cliente se nell'anagrafico è blank. È un elemento della tabella IVA.
 :  : FLD T$V51O **Aliq.Iva Art assunta**
È il codice dell'aliquota Iva assunta per l'articolo, se nell'anagrafico è blank. È un elemento della tabella IVA.
 :  : FLD T$V51V **Reg.contab.solo lire**
Inserendo il carattere '1', la contabilizzazione delle fatture in valuta viene trasformata in lire.
 :  : FLD T$V51C **Evad.al lordo att.spedizione**
Inserendo il carattere '1' nell'analisi evadibilità, la quantità residua in ordine non viene nettificata della quantità in attesa spedizione (già portata in bolla e non ancora collegata a magazzino). Lasciandolo a blanks viene nettificata di questa quantità.
L'impostazione di questo campo ha lo scopo di velocizzare le funzioni di evadibilità, in quanto nelle singole fonti si specificherà se saranno al netto o al lordo dell'attesa spedizione. Con questo filtro si escluderanno preventivamente le righe che, con l'attesa spedizione, risulteranno saldate, senza dover eseguire l'analisi disponibilità per scoprirlo.
 :  : FLD T$V51P **Cod.sconto pagamento**
È un elemento della tabella V5S. Se la tabella modalità di pagamento prevede uno sconto in percentuale a fine fattura, questo codice ne determina le caratteristiche.
 :  : FLD T$V516 **Cod.Spese di incasso**
È un elemento della tabella V5S. Se la tabella modalità di pagamento prevede un importo di spese di incasso a fine fattura, questo codice ne determina le caratteristiche.
 :  : FLD T$V51Q **Calendario fatturaz.**
È un elemento della tabella TRG. È utilizzato per definire il calendario della fatturazione speciale. La risorsa di questo calendario è un elemento della tabella BR*CF. La risorsa è legata al cliente tramite l'estensione dei contatti (elemento £08 della tabella BRI) ed unisce un cliente ad un tipo di fatturazione.
 :  : FLD T$V51R **Dettaglio conti**
Indica il dettaglio con cui la £V5F ritorna i valori relativi ai singoli conti (dettaglio di registrazione). I valori possibili sono : 
- ' '  Riepilogo per conto;
- '1'  Riepilogo per conto/centro di costo;
- '2'  Riepilogo per conto/commessa;
- '3'  Riepilogo per conto/centro di costo/commessa;
- '4'  Riepilogo per conto/centro di costo/Voce di spesa;
- '5'  Riepilogo per conto/commessa/Voce di spesa;
- '6'  Riepilogo per conto/centro di costo/commessa/Voce di spesa;
- '7'  Riepilogo per conto/Voce di spesa;
- 'A'  Riepilogo secondo il modello di analitica inserito.
 :  : FLD T$V510 **Ambiente provvigione**
È un elemento della tabella *CNAA ed indica in che ambiente applicativo vengono calcolate le provvigioni agente.
 :  : FLD T$V51S **Responsabile C.A./Parametro**
Inserendo il tipo e il parametro si specifica l'oggetto da inserire nel campo responsabile nei documenti del ciclo attivo (tipo modelli che iniziano con A*).Iil default è DI/ (dipendente).
 :  : FLD T$V51T **Responsabile C.A./Parametro**
È il parametro dell'oggetto inserito nel campo responsabile C.A.
 :  : FLD T$V51U **Responsabile C.P./Parametro**
Inserendo il tipo e il parametro si specifica l'oggetto da inserire nel campo responsabile nei documenti del ciclo passivo (tipo modelli che iniziano con P*). Il default è DI/ (dipendente).
 :  : FLD T$V51Z **Responsabile C.p./Parametro**
È il parametro dell'oggetto inserito nel campo responsabile C.P.
 :  : FLD T$V512 **Forzatura conto contabile su riga**
Indica la possibilità di modificare, forzandolo, il conto assegnato alla riga.
1=Nel campo è contenuto il conto contabile normale completo.
 :  : FLD T$V513 **Arrotondamento IVA**
È il metodo con cui viene arrotondato l'importo IVA nei documenti. Può assumere i seguenti significato : 
- '+'  Per eccesso;
- '-'  Per difetto;
- 'H'  Per eccesso/difetto;
Se lasciato ' ' (blanks) viene assunto il metodo '+'.
 :  : FLD T$V514 **Gest.conto abbuoni**
Inserendo il valore '1', si introduce la gestione del conto sconto/abbuono diverso al conto merce, nelle registrazioni contabili legate a righe documento con omaggi imponibili.
Lasciando questo campo blanks (' ') il programma utilizza  il conto merce sia per il dare che per l'avere.
 :  : FLD T$V515 **Tipo ente spedizione documenti V5**
Definisce (ed abilita) il tipo contatto (tabella BRE) da utilizzare per la gestione dei dati di spedizione specifici di un documento, ovvero la possibilità di specificare un determinato indirizzo di spedizione che verrà utilizzato e legato al documento V5 che si stà gestendo.
 :  : FLD T$V518 **Attiva Cont.Analit.**
Inserendo il valore '1', si attiva la funzione di gestione della contabilità analitica durante la contabilizzazione delle fatture del ciclo attivo.
 :  : FLD T$V517 **Disab.F06 Doc.Coll.**
Inserendo il valore '1', si disattiva il controllo dei documenti collegati. Lasciando il valore a ' ', se un documento è collegato, anche se autorizzati, chiede conferma (F06) per la gestione (modifica e cancellazione).
 :  : FLD T$V51J **Rata scadenze variabili**
È il tipo rata da utilizzare per definire delle modalità di pagamento che non rientrano nelle normali modalità, codificabili tramite un codice pagamento (ad esempio un pagamento del tipo 20% a 30gg  30% a 48gg  e 50% a 65gg)
 :  : FLD T$V51Y **Suffisso pgm exit post-contabilizzazione**
Se impostato dopo l'esecuzione della contabilizzazione verrà eseguito il pgm V5FA08_+"codice ambiente applicativo", in cui è possibile implementare comportamenti specifici da eseguire al termine della contabilizzazione di tutti i documenti elaborati.
 :  : FLD T$V51K **Att.pgm creaz. rate**
Inserendo il valore '1' in questo campo, si attiva la costruzione delle rate mediante il programma utente V5FA05R_U.
È possibile condizionare (durante la scrittura del file C5BATC0F) la costruzione delle rate della fattura.
Se lasciato bianco, il programma di contabilizzazione genererà le rate normalmente utilizzando il codice di pagamento.
 :  : FLD T$V51W **Flag 07 standard**
Se impostato, il flag 07 di riga documento V5 (campo R§FL07 file V5RDOC0F Inversione quantità/valore) verrà impostato utilizzando la modalità standard, che prevede di utilizzare il valore specificato nel gruppo flag specifico (tabella B£Y).
Se questo flag non è impostato, il valore del campo R§FL07 verrà impostato in fase di inizializzazione dalla routine £V5Z (programma V5V5Z0), che inserirà il valore 1 in tutte le righe di documenti il cui tipo modello sia : 
-   AE   Ciclo att.  Entrate;
-   AN   Ciclo att.  Note di credito;
-   PU   Ciclo pass. Uscite;
-   PN   Ciclo pass. Note di credito;
Va ricordato che il tipo modello di un documento V5 viene specificato nella tabella V5Axx.
Nel caso si decida di gestire in modalità standard il flag 07, si consiglia di controllare che in tutti i gruppi flag utilizzati nei documenti appartenenti ai tipi modelli sopraelencati, sia opportunamente impostato il valore da assegnare al flag 7 (che NON verrà in questo caso impostato automaticamente dall'inizializzatore di riga).
Si consiglia di impostare questo flag qualora si gestiscano documenti con gestione quantità a partita (vedi campo R§FL03  file V5RDOC0F Metodo gestione quantità) o qualora si voglia gestire la riapertura dei documento origine (ordini) in caso di resi.
 :  : FLD T$V51X Att.Gest.conti mult.  
Inserendo il valore '1' in questo campo si attiva la gestione multipla dei conti contabili legati
ad una riga di v5. Tramite il pgm V5V5F0_C (programma con nome fisso) è possibile spezzare la riga
fino a 5 conti contabili (con relativi dettagli di analitica)
 :  : FLD T$V51§ No.Rottura Ass.Iva    
Inserendo il valore '1' in questo campo si disattiva la rottura conto per assoggettamento IVA
 :  : FLD T$V51$ Blocco Documento    
Inserendo il valore '1' Si attiva il blocco logico di un documento in manutenzione, che consiste nel impedire la
modifica, la cancellazione e gli inserimenti di nuove righe per un documento in manutenzione da un altro utente
(il blocco è gestito sia sulla testata che sulle righe).
Questa scelta si applica su tutti i documenti, è possibile eseguire delle eccezioni nella tabella V5D per singoli tipi
documento.
La gestione dei vincoli (lock di tipo pessimista) è fatta mediante il codice oggetto 1 "DO", gestito tramite £G81 ed
inserito nella tabella B§L.
 :  : FLD T1V51A Num.Fat.Sp.   
Il campo è il suffisso del programma di aggiustamento V5FA01S_x
Con il programma in questione (presente una exit standard '1' che sotto specifichiamo) si riesce a gestire numeratori
Speciali (particolari rispetto allo standard di V5A).
Nella EXIT distribuita (v5fa01s_1) viene utilizzato il numeratore standard contabile (keep.UP) recuperato, e creato in
sua mancanza, l'elemento della tabella CRN C5 collegato al registro iva associato al documento (è controllata la
causale contabile collegata al documento che l'eventuale causale di forzatura presente nel documento)
 :  : FLD T1V51B  Att.Scen.
Inserendo il valore '1' si attiva su tutti i documenti la gestione per scenario.
E' possibile modificare la attivazione/disattivazione sul singolo tipo documento agendo sul campo
presente nella tabella V5D.
Per un maggiore dettaglio riferirsi alla PTF V521213A
