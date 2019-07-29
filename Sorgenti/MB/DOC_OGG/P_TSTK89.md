s# GESTIONE OGGETTO

## Obiettivo
Gestire tutte le azioni di controllo ed aggiornamento su un oggetto.

## Struttura

I dati fondamentali di input sono : 
* un'oggetto smeup (es. un cliente, un articolo), che viene passato tramite le variabili £K89I_TP e £K89I_CD.
* un'azione, che viene passata attraverso il parametro di setup AziExe. Il codice corrisponde alle azioni di gestione che posso fare sull'oggetto smeup (es. 01, 02, 03, 04, 05, ma anche RI nel caso delle testate documento). Alle suddette azioni si può aggiungere la pre-immissione (identificata dal codice 00), tramite cui è possibile attivare una gestione che antecede l'inserimento (in richiamo al passato l'azione 00 corrisponde alla funzionalità un tempo svolta dai pgm "I" es. BRAR01I).
* un contesto, di solito non viene passato ed assume **, altrimenti è possibile passarlo nel setup attraverso il parametro NamSet. Attraverso esso è possibile settare la K89 in base ad una particolare condizione dell'azione sintetizzata nell'informazione del contesto (es. inserimento di un ordine in una pagina web di B2B).

Sulla base di questi dati di input vengono poi elaborati : 
* Lo script SCP_A36 corrispondente al tipo oggetto
* Lo script SCP_A36PER corrispondente al tipo oggetto (se implementato dal cliente)
* L'eventuale script SCP_LAY indicato nella riga dell'SCP_A36 (o SCP_A36PER) corrispondente al TAG VAR dell'azione che si sta eseguendo in quel momento
* Il pgm specifico dell'oggetto con nome B£K89_xx dove xx è il tipo oggetto (es. B£K89_AR)
* L'eventuale exit prevista dall'SCP_A36 (o SCP_A36PER)

## Funzioni
La £K89 gestisce le seguenti funzioni : 
* SET - Setup  :  si occupa di caricare i setup di configurazione con cui la K89 dovrà essere eseguita (reperisce i parametri in base a quanto definito all'SCP_A36 e li fonde con gli eventuali parametri passati in input). Per questa funzione sia il pgm specifico che il pgm di exit, vengono richiamati non cono funzione SET, ma con funzione SET.PRE e SET.POS :  in sostanza possono intervenire sul setup prima che standard venga caricato o dopo che questo è stato caricato.
* AUT - Autorizzazioni :  si occupa di controllare le autorizzazioni dell'azione che si vuole eseguire. La parte standard carica quelle previste dallo standard, l'exit permette di integrare tali controlli con logiche proprie.
* LCK - Lock :  per le azioni di gestione, setta il lock dell'oggetto (attraverso la £H81). Questa funzione viene gestita solo dal pgm base e non transita per i pgm specifici e per l'exit.
* CAR - Carica dati :  si occupa di caricare i dati dell'oggetto (in inserimento inizializza i valori, per tutte le altre azioni legge semplicemente il record). Attraverso questa funzione è possibile inoltre configurare il trattamento di tali informazioni (es. se l'informazione deve essere protetta o nascosta). Va infine inoltre considerato che le i dati un oggetto vengono codificati attraverso gli oav e che gli attributi intrinseci (I/) vanno caricati dal pgm specifico, mentre tutti gli atri (J/, N/, P/, K/), vengono caricati dai pgm base.
* CTR - Controllo :  è la funzione attraverso cui viene effettuato il controllo degli errori. E' da notare che per questa funzione, solo l'eventuale exit viene richiamata con funzione CTR-PRE e CTR-POS, al fine di poter applicare delle funzioni di controllo prima e dopo l'esecuzione dei controlli standard.
* EXE - Esecuzione :  è la funzione attraverso cui viene applicata l'azione all'oggetto (inserimento, copia, modifica, cancellazione). Come per la funzione CTR, solo l'eventuale exit viene richiamata con funzione EXE-PRE e EXE-POS al fine di poter eseguire della azioni prima o dopo l'aggiornamento dell'archivio.
* ABB - Abbandono :  permette di eseguire, di eseguire eventuali azioni da applicare nel caso in cui un'azione venga abbondonata. In questa funzione non è incluso l'unlock dell'oggetto.
* FCO - Richiami combinati : 
** CAR - Caricamento :  esegue in sequenza SET e CAR
** CTR - Controllo :  esegue in sequenza SET, CAR, CTR
** ALL - Completa :  esegue in sequenza SET, CAR, CTR, EXE o ABB
* FSU - Funzione successiva :  implementabile solo nei pgm specifici o nelle exit permette di forzare l'esecuzione di una funzione da eseguire a seguito di un'azione. Per un esempio si rimanda al sorgente di exit del prototipo, anche se si
* DER - Deriva :  è una funzione slegata da tutte le altre che permette a partire da certe informazioni dell'oggetto di individuare il codice.

## Programmi

Le funzioni della K89 sono svolte dai seguenti programmi : 
* B£K89G :  è il pgm base della K89. Quest'ultimo esegue una serie di logiche comuni e demanda ai pgm riportati a seguire l'esecuzione di logiche più specifiche.
* B£K89G1 :  attraverso l'elaborazione degli script SCP_A36 ed SCP_A36PER determina il setup della K89 da applicare all'elaborazione di un'azione su un oggetto
* B£K89G2 :  si occupa di elaborare tutte le anagrafiche delle informazioni riferibili ad un oggetto (carica tutti gli oav di un oggetto e come tali oav devono essere trattati in scheda, quando la k89 viene usata in un'elaborazione interattiva)
* B£K89G3 :  si occupa di determinare quale suffisso numeri debba essere utilizzato quando si tratta un archivio che non corrisponde ad un oggetto Smeup. Come si vedrà a seguire ogni oggetto ha un pgm di elaborazione specifico che prende come nome il codice del tipo oggetto Smeup es. l'oggetto CN è trattato dal pgm B£K89_CN, se si vuole invece trattare un archivio come il C£ALIA0F non è possibile avere un legame immediato con un suffisso se non che tramite il B£K89G3, che nel caso del C£ALIA0F ad esempio determina che il suffisso è 01, es. B£K89_01. Il fatto di usare codici numerici per questi casi è voluto al fine di non sovrapporsi ai codici degli oggetti Smeup.
* B£K89J :  Esegue una serie di funzioni di servizio atte al funzionamento del B£K89G
* B£K89_XX :  dove XX è il tipo oggetto che si sta utilizzando, è il pgm che permette di eseguire i controlli, le letture e gli aggiornamenti specifici del particolare oggetto. Da qui in poi questo pgm verrà individuato con il termine "pgm specifico".
* Pgm di exit :  è un pgm che può essere attivato tramite lo script SCP_A36PER, che permette di estendere tutte le considerazioni specifiche delle standard con logiche specifiche della particolare azienda che usa il prodotto. Il nome della exit è libero, però per rendere facilmente rintracciabili i programmi è consigliato usare la nomenclatura B£K89_XXYY,  Dove B£K89_XX è il nome del programma specifico dell'oggetto. A standard YY è £Y dove Y è un progressivo.

Salvo specificato differentemente a seguire, tutte con le funzioni/metodi previste dalla /COPY, vengono anche richiamati i pgm specifici e le exit. Da questo punto di vista è importante notare che il pgm base richiama i pgm specifici ed i pgm specifici richiamano le eventuali exit.

## Script

E' inoltre importante notare che il funzionamento della K89 si appoggia sui seguenti script : 
* SCP_A36, con codice = tipo oggetto (es. CN per i contatti) o IDnumero nel caso degli archivi che non sono oggetti smeup (numero determinato dal B£K89G3). Questo script permette di settare come la K89 debba essere utilizzata per l'oggetto intestatario del membro. Tale setup può essere suddivisa per azione, contesto ed eventuali attributi dell'oggetto.
* SCP_A36PER con codice = tipo oggetto, permette di sovrascrivere o estendere i setup della K89 previsti dallo standard.
* SCP_LAY, con codice = tipo oggetto_nnn (dove nnn è un codice numerico) :  tale script è reperito attraverso il setup dell'SCP_A36 (o dell'SCP_A36) tramite i campi TipFlt e CodFlt, ma viene qui evidenziato per la ricchezza di informazioni che esso contiene ed in quanto è attraverso esso che viene definito cosa si vedrà in scheda per la gestione dell'oggetto.

 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_A36)
 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_LAY)

## /COPY

 :  : DEC T(MB) P(QILEGEN) K(£K89) I(£K89 Master)
 :  : DEC T(MB) P(QILEGEN) K(£K89_P) I(£K89_P Entry Plist per pgm impiegati nella /COPY)
 :  : DEC T(MB) P(QILEGEN) K(£K89DS) I(£K89DS Definizione dei DS e delle schiere utilizzate)
 :  : DEC T(MB) P(QILEGEN) K(£K89DS_P) I(£K89DS_P Definizione dei parametri di setup)
 :  : DEC T(MB) P(QILEGEN) K(£K89C) I(£K89C Gestisce il caricamento dei controlli)
 :  : DEC T(MB) P(QILEGEN) K(£K89J) I(£K89J Gestisce il richiamo del B£K89J per l'esecuzione di funzioni di servizio interne)
 :  : DEC T(MB) P(QILEGEN) K(£K89U) I(£K89U Gestisce il richiamo del B£K89U che a sua volta si occupa di richiamare le exit)

## Procedure

Definite nelle /COPY in QPROGEN £K89_PMC e £K89_PMD.
* £IK89P Recupera l'indice nelle schiere di definizione di un nome campo/oav/campo di db
* £WK89P Semplifica l'aggiunta di variabili di work
* £LK89P Setta la definizione dei parametri interni
* £CK89P Pulizia elemento di schiera di definizione campi

## Variabili

**Input**
* £K89I_LC Livello di chiamata
* £K89I_FU Funzione
* £K89I_ME Metodo
* £K89I_TP Tipo/Param.Oggetto
* £K89I_CD Codice Oggetto
* £K89I_PA Parametri input :  in formato attributo(valoreparametro) permette di passare i parametri di setup che si vuole forzare nella particolare chiamata rispetto a quelli che vengono reperiti in automatico dalla funzione SET. Gli attributi passabili sono quelli previsti dal wizard dell'SCP_A36 all'istruzione " :  : VAR"
* £K89I_OR Origine, viene valorizzato in automatico con il pgm che richiama la K89

**Output**
* £K89O_MS Codice messaggio
* £K89O_FI File
* £K89O_VA Variabili
* £K89O_35 Errore
* £K89I_NC Numero elementi schiera £K89I_SC (campi)
* £K89O_NC Numero elementi schiera £K89O_SC (controlli)
* £K89O_FF Funzione da eseguire per i flussi Post

**Schiere Attributi Oggetto**

Le schiere riportate a seguire vengono caricate nel seguente modo : 
* Vengono caricati tutti i campi con le relative proprietà previsti dal filtro previsto per la gestione (tipicamente lo script di SCP_LAY)
* A tale elenco vengono aggiunti tutti gli attributi dell'oggetto con le relativa proprietà che non sono già stati caricati dal passo precedente. In questa elaborazione i campi già caricati corrispondenti ad un oav, vengono integrati con le informazioni reperibili dall'oav.
* Per gli attributi che corrispondono ad un campo di database i campi vengono ulteriormente integrati delle informazioni mancanti reperibili dalla definizione del campo
* Infine vengono chiamato il pgm specifico e l'eventuale exit che possono integrare l'elenco con campi di work specifici e/o integrare/modificare le proprietà dei campi già caricati


| Variabille|Intestazione|Note|Oggetto|Attributo SCP_LAY|Attributo OAV|Attributo £IR1 |
| ---|----|----|----|----|----|----|
| £89I_NM|Nome campo|Salvo considerazioni diverse tende a corrispondere al codice dell'oav||Nam|£OAVAT|£IR1DE |
| £89I_TX|Intestazione|||Txt|£OAVIN| |
| £89I_ON|Nome campo riferimento Oav|Tramite questo campo è possibile indicare che il campo successivo, non è un attributo dell'oggetto intestatario, ma dell'oggetto corrispondente al nome campo qui indicato||OavNam|| |
| £89I_OA Attributo Oav|codice attributo|se il campo precedente è vuoto è un oav dell'oggetto intestatario, altrimenti è un oav del campo indicato nel precedente attributo). Nota bene :  non è detto che tutti i campi siano oav, possono essere previsti dei campi di comodo che non corrispondono ad alcun attributo||Oav|£OAVAT| |
| £89I_CF|Campo del database|se il campo corrisponde anche da un campo del database, qui viene indicato tale riferimento|||£OAVO_FLDN| |
| £89I_OD|Tipo Oggetto previsto dal Database|E' il tipo oggetto previsto dal database|OG||| |
| £89I_OS|Tipo Oggetto Struttura|Rispetto alla proprietà successiva, può contenere ancora le variabili da risolvere|OG||£OAVOT+£OAVOP| |
| £89I_OG|Tipo Oggetto Risolto||OG|Ogg|£OAVO_OGGA|£IR1OG |
| £89I_OY|Tipo Oggetto Matrice|Corrisponde al campo _OD, con la differenza che se il tipo oggetto è dinamico, si sostituire il riferimento alle variabili del database con quelle previste dalla griglia di matrice|OG||£OAVOT+£OAVOP| |
| £89I_LU|Lunghezza del campo|||Lun|£OAVO_LUNG|£IR1LU |
| £89I_ND|Numero decimali|||Dec|£OAVO_DECI|£IR1ND |
| £89I_LG|Lunghezza grafica|è possibile forzare la lunghezza con cui il campo deve essere risposto, in sovrapposizione alla reale lunghezza del campo||Luv|£OAVO_LUGR| |
| £89I_FG|Forma grafica|definisce il componente grafico da applicare in visualizzazione dell'oggetto|V2FOGOG|Cmp|| |
| £89I_PG|Proprietà grafica|definisce la configurazione del componente grafico||Ext|| |
| £89I_SI|Stile grafico Intestazione|definisce lo stile grafico dell'intestazione del campo|J3STY|LabSty|| |
| £89I_SV|Stile grafico Valore|definisce lo stile grafico con cui viene presentato il campo|J3STY|FldSty|| |
| £89I_TK|Tipo funzione di controllo|definisce l'applicazione di una particolare modalità di ricerca/controllo del campo, per i valori si rimanda ai valori imputabili nell'attributo Tfk del tag  :  : Fld degli script SCP_LAY||Tfk|| |
| £89I_PK|Parametro funzione di controllo|parametrizza la particolare modailtà di ricerca/controllo prevista dal campo precedente, per i valori possibili ai valori imputabili dall'attributo Tfk del tag  :  : Fld degli script SCP_LAY||Pfk|| |
| £89I_PE|Indica a schiera valori estesi|qualora il campo abbia una lunghezza superiore a 2560, il valore verrà memorizzato nella schiera £89E_AL, qui è indicato in puntatore a tale schiera|||| |
| £89I_PL|Parametro libero|usato per fare memorizzare informazioni, sul trattamento del campo utilizzate poi nel pgm specifico|||| |
| £89I_KY|Campo chiave||||£OAVO_FLKY| |
| £89I_OB|Campo obbligatorio|||Obb|£OAVO_OBBL|£IR1OB |
| £89I_NL|Campo di cui non va controllata il il tipo oggetto cui fa riferimento esista|||Fnl|| |
| £89I_NT|Campo di cui non va controllato che il codice oggetto esista|||Fnt|£OAVO_NCTP|£IR1CO |
| £89I_NC|Campo che non va controllato e in cui si può accettare codice **|||Fnc|£OAVO_NCCO|£IR1CO |
| £89I_IO|Attributo Input/Output|Può assumere i valori B, O, H||Cio|£OAVO_INOU|£IR1DP |
| £89I_CS|Case sensitive|Può assumere il valore LC o UC||For|£OAVO_CASE|£IR1CH |
| £89I_TF|Testo fisso|Per i campi con tipizzazione dinamica va a bloccare l'intestazione||Nri|£OAVO_TEFI| |
| £89I_LM|Attivazione log di campo||V2SI/NO||£OAVO_LOGM| |
| £89I_AR|Autoenter||V2SI/NO|Far|£OAVO_AUEN| |
| £89I_AU|Autorizzazione|Prevede gli stessi valori del campo IO, pensato per scopo futuro|||£OAVO_INOU| |
| £89I_IS|Indispensabile||||£OAVO_SPAR| |
| £89I_PU|Pubblicato|Indica se il campo è previsto nella scheda di interfaccia con l'utente o meno|||| |
| £89I_ER|Campo con errore||||| |
| £89I_AL|Valore campo se alfanumerico e con lunghezza <= 2560||||| |
| £89I_NU|Valore campo numerico||||| |
| £89E_SA|Valore campo se alfanumerico e lunghezza > 2560|Sono previsti massimo 10 campi, il cui puntamento è dato dal campo £89I_PE|||| |
| 


**Parametri I/O Programma calcolo suffisso Pgm K89**
* £K893_TP Tipo oggetto (in input)
* £K893_SP Suffisso Pgm Specifico (in output)

**Parametri I/O Funzione controllo**
* £K89C_CC Codice di controllo (oggetto smeup CK)
* £K89C_TM Tipologia messaggio (può assumere i valori W, per i messaggi di warning che non sono bloccanti, E per errore e M per mandatario, la differenza fra i due sta nel fatto che gli errori E, nei casi in cui la K89 viene impiegata in una gestione interattiva, è segnalato solo  se il campo in questione, è visibile all'utente)
* £K89C_PN Puntatore schiera DB (puntatore alla schiera degli attributi dell'oggetto)
* £K89C_TP Tipo messaggio (parametro dell'oggetto VO)
* £K89C_CD Codice messaggio (istanza dell'oggetto VO)
* £K89C_TX Testo messaggio
* £K89C_PS Peso messaggio
* £K89C_PG Programma messaggio (programma che si occupa del controllo)
A queste variabili corrisponde la schiera £K89O_SC, con le corrispondenti sottoschiere £89O_.

## Note su su trattamento Oav P e K (Parametri)

I parametri si possono presentare in 9 tipologie di gestione.

Ciascuna viene gestita nella £K89 con una sua forma specifica

* parametro SINGOLO alfanumerico
Viene presentato come campo il parametro con l'oggetto della tabella "B£N"
Il parametro K89I_PL contiene l'informazione di parametro singolo alfanumerico nella forma Par(A)

* parametro SINGOLO numerico
Viene presentato come campo il parametro con l'oggetto fisso "NR"
Il parametro K89I_PL contiente l'informazione di parametro singolo numerico nella forma Par(N)

* parametro SINGOLO alfanumerico e numerico
Il parametro viene suddiviso in due campi : 
** Un campo alfanumerico con l'oggetto dalla tabella "B£N". Viene aggiunto il suffisso /A£K89 al
nome del campo (Esempio P/NOM/NOM/A£K89)
Il parametro K89I_PL contiente l'informazione di parametro singolo alfanumerico nella forma Par(SA)
** Un campo numerico con oggetto fisso "NR". Viene aggiunto il suffisso /N£K89 al nome del campo.
(Esempio P/NOM/NOM/N£K89).
Il parametro K89I_PL contiente l'informazione di parametro singolo numerico nella forma Par(SN)

* Parametro MULTIPLO alfanumerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificativo CD() e con separatore di record ";"
Esempio :  CD(AR1);CD(AR2);CD(AR3);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico nella forma Par(MA)
e l'informazione della configurazione nella forma LC(CD)

* Parametro MULTIPLO numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto fisso "NR" (Esempio LCNR)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificativo NR() e con separatore di record ";"
Esempio :  NR(1,50000);NR(2,50000);NR(7,00000);
Il parametro K89I_PL contiente l'informazione di parametro multiplo numerico nella forma Par(MN)
e l'informazione della configurazione nella forma LC(NR)

* Parametro MULTIPLO alfanumerico e numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificativo CD() e NR() con separatore di
record ";"
Esempio :  CD(AR1)NR(1,50000);CD(AR2)NR(2,50000);CD(AR3)NR(7,00000);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico e numerico nella
forma Par(MAN) e l'informazione della configurazione nella forma LC(CD;NR)

* Parametro MULTIPLO E DATATO alfanumerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificativo CD(), DI() e DF() e con separatore
di record ";"
Esempio :  CD(AR1)DI(20150101)DF(20151231);CD(AR2)DI()DF();CD(AR3)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico e datato nella
forma Par(DA) e l'informazione della configurazione nella forma LC(CD;DI;DF)

* Parametro MULTIPLO E DATATO numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto fisso "NR" (Esempio LCNR)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificativo NR(), DI() e DF() e con separatore
di record ";"
Esempio :  NR(1,50000)DI(20150101)DF(20151231);NR(7,00000)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo numerico e datato nella
forma Par(DN) e l'informazione della configurazione nella forma LC(NR;DI;DF)

* Parametro MULTIPLO E DATATO alfanumerico e numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificativo CD(), NR(), DI(), e DF(), e con
separatore di record ";"
Esempio :  CD(AR1)NR(1,50000)DI(20150101)DF(20151231);CD(AR2)NR(7,00000)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico, numerico e datato
nella forma Par(DAN) e l'informazione della configurazione nella forma LC(CD;NR;DI;DF)


