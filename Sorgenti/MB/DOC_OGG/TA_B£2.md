# B£2 - Personaliz. (in coda a B£1)
 :  : DEC T(ST) K(B£2)
## CONTENUTO DEI CAMPI
 :  : FLD ££UMHR  **Unità di misura frazioni ora**
È un flag che indica come vengono rappresentate in azienda le frazioni di ora, se in centesimi o in minuti (o sessagesimi).
Può assumere due valori : 
C=centesimi (default)      mezz'ora = 0,50
S=sessagesimi              mezz'ora = 0,30
 :  : FLD ££PAMI **Arrotondamento ore**
È espresso in minuti. Viene usato per controllare le ore immesse e per arrotondare quelle calcolate. Per non avere arrotondamenti si deve immettere 0 o 1, per arrotondare all'ora si deve immettere 60.
 :  : FLD ££MAGD **Magazzino unico**
È un elemento della tabella MAG :  se impostato definisce il plant utilizzato nell'applicazione, che risulta quindi essere monoplant.
 :  : FLD ££B£2L **Attivazione LOG utilizzo oggetti**
Definisce (dove previsto) se il programma deve presentare le tabelle utilizzate mediante il comando F22 .
La tecnica utilizzata è quella del doppio assenso. Il programma imposta il secondo carattere a "1" se intende gestire la memorizzazione degli oggetti utilizzati. L'utente può impostare in personalizzazione il primo carattere a "1". Se entrambi i caratteri sono in tale situazione, la funzione è attiva.
 :  : FLD ££B£2P **Attivazione PROTEZIONE a Livello campo**
Permette la definizione delle condizioni desiderate, relativamente alla funzione di protezione livello campo richiamata dai principali programmi di gestione dettaglio dei dati.
Sono previsti i seguenti valori : 
' '= Non sono attive le protezioni. Tutti i campi del dettaglio sono visualizzati e modificabili
1  = Protezioni attive in modo normale
2  = Protezioni attive ma esse stesse sotto autorizzazione
Si intendono autorizzati a definire e salvare le autorizzazioni solo coloro che, nella classe "AUT", sono abilitati ad impostare le autorizzazioni alla funzione
"PLC-xxxxxx" tipica del contesto.
3  = Come sopra. Inoltre, quando viene letta l'impostazione utente, se mancante, si ricerca un default per tutti gli utenti. La memorizzazione di tale default è responsabilità del gestore del sistema che dovrà utilizzare la funzione manuale di gestione archivio memorizzazioni (UP MDV), copiando i dati desiderati sull'utente "**"
 :  : FLD ££B£2S **Attivazione SCENARI multipli**
Per sviluppi futuri
 :  : FLD ££B£2A **Azienda**
È un elemento di oggetto AZ :  definisce il codice dell'azienda a cui si riferisce questa installazione.
Viene utilizzato principalmente dalle applicazioni contabili.
 :  : FLD ££B£2B **Modo presentazione istanti**
È un elemento V2/TI_I1 che indica come saranno presentati gli istanti di inizio e fine in tutte le applicazioni.
 :  : FLD ££B£2C **Controllo compatibilità stati**
Stabilisce le modalità di controllo delle regole di transizione di stato, previste dalle tabelle B£Wxx.
I valori gestiti per questo campo sono : 
- ' '  Viene effettuato il controllo standard (stato minimo e massimo di provenienza...).
- '1'  Viene effettuato unicamente il controllo di esistenza dello stato sulla tabella B£Wxx.
 :  : FLD ££B£2F **Descrizione estesa assunta**
È un elemento della tabella LIN :  definisce la lingua assunta durante la lettura delle descrizioni estese. Esempio :  se in distinta o in stampa documenti, si vogliono visualizzare le descrizioni aggiuntive, se nessuna lingua è specificata, si assumerà la lingua corrente.
 :  : FLD ££B£2D **Codice divisa corrente**
È un elemento della tabella VAL :  definisce la divisa corrente per il sistema.
Il campo "divisore", se impostato a "1", indica che nei confronti della valuta corrente i cambi sono espressi in valuta estera per un valore unitario di valuta corrente (es. caso EURO o STERLINA INGLESE).
Se non impostato, indica che il cambio verrà espresso nella forma per cui si indica il valore di valuta corrente per un valore unitario di valuta estera (es. caso LIRA o DOLLARO).
 :  : FLD ££B£2E **Codice divisa EURO**
È un elemento della tabella VAL :  definisce il codice della divisa che identifica l'EURO.
 :  : FLD ££B£2G **Magazzino di competenza**
È un elemento della tabella MAG :  è significativo, se non è stato impostato in questa tabella il magazzino unico.
Se impostato, tutti gli articoli hanno questo articolo come magazzino di competenza.
Se non impostato, è obbligatoro definire nell'anagrafica, per ogni articolo, il proprio magazzino di competenza (nel campo ente interno responsabile).
Il campo di anagrafica, se impostato, ha comunque la priorità su questo campo.
 :  : FLD ££B£2H **Nazione assunta**
È un elemento della tabella V§N :  se impostato, viene assunto dagli enti che hanno il codice nazione in bianco. Questa assunzione viene eseguita a livello di deviatore, quindi è valida anche per enti non Sme_up.
 :  : FLD ££B£2I **Lingua assunta**
È un elemento della tabella V§L :  definisce la lingua in cui verrà presentata l'interfaccia utente. L'indicazione di questo valore induce l'innesco automatico della gestione multilingua, con relativo carico di elaborazione in tempo reale; nel caso la lingua assunta sia l'italiano è opportuno omettere tale valore, per evitare inutile utilizzo di risorse di elaborazione, essendo l'interfaccia utente nativa in italiano.
 :  : FLD ££B£2M **Formato data**
È un valore V2/FMDAT :  definisce il formato di presentazione della data :  DMY oppure MDY.
Può assumere i seguenti valori : 
  :  Formato DMY
1 :  Formato MDY
* :  In questo caso non viene forzato nessun formato data, rimane quindi valido quello di sistema o
   quello impostato tramite il campo T$A£BE (Attrib spec lingua)
 :  : FLD ££B£2N **Codice divisa ALTERNATIVA**
È un elemento della tabella VAL :  definisce il codice della divisa alternativa con cui visualizzare gli importi (es. £V5V)
Nel contesto con valuta corrente LIRE, la valuta alternativa sarà EURO e viceversa (almeno nel periodo transitorio).
 :  : FLD ££B£2O **Divisore**
Puà assumere i valori ' ' o '1'. Nel caso in cui si inserisca il valore '1' si imposta la gestione del
cambio delle valute Non correnti come "divisori". Nel caso di valuta corrente EURO, deve essere impostato
a '1' .
Il calcolo per ottenere la valuta corrente è quidi : 
       VALUTA STRANIERA / CAMBIO = VALUTA CORRENTE
a '1' e quindi i cambi sono da considerarsi come VALUTA STRANIERA / CAMBIO = VALUTA CORRENTE
Puà assumere i valori ' ' o '1'. Nel caso in cui si inserisca il valore '1' si imposta la gestione del
 :  : FLD ££B£2Q **Tipo cambio**
Nella gestione della valuta alternativa c'è la possibilità di impostare un tipo cambio diverso da quello
Effettivo. Il campo assume il valore '1' che quindi non è indispensabile impostarlo.
Esempio della gestione :  in caso di multinazionale con valuta alternativa "USD" si può impostare un cambio
Standard annuale impostato dalla compagnia.
 :  : FLD ££B£2R **Separatore decimale**
lasciando il campo ' ' la virgola separa gli interi dai numeri decimali, impostando '1' viene invertito il
significato con il '.' (punto).
Il valore speciale * invece non forza nessun separatore decimale, rimane quindi valido quello di sistema o
quello impostato tramite il campo T$A£BE (Attrib spec lingua)
 :  : FLD ££B£2T **Time Zone AS400**
Definisce lo sfasamento (espresso in ore in formato centesimale, ovvero 1h 30m equivalgono al valore 1,50) del fuso orario del sistema AS400 rispetto al meridiano di riferimento GMT. Questa informazione è contenuta anche nella variabile di sistema QUTCOFFSET, ma viene inserita in questa tabella per ottimizzare le performance. Questo valore viene utilizzato con il successivo per determinare l'ora corretta dell'utilizzo del sistema da parte degli utenti.
 :  : FLD ££B£2U **Time Zone Utenti**
Definisce lo sfasamento (espresso in ore in formato centesimale, ovvero 1h 30m equivalgono al valore 1,50) del fuso orario degli utenti del sistema AS400, che potrebbe essere diverso da quello del sistema AS400. Questo valore viene utilizzato con il precedente per determinare l'ora corretta dell'utilizzo del sistema da parte degli utenti.
 :  : FLD ££B£22 **Fuso orario utente**
E' il codice del fuso orario (oggetto di sistema *TIMZON) che verrà applicato all'orario degli utenti. Se impostato, ££B£2T e ££B£2U vengono ignorati.
Se presenti più versioni dello stesso OJ *TIZON quella che corrisponde al fuso orario più aggiornato è quella con il codice che termina per il progressivo maggiore.
E' possibile codice che termina per il progressivo maggiore.
Il fuso orario per l'Italia è quello la cui descrizione è "Central European Time".
**N.B. : ** Questa implementazione risolve in particolare problematiche emerse quando le date di passaggio dell'ora legale per il fuso orario utente non corrispondono con quelle del fuso orario di sistema.
 :  : FLD ££B£2V **Suff.Agg.     £INZDS**
Se impostato, induce il richiamo del programma B£INZ0_x (x è il suffisso indicato), ad ogni inizializzazione di programma, sia standard che personale, che contenga la /copy £INZSR.
Mediante tale programma è possibile : 
-    agire sul contenuto della ds di lettura delle tabelle di personalizzazione B£1 e B£2
-    agire sul contenuto dei campi della ds di inizializzazione programma £INZDS contenuta nella /copy £PDS.
E' utilizzata nel caso si debba intervenire a modificare tutti i campi della £INZDS comreso quelli della B£1 e B£2,
per quest'ultimi è  consigliabile utilizzare il pgm di aggiustamento lanciato con il campo
££B£2K "Suff.Agg.Amb. B£1/B£2" (per un dettaglio maggiore rimandiamo al help del campo citato).
Il programma lanciato tramite questo parametro viene eseguito a TUTTE le inizializzazioni di tutti i pgm lanciati.
 :  : FLD ££B£2K **Suff.Agg.Amb. B£1/2S**
Se impostato, induce il richiamo del programma B£QQ00V_x (x è il suffisso indicato), ad ogni cambio ambiente.
Mediante tale programma è possibile modificare il contenuto dei campi delle tabelle B£1 e B£2.
Questo programma è lanciato sempre e SOLO al cambio ambiente, quindi per la modifica di questi campi (B£1/2) è
consigliabile utilizzare questo richiamo al posto del campo ££B£2P (Suff.Agg.  £INZDS)
NOTA :  consultare il prototipo B£QQ00V_U per alcuni dettagli relativi al reperimento (all'interno
      della exit stessa) di alcuni valori (come ad esempio la lingua assunta)
 :  : FLD ££B£2X **Nuova gestione azioni**
Si veda : 
- [Approfondimenti azioni su oggetti](Sorgenti/MB/DOC/B£BASE_05)
 :  : FLD ££B£2Y **Gestione Modalità**
Se impostato, attiva nei principali data entry di Smeup il controllo sulla modalità dell'ambiente.
In sostanza viene gestito il controllo della modalità di gestione nella gestione dati
(inserimento, modifica, visualizzazione).
 :  : FLD ££B£2W  **Costruzione automatica**
Se impostato, per le tabelle sulle quali è predisposta, è attivata la costruzione automatica (del codice, della descrizione e dei campi). La predisposizione si attiva modificando l'exit
prevista, costituita dal programma B£AR16_IM (esempi proposti :  tabelle GMC, V5D, ...).
 :  : FLD ££B£2Z  **Ambiente di test**
Identifica il sistema informativo come ambiente di test. Questa informazione può essere utilizzata per considerazioni specifiche aziendali ed in alcune funzionalità standard : 
- Invio mail (Vedasi relativa documentazione /COPY £G53)
 :  : FLD ££B£2J **Abilita monitor API**
Se impostato, i programmi richiamati dalle API di Sme.Up, saranno monitorizzate per non emettere segnalazioni di errore. Naturalmente questa metodologia non permetterà la gestione degli errori da parte del sistema operativo.
 :  : FLD ££B£20 **Abilita RCLRSC**
Se impostato, i programmi che terminano in**LR**, eseguiranno la chiamata al comando RCLRSC.

Tale impostazione è consigliata quando sul sistema sono presenti installazioni di sowftware NON SME.UP che
però utilizzano programmi o API Sme.UP.
E in tutti i casi in cui l'accesso a programmi e funzionalità Sme.UP non passa per il B£UT50.

In tutti gli altri casi tale impostazione non è necessaria.
 :  : FLD ££B£21 **Abilita mascheramento**
Se impostato, la £DEC, attiva un mascheramento dei dati sensibili.
 :  : FLD ££B£23 **Archivio default lock (SV)**
Indica quale archivio va utilizzato di default per la gestione dei lock (£G81).
Per dettagli fare riferimento alla documentazione dell'API : 
- [Test Vincolo su un Oggetto Applicativo](Sorgenti/MB/DOC_OGG/P_TSTG81)
