# C53 - Impostazioni base pagamenti
 :  : DEC T(ST) K(C53)
## OBIETTIVO
Definisce i parametri generali di impostazione per i programmi di gestione pagamenti (costruzione pratiche/saldaconto)
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$C53A **Tipo gestione valuta**
È un elemento V2/C5V01. Nel saldaconto definisce il modo di rappresentare  le righe di dovuto non della valuta impostata : 
-    ' '  righe escluse.
-    '1'  righe presentate ma non selezionabili.
-    '2'  righe presentate e selezionabili (con calcolo cambio contestuale) (SV).
 :  : FLD T$C53B **Ordinamento**
È un elemento V2/C5V02. Definisce l'ordinamento con cui vengono proposte le righe di pagato nel saldaconto : 
-    ' '  per data scadenza.
-    '1'  per documento (SV).
 :  : FLD T$C53C **Primo sollecito**
Tipo sollecito di livello minimo
 :  : FLD T$C53D **Spese amministrazione per sollecito**
Spese relative alla spedizione del sollecito
 :  : FLD T$C53E **Percentuale interessi di mora**
Percentuale di mora su ritardo pagamento
 :  : FLD T$C53F **Numerazione pratiche di tipo proposte**
Definisce il numero di pratica associato alle proposte (tipi pratiche con prefisso 'P'). Sono dei contenitori formati da proposte di pratiche.
Valori possibili : 
-    ' ' assume il valore fisso 'PROPOSTA'.
-    '1' assume il nome del gruppo utenti a cui appartiene l'utente di lavoro specificato nella tabella B£U.
-    '2' assume il nome dell'utente di lavoro.
 :  : FLD T$C53G **Calendario Codice Pagamento**
Definisce la risorsa collegata ai codici pagamento per la gestione di un loro specifico calendario.
 :  : FLD T$C53H **Tipo Registrazione Pareggio Documenti**
Definisce il Tipo Registrazione da utilizzare nella registrazione di pareggio partite automatico.
 :  : FLD T$C53I **Codice Pagamento Pareggio Partite**
Definisce il Codice Pagamento che verrà forzato sulle rate di una registrazione di pareggio partite automatico.
 :  : FLD T$C53J **Utilizzo data valuta in trasmissione bonifici**
Indica se la data valuta deve essere utilizzata nella trasmissione dei bonifici : 
-    ' '=SI -----> la data valuta viene trasmessa (se ha valore 0 viene trasmesso 0).
-    'N'=NO -----> la data valuta non viene trasmessa (viene sempre trasmesso a 0).
 :  : FLD T$C53K **Calendario Tipo Pagamento**
Definisce la risorsa collegata ai tipi pagamento per la gestione di un loro specifico calendario. Questo calendario viene applicato sia agli incassi che ai pagamenti salvo che sia stato definito  anche il calendario specifico dei tipi sui pagamenti passivi.
 :  : FLD T$C53L **Valore Scostamento Pareggio Partite**
Indica l'importo massimo del residuo da abbuonare su una rata che viene pareggiata.
 :  : FLD T$C53M **GG aggiuntivi calcolo interessi di mora**
GG che vengono addizionati all'effettivo ritardo per il calcolo degli interessi di mora nei solleciti
 :  : FLD T$C53N **Tipo cambio fine esercizio**
Definisce il tipo cambio da utilizzare per l'attualizzazione dell'attivo e del passivo, circolante alla fine di un esercizio.
 :  : FLD T$C53O **Importo minimo non sollecitabile**
Se il totale dei solleciti per Ente è al di sotto dell'importo indicato la lettera non verrà generata.
 :  : FLD T$C53P **Intervallo in giorni**
Indica il numero di gg che devono passare dalla scadenza prima che venga estratto il primo sollecito in caso di mancato incasso.
 :  : FLD T$C53Q **Controllo Cooridinate bancarie bonifico**
Con valore 2 permette di disattivare il controllo sulle coordinate bancarie in fase di creazione della distinta. Questo dovrebbe servire solo per una situazione transitoria, se in precedenza le coordinate bancarie complete sono state compilate solo sul file di remote.
Il valore 1 esiste per ragioni storiche ma a ora lo stesso significato del blank.
 :  : FLD T$C53R **Tipo Registrazione Pareggio Partite**
Se valorizzato il tipo registrazione indicato viene utilizzato in sostituzione del tipo registrazione indicato
nel camp Pareggio Partite Documenti, qualora il pareggio non avvenga fra documenti di segno opposto, ma fra
scadenze di altra natura (es. anticipi).
 :  : FLD T$C53S **Pareggio Automatico Anticipi su Reg. Documento**
Se attivato, questo campo permette di lanciare successivamente alla registrazione interattiva di un documento
l'esecuzione di una registrazione di pareggio partite in presenza di rate d'anticipo di segno opposto presenti
per il soggetto intestatario del documento. Il campo può assumere i seguenti valori : 
"1" = Automatico, viene eseguito in modo cieco e solo se gli anticipi presentano i medesimi riferimenti
      di n° e data documento
"2" = Interattivo, include anche il metodo automatico, ma adesso aggiunge nel caso siano presenti solo
      anticipi con riferimenti non corrispondenti il lancio interrattivo di una registrazione di pareggio
      che propone come rate da saldare il minor ammontare fra le rate del documento e gli anticipi di segno
      opposto pareggiabili.
I valori 3/4 e 5/6 hanno lo stesso significato dei corrispondenti valori 1/2, con la differenza che limitano la funzione al solo ciclo attivo/passivo.
Se viene attivato questo campo si consiglia di impostare per le registrazioni di pareggio partite l'ingresso in lista sul saldaconto dalla C5D.
 :  : FLD T$C53T **Data registrazione in pareggio partite**
Questo campo determina la data registrazione da utilizzare nella funzione di pareggio partite
" " = Indica che la data registrazione viene calcolata dal sistema
"1" = Indica che la data registrazione è sempre uguale alla data odierna
 :  : FLD T$C53U **Calendario Tipi Pagamento su Pagamenti (For)**
Valorizzare questo campo per definire la risorsa collegata ai tipi pagamento per i soli pagamenti,
per la gestione di un loro specifico calendario.
 :  : FLD T$C53V **Tipo Evento Gestione Crediti**
Se valorizzato indica il Tipo Evento che definisce gli eventi collegati ad una partita per la gestione dei crediti.
 :  : FLD T$C532 **Tipo Responsabile**
Se valorizzato indica il Tipo Oggetto di Riferimento utilizzato per tipizzare i responsabili del credito, sulle rate, qualora questo non coincida con l'oggetto TAAGE (Agenti).
NOTA BENE :  questo campo serve solo come riferimento per elaborazioni di carattere generale. Sulle scadenze il tipo oggetto viene ripreso in base alla configurazione degli elementi della tabella C5E ed il contenuto della C53 dovrebbe esservi congruente.
 :  : FLD T$C533 **Livello Blocco**
Definisce se il blocco pagamento può essere gestito a livello di singola rata, per solo per intero documento (quindi a livello di testata).
 :  : FLD T$C534 **Riferimento fiscale debitore per trasmissione riba**
Determina il riferimento fiscale del debitore da prendere in considerazione per la trasmissione delle riba italiane.
A livello di regolamentazione dell'Organo CBI è previsto che venga utilizzato solo il codice fiscale, ma nella prassi le banche possono chiedere anche la partita iva.
Sono possibili i seguenti valori : 
* "1" = Partita iva ed in sua assenza il codice fiscale
* "2" = Codice fiscale ed in sua assenza la partita iva
* " " = Codice Fiscale (quello previsto dalla normativa cbi)


