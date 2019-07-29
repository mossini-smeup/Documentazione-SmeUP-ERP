Le /COPY £Jay sono state scritte con l'obiettivo di semplificare la costruzione di servizi di aggiornamento, fornendo diverse funzionalità standard per tali servizi e cercando di garantire la flessibilità richiesta dall'ampia varietà di servizi implementabili.

A questo scopo esse : 

- Sgravano l'utilizzatore di tutta la parte di lettura/scrittura dirette dell'XML da/verso il client, fornendo un insieme di variabili intermedie che contengono o in cui vanno scritte le informazioni di colloquio con il client
- Rendono disponibile una serie di controlli standard di consistenza, tipo, obbligatorietà sui campi
- Effettuano automaticamente la conversione in alfanumerico (per il passaggio tramite XML) dei campi numerici


# Struttura delle /COPY
Elenchiamo di seguito le £Jay disponibili : 

- £Jay_D :  definizioni (richiesta)
- £Jay_PD1, £Jay_PC1 :  procedure (richieste)
- £Jay_C0 :  funzioni comuni (richiesta)
- £Jay_C1 / £Jay_C2 :  funzioni relative all'aggiornamento mono-linea
- £Jay_C2 :  funzioni relative all'aggiornamento multi-linea con unica esecuzione
- £Jay_C3 :  funzioni relative all'aggiornamento multi-linea con restore automatizzata ed esecuzione per ogni riga


# Funzionamento
Le £Jay sono implementate, in maniera analoga alle £Jax, come "pezzi di codice".

Esse forniscono tre routine-base :  £Jay_SETUP, £Jay_UPDATE, £Jay_INIT che guidano il servizio di aggiornamento nelle operazioni di setup e aggiornamento ed inizializzazione. Queste routine : 

- Effettuano le azioni comuni dei servizi di aggiornamento (configurabili tramite una serie di variabili)
- Passano il controllo al servizio stesso per le parti non generalizzabili (ad esempio la scrittura su AS)


Descriviamo di seguito le operazioni svolte da queste routine; altre fonti di informazioni sono i servizi di aggiornamento di esempio e la /COPY £Jay_D, contenente le descrizioni dei campi impiegati dalle £Jay.

## SETUP
Per gestire correttamente il colloquio al momento del setup è necessario nel servizio di aggiornamento chiamato con £UIBME='*SETUP', valorizzare alcune variabili e chiamare la routine £Jay_SETUP.
Le variabili da impostare sono : 

- Abilitazione operazioni possibili
-- £JayAutIns (V2SI/NO) :  Abilita inserimento
-- £JayAutUpd (V2SI/NO) :  Abilita modifica dei record
-- £JayAutDel (V2SI/NO) :  Abilita cancellazione dei record
-- £JayAutChk (V2SI/NO) :  Abilita pulsante per azione "*CHECK"
-- £JayAlwUpd (V2SI/NO) :  Sempre in aggiornam.
- Tasti funzionali :  sono schiere tramite le quali è possibile passare il codice di un comando  e la descrizione del comando stesso. Quando il tasto funzionale verrà premuto, il servizio di update verrà richiamato con impostato come metodo il codice del comando.
-- £JayCmd :  Codice comando (in formato *Fnn dove nn è il numero corrispondente al tasto funzionale)
-- £JayCmdDes :  Descrizione comando
- Gestione inserimento
-- £JayIniRow (V2SI/NO) :  Se valorizzato attiva all'inserimento una chiamata da parte del client verso il servizio di update con metodo *INIT al fine di poter permettere l'inizializzazione dei dati di inserimento
-- £JayFirIns (V2SI/NO) :  Se valorizzato attiva la chiamata automatica di inserimento all'apertura della matrice
- Disabilitazione controlli automatici
-- £JayDisCon (V2SI/NO) :  Se valorizzato disabilita i controlli di consistenza di tutti i campi della matrice.
-- £JayDisTip (V2SI/NO) :  Se valorizzato disabilita i controlli rispetto al tipo oggetto previsto nella matrice.
-- £JayDisObb (V2SI/NO) :  Se valorizzato disabilita i controlli di obbligatorietà previsti nella matrice.
-- £JayUpdClk (V2SI/NO) :  Se valorizzato abilita (solo sui V2SI/NO) l'update al click del check box.
- Variabili di definizione aggiuntive della matrice di update
-- £JayFldLst :  è una schiera contenente le definizioni aggiuntive della matrice necessarie per la gestione delle funzioni di aggiornamento. Ogni elemento è costruito sulla DS £JayDSFld
-- £JaySeaLst :  è una schiera aggiuntiva di definizione. In essa per ogni campo è possibile una funzione loocup specifica di ricerca sostitutiva rispetto a quella prevista dal client. Il contenuto di ogni elemento è costruito sulla DS £JayDSSea
-- £JayComLst :  è una schiera aggiuntiva di definizione. In essa per ogni campo è possibile una funzione loocup specifica di combo sostitutiva rispetto a quella prevista dallo standard. Il contenuto di ogni elemento è costruito sulla DS £JayDSCom. NOTA BENE :  perchè questa schiera venga presa in considerazione è necessario che la classe o la definizione della colonna di riferimento nel servizio, prevedano l'impiego delle combo (si veda la documentazione tecnica del modulo B£EQRY).
-- £JayDSFld :  è la schiera che definisce i sottocampi di ogni elemento della schiera £JayFldLst
--- £JayFNM :  Nome del campo
--- £JayFNM :  Nome del campo
--- £JayFIO :  Gestione
---- K = modif.solo all'imm.
---- B = modificabile, con applicazione combo se previste (vedi doc. modulo B£EQRY)
---- b = modificabile, con forzatura di non utilizzo delle combo
---- C = modificabile, con forzatura dell'utilizzo delle combo ad elenco completo
---- E = modificabile, con forzatura dell'utilizzo delle combo con ricerca
---- O = Output
---- H = Hidden
---- I = Solo Input
--- £JayFOB :  Obbligatorietà (V2SI/NO)
--- £JayFNT :  Controllo tipo oggetto (' ' = Si / '1' = No / '2'= Loocup, significa che prima di chiamare il servizio di update il client si occupa di controllare la consistenza del codice rispetto al tipo oggetto). Questo campo diventa irrilevante se viene attivato nel setup il campo £JayDisTip.
--- £JayFNC :  Controllo consistenza  (' ' = Si / '1' = No). Questo campo diventa irrilevante se viene attivato nel setup il campo £JayDisCon.
--- £JayFAR  :  Se aggiornamento deferred, quando si conferma la cella viene richiamato il servizio di update con funzione *CHECK
--- £JayFLL :  Lunghezza campo numerico (2 caratteri)
--- £JayFDD :  N° decimali campo numerico
--- £JayFFM :  Utilizzo Caratteri minuscoli ('LC' = Lower Case / 'UC' = Upper Case)
--- £JayFOG :  Tipo Oggetto (può anche essere dinamico, facendo riferimento ad altre colonne tramite l'indicazione fra parentesi quadre del nome del campo di riferimento)
--- £JayFDV :  Valore di default
--- £JayDES :  Campo descrizione. Se il indicato il nome del campo corrispondente questo verrà automaticamente valorizzato con la descrizione del campo in questione. E' importante ricordare che in questo caso per il campo di descrizione va disabilitato il controllo di consistenza.
-- £JayDSSea :  è la schiera che definisce i sottocampi di ogni elemento della schiera £JaySeaLst
--- £JaySNM :  Nome campo
--- £JaySCH :  Carattere/Caratteri che attivano la funzione di ricerca specificata. Possono essere indicati fino a 5 differenti caratteri. Indicato *ALL la funzione di ricerca/controllo sarà sempre
quella specificata
--- £JaySFU :  Funzione da lanciare per eseguire la ricerca/controllo del campo
-- £JayDSCom :  è la DS che definisce i sottocampi di ogni elemento della schiera £JayComLst
--- £JayCNM :  Nome del campo di riferimento, a cui verrà applicata la combo
--- £JayCDY :  Tipo combo. Con valore "F" indica che la combo è definita attraverso una funzione, con valore " " indica che attraverso la schiera viene indicato l'elenco puntuale dei valori possibili
--- £JayCCD :  Se il tipo combo è " ", in questo campo va indicato il codice selezionabile
--- £JayCDE :  Se il tipo combo è " ", in questo campo va indicata la descrizione del codice selezionabile
--- £JayCFU :  Se il tipo combo è "F", in questo campo va indicata la funzione da lanciare per ottenere la l'elenco di risposta alla combo. In merito a questo è importante notare : 
---- che le funzioni normalmente sono automaticamente compilate, quando è previsto per un campo che venga utilizzata la combo (le funzioni sono quelle visibili dal TST della K04 con funzione COM)
---- qual'ora si voglia sovrascrivere la funzione standard, la funzione specifica dovrà rispondere con l'sql di una griglia di due sole colonne :  codice e descrizione.
---- A disposizione, purchè vengano gestiti di dinamismi opportuni (When Change e LostFocus) si hanno tutte le variabili corrispondenti alla riga della matrice, nonchè le variabili T1/P1/K1 che contengono il tipo, il parametro ed il contenuto della cella da cui viene lanciata la funzione della combo.
-- £JayNFld :  Numerica viene automaticamente valorizzata in funzione del numero di elementi valorizzati nella schiera £JayFldLst


## INIZIALIZZAZIONE
Il servizio viene chiamato con £UIBME="*INIT" se nel setup è stato impostata la variabile £JayIniRow a "1". In questo caso il servizio dovrà valorizzare le schiere £JayVBef/NumBef con i valori per i quali un nuovo record va inizialmente valorizzato e chiare la routine £Jay_INIT.

## AGGIORNAMENTO / CONTROLLO
Quando un servizio è chiamato con £UIBME="*UPDATE" oppure "*CHECK" è necessario chiamare la routine £Jay_UPDATE (definita in £Jay_C1 o £Jay_C2 a seconda del tipo di aggiornamento che si sta trattando) e definire le subroutine specifiche dettagliate nel seguito.
NB :  essendo queste subroutine chiamate dal £Jay_UPDATE è necessario comunque definirle per compilare, poi a seconda delle esigenze verranno utilizzate o meno.

## £JAY_C1 - UPDATE MONOLINE
Cominciamo dal caso, più semplice, dell'aggiornamento MonoLine.
Per MonoLine si intende un servizio a cui arrivano una o più Line ma in cui ognuna, in maniera sequenziale, è trattata indipendentemente dalle altre (controllo / scrittura / restituzione XML). Non è possibile, inoltre, creare Line aggiuntive rispetto a quelle ricevute dal client (effettuare modifiche su righe diverse da quelle toccate dall'utente).
In sintesi, la routine £Jay_UPDATE : 

- Legge l'XML per per istanziare una serie di variabili su una Line
-- £JayID     = Id della line
-- £JayOP     = Tipo di azione U = Update  D = Delete I = Insert
-- £JayVBef   = Carica valori alfanumerici prima della modifica
-- £JayNumBef = Carica valori numerici prima della modifica
-- £JayRo     = Numero di riga
-- £JayVAft   = Carica valori alfanumerici dopo della modifica
-- £JayNumAft = Carica valori numerici dopo della modifica
- Chiama la routine £Jay_LOAD (da definire nel servizio) per le verifiche di fattibilità dell'operazione (esistenza record) e caricare i valori presenti sul database da aggiornare. Se si vogliono aggiornare anche dei campi che non sono stati modificati in matrice (es. campi di output correlati) oltre a valorizzare i relativi elementi delle schiere Aft, vanno valorizzati anche i campi £JayAftUse (='1').
-- £JayVSav   = Schiera in cui caricare i valori alfa del database esistenti. E' da tenere in  che se sono attivi i controlli di consistenza, se questa e la successiva schiera contengono valori differenti rispetto alle corrispettive schiere Bef, verrà segnalato errore di consistenza in quanto in questo caso si assume che i dati presenti nel database (quelli caricati appunto nelle Sav) siano differenti rispetto a quelli presenti a video (cioè quelli in VBef).
-- £JayNumSav = Schiera in cui caricare i valori numerici del database esistenti
-- £Jay35     = Indicatore di errore, qui utilizzato per la verifica dell'esistenza dei dati nel database. NOTA BENE :  se sono in inserimento questo indicatore va acceso.
- Effettua (opzionalmente in funzione del setup) controlli di consistenza (cioè il confronto
fra i valori presenti sulla matrice prima della modifica e quelli presenti sul database), tipo ed obbligatorietà
- Chiama la routine £Jay_AFTER (da definire nel servizio) per ulteriori controlli specifici sui campi della Line in esame
-- £JayFld35  = Indicatore di errore (poi fa accendere anche il £Jay35)
-- £JayFldErr e £JayFldErrLev = Schiera con errori specifici per campo (£JayFldErr schiera con i testi degli errori e £JayFldErrLev corrispondente schiera per i livelli di gravità)
- Chiama la routine £Jay_EXEC (da definire nel servizio) per l'esecuzione della scrittura/cancellazione. E' compito di £Jay_EXEC discriminare tra *CHECK e *UPDATE, ad esempio eseguendo l'operazione solo su *UPDATE e controllare l'indicatore di errore £Jay35
- Scrive l'XML di ritorno per la Line, e ricomincia leggendo la Line successiva


Esaminiamo nel dettaglio il funzionamento della routine £Jay_UPDATE presentando le strutture dati che vengono utilizzate nel processo.
Sono gestite varie schiere i cui valori si riferiscono ai campi della matrice (Before, After, valori salvati Save, errori sui campi) :  l'indice di queste schiere corrisponde alla posizione del campo nella schiera £JayFldLst di dichiarazione a *SETUP dei campi trattati.
La schiera £JayFldLst, di DS £JayDSFld, contiene gli £Jay_NFld elementi trattati dalle operazioni di aggiornamento.

### Caso MonoLine : 
Per implementare un servizio di aggiornamento MonoLine tramite £Jay è necessario definire nel servizio le seguenti routine : 

- £Jay_LOAD
- £Jay_AFTER
- £Jay_EXEC


Vediamole nel contesto di un ciclo di aggiornamento.

### CARICAMENTO VARIABILI
**Lettura da XML**
Dall'XML passato dal client vengono ricavate le seguenti informazioni : 

- £JayOP, tipo operazione :  'I' insert, 'U' update, 'D' delete. Da notare che nell'XML vengono passati valori diversi (I,V,A), mantenuti per compatibilità con il passato e convertiti dalla £Jay.
- £JayID, identificativo Line, cioè dell'operazione di gestione (£JayIA in alfanumerico)
- £JayRO, numero di riga della matrice di visualizzazione (£JayRA in alfanumerico)
- Schiere Before £JayVBef, £JayNumBef :  contengono i valori Before (pre-operazione), rispettivamente alfanumerici e numerici, dei campi
- Schiera £JayBefUse (V2SI/NO) :  contiene l'indicazione del fatto che un campo fosse valorizzato prima delle modifiche
- Schiere After £JayVAft, £JayNumAft :  contengono i valori After dei campi (dopo l'operazione)
- Schiera £JayAftUse (V2SI/NO) :  contiene l'indicazione del fatto che un campo fosse valorizzato dopo le modifiche


**£Jay_LOAD**
Questa routine viene chiamata dopo la lettura dell'XML. I suoi compiti : 

- Indicare  la fattibilità dell'operazione :  se modifica o cancellazione DEVE essere presente il record, se inserimento in genere NO. Si usa l'indicatore £Jay35 con il seguente significato :  *BLANKS trovato record (consentite modifica e cancellazione), '1' record non presente (consentito inserimento). Nel caso in cui fosse possibile inserire record multipli è sufficiente restituire sempre £Jay35='1' all'inserimento.
- Se sono abilitati i controlli di consistenza deve caricare le schiere £JayVSav e £JayNumSav, che contengono i valori salvati su AS dei campi della matrice. I controlli di consistenza vengono effettuati comparando £JayVSav con £JayVBef per i tipi alfanumerici, £JayNumSav con £JayNumBef per quelli numerici (NR e D8). Si noti che per caricare i valori salvati su AS spesso serviranno chiavi per individuare un record :  si usino a tale scopo i valori salvati in £JayVAft (in immissione) o £JayVBef (negli altri casi).
- Integrare / effettuare le prime modifiche ai valori After dei campi (£JayVAft, £JayNumAft). Si noti che vengono ritornati solo i campi che risultano accesi sulle schiere £JayBefUse o £JayAftUse, per tali motivi anche la schiera £JayAftUse va adeguata nel dovuto modo.


**Valutazione dei tipi dinamici**
La schiera di definizione dei campi viene scandita alla ricerca di tipi dinamici (per ora è supportato solo il formato [NomeCampo], che sostituisce il valore del campo NomeCampo, ad esempio per il V5TDOC0F il tipo di T§NDOC è DO[T§TDOC]); se presenti vengono risolti sulla base dei valori ora presenti nelle schiere After.

**Esecuzione controlli**
Variabili a disposizione in £Jay_UPDATE per la rilevazione e gestione degli errori/messaggi : 

- £Jay35, indicatore di errore sulla Line
- £JayMS, eventuale messaggio di errore su Line
- £JayFld35, presenza di errori di campo
- £JayFldErr, schiera del testo errori di campo
- £JayFldErrLev, schiera del livello errori di campo

Tutte queste variabili possono essere valorizzate sia dalla £Jay_UPDATE che dall'utente.
Ad esempio, un controllo di tipo errato su un campo setta a '1' £Jay35 e £JayFld35 e segna un messaggio di errore nella posizione equivalente di £JayFldErr (con la corrispondente gravità in £JayFldErrLev).
Queste variabili sono sempre a disposizione, in particolare saranno utili nella £Jay_EXEC per valutare se eseguire o meno l'operazione.

**Controlli standard**
Vengono eseguiti controlli di : 

- Fattibilità dell'operazione :  inserimento se £Jay35='1', modifica/cancellazione se £Jay35=*BLANKS. Subito dopo £Jay35 viene pulito e verrà usato nel resto della routine per segnalare errori generici.
- Consistenza (opzionali), tra i valori Bef e quelli Sav
- Tipo (opzionali) :  viene fatta la £DEC sui campi tipizzati (eventualmente anche in maniera dinamica); per i numerici vengono controllati lunghezza e decimali (decimali da implementare); per le date si controlla con £DA8
- Obbligatorietà (opzionali)


**Controlli specifici :  £Jay_AFTER**
Scopo di questa routine è eseguire qualunque tipo di controllo non effettuato a standard e integrare / modificare ulteriormente le strutture dati (in particolare i valori After e le variabili di errore).

**Esecuzione dell'operazione :  £Jay_EXEC**
Sulla base delle variabili di errore, di eventuali variabili interne al servizio e dei valori After è infine possibile decidere se e come eseguire l'operazione di aggiornamento.
E' ancora possibile modificare lo stato delle variabili di errore, prima della restituizione dell'XML al client.

**Restituzione dell'XML**
L'ultimo passo consiste nello scrivere un XML dettagliato dell'esecuzione dell'operazione di aggiornamento.
Vengono restituiti, a livello di Line : 

- Numero Line
- Numero riga matrice visualizzazione
- Esito dell'operazione :  positivo se £Jay35=*BLANKS, negativo se £Jay35='1'
- Eventuale messaggio di Line in £JayMS

Per ogni campo trattato, poi : 

- Nome campo
- Valore (se numerico la conversione in stringa per il passaggio in XML è automatica)
- Eventuale errore dalla posizione corrispondente nelle schiere £JayFldErr e £JayFldErrLev



## £JAY_C2 - UPDATE MULTILINE con unica esecuzione
A differenza del caso monoline, può capitare che in un servizio si debba trattare un insieme di Line in maniera congiunta. Un esempio banale è la necessità di deferire la scrittura vera e propria solo dopo avere controllato tutte le Line e avere verificato PER TUTTE l'assenza di errori.
Le operazioni svolte dalla £Jay_UPDATE in questo caso sono : 

- Legge una Line da XML, istanzia le variabili
- Chiama la routine £Jay_LOAD come sopra
- Effettua (opzionalmente) controlli di consistenza, tipo, obbligatorietà sui  campi
- Chiama la routine £Jay_AFTER (da definire nel servizio) per ulteriori controlli specifici sui campi della Line in esame (e, in questo caso, per salvarsi le opportune variabili temporanee per il proseguimento)
- Ricomincia leggendo la prossima Line

Al termine della scansione delle Line : 

- Chiama la routine £Jay_GLOBAL (da definire nel servizio) per controlli e aggiustamenti globali
- Chiama una sola volta la routine £Jay_EXEC per l'esecuzione della/e scritture o cancellazioni
- Effettua un ciclo su variabili ripristinate da variabili temporanee nel servizio per scrivere l'XML di ritorno per le Line



Presentiamo ora la routine che permette di gestire contemporaneamente insiemi di Line.
In sintesi : 

- Vengono scandite e controllate singolarmente tutte le Line
- Viene eseguito un eventuale controllo globale £Jay_GLOBAL
- Viene chiamata £Jay_EXEC per l'esecuzione dell'aggiornamento (in un colpo solo)
- Viene restituito l'XML di tutte le Line


Poichè la scrittura dell'XML di ritorno non viene eseguita contestualmente al controllo di ogni Line ma alla fine, è necessario tenere salvati i valori che vanno restituiti (estremi delle Line, valori dei campi, messaggi).
Si è scelto di lasciare al servizio il compito di salvare e ripristinare tali informazioni poichè una generalizzazione avrebbe implicato l'utilizzo di strutture dati di dimensioni eccessive.

Viene fornita, invece, una struttura dati (modificabile dal servizio) contenente informazioni sugli estremi delle Line processate, a partire dalla quale alla fine dell'aggiornamento viene eseguito il ritorno dell'XML. Tale struttura è la schiera £JayOpeLst, di £JayOpeCnt elementi (il numero di Line trattate in questa sessione di aggiornamento), e di DS £JayDSOpe : 

- £JayOID, numero di Line
- £JayORO, numero di riga della matrice

La variabile £JayMaxID tiene traccia del massimo Id di Line utilizzato. Ogni Id deve essere univoco, ed è possibile creare Line aggiuntive rispetto a quelle ricevute dal client (perchè si vuole modificare automaticamente una riga di matrice non toccata dall'utente).
Aggiungendo elementi alla schiera è possibile segnalare alla £Jay_UPDATE di aggiungere Line al ritorno XML.

### Differenze rispetto al caso MonoLine
Le routine da implementare nel servizio in questo caso sono : 

- £Jay_LOAD
- £Jay_AFTER
- £Jay_GLOBAL
- £Jay_EXEC
- £Jay_RESTORE

Valgono in generale le stesse considerazioni per il caso MonoLine, con le seguenti eccezioni.

### £Jay_AFTER
In questa routine, oltre ad effettuare controlli aggiuntivi sui campi della Line in esame, è necessario salvare in variabili interne al servizio le informazioni che andranno restituite in seguito al ritorno dell'XML.

### £Jay_GLOBAL
Qui vengono eseguiti i controlli globali, dopo quelli delle singole Line. E' possibile aggiungere nuove Line oltre a quelle richieste dall'utente. Tale operazione avviene tramite l'esecuzione della routine £Jay_ADDOPE alla quale vanno passate le variabili £JayOID e £JayORO che identificano la line aggiuntiva da ritornare e incrementando la variabile £JayMaxID che numera le line da ritornare.

### £Jay_RESTORE
Questa routine ha il compito di ripristinare le variabili/schiere per la scrittura dell'XML.    La routine viene eseguita per ogni line passando come variabili di input £JayID e £JayRo, a fronte di esse appoggiandosi a variabili/schiere definite internamente al servizio dovranno per ogni
line essere ri-caricati : 

- £JayVAft
- £JayNumAft
- £JayFldErr
- £JayFldErrLev
- £JayBefUse
- £JayAftUse
- £JayMS


## £JAY_C3 - UPDATE MULTILINE con restore automatizzata ed esecuzione per ogni riga

A differenza del caso monoline, può capitare che in un servizio si debba trattare un insieme di Line in maniera congiunta. Un esempio banale è la necessità di deferire la scrittura vera e propria solo dopo avere controllato tutte le Line e avere verificato PER TUTTE l'assenza di errori.
Le operazioni svolte dalla £Jay_UPDATE in questo caso sono : 

- Legge una Line da XML, istanzia le variabili
- Chiama la routine £Jay_LOAD come sopra
- Effettua (opzionalmente) controlli di consistenza, tipo, obbligatorietà sui  campi
- Chiama la routine £Jay_AFTER (da definire nel servizio) per ulteriori controlli specifici sui campi della Line in esame (e, in questo caso, per salvarsi le opportune variabili temporanee per il proseguimento)
- Ricomincia leggendo la prossima Line

Al termine della scansione delle Line : 

- Chiama la routine £Jay_GLOBAL (da definire nel servizio) per controlli e aggiustamenti globali
- Chiama la routine £Jay_EXEC per ciascuna riga per l'esecuzione della scrittura o cancellazione
- Scrive automaticamente l'XML di ritorno delle righe



In sintesi : 

- Vengono scandite e controllate singolarmente tutte le Line
- Viene eseguito un eventuale controllo globale £Jay_GLOBAL
- Viene chiamata £Jay_EXEC per l'esecuzione dell'aggiornamento PER CIASCUNA RIGA
- Viene restituito automaticamente l'XML di tutte le Line


E' stato implementato un file d'appoggio B£SUPD0F gestito direttamente all'interno della £JAY_C3, in cui vengono salvati in modo automatico i valori delle diverse schiere relative ai dati di riga (After, Before e messaggi).

Nella £JAY_C2 la routine £JAY_RESTORE doveva essere implementata in ciascun servizio di aggiornamento multiline, con lo scopo di ripristinare i valori delle schiere  After, Use e delle schiere di messaggio necessarie alla restituzione a Loocup dello stato di ciascuna riga.
Nella nuova /copy £JAY_C3 la routine £JAY_RESTORE avviene in modo automatizzato.

Oltre a rendere inutile il salvataggio dei valori in schiere d'appoggio, la £JAY_C3 differisce dalla £JAY_C2 in quanto la £JAY_EXEC non viene eseguita una sola volta, ma **UNA VOLTA PER CIASCUNA RIGA (in questo modo il servizio di aggiornamento tratta sempre una sola riga, semplificando l'implementazione della routine di scrittura dei dati).
Per il programmatore la presenza del file di appoggio è completamente trasparente :  lo sviluppatore  dovrà fare riferimento sempre e soltanto alle schiere before e after della riga corrente, senza preoccuparsi d'altro.

E' stata inoltre aggiunta la nuova routine £Jay_GLOBAL_I per eventuali operazioni globali iniziali effettuate prima dell'elaborazione delle righe e la £Jay_GLOBAL_F per eventuali operazioni globali finali eseguite dopo il ciclio contenente la £JAY_EXEC e prima della £JAY_RESTORE .

La pulizia dei dati scritti nel B£SUPD0F per la sessione avviene alla chiusura di Loocup.

### Differenze rispetto al caso MonoLine
Le routine da implementare nel servizio in questo caso sono : 

- £Jay_GLOBAL_I
- £Jay_LOAD
- £Jay_AFTER
- £Jay_GLOBAL
- £Jay_EXEC (richiamata per ciascuna riga
- £Jay_GLOBAL_F



## £JAY_C0 - Routine interne

- £JAY_INIVAR  :  Richiama le riabile £Jay_NFld, che numera di campi di definizione passati. Viene richiamata dalla routine £JAY_SETUP.
- £JAY_FLDTIP  :  Memorizza nella schiera £JayFldLstT i tipi oggetto della schiera £JayFldLst che risultano dinamici. Viene richiamata dalla routine £JAY_INIVAR.
- £JAY_FLDCNT  :  Valorizza la variabile £Jay_NFld, che numera di campi di definizione passati. Viene richiamata dalla routine £JAY_INIVAR.
- £JAY_CARCMD  :  Scrive l'XML relativo ai comandi passati nel SETUP tramite le schiere £JayCmd/CmdDes
- £JAY_CARLIN  :  Viene eseguita dalla routine £JAY_UPDATE per ogni line da elaborare e per ognuna di esse va ad eseguire le seguenti azioni : 
-- Carica le seguenti variabili leggendole dall'XML passato dal client : 
--- £JayIA/ID :  i n° della line fra quelle ritornate dal client in formato alfa/numerico
--- £JayOp :  il tipo di operazione si vuole eseguire sulla line (I=Insert/U=Update/D=Delete)
--- £JayRA/RO :  i n° di riga della line all'interno della matrice
--- £JayVBef :  schiera dei valori dei campi alfa prima della modifica
--- £JayNumBef :  schiera dei valori dei campi numerici prima della modifica
--- £JayVAft :  schiera dei valori dei campi alfa dopo la modifica
--- £JayNumAft :  schiera dei valori dei campi numerici dopo la modifica
-- Esegue la routine £Jay_LOAD per verifica esistenza record / caricamento valori schiere VSav/NumSav con i valori presenti sul database
--- Risolve i tipi oggetto dinamici
- £JAY_CTRLIN  :  Viene eseguita dalla routine £JAY_UPDATE per ogni line da elaborare  subito dopo la routine di £JAY_CARLIN. Questa routine esegue i seguenti controlli ed ognuna di essi ad esclusione del primo valorizza le schiere £JayFldErr e £JayFldErrLev per l'errore specifico di ogni campo : 
-- Verifica il valore della variabile £Jay35 rispetto all'operazione che si vuol fare (in inserimento deve essere '1', in aggiornamento/cancellazione deve essere ' ')
-- Salvo risultino disabilitati esegue i controlli di consistenza
-- Salvo risultino disabilitati esegue i controlli sul tipo oggetto
-- Se non è una cancellazione esegue la routine £JAY_AFTER
- £JAY_CTRAFT  :  Richiamata dalla routine £JAY_CTRLIN scandisce i campi e ne esegue i controlli basati sul tipo oggetto £JAY_CTRTIP
- £JAY_CTRTIP  :  Richiamata dalla routine £JAY_CTRAFT eseguo di un singolo campo i controlli basati sul tipo oggetto.
- £JAY_XMLLIN  :  Viene eseguita dalla routine £JAY_UPDATE dopo la routine £JAY_EXEC
per costruire l'XML da ritornare al client sulla base delle seguenti variabili : 
-- £Jay35 :  per indicare se l'operazione sia avvenuta correttamente o meno
-- £JayID :  per indicare l'ID della Line sulla quale è stata effettuata l'operazione
-- £JayRO :  per indicare la riga della line nella matrice sulla quale l'operazione è stata effettuata.
-- £JayBefUse/AftUse :  per ritornare i campi che risultano aggiornati
-- £JayVAft/NumAft :  per ritornare i valori dei campi aggiornati
-- £JayFldErr/£JayFldErrLev :  per ritornare il messaggio e la gravità dell'errore del singolo campo aggiornato
- £JAY_MSGFLD (C0) :  Viene eseguita dalla routine £JAY_XMLLIN per costruire a partire dai campi utilizzati


# SALVATAGGIO DATI SETUP MATRICE AGGIORNAMENTO

## Descrizione
Al fine di facilitare la creazione di servizi di aggiornamento, è stata implementato in  modo automatizzato all'interno della /copy £JAY_C0 il salvataggio dei dati di setup della matrice.
Questo avviene salvando i valori della schiera dei campi gestiti (£JayFldLst), delle autorizzazioni e delle altre informazioni di setup (£JayDSSetup) e di eventuali informazioni specifiche impostate nel servizio (£JaySpecInfo) nel file di appoggio B£SUPS0F direttamente nella /copy £JAY_C0.

Salvare queste informazioni consente utilizzi contemporanei dello stesso servizio in più  schede nella stessa sessione Loocup, senza che le impostazioni vengano sovrascritte.
Inoltre predispone il servizio aumentandone la compatibilità con web e mobile.

La pulizia dei dati scritti nel B£SUPS0F per la singola matrice avviene alla chiamata del servizio di aggiornamento con £UIBME='*EXIT'.
La pulizia dei dati scritti nel B£SUPS0F per la sessione avviene alla chiusura di Loocup.


## Implementazione
Aggiungere nella IMP0 del servizio di aggiornamento l'esecuzione della routine £JAY_SETLET .

Verificare che nel servizio di aggiornamento sia gestita la chiamata con £UIBME='*EXIT' e in caso manchi aggiungerla nel main del programma.
Aggiungere sotto la chiamata con £UIBME='*EXIT' l'esecuzione della routine £JAY_EXIT.

### ATTENZIONE : 
Prestare attenzione ad eventuali conflitti tra la rilettura del setup e ottimizzazioni interne al servizio in merito alla rilettura delle autorizzazioni :  potrebbe causare problemi dopo il refresh della sezione.

