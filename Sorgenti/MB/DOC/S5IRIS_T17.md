# SVILUPPI


##  Da finire la gestione del calendario di simulazione (Comet)
Adesso ci sono le parti nello script INT asteriscate : 
- la copia del calenadario in un calendario di simulazione
- la copia del calendario di simulazione in quello originale
Il pgm da completare è S5SMES_01C


## Da completare i tipi di sovrapposizione (Cattini)                FATTO
Far riferimento alla documentazione sul server
- percorso (Sviluppo/Schedulazione/BCD - presentazione tecinca)
- pgm da finire :  S5SMES_14. Adesso non fa tutti i qur
E' da fare anche nella schedulazione a capacità infinita ?
Fatto :  documentare.


## Smagrimento alternative (per Cattini)                            FATTO
L'idea è di standardizzare quanto fatto con la tabella CLO per Almenno.
Capire se comprendere quanto fatto per SIL
Attualmente viene  scritto un DSALTE per ogni macchina del centro.
Si assume che le macchine alternative vengano scritte in una risorsa produttiva secondaria della
fase.
Per semplicità farei un pgm successivo che scrive una DS di risp.sec. (vedere come, per velocità)
e taglia le alternative non previste.
Problema :  quando si è in un gruppo, si può spostare una fase su tutte le macchine del centro oppure
solo su quelle previste nelle risp.?  (seconda risposta)
Il problema potrebbe forse non esserci, se il centro ha dei sottoinsiemi di macchine che non si
intrecciano : 
Es :  CDL1 MAC1 - MAC2 - MAC3 - MAC4
Se ci sono gli articoli A1 e A2 che vanno solo su MAC1 e MAC2 e gli articoli A3 e A4 che vanno solo
su MAC3 e MAC4, mi pare che il sistema dovrebbe costruire due gruppi distinti.
Però non si sa se ci sono gruppi distinti (forse mettere un flag sull'impegno per capire se è così)
Appena c'è una transitività nascono i problemi.
In questo caso si deve : 
- controllare che lo spostamento sia valido (solo le macchine permesse)
- presentare / scegliere dove può essere spostato un impegno
Se non ci sono ris.secondarie assume tutte le macchime del centro (va bene ????)
Fatto :  documentare.


## Alternative di ciclo (tema generale :  non c'è nessuna richiesta attiva)
Da standardizzare quanto fatto per la Dischi.
La situazione attuale è la seguente : 
. Il pgm S5SMES01_I scrive il DSIRIS, in cui mette il GRAL se previsto dallo scenario (alternative
multiple).
. Il pgm S5SMES01_K scrive le alternative di risorse specifiche (se previsto nello scenario), e
copia il GRAL dall'IRIS all'ALTE.
Se attive le alternative di ciclo e se XAGRAL non è bianco, lancia S5SMES_01J.
Per ora questo pgm esegue solo i controlli di buon reticolo e segnala gli errori.
Cose da fare : 
. Completare lo 01J con la scrittura dei puntatori del reticolo
. Nel 12 implementare una strategia di miglior fase (clclo preferenzlale se non sfonda ....)
. Nel 13 tagliare i rami secchi (in base alla scelta di un'alternativa) :  si potrebbe farlo sempreo
con una funzione dello 01J (che si specializzerebbe nel reticolo :  costruzione / percorso).
. Grosso problema :  modifica manuale dell'alternativa sul GANTT : 
-- Tecnicamente è una forzatura / congelamento di una attività
-- Si può farla solo sulla radice.
-- Come si evidenziano i rami inattivi sul GANTT ?
-- Eventuali azioni di forzatura e congelamento fatte su rami che diventano inattive vanno perse
-- Problema se si cambia un ramo, NON si schedula globalmente, e si passa ad altro centro che prima
   era attivo, ma dopo le scele fatte diventa disattivo :  le azioni fatte andranno perdute.
-- Alla fine bisogna consolidare quanto scelto (attivare/disattivare le fasi...)


## Scenari dipendenti, ambiti di schedulazione ... (temi di Toora)
Rivedere lo stato dello sviluppo ed eventualmente proseguire se ci sarà interesse (specialmente per
la parte di scenari dipendenti che sembra un po' specifica).
Rivedere gli ambiti (sia in parallelo sia in serie :  questi ultimi serviranno quando ci sono più
utenti di schedulazione su risorse diverse). Ci sono problemi di contemporaneità e di
autorizzazioni. Soprattutto la contemporaneità è critica. Mi pare che potrebbe essere un tema Artex : 
se si modificano insieme due ambiti, cosa succede ?).
Pensare se gli ambiti potranno essere usati per schedulare separatamente gli ordini di livelli
diversi. Occorrerà costruire i legami (di proirità) ma la schedulazione avviene in più passate.
Vedere se è lo standard o una possibilità.


## Accostamento (tema generale)
E' stato fatto qualcosa ma non portato a termine, in quanto non serviva a nessuno.
Rivedere e completare, se servirà davvero. Il pgm da modificare è S5SMES_13.


## Schedulazione operazioni a capacità infinita       FATTO
Completarla.


## Problena holes e saturazione
Ad oggi piazza una hole se successivamente c'è un impegno schedulato. Dopo l'ultimo impegno non piazza altre holes. Questo incide sulla % di saturazione, che è quindi dipendente dal profilo di carico di ogni risorsa. Vedere se questo è giusto, oppure se si dovrà piazzare una hole dall'ultimo impegno fino all'ultima operazione schedulata (makespan).


## Miglioramenti al GANTT
Apertura condizionale di un Gantt completo chiuso (solo un centro) :  come fare ?
Gantt filtrato (da un OAV della risorsa generale) :  per non vedere tutto ma, ad esempio, un reparto.
(vedi punto successivo).

## Presentazione GANTT completo            FATTO
Portare a std il Gantt completo (da mollificio) :  _D3 e _D4.


Manutenzione matrice opzionale (da script :  vedere dopo)  NO
Campi I/O :  Codice Risorsa Forzata (quando si inserise si completa con il tipo, che è il capo del
tipo risorsa specifica dello scenario) e numero forzatura

Sulle operazioni iniziate non ammettere nessuna azione :  per ora trascurerei quanto digitato, senza
nessuna seglanazione, in futuro sarà possibile proteggere i campi di una riga, e quindi ci
attiveremo in tal senso

La azioni ammesse sul Gantt sono :  locali (tramite pop up) e di trascinamento.
Sulla matrice le azioni locali, se possibile, le replicherei :  si apre un popup di cogelamento
on/off e forztura on/off, e si ricongiunge all'elaborazione del popup dal gantt.
Le azioni di trascinamento si ottengono digitando i campi di I/O
Il trattamento dovrebbe ricollegarsi al controllo della finestra richiamata dal G18 in emulazione
  Risorsa Forzata         N.Forzatura
1)      --                     --
2)      --                     Si
3)      Si                     --
4)      Si                     Si

1) Si puliscono entrambi i campi
2) Si mette nella la risorsa forzata la risorsa specifica attuale e si esegue il controllo del
   numero forzatura (non deve essere già presente in un'altra riga della stessa risorsa specifica e
   che sia rispettato l'ordinamento delle fasi dello stesso ordine
3) Si controlla che la risorsa forzata sia valida e appartenga al gruppo della riga (nel caso
   normale al centro di lavoro) e si pulisce il numero forzatura
4) Si eseguono i controlli 3) e del numero di forzatura (non deve essere presente in un'altra riga
   della stesa risorsa forzata e deve essere rispettato l'ordinamento delle fasi dello stesso ordine

Si deve ogni volta riordinare il numero forzatura (con passo 10) vedere se si può riprndere la
parte attuale che la fa.

All'uscita se é stato modificato qualcosa, bisogna far capire che la risorsa generale è stata
modificata, e quindi è necessario rischedulare.


##  Rinuncia
Si potrebbe creare una nuova ds multipla,
all'interno del D4, del n.elementi pari a quello di DSIRIS, con i campi tipo/codice e n.forzatura)
Ad ogni ingresso si memorizzano i valori dell'Iris, e si aggiunge un tasto funzionale di ritorno
nella scheda, dove copiare i dati da questa DS all'IRIS e ripresentare il GANTT/MATRICE
dall'inizio (è forse un problema di chi ascolta)....
Se c'è qualcosa di diverso impostare che la risorsa è stata modificata (mah ..)

In questo modo si ottiene un ritorno all'ultima situazione precedente, non a quella iniziale : 

Esempio : 
lancio D3
lancio D4 sulla macchina M1
--> situazione iniziale A che viene memorizzata
--> modifiche :  sitiazione B
--> ritorno a D3
lancio D4 sempre sulla macchina M1
--> situazione iniziale B che viene memorizzata
--> modifiche :  situazione C
--> se a questo punto si rinuncia si ritorna alla situazione B, non alla situazione A

oops :  c'è già in emulazione, però sono gli iniziali. Vedere se e come coprenderlo in Loocup


##  Riclassifica risorsa    FATTO
Potre impostare (in PAR_SCP) un OAV della risorsa generale che fa da filtro nei GANTT, in modo da
poter visualizzare (aperti o chiusi, in base a quanto impodtato in F17) solo un gruppo di centri.











