# B£5 - Personalizzazione
 :  : DEC T(ST) K(B£5)
Attraverso questa tabella è possibile definire i parametri di gestione del sistema, per quanto riguarda le seguenti parti principali : 
- exit durante la sottomissione di lavori batch
- parametrizzazione dell'attività di chiusura di sistema.
In particolare, la parte di parametrizzazione dell'attività di chiusura di sistema è basata sul fatto che l'attivazione viene effettuata mediante la personalizzazione del programma di sistema**QSYS/QEZPWROFFP**, operazione che si effettua compilando il sorgente**B£PWR01CL**come oggetto**QSYS/QEZPWROFFP**(sostituendo quello di sistema). Il sorgente B£PWR01CL viene fornito come prototipo nel file sorgente SMEUTI.
Il programma viene lanciato automaticamente dalla gestione attività di accensione/spegnimento negli orari impostati mediante il menu di sistema**POWER**(GO POWER).
Questo programma sottomette il processo di chiusura del sistema, eseguendo una SBMJOB parametrizzata mediante una jobd di nome fisso**B£PWRJD**che deve essere creata nella libreria**SMESYS**(definisce la lista di librerie che il job di chiusura deve utilizzare, mediante la quale deve di base indirizzare il file tabelle TABELQ0F e la libreria degli oggetti
Sme.Up).
**N.B.**la SBMJOB viene sottomessa dall'utente QSYSOPR. Quindi tale utente deve essere autorizzato all'utilizzo dell'utente impostato nella SBMJOB. Si consiglia perciò di impostare QSYSOPR come utente di esecuzione del job sottomesso.
L'utente finale di esecuzione del job deve inoltre essere autorizzato all'utilizzo del comando PWRDWNSYS.
Qualora, per un qualsiasi motivo, si intendesse ripristinare il funzionamento di default del sistema operativo (ovvero
riposizionare il programma QEZPWROFFP), è sufficiente scrivere un membro sorgente CLP da compilare come QSYS/QEZPRWOFFP con le seguenti 3 specifiche : 
     PGM
     PWRDWNSYS OPTION(*IMMED)
     ENDPGM
## CONTENUTO DEI CAMPI
 :  : FLD T$B£5A **Suff. pgm Exit £GPE**
Se impostato induce il richiamo del programma B£CSJ1_x ad ogni sottomissione di job batch, eseguito mediante la routine £GPE.
Mediante tale programma è possibile gestire la traccia dei lavori sottomessi in batch.
Il programma, se presente, viene richiamato in tre istanze : 
>    all'esecuzione della SBMJOB del lavoro batch (esecuzione £GPE)
>    all'inizio dell'esecuzione del lavoro batch
>    al termine dell'esecuzione del lavoro batch.
Al programma viene passato un insieme di campi che definisce i parametri ambientali del job (nome, utente, numero, ecc.).
 :  : FLD T$B£5B **Programma di chiusura sistema**
Se specificato, è il programma che verrà eseguito durante l'attività di _7_Chiusura di sistema, prima di completare le attività di chiusura/riavvio, come definite nel campo _7_Azione chiusura(T$B£5D).
Riferirsi al testo di aiuto del campo _7_Azione di chiusura per le istruzioni operative per attivare la gestione della**Chiusura di sistema**.
 :  : FLD T$B£5C **Libreria programma di chiusura sistema**
Se specificato il campo precedente__Programma di chiusura sistema__(T$B£5B), è possibile indicare in questo campo la libreria dove risiede il programma.
Per questo campo è ammesso anche il valore *LIBL, che è il valore assunto.
 :  : FLD T$B£5D **Azione di chiusura**
Costituisce l'azione che viene intrapresa al termine delle attività di**Chiusura di sistema**.
Può assumere i seguenti valori : 
_7_' 'nessuna azione viene intrapresa :  al termine delle attività di chiusura, il sistema è immediatamente disponibile
_7_'1'spegnimento sistema :  al termine delle attività di chiusura, il sistema viene spento mediante il comando PWRDWNSYS OPTION(*IMMED)
_7_'2'riavvio sistema :  al termine delle attività di chiusura, il sistema viene spento e immediatamente riavviato mediante il comando PWRDWNSYS OPTION(*IMMED) RESTART(*YES)
 :  : FLD T$B£5E **Salvataggi via O.S.**
Se selezionato, durante le attività di**Chiusura di sistema**, vengono eseguiti i salvataggi di sistema via **Supporto Operativo**, così come definiti dal menu__BACKUP**di sistema.
Attraverso tale opzione si può sincronizzare in maniera sequenziale l'esecuzione dei salvataggi di sistema, quindi una volta terminati questi ultimi, l'esecuzione dell'azione di chiusura, così come descritta nel campo**T$B£5C** di questa tabella.
 :  : FLD T$B£5F **Menù ad Albero**
Se impostato, il programma di gestione dei menù (B£MENU) esegue, in emissione, un raggruppamento dei livelli di titoli (ad albero). La scelta influenza tutti gli utenti, che però possono abilitare e/o disabilitare singolarmente la funzione tramite le impostazioni di programma.
 :  : FLD T$B£5G **Pgm di Supp.Compil
Se impostato, il programma di compilazione oggetti SMEUP (opzione CO programma B£UT13A) lancia il programma di exit B£UT13A_U (nome fisso) che consenti di effettuare delle operazioni sugli oggetti appena compilati. Viene lanciato in quattro momenti (PRE e POST compilazione e PRE e POST azioni utente impostate nel sorgente in compilazione PRP* e POP).
Vedi esempio di programma nei sorgenti standard.
 :  : FLD T$B£5H **Log Attività Utenti**
Inserendo il valore '1' si attiva la gestione dei log delle attività utente. Il log, gestito nel file dei Log (JALOGT0F), registra tutte le azioni svolte dagli utenti tramite i menu standard di SMEUP e di LOOCUP.
 :  : FLD T$B£5I **Compil pgm in lingua**
Mediante questo campo è possibile decidere se compilare i pgm con il supporto per le lingue o meno.
Inserendo BLANK vengono compilati con il supporto per le lingue solo i pgm in librerie standard.
Come librerie standard si intendono la &SMEDEV, la &SMESRC, la &SMETST e la &SMEUPOBJ (tab. B§V)
Inserendo 'N' nessun pgm viene compilato con il supporto per le lingue
Inserendo 'A' tutti i pgm vengono compilati con il supporto per le lingue
Inserendo 'P' vengono compilati con il supporto per le lingue tutti i programmi in librerie standard
e quelli nella libreria di personalizzazione (&LIBPER della tabella B§V).
 :  : FLD T$B£5J **Controllo Costanti pgm**
Attiva il controllo dell'utilizzo delle costanti nei pgm.
 :  : FLD T$B£5K **Attivazione Aggiornamento Modello Dinamico in Compilazione Pgm**
Se attivato in compilazione verrà automaticamente eseguito l'aggiornamento del modello dinamico relativo ai pgm.
 :  : FLD T$B£5M **Attivazione log £GPE**
Mediante questo campo è possibile attivare il log (su JALOGT0F) di tutte le sottomissioni batch effettuate tramite £GPE.
Solo i programmi esplicitamente esclusi (tramite flag in tabella PGM) non verranno tracciati.
 :  : FLD T$B£5N **Suff. oggetto £GPE**
Se impostato induce il richiamo del programma B£GPE2_x ad ogni richiesta di sottomissione del job batch eseguita mediante la routine £GPE.
Lo scopo è di indurre una nuova risalita per identificare meglio gli attributi del job stesso.
Attivando la gestione verrà richiesta l'obbligatorietà del nuovo oggetto e sarà compito del programma B£GPE2_x ritornale l'oggetto da utilizzare nelle risalite della £GPE.
 :  : FLD T$B£5P **SV-Att Setup default**
Se impostato non verranno più inviati a Looc.UP, insieme all'XML della scheda, i setup utenti.
Questa attivazione va impostata solo se è stata attivata la nuova gestione dei SETUP.
 :  : FLD T$B£5O **Specifiche di precompilatzione**
In alcuni ambiti, per poter rendere grafiche le applicazioni 5250, è stato necessario aggiungere
alcune specificità di conversione del sorgente.
Visto l'impatto minimale delle stesse si è scelto di includerle nello standard anche se appartenenti
ad applicativi esterni.
**01**STAR
Modifica il comportamento standard per adeguarsi all'applicativo STAR
**02**SIGLAM
Modifica il comportamento standard per adeguarsi all'applicativo SIGLAM
 :  : FLD T$B£5Q**Attiva funzioni AOP**
Impostando questo flag si attiverà, durante la generazione delle stampe, la possibilità di indirizzare l'output verso il server AOP. Naturalmente la stampa deve essere stata integrata con le funzioni AOP e predisposta l'infrastruttura.
