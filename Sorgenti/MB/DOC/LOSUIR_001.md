# Obiettivo
Il modulo LOSUIR si pone come obiettivo quello di fornire al tecnico Smeup degli strumenti standard per l'implementazione di funzionalità di "richiesta informazioni all'utente" (User Input Request), necessarie per l'esecuzione di particolari funzioni. Si pongono come esempi queste situazioni : 
* Prima dell'esecuzione di una funzione che comporta l'aggiornamento/cancellazione di dati, la richiesta di una conferma aggiuntiva
* La richiesta di dati filtro per l'esecuzione di una query

# Struttura Tecnica
Le soluzioni proposte dalla modulo LOSUIR si compongono da un insieme di schede SCP_SCH, il cui nome è viene così composto LOSUIR_letteramodalitàgrafica. Quest'ultima parte del codice corrisponde alla lettera indicabile nell'attributo grafico UirMGr dei setup (descritti a seguire).
La dinamica di tali schede è pilotata/monitorata da un unico servizio denominato LOSUIR_SE.

# Utilizzo
Le succitate schede LOSUIR ed il succitato servizio non vengono mai chiamati direttamente. Al tecnico smeup sono forniti in scheda alcuni TAG specifici che permettono di configurare il loro richiamo in modo guidato.

Tali tag identificando in modo preciso le tre forme di User Input Request : 
* UMC :  Richiesta Messaggio di conferma
* UCF :  Richiesta Configurazione
* UPA :  Richiesta Parametri (SV)
* UQR :  Richiesta Query

La prima forma dovrebbe parlare da sé, permette di richiedere all'utente, tramite l'emissione di un messaggio, la conferma di esecuzione di una funzione.
Entrambe le due forme successive, permettono di porre all'utente una serie di domande. La differenzia sostanziale fra le due è che la prima permette di utilizzare una serie di domande maggiormente particolareggiata e strutturata (si possono ad esempio utilizzare delle exit), mentre la seconda è più limitata, ma permette un'implementazione più immediata.
L'ultima forma, è dedicata al lancio di una funzione di query, attraverso essa viene quindi gestita la richiesta e la risoluzione di una specifica query (si veda il modulo B£EQRY).

Per l'utilizzo di tali funzionalità abbiamo quindi a disposizione in scheda i tag.

* G.SUB.Uxx  :  per identificare una subsezione che supporterà le funzionalità sopracitate
* G.SET.Uxx  :  per configurare la richiesta informazioni (a seconda della forma le domande saranno differenti)
* D.FUN.Uxx :  la funzione da eseguire

E' importante notare che nella subsezione Uxx è possibile inoltre specificare i TAG relativi ai dinamismi ed ai setup.
Per la modalità UQR non è inoltre necessario specificare alcuna funzione, in quando verrà automaticamente eseguita la query correlata alla setup della query (cioè F(EXB;LOA10_SE;EQR) cui vengono accodati tutti i parametri di input che arrivano dalla query).

Es.
G.SUB.Uxx
G.SET.Uxx
G.SET.xxx
G.SET.xxx
G.DIN When
D.FUN.Uxx

Per un maggior dettaglio si rimanda alle schede di esempio.

