# Configurazione dell'AS/400

## Configurazione comunicazione
### Breve descrizione
La comunicazione tra il lato Client (PC) e il lato Server (AS400) avviene tramite appositi processi che vengono attivati al momento della connessione.
La comunicazione tra AS400 e Client PC avviene tramite code dati (oggetto AS400 *DTAQ).
La configurazione del lato server consiste di fatto nella configurazione dell'ambiente di questi processi.
I processi di comunicazione sono a tutti gli effetti dei lavori di tipo batch, e per poter funzionare hanno bisogno di definire la coda lavori nella quale vengono lanciati.
Viene qui descritta una procedura per creare il tipico ambiente di esecuzione sul Server.
I nomi dei sottosistemi e delle code lavoro utilizzati non sono vincolanti, ma si consiglia di utilizzarli per maggior coerenza con le altre configurazioni di LoocUp.
Nota : 
Per l'effettiva operazione di configurazione, __consigliamo di leggere questa documentazione direttamente tramite client access (non tramite versioni cartacee, pdf e loocup), in quanto così si avrà la possibilità di eseguire direttamente i comandi indicati senza doverli impostare manualmente.

### Sottosistema
E' preferibile che i processi di comunicazione siano attivi in un sottosistema dedicato, anche se non ci sono controindicazioni nell'utilizzo di un sottosistema già esistente (Es. QINTER o QBATCH)
Si consiglia di creare un sottosistema denominato QBATCHUI.
Normalmente i sottosistemi vengono creati nella libreria SMESYS.

### Parametri di creazione del sottosistema
>.  Descrizione sottosistema . . . . > QBATCHUI      Nome
.    Libreria . . . . . . . . . . .     SMESYS      Nome, *CURLIB
.  Lotti di memoria : 
.    Identificativo di lotto  . . . > 1             1-10
.    Ampiezza memoria . . . . . . . > *BASE         Numero, *BASE, *NOSTG...
.    Livello attività . . . . . . .                 Numero
.                + per altri valori
.  Numero massimo di lavori . . . .   *NOMAX        0-1000, *NOMAX
.  Testo 'descriz.' . . . . . . . .   'Looc.up batch subsystem'

### Comando di creazione sottosistema
CRTSBSD SBSD(SMESYS/QBATCHUI) POOLS((1 *BASE)) TEXT('Looc.up batch subsystem')
 :  : INI Creazione sottosistema
 :  : CMD ?CRTSBSD SBSD(SMESYS/QBATCHUI) POOLS((1 *BASE)) TEXT('Looc.up batch subsystem')
 :  : FIN

Dopo aver creato il sottosistema è necessario definire il passo di instradamento.
### Parametri  del passo di instradamento
>.  Descrizione sottosistema . . . . > QBATCHUI      Nome
.    Libreria . . . . . . . . . . .     SMESYS      Nome, *LIBL, *CURLIB
.  Num. seq. spec. instradamento  . > 9999          1-9999
.  Dati di confronto : 
.    Valore confronto . . . . . . . > *ANY
.
.    Posizione iniziale . . . . . .                 1-80
.  Programma da richiamare  . . . . > QCMD          Nome, *RTGDTA
.    Libreria . . . . . . . . . . .     *LIBL       Nome, *LIBL, *CURLIB
.  Classe . . . . . . . . . . . . .   QBATCH        Nome, *SBSD
.   Libreria . . . . . . . . . . .                 Nome, *LIBL, *CURLIB
.  Num. max passi instrad. attivi     *NOMAX        0-1000, *NOMAX
.  ID lotto memoria . . . . . . . .   1             1-10

### Comando di creazione del passo di instradamento
ADDRTGE SBSD(SMESYS/QBATCHUI) SEQNBR(9999) CMPVAL(*ANY) PGM(QCMD) CLS(QBATCH)
 :  : INI Creazione passo di instradamento
 :  : CMD ?ADDRTGE SBSD(SMESYS/QBATCHUI) SEQNBR(9999) CMPVAL(*ANY) PGM(QCMD) CLS(QBATCH)
 :  : FIN

**ATTENZIONE : ** Il parametro Classe viene impostato di default al valore *SBSD, modificarlo al valore QBATCH.

**IMPORTANTE : ** La principale causa del mancato funzionamento di LoocUp è dovuta alla mancanza della definizione del passi di instradamento.

### Coda lavori
Creare una coda lavori specifica per i processi di comunicazione, si consiglia di denominrla QBATCHUI.
Si consiglia di creare le code lavori nella libreria SMESYS. Bisogna però assicurarsi che
tale libreria sia in lista librerie (normalmente essa è inserita tra la librerie di sistema).

### Parametri della coda lavori
>.  Coda lavori  . . . . . . . . . . > QBATCHUI      Nome
.    Libreria . . . . . . . . . . . >   SMESYS      Nome, *CURLIB
.  Testo 'descriz.' . . . . . . . .   'Looc.Up batch subsystem jobq'

### Comando di creazione coda lavori
CRTJOBQ JOBQ(SMESYS/QBATCHUI) TEXT('Looc.Up batch subsystem jobq')
 :  : INI Creazione coda lavori
 :  : CMD ?CRTJOBQ JOBQ(SMESYS/QBATCHUI) TEXT('Looc.Up batch subsystem jobq')
 :  : FIN
**IMPORTANTE : **  Il nome dalla coda lavori creata deve essere riportata nella tabella UI1

 :  : INI Modifica della tabella
 :  : CMD CALL B£AM30 PARM('UI1' '  ' '*              ')
 :  : FIN
### Esempio di tabella UI1 compilata
>.  Sme.Up V3R2           **   MANUTENZIONE TABELLE   **      S44256CA   B£AM30
.   8/07/05                    Gestione elemento             QPADEV0051 AS
.  Set. UI1 Main User Interface
.  Ele. *                                                             Archivio 0
.  Descrizione          Personalizzazione UI
.  Ambiente             SM                 SME_up
.  Coda lavoro          QBATCHUI           Looc.Up batch subsystem jobq
.  Chiusura Job Emulat.                    NO


### Assegnazione della coda lavori al sottosistema
Occorre associare la coda lavori creata al sottosistema precedentemente definito.
### Parametri del comando
>.  Descrizione sottosistema . . . .   QBATCHUI      Nome
.    Libreria . . . . . . . . . . .     SMESYS      Nome, *LIBL, *CURLIB
.  Coda lavori  . . . . . . . . . .   QBATCHUI      Nome
.    Libreria . . . . . . . . . . .     SMESYS      Nome, *LIBL, *CURLIB
.  Num. massimo lavori attivi . . .   *NOMAX        0-1000, *NOMAX
.  Numero sequenza  . . . . . . . .   10            1-9999
.  Massima priorità attiva 1  . . .   *NOMAX        0-99, *NOMAX
.  Massima priorità attiva 2  . . .   *NOMAX        0-99, *NOMAX
.  Massima priorità attiva 3  . . .   *NOMAX        0-99, *NOMAX
.  Massima priorità attiva 4  . . .   *NOMAX        0-99, *NOMAX
.  Massima priorità attiva 5  . . .   *NOMAX        0-99, *NOMAX

**IMPORTANTE : ** Prestare particolare attenzione al valore *NOMAX del parametro Num. massimo lavori attivi.
### Comando di associazione della coda lavori al sottosistema
ADDJOBQE SBSD(SMESYS/QBATCHUI) JOBQ(SMESYS/QBATCHUI) MAXACT(*NOMAX)
 :  : INI Assegnazione coda lavori al sottosistema
 :  : CMD ?ADDJOBQE SBSD(SMESYS/QBATCHUI) JOBQ(SMESYS/QBATCHUI) MAXACT(*NOMAX)
 :  : FIN  _

### Avvio del sottosistema
E' necessario avviare il sottosistema precedentemente creato.
## Parametri del comando
>.  Descrizione sottosistema . . . .   QBATCHUI      Nome
.    Libreria . . . . . . . . . . .     SMESYS      Nome, *LIBL, *CURLIB

### Comando di avvio del sottosistema
STRSBS SBSD(SMESYS/QBATCHUI)
 :  : INI Avvio del sottosistema
 :  : CMD ?STRSBS SBSD(SMESYS/QBATCHUI)
 :  : FIN

**IMPORTANTE : ** I sottosistemi NON vengono automaticamente avviati all'accensione dell'AS400. Modificare quindi il programma di avvio dell'AS400 (QSTRUP) e avviare esplicitamente il sottosistema.

### Libreria code dati
Gli oggetti *DTAQ che vengono utilizzati per la comunicazione vengono creati nella libreria SMEUPUIDQ, la quale deve essere creata appositamente.
## Parametri del comando di creazione della libreria
>.  Libreria . . . . . . . . . . . . > SMEUPUIDQ     Nome
.  Tipo libreria  . . . . . . . . .   *PROD         *PROD, *TEST
.  Testo 'descriz.' . . . . . . . . > 'Sme_Up V3R2 - Libreria standard code'

**NOTA : ** Il nome della libreria è fisso e non può essere modificato.
### Comando di creazione della libreria
CRTLIB LIB(SMEUPUIDQ) TEXT('Sme_Up V3R2 - Libreria standard code')
 :  : INI creazione della libreria SMEUPUIDQ
 :  : CMD CRTLIB LIB(SMEUPUIDQ) TEXT('Sme_Up V4R1 - Libreria standard code')
 :  : FIN

### Controlli finali
_9_A questo punto tutto il necessario sul lato Server è stato configurato.
In caso di mancato funzionamento, controllare che tutti i passi siano stati eseguiti correttamente : 
 :  : PAR F(01) L(PUN)
-Sottosistema avviato
-Passi di instradamento definiti
-Coda lavori associata al sottosistema (con numero lavori *NOMAX)
-Tabella UI1 corretta


Per verificare il corretto funzionamento della coda lavori e del sottosistema creato provare a lanciare una procedura batch nella coda QBATCHUI.

**NOTA : ** L'utilizzo di Looc_Up prevede la corretta compilazione delle tabelle MEA relative ai menù.
Per verificare la corretta impostazione delle tabelle MEA è possibile utilizzare il comando (da linea comandi della normale emulazione 5250) **UP SER**, impostando i parametri come evidenziato : 
>.  Sme.Up V3R2        **    Set - Play Funzioni    **         S44256CA   JASEP2
.  Q80705                                                     QPADEV0033 AS
.
.  Servizio        *MNU   Menù completo            Fornito da :  JATRE_01C
.  Funzione.Metodo
.  Componente      TRE    Albero
.
.  Oggetto         Tipo    Parametro    Codice     Descrizione
.  1
.  2
.  3
.  4
.  5
.  6
.
.  Parametro
.
.  Modo grafico
.
.  Risultato       F(TRE;*MNU;)


Dovrà apparire una videata come la seguente : 
>.   Sme.Up V3R2  **  ANALISI XML DI UN PROGRAMMA  **  18/07/05 S44256CA   TSTJASX
.                        Sviluppo di dettaglio         16 : 18 : 49 QPADEV0033 AS
.
.
.
.   ?
.
.     Albero di oggetti in XML
.     Albero di oggetti in XML
.
.    1 < Oggetto Nome=   Tipo=   Parametro=   Codice=   Testo= User List
.     2 < Oggetto Nome=   Tipo=   Parametro=   Codice=   Testo= Arrighini Ste ...
.      3 < Oggetto Nome=   Tipo=   Parametro=   Codice=   Testo= Ultime esegu ...
.      3 < Oggetto Nome=   Tipo=   Parametro=   Codice=   Testo= Dipendente
.       ...


### Alcuni utili suggerimenti
Nella libreria SMEUPUIDQ vengono creati continuamente oggetti di tipo *DTAQ che in alcuni casi particolari (malfunzionamenti) potrebbero non venire eliminati. Si consiglia quindi di attivare periodicamente (inserendola ad esempio nelle procedure di spegnimento dell'As400) una procedura di "pulizia".
### Esempio di procedura per l'eliminazione degli oggetti *DTAQ dalla libreria SMEUPUIDQ
__chiusura del sottosistema x chiudere tutti i lavori attivi__
ENDSBS     SBS(QBATCHUI) OPTION(*IMMED)
__attesa di completamento dell'operazione di chiusura__
DLYJOB     DLY(60)
__eliminazione di tutte le code dati__
CLRLIB     LIB(SMEUPUIDQ)
__riavvio (eventuale) del sottosistema__
STRSBS     SBSD(SMESYS/QBATCHUI)

# Simulazione funzioni AS/400
Condizione necessaria per il funzionamento di Looc.up è che la parte AS/400 sia funzionante. A tale fine sono state predisposte delle funzioni per verificare che la parte server sia correttamente attivata. Ad esempio Looc.up non parte se mancano i menù oppure il profilo utente non consente l'accesso al programma di START.

Si consiglia pertanto, una volta verificati i prerequisiti di procedere nel modo seguente : 

### Verificare il collegamento
 * Programma = TSTJAC ( T JAC)
 * Messaggio = DATSES
 * Funzione = CON

 - Si vede un numero di 6 cifre in OUTPUT D2
 - Verificare l'inizio dei lavori per l'utente
 - Verificare la creazione delle code con tale nome nella libreria SMEUPUIDQ
 -  Funzione = DIS (se si è usciti fornire nei parametri il numero ricavato in precedenza)
 - Verificare la fine dei lavori per l'utente
 - Verificare l'assenza delle code create prima

### Verifiche di esecuzione delle funzioni estese
- Immettere "UP SER" nella linea comandi
- Inserire "F(TRE;*MNU;)" nel campo risultato e premere F21 poi F20 e scegliere un ambiente
- La funzione JS deve presentare il formato XML della lista dei menù.

Se la lista non si presenta significa che manca un prerequisito, oppure il programma è in errore.


# Nota storica su vecchie release di sistema operativo (non più supportate da Sme.UP)
Per versioni molto vecchie di sistema operativo (non più supportate da Sme.UP) era necessario installare una PTF correttiva ed effettuare alcune operazioni per velocizzare la lettura code

## Descrizione del problema
A causa di un problema del supporto SLIC, nelle versioni V4R3, V4R4, V4R5, V5R1 e V5R2 del sistema operativo OS/400, si verifica un ritardo di 2 secondi su tutte le letture da code dati effettuate dall'esterno del sistema. Questo ritardo, pur non pregiudicando il funzionamento di Looc.Up, porta ad un rallentamento generale dell'interfaccia grafica.

## Come procedere
Per le release V4R3, V4R4, V4R5 e V5R1 è necessario

- Installare su AS/400 la corretta PTF
- Disabilitare il ritardo SLIC


Per la release V5R2 è necessario semplicemente Disabilitare il ritardo SLIC.

Le PTF sono le seguenti : 

-MF24942 - se V4R3
-MF24475 - se V4R4
-MF24728 - se V4R5
-MF27269 - se V5R1


Per disabilitare il supporto SLIC collegarsi come QSECOFR (o con un utente con pari autorizzazioni) ed immettere il comando
**call qskmaint parm(20 x'80')**

Nel caso il supporto SLIC debba essere riattivato per qualche motivo, immettere il comando : 
**call qskmaint parm(20 x'81')**

## Ulteriori informazioni
Per informazioni più dettagliate su queste PTF vedere il seguente link IBM : 
[http://www-01.ibm.com/support/docview.wss?uid=nas8N1017346](http://www-01.ibm.com/support/docview.wss?uid=nas8N1017346)
