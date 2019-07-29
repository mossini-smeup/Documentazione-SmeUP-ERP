# OBIETTIVO

## Obiettivo
Gestire tutte le azioni su un oggetto. Dal controllo all'aggiornamento dei suoi dati.
Il flusso di gestione è il seguente : 
. setup
. caricamento struttura
. caricamento dati
. controllo dati
. applicazione o abbandono
Ci sono poi delle funzioni aggiuntive che vengono lanciate in automatico dalle funzioni di gestione
. autorizzazioni
. overlay
. funzione successiva
. derivazione oggetto

## Programm specifico oggetto
Per ogni oggetto esiste il programma B£K89_XX dove XX è l'oggetto.
Per il file che non hanno oggetto si ulizza l'oggetto ID dove il parametro è il nome del file. In questo caso il suffisso XX del programma B£K89_XX è un progressivo numerico definito da Smeup.
Automaticamente la £K89 associa la gestione dell'oggetto al corrispondente programma.

## Funzioni
La £K89 gestisce le funzioni :  SET, CARSTR, CARVAL, CTR, APP, ABB, FSU.

Tutte queste funzioni transitano da un programa di exit. Il richiamo del programma di exit è sempre POST. Tranne per la funzione di aggiornamento APP dove c'è anche un richiamo PRE. Questo richiamo viene fatto prima di eseguire l'aggiornamento del record e con in essere il record stesso.In questo modo è possibile modificare in ultima istanza nella exit qualsiasi campo del record.
Il nome della exit è libero, però per rendere facilmente rintracciabili i programmi è consigliato usare la nomenclatura B£K89_XXYY,  Dove B£K89_XX è il nome del programma specifico dell'oggetto. A standard YY è £Y dove Y è un progressivo.
La exit viene impostata nel parametro "PgmExt" che si può impostare direttamente nel richiamo del A36 che nello script di Setup

* SET Setup
La funzione di setup viene eseguita in automatico prima della gestione.
Ricostruisce tutti i parametri di input in funzione di quelli ricevuti e dall'eventuale setup attivato nello script SCP_A36. o SCP_A36PER per le personalizzazioni. Lr priorità dei dei parametri è sempre su quelli riceuti in nput rispetto a quelli del Setup.
Ii nome dello script corrisponde con la exit del programma specifico. Per i files senza oggetto è IDXX dove XX è il suffisso del corrispondente programma specifico.
I parametri fondamentali del setup sono : 
** la finestra di gestione "TipFlt" e "CodFlt"
** l'eventuale programma di exit "PgmExi"
Il programma che gestisce la funzione "SET" è il B£K89T
E' sempre possible modificare i parametri di setup ricevuti in input e completati dallo script nel programma specifico e nella exit.
Per esempio nel costi di un oggetto (File D5COSO0F) il suo programma specifico B£K89_04 quando riceve l'azione di immissione verifica se per i campi ricevuti in input esiste già un record nel DB,
 in caso affermativo trasforma l'azione da immissione in modifica.  In questo modo l'utente ha una sola azione che gestisce contemporanenamnte immissione e modifica.

* CARSTR
Questa funzione costruisce la struttura della gestione, ovvero i campi da presentare in gestione con tutte le loro proprietà.
Lo standard gestisce generalmente campi che sono OAV dell'oggetto stesso. OAV che determina anche le proprietà stadard di ciascun campo.
Il programma specifico, in questa funzione, può completare o aggiungere anche altri campi al di fuori degli OAV. In questo caso dovrà anche preoccuparsi di eventalmente aggiornarli nel DB.
Nella Exit è possibile intevenire e modificare le proprietà dei campi o aggiungere campi specifici di work.
La lista dei campi da presentare poi effettivamente in gestione viene definita nei parametri : 
"TipFlt" e "CodFlt".
Ci sono diversi modi per definire la lista dei campi.
Sono gestiti i seguenti tipi di lista "TipFlt" : 
** PRF :  Preferiti. E' una lista di OAV proveniente dai preferiti
** SCH :  Schema (SVI). E' una lista OAV proveniente da uno schema
** PRE :  Prefisso OAV. E' la lista di OAV che iniziano con un determianto prefisso
** LIS :  Lista OAV. E' una lista di OAV proveniente dalla gestione dell liste.
** OAV :  OAV Singolo. Gestione di un signolo OAV
** CAT :  Categoria OAV. E' la lista degli OAV appartenenti ad una categoria
** GES :  OAV di gestione. Sono stati identificati come OAV di gestione tutti quelli che NON iniziano per G, J, U, V
** LAY :  Da SCP_LAY. Sono OAV definiti in uno script del file SCP_LAY
** S-  :  Questionario. Sono OAV definiti in uno script del file SCP_CFG
**ALL  :  Tutti
dove il "CodFlt" è specifico di ogni "TipFlt".
Il parametro TipFlt e CodFlt può essere modificato anche nella exit.
Qunando la lista non è di tipo "LAY" e comunque possibile costruire un SCP_LAY da mettere nel parametri "ScpLay" dove ridefinire le propietà del campo. In questo caso dell'SCP_LAY viene usato solo per ridefinire le propietè e non per l'agguinta di altri campi. E' una specie di dizionario.
La corrispondenza è in nome del campo.
Per le proprità gestite vedere la documentazione specifica
il programma che sotruisce la struttura è il B£K89S
Queste proprietò possono avere la seguente origine : 
** "A" Da Definizione
Come prima istanza le proprietà di un campo sono quelle insite nella sua definizione.
Vengono impostate dal programma di gestione struttura B£K89S che le deriva direttamente dalla copy £OAV o £IR1 del file in gestione.
** "B" Dal programma di gestione struttura
Solo le proprietà costruite o forzate direttamente dal programma di gestione struttura B£K89S.
** "C" Dal programma base
Solo le proprità costruite o forzate direttamente dal programma base B£K89G
** "D" Dal programma specifico oggetto
Solo le proprietà costruite o forzate dal programma specifico dell'oggetto B£K89_XX
** "E" Dal programma di exit
Solo le proprietà costruite o forzate dal programma di exit
** "F" Dal SCP_LAY
Solo le proprietà costruite o forzate nell'SCP_LAY
** "G" Da Autorizzazioni
Solo le proprietà forzate dei limiti imposti dalle autorizzazioni. (SV)

NOTA IMPORTANTE : 
Poichè la struttura si basa come default sugli OAV di un oggetto è importante che vengano ricostruiti nel caso si aggiungano nuovi parametri, o nuove contenitori e/o capitoli note.
Il programma standard degli OAV costruisce questi attributi nel segente formato : 
. parametri  P/XXX/YYY dove
  .. XXX è la categoria, tabella "C£E" e campo DB C£TPRC
  .. YYY è il parametro, tabella "B£NXX" e campo DB C£NUMP.
  il programma standard di gestione B£K89_PA li riconosce e gestisce nel file di DB.
. note       N/XXX/YYY dove
  .. XXX è il contenitore, tabella "NSC" e campo DB C$TIPC
  .. YYY è il tipo informazione, tabella "NSI" e campo DB C$TIPI
  il programma standard di gestione B£K89_NT li riconosce e gestisce nel file di DB.

* CARVAL
Questa funzione carica i valori in gestione.
In immissione inizializza il record senza generare il codice o numeratore. La scelta è stata quelle di generare il codice o il numertore solo nella funzione di conferma in modo da non dover gestire il roll-back dei numeratore in caso di abbandono
E' possibile modificare le tutte le proprietà dei campi, che vanno a sostiuire quelle della struttura, comprese quelle impostate dall'SCP_LAY.
Il caricamento valori si distingue in tre diverse modalità in funzione dell'azioni che si sta
eseguento
. Azione "00" :  pre-immissione
. Azione "01" :  immissione nuovo oggetto
. Altre azioni :  gestione oggetto esistente
La pre-immissione generalmente chiede delle informazioni preliminari ncessarie prima di poter eseguire l'immissione. Non necessita della lettura di dati ma propone quelli ricevuti in input nel parametro InzDat.
L'immissione di uno oggetto generalmente esegue il suo inizializzatore specifico.
Qualore si volesse far arrivare determinati campi all'inizializzatore o assumerli come default si deve utizzare com per la pre-immissione il parametro "InzDat".
La sua struttura è NomeCampo(Valore), dove in NomeCampo può essere : 
. £89I_NM il nome del campi          Esempio classe materiale articolo :   W$CLAM(PIPPO)
. £89I_OA il nome dell'OAV           Esempio classe materiale articolo :   I/10(PIPPO)
. £89I_CF il nome del campo del DB                                       A§CLMA(PIPPO)
. £K89_OG l'oggetto                                                      TACLS(PIPPO)
Nel caso di oggetto vengono caricati tutti i campo con quell'oggetto
Il campo deve necessariamente essere presente nella struttura. Se non lo si vuole vedere basta
definirlo come Hidden.
La gestione di un oggetto esegue la lettura di tutti gli OAV che compongono la struttura.
Per ottimizzare le lettura nel caso di OAV interni è stato inibilito il caricamento tramite OAV
e implementata la lettura diretta del record del file.
Questa funzione viene eseguita dal programma specifico dell'oggetto.
In ultima istanza sia per per l'immissione che per la gestione si passa dal programma specifico
sia dell'oggetto che della exit utente dove è possibile intervenire sul caricamento di dati

* CTR
Questa funzone gestisce tutti i controlli dei dati.
I controlli sono a tre livelli : 
. controlli generici di oggetto
. controlli specifici dell'oggetto
. controlli utente
I controllo generici sono fatti dalla K89 e controllano semplicemente la validità dell'oggetto
(tranne il caso in cui non venga esplicamente detto nelle sue proprieà di non eseguire controlli)
I controllo specifici dell'oggetto sono definiti nel programma specifico dell'oggetto. Ogni
oggetto può decidere determinati controlli di validtà o di congruenza dei dati.
I controllo utente sono definiti nel programma di exit.
Gli errori devono essere caricati nella specifica schiera £K89O_SC dove va indicato
- £89O_PN l'indice di schera delle £K89I_SC a cui appartiene il campo in errore,
- £89O_TP, £K89O_CD il tipo e codice messaggio di errore (Facoltativo se presente £89O_TX)
- £89O_TX  un testo di errore (Facoltativo se presente £89O_CD)
- £89O_GM la gravità (Da 0 a 99, fino a 33 il messaggio è di warning, da 34 è vincolnte)
- £89O_PM il programma che sta inserendo l'errore.
E' possibile modificare la propietà di I/O del campo in modo che un campo diventi Hidden, di solo output o di Input/output in funzione del contenuti di un altro campo.
Non è possibile modificare la proprietà di obbligatorietà perchè è gestita direttamente dal client e viene controllata prima di essere modificata con l'effetto che rimane la segnalazione di campo obbligatorio anche se il campo è stato digitato e per eliminaria si è costretti a fare un enter, In questo caso è meglio gestire la variazione del campo tra obbligatorio e non obbligatorio con i messaggi di errore gestiti direttamente nella exit della CTR. Tenendo come prorpità di campo sempre non obbligatorio .


* APP
Questa funzione esegue l'aggiornamento del Data-Base per l'azione scelta. Parametro "AziExe"
Sono gestite le seguenti azioni : 
** "00" Pre-Immissione
E una funzione che presenta una finestra dove si inseriscono dei valori per poi passare ad un'altra finestra di pre-immissione o all'azione di immissione.
Generlamente NON esegue alcun aggiornamento dul DB.
** "01" Immissione
E' l'azione di immissione di un oggetto
** "02" Modifica
E' l'azione di modifica di un oggetto
** "03" Copia
E' l'azione di copia un oggetto in un altro oggetto
** "04" Cancella
E' l'azione di cancellazione di un oggetto
** "05" Visualizza
E' l'azione di visualizzazione i un oggetto
A standard si hanno in gestione tutti gli oav di tipo "I" campi del DB, "N" Note, "P" parametri e "K" parametri estesi.
E' possible mettere in gestione gli OAV di tipo "U" utente solo se poi in una exit si gestisce il corripondente aggiornamento nel Data-Base
** Deriva Oggetto.
Permette di derivare il codice oggetto qualora in input non si conosca me ci siano altre informazioni con cui è possibile identificarlo univocamente.
Per esempio nei clienti quando si conosce la partita iva ma non il codice cliente.
Viene eusato principalmente per l'import di dati LOA40.

** AUT Autorizzazioni
Controlla l'autorizzazione sull'azione scelta

** OVR Overlay
E' la funzione che esegue l'ovrlay delle proprieta dei campi della struttura dall SCP_LAY scelto

* FSU
Questa funzione permette di definire a programma la funzione successiva che si vuole eseguire dopo la conferma dell'azione.
Nel caso della pre-immissione, azione "00", è possible impostare il parametro "NamSuc" che identifica la prossima finestra da aprire Cmpreso il valore "*FINE" che determinal la fine del flusso per passare all'azione "01" con l'effettiva finestra di immissione

* ABB
Questa funzione viene richiamata quando si decide di uscire senza confermare l'azione. In questo caso è possibile ripristinare eventuali azioni eseguite durante le funzioni precendenti.


## Messaggio
Ogni errore viene caricato nelle schiere dei messaggi : 
. £89O_PN Puntatore schera DB
. £89O_TP Tipo messaggio
. £89O_CD Codice messaggio
. £89O_TX Testo messaggio
. £89O_GM Gravità messaggio
. £89O_PG Programma messaggio
Per ogni campo viene presensato il suo primo messaggio.
E' sempre possibile visualizare attraverso il bottone "Dettaglio messaggi" tutti i messaggi
caricati. Dove in particolare sarà visibile la gravità e il programma che ha determinato il
il messaggio. Se la gravità del messaggio è inferiore a "33" il messaggio sarà di solo warning e non determinerà l'errore sul suo campo.


## Gestione Parametri Smeup (Campi configurati)

I parametri si possono presentare in 9 tipologie di gestione.

Ciascuna viene gestita nella £K89 con una sua forma specifica

* parametro SINGOLO alfanumerico
Viene presentato come campo il parametro con l'oggetto della tabella "B£N"
Il parametro K89I_PL contiente l'informazione di parametro singolo alfanumerico nella forma Par(A)

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
* Il campo contiene tutti i valori multipli nell'identificatico CD() e con separatore di record ";"
Esempio :  CD(AR1);CD(AR2);CD(AR3);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico nella forma Par(MA)
e l'informazione della configurazione nella forma LC(CD)

* Parametro MULTIPLO numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto fisso "NR" (Esempio LCNR)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico NR() e con separatore di record ";"
Esempio :  NR(1,50000);NR(2,50000);NR(7,00000);
Il parametro K89I_PL contiente l'informazione di parametro multiplo numerico nella forma Par(MN)
e l'informazione della configurazione nella forma LC(NR)

* Parametro MULTIPLO alfanumerico e numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD() e NR() con separatore di
record ";"
Esempio :  CD(AR1)NR(1,50000);CD(AR2)NR(2,50000);CD(AR3)NR(7,00000);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico e numerico nella
forma Par(MAN) e l'informazione della configurazione nella forma LC(CD;NR)

* Parametro MULTIPLO E DATATO alfanumerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD(), DI() e DF() e con separatore
di record ";"
Esempio :  CD(AR1)DI(20150101)DF(20151231);CD(AR2)DI()DF();CD(AR3)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico e datato nella
forma Par(DA) e l'informazione della configurazione nella forma LC(CD;DI;DF)

* Parametro MULTIPLO E DATATO numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto fisso "NR" (Esempio LCNR)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico NR(), DI() e DF() e con separatore
di record ";"
Esempio :  NR(1,50000)DI(20150101)DF(20151231);NR(7,00000)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo numerico e datato nella
forma Par(DN) e l'informazione della configurazione nella forma LC(NR;DI;DF)

* Parametro MULTIPLO E DATATO alfanumerico e numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD(), NR(), DI(), e DF(), e con
separaotre di record ";"
Esempio :  CD(AR1)NR(1,50000)DI(20150101)DF(20151231);CD(AR2)NR(7,00000)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico, numerico e datato
nella forma Par(DAN) e l'informazione della configurazione nella forma LC(CD;NR;DI;DF)

## Flussi

## Autorizzazioni per campo

## Lock oggetto

## Gestione transazioni

## Notifiche

## Log di modifica campo
