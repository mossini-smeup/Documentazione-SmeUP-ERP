Nel seguente documento verrà esposta l'architettura generale della programmazione Sme.UP.
Tale documento è indispensabile sia per chi sviluppa Sme.UP che per chi scrive programmi personali o personalizzati.

Non seguire le indicazione inserite in questo documento può portare a problemi nel funzionamento o a comportamenti imprevisti.

Nella release V3R1 di Sme.UP è stata fatta una profonda revisione dell'architettura, sopratutto per quanto concerne l'uso dei gruppi di attivazione. E' molto importante quindi leggere con attenzione queste indicazioni.

# Linee guida della struttura dei programmi
Con la V3R1 è stato consolidato il disegno architetturale della programmazione Sme.UP.

Queste sono le linee guida che sono state seguite : 
- Nessun programma deve essere eseguito nel gruppo di attivazione di default (comunemente chiamato DAG - Default Active Group)
- I programmi con gruppo di attivazione *NEW lo sono per scelta e non bisogna abusarne
- Gli RCLACTGRP vanno fatti in modo mirato e specifico, non va mai fatto un RCLACTGRP ACTGRP(*ELIGIBLE) (se non al cambio ambiente)
- Va garantita la certezza che al cambio ambiente tutti i file precedentemente aperti vengano chiusi
- Esistono gruppi di attivazione che non si chiudono mai (se non al cambio ambiente) e altri che invece possono essere chiusi
- I programmi che si "chiudono in RT" devono essere tali. Ossia devono essere in grado di gestire la non esecuzione della £INIZI senza basarsi ad esempio sul fatto che essi siano richiamati da un programma che si "chiude in LR".
- Gli override che vengono impostati hanno normalmente lo scope di "livello di chiamata". I casi in cui hanno validità nel gruppo di attivazione sono le eccezioni
- Gli attributi di job riguardanti la localizzazione (ad esempio il separatore decimale) devono essere corretti "a livello di job", altrimenti tutti i comandi o le bif che si basano su questi valori (come il %EDITC) danno risultati non corretti
- Se gli errori vengono intercettati, vanno gestiti nello specifico. Non viene utilizzata nessuna struttura "generalizzata" di intercettazione degli errori
- E' necessario essere indipendenti dai default di sistema dei comandi

L'adozione di queste linee guida ha portato ad alcuni cambiamenti importanti nello stile di programmazione da adottare.

# Gruppi di attivazione e impostazioni di localizzazione linguistica
Con la V3R1 è stato consolidato il disegno dell'uso dei gruppi di attivazione.
I programmi Sme.UP di default vengono compilati con gruppo di attivazione *CALLER. Quindi per non essere eseguiti MAI nel gruppo di attivazione di default, nella lista richiami deve essere sempre presente "in testa" un programma che viene eseguito in un gruppo di attivazione non default.
Inoltre, come detto, i job devono avere impostati correttamente i valori relativi alla localizzazione.
Quindi tutti i job in cui vengono eseguiti "programmi Sme.up" devo avere un programma di partenza particolare. Questo programma ha essenzialmente due compiti :  "impostare" il gruppo di attivazione non default e impostare gli attributi di localizzazione corretti.

Per quanto riguarda la parte interattiva non c'è nessun problema, in quanto il B£QQ50 e gli altri programmi collegati si occupano di queste impostazioni.
Discorso analogo per Looc.UP.
Anche la sottomissione in batch tramite £GPE effettua tutte le inizializzazioni in modo corretto (l'esecuzione "interattiva" della £GPE esegue comunque il comando in un gruppo di attivazione *NEW).
Quali situazioni rimangono da controllare?
- SBMJOB
- Azioni eseguite non tramite menù Sme.UP (ad esempio perché lanciate da modulo base)
- Lavori schedulati

Per risolvere tutte queste situazioni è stato creato un comando, il B£QQ02, che si occupa di eseguire tutte le impostazioni richieste e poi di eseguire il comando che gli viene passato in input.
Per i lavori schedulati c'è anche la possibilità (per altro consigliata) di utilizzare il programma B£QQ01 che oltre ad eseguire le impostazioni richieste, consente anche di eseguire il lavoro con una lista librerie particolare.
Nel seguito del documento verrà approfondito l'argomento e risulterà quindi chiara l'estrema importanza del fatto che tutti i programmi/comandi Sme.UP che vengono sottomessi da un qualunque job (sia Sme.UP che no) od eseguiti da un job Non-Sme.UP debbano essere eseguiti "tramite" il B£QQ02.


# Gestione degli errori
La filosofia seguita è "se non so precisamente come gestire un errore, meglio non gestirlo del tutto".
Questo significa che la tecnica di monitorare con indicatori (o con costrutto MONITOR-ENDMON) le CALL o le operazioni sui file vanno fatte solo se poi si è in grado di gestire correttamente l'errore.
Monitorare un'operazione su un file o la CALL di un programma implica due possibili scenari : 
- per ogni errore monitorato so quale azione correttiva intraprendere
- l'operazione monitorata è "facoltativa", la sua esecuzione non è vincolante

La seconda possibilità è decisamente remota... se faccio qualcosa è perché mi interessa farlo.
Quindi l'unica possibilità è che si sappia con precisione cosa fare al verificarsi di un determinato errore.

L'indicatore come strumento di monitor è sempre sconsigliato, perché monitora qualunque tipo di errore. Il costrutto MONITOR-ENDMON è più flessibile perché consente di monitorare solo alcuni errori.

Monitorare una CALL con un indicatore ad esempio è sconsigliatissimo, perché QUALUNQUE errore possa presentarsi nel programma richiamato, viene "nascosto" da questo indicatore.
Spesso l'indicatore sulle CALL viene messo come "controllo di programma inesistente". Il problema è che se il programma esiste e va in errore, viene trattato alla stessa stregua di programma inesistente.
In questo caso la soluzione migliore è usare il costrutto MONITOR ed andare a gestire l'errore "programma non trovato", lasciando non gestito ogni altro errore.
Per gestire situazioni come questa, è consigliato l'uso della parola chiave £MON nei commenti, per il cui utilizzo di rimanda alla documentazione specifica.

a standard la gestione "generalizzata" degli errori è stata eliminata., Nello specifico : 
- è stata eliminata la *PSSR dalla £INIZI
- è stato eliminato l'indicatore dalla CALL delle /COPY
- è stato eliminato l'indicatore dalle CALL delle exit sostituendo con "£MON" per il controllo delle exit inesistenti

La *PSSR può essere reintrodotta nei programmi in cui la si vuole esplicitamente. Per farlo è necessario definire a inizio programma la direttiva
/DEFINE SI_PSSR

Inoltre l'indicatore sulle /COPY può essere "reintrodotto" semplicemente andando ad agire sul flag ££B£2J della tabella B£2.
In realtà nella /COPY c'è una struttura tipo : 
IF        ££B£2J = '1'
CALL      'XXXXXX'                             37
ELSE
CALL      'XXXXXX'
ENDIF


# Attenzioni di programmazione
Per poter restare all'interno delle linee guida precedentemente citate è necessario, in fase di programmazione,  seguire alcuni accorgimenti.

## Gruppi di attivazione non default
Il fatto che tutti i programmi Sme.UP vengono eseguiti in un gruppo di attivazione diverso da quello default, porta alcuni cambiamenti (rispetto al passato) nell'esecuzione del programma stesso.
Tali differenze vanno tenute in considerazione per scrivere un programma corretto.
Le differenze riguardano : 
- Scope di Override
- Chiusura programmi in LR/RT
- RCLRSC

### Scope di override
I comandi OVRDBF, OVRPRTF e DLTOVR hanno un comportamento di default diverso, per quanto riguarda il loro ambito di attivazione, a seconda che vengano eseguiti nel gruppo di attvazione
Il parametro che guida questo comportamento è OVRSCOPE per i comandi OVRDBF e OVRPRTF e il parametro LVL per il comando DLTOVR.
Il valore di default è sempre *DFTACTGRP, che fa assumere il seguente comportamento : 
Comandi OVRDBF e OVRPRTF
- se eseguito nel gruppo di default, coincide con il valore *CALLLVL, vale a dire che il suo ambito di applicazione è il livello di chiamata del programma in cui è eseguito. Il suo effetto termina alla fine di questo programma (sia in LR sia in RT)
- se eseguito in un altro gruppo, il suo ambito di applicazione è l'intero gruppo :  il suo effetto termina alla chiusura del gruppo.
Comando DLTOVR
- se eseguito nel gruppo di default, coincide con il valore '*', vale a dire che vengono eliminate le override aperte dal livello di chiamata in cui eseguito in poi.
- se eseguito in un altro gruppo, vengono eliminate TUTTE le override eseguite in precedenza nello stesso gruppo di attivazione  (comprese quelle eseguite in programmi chiamanti).

Nelle linee guida abbiamo detto che gli override hanno normalmente lo scope di "livello di chiamata". Quindi __normalmente sarà necessario impostare  OVRSCOPE(*CALLLVL) per i comandi OVRDBF e OVRPRTF e LVL(*) per DLTOVR. A meno che non si voglia specificamente uno scope diverso (gruppo di attivazione o job).
Le /COPY £OVR e £DOV utilizzano già tali valori come default.
Anche per questo motivo, nei programmi RPG non deve mai essere esguito il comando di OVRDBF direttamente ma bisogna __sempre utilizzare la /COPY £OVR__ (e analogamente DLTOVR - £DOV).

### RCLRSC
L'RCLRSC invocato da un programma eseguito in un gruppo di attivazione non default è inefficace.
Non effettua la chiusura di nessun file e di nessun programma.
Per questo motivo __il comando RCLRSC non ha ragione di essere utilizzato__.

### LR/RT
Dato che il comando RCLRSC nella nuova "struttura" è inefficace, è stato tolto dalla £INZSR.
Di conseguenza __quando un programma si chiude in LR, non effettua la chiusura dei programmi da esso richiamati e che avevano una chiusura in RT.
Questa che sembrerebbe una limitazione in realtà è un "pulizia" dei programmi. Infatti in questo modo un programma che si chiude in RT resta "aperto" fino a quando non si chiude il gruppo di attivazione" in cui sta girando, indipendentemente da quale programma l'ha richiamato.
E' quindi di fondamentale importanza considerare questo fatto.
Chiariamo la situazione con un esempio : 
Il programma A (LR) richiama il programma B (RT). Entrambi sono nello stesso gruppo di attivazione.
Al primo richiamo del programma A (che poi richiamerà B), entrambi i programmi passeranno dalla loro £INIZI, quindi entrambi effettueranno l'operazione di IN della LDA (inclusa nella £INZSR).
Alla chiusura di A, esso effettuerà la OUT (inclusa anch'essa nella £INZSR) e chiuderà i file da esso aperti.
Al secondo di chiamo del programma A, esso ripasserà dalla £INIZI e ripeterà l'operazione di OUT. Il secondo richiamo del programma B invece non ripasserà dalla £INIZI e non comporterà l'operazione di IN.
Nella precedente struttura dei programmi Sme.UP (Pre V3R1), la chiusura del programma A avrebbe causato l'invocazione del comando RCLRSC che avrebbe causato la chiusura ANCHE del programma B. Anche il secondo richiamo di B avrebbe quindi comportato il passaggio presso la £INIZI e l'esecuzione del comando IN.
Bisogna precisare che questo comportamento non era "certo". Infatti c'erano in gioco altre variabili come la possibilità che altri programmi (C) chiamassero a loro volta B. Questo è uno dei motivi per cui questo tipo di struttura non era considerata "solida".

## Uso di RCLACTGRP
Come indicato nelle linee guida, esistono gruppi di attivazione che non si chiudono mai (se non al cambio ambiente) e altri che invece possono essere chiusi.
Per mantenere valida questa impostazione ovviamente è imperativo che __nessun programma esegua il comando RCLACTGRP ACTGRP(*ELIGIBLE).
L'utilizzo di tale comando è comunque sconsigliatissimo in ogni manuale o forum che si rispetti.
Attualmente l'unico gruppo di attivazione che non si chiude mai è il SM_ENDLESS.

## Menù e gruppi di attivazione
Tutte le azioni richieste da menù vengono eseguite in un nuovo gruppo di attivazione. questo per consentire il recupero della memoria utilizzata una volta tornati a menù.

## Riga di comando
Come detto le azioni invocate da riga di comando vengono eseguite in un nuovo gruppo di attivazione.
Per ottenere da riga di comando lo stesso "effetto" è necessario che anche le "azioni" richiamate da essa, vengano eseguite in un nuovo gruppo di attivazione. Di questa operazione si occupano tutti i comandi Sme.UP invocabili (UP, T, C ecc.).
Ovviamente non è possibile effettuare questa operazione sul comando CALL.
E' quindi necessario che __le "call" da riga comando vengano effettuate tramite il comando C e non CALL.

## Cambio ambiente
La nuova struttura di Sme.UP, come detto, è stata pensata (tra l'altro) per garantire un corretto cambio ambiente.
Per poter garantire questo comportamento è necessario rispettare alcune regole.
Innanzitutto non è possibile effettuare un cambio ambiente "run time". __Non è possibile cioè in un programma effettuare una cambio lista librerie.
Questo perché la probabilità che alcuni file restino "aperti" nel precedente ambiente (quindi puntino ad un libreria non in lista) è troppo alta. L'unico modo per essere sicuri che questo cambio ambiente sia "sicuro" (ossia tutti i file vengano chiusi) è quello di tornare a menù e scegliere un ambiente differente.

### Esecuzione "comandi" in un diverso sistema informativo
Vista l'impossibilità di effettuare un cambio ambiente in un programma, è stato creato un comando apposito (B£QQ01) che __consente di sottomettere un comando con una lista librerie diversa da quella del job sottomettente. Tale sottomissione può essere bloccante o meno. Se è bloccante, il job lanciante resta in attesa del completamento, altrimenti prosegue normalmente.
Questi sono i parametri che è possibile specificare nel comando : 
* B£B£B :  B£B da utilizzare (parametro obbligatorio)
* B£CMD :  comando da eseguire (parametro obbligatorio)
* B£JOBQ :  JOBQ in cui eseguire il comando. Se tale campo viene lasciato blank, l'esecuzione del comando diventa bloccante, ossia il programma che esegue il comando B£QQ01 attende che il comando termini prima di proseguire.
* B£MSGQ :  MSGQ del lavoro
* B£JOB :  Nome JOB
* B£USER :  Utente di esecuzione del comando
Tale comando ha attualmente alcune limitazioni : 
* non consente di ricevere una risposta dal comando eseguito
* non consente di eseguire operazioni "interattive" all'interno del comando eseguito (essendo eseguito appunto in un lavoro batch)

### Gestione ambienti non Sme.UP e lavori sottomessi
Un discorso analogo va fatto per i comandi (e i programmi) sottomessi o eseguiti da ambienti non Sme.UP (come ad esempio i moduli base non Sme.UP - ACG, Gruppo Pro ecc. -).
Tali comandi, come detto precedentemente, __devono essere "incapsulati" nel comando B£QQ02__.
Il comando B£QQ02 esegue tutte le impostazioni necessarie (gruppi di attivazione, B£1, B£2, impostazioni di localizzazione ecc.) e successivamente esegue il comando indicato.
Quindi non sarà consentito effettuare l'operazione
SBMJOB CMD(CALL PGM(XXX))
la quale andrà sostituita con : 
SBMJOB CMD(B£QQ02 B£CMD(CALL PGM(XXX)))
Identico discorso per azioni eseguite ad esempio da modulo base ACG. Comandi e CALL dovranno puntare sempre al comando B£QQ02.

# Indipendenza dai valori di sistema
L'esecuzione di Sme.UP dovrebbe essere il più possibile indipendente dai valori di default impostati per i comandi (almeno alcuni).
In questo modo si lascia piena libertà agli amministratori del sistema di impostare i valori che preferiscono. Inoltre preveniamo possibili malfunzionamenti dovuti al cambio dei default stessi da parte di altri tool.
## SQL
In quest'ottica di indipendenza sono state create le /COPY £INIZSQ1 e £INIZSQ2.
Tali /COPY impostano i parametri di compilazione dei programmi SQLRPGLE in cui sono inserite disinteressandosi di quanto impostato come default di sistema.

# Alcuni "comportamenti" errati
## Gruppo di attivazione *NEW
Erroneamente si pensa che l'esecuzione di un comando (o un programma) in un gruppo di attivazione *NEW significhi aprire un "ramo" isolato e indipendente da quanto è stato eseguito precedentemente.
Questo non è vero, infatti eventuali programmi eseguiti all'interno di questo "ramo" che non sono stati compilati con Gruppo di Attivazione *CALLER potrebbero essere già stati aperti e quindi essere già inizializzati.

# Adeguamenti programmi pre V3R1
I programmi scritti prima della V3R1 (e che quindi non beneficiavano di questa nuova architettura) devono essere adeguati per evitare comportamenti dannosi od errati.
I programmi standard sono ovviamente stati adeguati. Per quanto riguarda quelli personali si rimanda alla PTF
 :  : DEC T(MB) P(PTF) K(B£01027A)
