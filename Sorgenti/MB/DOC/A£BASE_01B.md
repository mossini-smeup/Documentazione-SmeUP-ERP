# Caricamento librerie Sme.up V5R1
Caricare sul sistema le librerie necessarie.

## Prerequisiti
E' richiesta una versione di sistema operativo pari alla V6R1 o superiore.

## Nota bene
Nel caso di caricamento da supporto magnetico o da DVD-ROM, riferirsi al documento  :  : DEC T(MB) P(DOC) K(A£BASE_IN1) L(1) R( )

# Adeguamento database ed ambiente di test
Con l'installazione della V5R1 sono stati modificati alcuni archivi del database, quindi si rende necessario il loro allineamento.

## Tipo accesso della sessione
Per potere acedere senza problemi ad una sessione da cui verranno eseguite le operazioni di allineamento (PTF, ecc.) è necessario che la sessione sia configurata con accesso a riga comando e non menù od altro.

## Ambiente di test
È consigliato come di consueto eseguire prima dell'attivazione effettiva della V5R1 sul sistema informativo di produzione o effettivo, l'installazione su un sistema informativo di TEST, risultante da una copia di quello di produzione.
La conversione degli archivi da versioni precedenti alla V5R1 di Sme.up avviene, come di consueto, tramite l'applicazione di PTF specifiche per applicazione
Effettuare una copia della/e libreria/e di dati di produzione in una o più librerie di test : 
(annotare le librerie duplicate per il test, per promemoria)

| 
| .COL Txt="Libreria di produzione / effettiva" A="L" |
| ---|----|
| 
| .COL Txt="Libreria di test" LunAut="1" |
|  . | . |
|  . | . |
|  . | . |
|  . | . |
|  . | . |
|  . | . |
|  . | . |
| 


# Aggiornamento di un ambiente che si trova a V4R1
Il modulo base V5R1 è compatibile con la release V4R1.
**Sarà quindi possibile associare ad un utente sia ambienti V5R1 che V4R1.**

# Aggiornamento di un ambiente che si trova a V3R2
Il modulo base V5R1 è compatibile con la release V3R2.
**Sarà quindi possibile associare ad un utente sia ambienti V5R1 che V3R2.**

_7_NOTA : 
A causa della profonda revisione del modulo delle traduzioni, per poter accedere ad un ambiente da migrare ad una release V5R1 è tassativo accedere con un ambiente con il campo "lingua assunta" uguale a BLANK (nessuna traduzione linguistica impostata).

Inoltre, prima di poter eseguire le PTF come di consueto, è necessario eseguire alcuni passi di pre-adeguamento.
Questi passi sono dovuti alla modifica di alcuni file strutturali (come l'AUTOAP0F). Senza l'aggiornamento preventivo di questi file risulta impossibile l'esecuzione di qualunque comando UP.

## Pre-PTF Adeguamento tabella MEA
Questa Pre-PTF deve essere OBBLIGATORIAMENTE applicata prima di qualsiasi altra PTF o pre-PTF, in quanto comporta l'esecuzione di azioni che vanno fatte in ambienti con in linea ancora i programmi della release precedente.
Queste azioni vanno fatte PRIMA di riallineare il tracciato della tabella MEA.

Per il dettaglio aggiornato delle azioni da eseguire, si rimanda alla lettura del seguente membro del file PTF : 
 :  : DEC T(MB) P(PTF) K(££30901A) D(Pre-PTF Adeguamento tabella MEA - FASE 1) L(1)
Non essendo a questo punto disponibile il comando UP PTF, tale membro va letto con il PDM.

_7_ATTENZIONE : 
__Non proseguire con le successive operazioni senza aver prima eseguito questa operazione__


## Pre-PTF Adeguamento file sensibili e accesso
Nella release V4R1 sono stati variati i tracciati dei file delle autorizzazioni (AUTOAP0F e AUTOOG0F). Tali variazioni comportano l'impossibilità di eseguire qualunque funzione che verifichi le autorizzazioni, compreso UP PTF. Quindi l'allineamento verrà fatto tramite un programma esterno.

Per il dettaglio aggiornato delle azioni da eseguire, si rimanda alla lettura del seguente membro del file PTF : 
 :  : DEC T(MB) P(PTF) K(££30901B) D(Pre-PTF Adeguamento file sensibili) L(1)
Non essendo a questo punto disponibile il comando UP PTF, tale membro va letto con il PDM.

## Altre PTF
A questo punto scollegarsi, ricollegarsi ed eseguire tutte le altr PTF come di consueto (Iniziando ovviamente dalle "££").


# Aggiornamento di un ambiente che si trova a V3R1 o precedente
Il modulo base V5R1 non è invece compatibile con release V3R1 e precedenti (come non lo erano le release V3R2 e V4R1).

Questo significa che **NON E' POSSIBILE ASSOCIARE AD UNO STESSO UTENTE SIA AMBIENTI V5R1 CHE V3R1 O PRECEDENTI.
Inoltre **NON E' POSSIBILE UTILIZZARE AMBIENTI V5R1 CON UNA JOBD V3R1 O PRECEDENTE**.

Nel caso sia necessario avere due ambienti (V5R1 di test e reale su release V3R1) sarà obbligatorio utilizzare 2 utenti diversi. Un utente con jobd precedente (V3R1) e ambienti precedenti (V3R1) e uno con jobd V5R1 e ambienti V5R1.

Purtroppo non è stato possibile impedire fisicamente questi comportamenti (compresenza di ambienti misti o V5R1 su jobd precedenti). Il loro rispetto quindi è a totale carico dell'installatore.
Ribadiamo l'estrema importanza di questo fatto onde evitare grossi problemi.

## Creazione utente di collegamento specifico
Per quanto detto in merito alla compatibilità con ambienti precedenti, in caso si stia aggiornando una release V3R1 o precedente è necessario eseguire alcuni passi preliminari prima di poter effettuare il primo collegamento.
E' quindi necessario : 
* Creare una JOBD V5R1 (es. SMEJOBD51 con librerie standard V5R1 e librerie cliente da aggiornare)
* Creare un nuovo utente (es. SME51) con associata la JOBD V5R1 precedentemente creata
** Tale utente deve avere impostato come"programma iniziale" (INLPGM) il valore *NONE
* Collegarsi con il nuovo utente creato
* Eseguire la chiamata CALL B£QQX01 che consente di : 
** Creare i file
** Popolarli
** Mediante UP UT5 creare un ambiente V5R1 e associarlo all'utente creato (SME51)
*** In caso quest'ultimo comando non funzioni, utilizzarlo dopo aver eseguito le due Pre-PTF della release V4R1
* Modificare il profilo utente inserendo come programma iniziale il B£QQ50 (o B£UT50)
* Scollegarsi, ricollegarsi e a quel punto procedere come di consueto

In alternativa alla creazione di utente con INLPGM *NONE è possibile mettere in linea "manualmente" le librerie V5R1 e poi eseguire la CALL B£QQX01

## Ulteriori Pre-PTF
A questo punto in base al rilascio di partenza è necessario eseguire Pre-PTF specifiche

### Release V1R5 o precedenti
Le modifiche al modulo base (B£) della V2R1 hanno comportato modifiche ai files tabelle (TABELxxx). Quindi se sul sistema è installata una versione di Sme.up antecedente alla V2R1, è necessario innanzitutto adeguare questi files mediante il comando "UP V21".
Mediante tale comando si accede alla lista di tutti i files tabelle (TABELx0F) presenti sul sistema, con indicato il relativo livello di modifica; procedere quindi come segue : 
 - verificare i parametri libreria/file "Sorgenti DDS TABELx0F", che alla prima esecuzione vengono impostati automaticamente con i nomi standard, in modo da indicare al programma di PRE-PTF , dove reperire i membri sorgente dds della nuova versione.
 - individuare quelli appartenenti alla libreria del sistema informativo che si desidera aggiornare, quindi procedere con il relativo aggiornamento mediante l'opzione "U", dalla quale verrà inoltre creata una copia di ciascun file tabelle come TABELx_OL. I files _OL potranno essere poi eliminati mediante l'opzione "4" del programma stesso.

### Release V2R2 o V2R1
Le modifiche al modulo base della V2R3 (B£) hanno comportato modifiche al file di definizione dei campi delle tabelle (TABDC00F), quindi (eventualmente dopo aver eseguito la Pre-ptf indicata precedentemente) è necessaria l'esecuzione di una ulteriore PRE-PTF per poter proseguire.
Per eseguire questo passo di PRE-PTF immettere il comando "CALL B£PTF04" dal quale si accede ad una procedura guidata che consente di effettuare l'allineamento del file in questione. Prima di eseguire l'allineamento (F06) si raccomanda di controllare attentamente la libreria in cui è contenuto il file da fasare (Libreria di appartenenza :  ) e la libreria in cui sono presenti i sorgenti (Libreria sorgenti : ).

## Pre-PTF V4R1
A questo punto eseguire le 2 Pre-PTF specifiche della V4R1 viste nel capitolo precedente e le successive PTF da UP PTF (cominciando tassativametne dalle ££).

# PTF di adeguamento
Occorre a questo punto procedere con la visualizzazione e/o applicazione delle ptf, mediante il consueto comando "UP PTF".
## Nota
Prima di eseguire il comando "UP PTF", si ricorda di adeguare le variabili contenute nella tabella B§V.
Per fare questo è necessario collegarsi con un ambiente con le "nuove" librerie dati, modificando successivamente alcuni elementi della tabella B§V.
Gli elementi da modificare sono :  &LIBDAT, &LIBPER, &SMEDEV, &SMESRC, &SMESTD e &SMEUPOBJ, che dovranno puntare ai nuovi nomi di librerie (quelle della versione V5R1).

## Estrazione nuova SMETAB
A questo punto è necessario estrarre (mediante il comando UP UT3) la nuova SMETAB, in quanto alcune delle PTF che verranno eseguite, richeideranno di effettuare la fasatura di alcune tabelle specifiche.

## UP PTF
E' possibile immettere direttamente la libreria in cui il programma può trovare le ptf da visualizzare (per questioni di prestazione), altrimenti omettendo tale informazione si accede ad un elenco contenente le librerie del sistema dove sono stati riscontrati files di ptf. Scelta la libreria da consultare mediante l'opzione "05", viene visualizzato l'elenco delle ptf in ordine rispettivamente di "Rilascio di Sme.up" decrescente, "Modulo applicativo", "Data emissione". Scelta la ptf da visualizzare mediante l'opzione "05", viene avviato l'interprete batch, dal quale verrà eseguita la consultazione testuale e l'eventuale esecuzione di comandi batch inseriti nel documento.
Le ptf da applicare sono non solo quelle di rilascio V5R1, ma tutte le ptf delle versioni precedenti comprese, a partire dall'ultima data di aggiornamento della SMEUP_DEV in uso sull'installazione corrente.
PTF eseguite : 
(annotare le ptf eseguite per l'adeguamento del sistema informativo, per promemoria)

| 
| .COL Txt="PTF" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" A="L" |
| 
| .COL Txt="Note" LunAut="1" |
|  . | . | . |
|  . | . | . |
|  . | . | . |
|  . | . | . |
|  . | . | . |
|  . | . | . |
|  . | . | . |
| 


Le ultime PTF da eseguire sono quelle generali : 
 :  : DEC T(MB) P(PTF) K(XX99998A)  L(1)
 :  : DEC T(MB) P(PTF) K(XX99999A)  L(1)
 :  : DEC T(MB) P(PTF) K(XX99999B)  L(1)
 :  : DEC T(MB) P(PTF) K(XX99999E)  L(1)
 :  : DEC T(MB) P(PTF) K(XX99999F)  L(1)

# Fasatura definizione tabelle
A questo punto fasare le definizioni di tabella non già allineate da PTF specifiche.
Utilizzare il comando "UP FTB" con "azione di massa" per verificare le definizioni tabelle da aggiornare, e tabella per tabella provvedere all'eventuale aggiornamento alla nuova versione.
Nell'esecuzione della fasatura dei settori (UP FTB), si raccomanda l'utilizzo delle "Opzioni di esclusione", qualora si voglia evitare di ricoprire le impostazioni effettuate sulle proprie definizioni di tabella.

# Restore e installazione di tutti i componenti aggiuntivi
Mediante il comando UP UT3 è possibile eseguire il restore e l'installazione di tutti i componenti e moduli aggiuntivi.
E' quindi possibile restorare il componenti SMENS, SMEDG e SMEPD.

