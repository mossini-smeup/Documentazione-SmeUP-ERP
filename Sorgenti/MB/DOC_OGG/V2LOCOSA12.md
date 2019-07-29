## Obiettivo
Gestire dell'insieme di azioni che definiscono un menù e del loro utilizzo.

## Utilizzo
I menù definiti tramite il LOA12 possono essere chiamati in modo esplicito (eseguendo una F che fa riferimento ad una sottoscheda del LOA12), ma vengono anche automaticamente utilizzati come schede dell'istanza degli oggetti di smeup a partire dal momento in cui viene definito lo script di menù corrispondente alla risalita prevista per quell'istanza (si veda quanto riportato di seguito al titolo "Costruzione della Funzione di Esecuzione").

Quindi dal momento in cui creo lo script interessato richiamando la funzione della scheda di un oggetto, non verrà più presentato lo script della scheda che vi corrispondeva ma lo script del LOA12 contenente le voci di menù corrispondenti.

Questo meccanismo può essere disattivato intervenendo sulla scheda B§K di impostazione di loocup. Per essa sono previsti due sottosettori : 
* £O :  in cui posso specificare le impostazioni per tipo+parametro di una classe e/o per il solo tipo
* £M :  in cui posso specificare le impostazioni per una istanza di modulo (TAB£AMO) o di applicazione (TAB£A)

## Definizione
Le voci del menù sono documentate nel manuale applicativo dell'Hypermenu.
- [Menù di Accesso Utente](Sorgenti/MB/DOC/B£MENU_02)
Per la codifica dei menù, oltre alle regole definite dal wizard vanno applicate le seguenti considerazioni
* Ad ogni voce di menù deve corrispondere un codice univoco all'interno dello script
* All'interno di tale codice il carattere "." definisce un nuovo livello all'interno dell'albero
* All'interno di ogni livello il carattere che definizione il livello deve essere univoco per quel livello
Per la definzione di tali livello è necessario l'utilizzo dell'inclusione di alcuni script "O.x" ed "M.x" (vedasi script "O_" e "O_TAB£AMO").

### Costruzione della Funzione di Esecuzione
Se viene passato il solo oggetto 1 tramite la logica riportata di seguito viene determinato lo script che individua il menù della azioni specifiche di tale oggetto.
Alla scheda è comunque possibile passare tutti i parametri che potrebbero essere poi necessari all'esecuzione delle azioni.
La logica di risalita di individuazione del menù è la seguente : 
* TAB£A :  A_ + Codice. In assenza dello script corrispondente risale viene utilizzato lo script O_TAB£A
* TAB£AMO :  M_ + Codice. In assenza dello script corrispondente risale viene utilizzato lo script O_TAB£AMO
* MB :  S_ + Parametro. In assenza dello script corrispondente risale viene utilizzato lo script O_MB
* VD :  V_ + Codice. In assenza dello script corrispondente risale viene utilizzato lo script O_ + Tipo Parametro
* OG :  O_OG + Codice.
* ID :  I_ + Parametro. Inoltre in questo caso viene effettuato anche un controllo per l'esistenza di un membro per I_ è il primo carattere del parametro (per l'indirizzamento di viste particolari).
* J1 :  Tipo + Parametr
* OJ*USRPRF :  O_OJ_USR
Per tutto il resto viene ripreso lo script che corrisponde a O_ + tipo oggetto + parametro oggetto.
In assenza di tale script viene ricercato quello corrispondente a O_ + tipo oggetto e in sua assenza allo script generico O_ .

## Modalità di richiamo
Se è stato creato lo script di menù di un oggetto, secondo le regole riportate di seguito, la scheda dell'oggetto viene automaticamente deviata sul richiamo della scheda LOA12 dell'oggetto, purchè non siano passati parametri aggiuntivi alla scheda.

La scheda LOA12 non ha una sezione scheda principale è costituita solo da sottoschede, per cui la relativa sottoscheda va sempre specificata.
Le sottoschede previste sono : 
* EXE :  ho due sezioni, il menù e la scheda di esecuzione. Nella scheda del menù ho la possibilità di modificare l'oggetto 1. Tutte le schede seguenti presuppongono il passaggio dell'oggetto che non è poi modificabile in scheda. Cambiano solo i componenti grafici impiegati.
* EXE_OG :  ho due sezioni, il menù ad albero a sinitra e la scheda di esecuzione a destra.
* ACP :  Il menù viene scelto tramite un campo di autocomplete in alto e la funzione di scheda viene eseguita in sezione. Solo per ambiente no loocup.
* BOL :  Il menù viene scelto tramite Boxlist a sinistra e la funzione di esecuzione a destra. NOTA BENE :  viene presentato solo il primo livello del menù. Se si sceglie una voce che prevede sottovoci viene lanciata una scheda in cui mi verrà presentata la scelta delle voci dei livelli successivi. Solo per ambiente no loocup.
* BOU :  A differenza della precedente tutta la scheda è occupata dalle voci del menù in boxlist. La funzione corrispondente verrà eseguita in una nuova finestra. Solo per ambiente no loocup.
* BTM :  Il menù viene scelto tramite bottoniera in alto. La funzione di esecuzione viene eseguita in scheda nella sezione sotto. Anche per questa forma vale quanto detto per il filtro del primo livello sulla BOL. Solo per ambiente no loocup.
* BTO :  La scheda in questo caso si riduce solo ad un bottone che permette di richiamare la scheda con il menù.
* CMB :  Del tutto simile alla scheda ACP, cambia solo il componente grafico impiegato.
* EXT :  Simile alla scheda EXE_OG si differenzia per il fatto che viene applicata la funzionalità tecnica che permette di avere l'albero definito in modo esterno. Solo per ambiente no loocup.
* HTR :  Il menù viene scelto tramite un albero esploso in modalità orizzontale. La funzione viene eseguita al click su un nodo, in una nuova finestra. Solo per ambiente no loocup.
* IML :  Il menù viene scelto tramite Image List a sinistra e la funzione di esecuzione a destra. NOTA BENE :  viene presentato solo il primo livello del menù. Se si sceglie una voce che prevede sottovoci viene lanciata una scheda in cui mi verrà presentata la scelta delle voci dei livelli successivi. Solo per ambiente no loocup.
* IMU :  Il menù viene scelto tramite Image List a sinistra e la funzione di esecuzione in alto. Come per la voce precedente il menù viene presentato filtrato per il primo livello.
* MIN :  Il menù viene scelto tramite il componente mind map. La funzione viene eseguita al click su un nodo, in una nuova finestra. Solo per ambiente no loocup.
* OGN :  Il menù viene scelto tramite il componente organigramma. La funzione viene eseguita al click su un nodo, in una nuova finestra. Solo per ambiente no loocup.
* RAD :  Il menù viene scelto tramite bottoniera in alto. La funzione di esecuzione viene eseguita in scheda nella sezione sotto. Anche per questa forma vale quanto detto per il filtro del primo livello sulla BOL. Solo per ambiente no loocup.
* TRE :  Del tutto simile alla versione ACP, cambia solo il componente di scelta della voce da eseguire.

### Parametri P
* MN :  Script di menù
* PRF :  "1" attiva la gestione dei preferiti
* NM :  "1" disattiva le voci di utility che vengono aggiunte in fondo al menù
* NTI :  "1" disattiva i titoli
* NLV :  "1" disattiva i livelli (vengono indentate le descrizioni), "*First" ritorna solo 1° livello
* GRU :  filtro per attributo "gruppo" delle azioni di menù
* ElAzi :  Separato da ";" permette di passare un elenco di voci di menù che saranno le uniche presentate nella risoluzione della funzione.
* MNU :  Filtro per prefisso del codice delle voci di menù
* FUN :  filtra per titolo una sezione del menù (es. se passo G, ritorna tutta le voci sotto il titolo con codice G)
* PFX :  filtra per prefisso le voci di menù
* LIS :  filtra le voci di menù, in base al fatto che la voce appartenza al codice lista (lista di ME) indicato in questo parametro.
* FST :  filtro delle voci di menù in base al contenuto di codice e descrizione
* CAC :  "Yes" Attiva la Cache del menù
* Dbg :  "1" attiva modalità debug
* SWI :  richiamo per risoluzione swipe. Il campo può valere : 
** K :  per risolvere lo swipe di classe
** F :  per risolvere lo swipe delle colonne fisse
** Se diverso da bianco per risolvere lo swipe a caricamento dinamico
* DOOG :  Tipo oggetto origine della voce di menù
* CDOG :  Codice oggetto origine
* ST :  Settore della B£H
* SK :  Da documentare
* CATE :  Da documentare
* VAT :  Da documentare
* LV :  Da documentare
* HL :  Attiva il richiamo dell'help al mio livello del menù

### Parametri INPUT
* TIT :  Forza il titolo del menù
* PMK :  Codice oggetto del parametro di un modulo parametrato
* PMT :  Tipo oggetto del parametro di un modulo parametrato
* PMP :  Parametro oggetto del parametro di un modulo parametrato
* Rot :  Da documentare
* Col :  Da documentare
* ShowInput :  Da documentare
* POP :  Da documentare
* AZI :  Solo per la funzione ESE.AZI permette di identificare l'azione da lanciare. Se valorizzato ad "*First" esegue la prima azione del menù.

### Variabili Aggiuntive
Oltre alle variabili disponibili per qualsiasi scheda sono inoltre state predisposte alcune variabili contestuali : 
* &CO.TO :  tipo oggetto di riferimento (vengono presi i primi due caratteri, se tipo oggetto OG, viene dal codice oggetto 1, se tipo oggetto LI/Qn dal parametro oggetto 1, in tutti gli altri dal tipo oggetto 1)
* &CO.PA :  parametro oggetto di riferimento  (se tipo oggetto OG, vengono presi i caratteri dal 3° del codice oggetto 1, se tipo oggetto LI/Qn dal parametro oggetto 1, in tutti gli altri vengono presi i caratteri dal 3° dal tipo oggetto 1)
* &CO.OG :  tipo oggetto completo di riferimento  (se tipo oggetto OG, viene preso dal codice oggetto 1, se tipo oggetto LI/Qn dal parametro oggetto 1, in tutti gli altri dal tipo oggetto 1)
* &CO.MB :  membro del menù
* &CO.DC :  descrizione della classe
* &CO.DP :  descrizione della parametro della classe
* &CO.CRU :  funzione cruscotto
* &CO.LOAP :  se previsto un ciclo nel menù è il codice dell'oggetto della scansione del menù.
* &CO.LOA2 :  se previsto un ciclo nel menù è la sottostringa dei primi due caratteri del codice dell'oggetto
* &CO.LOA3 :  se previsto un ciclo nel menù è la sottostringa a partire dal terzo carattere del codice dell'oggetto
* &CO.LOSI :  se previsto un ciclo nel menù è la descrizione dell'oggetto della scansione del menù.

Se l'oggetto di riferimento è un modulo, vengono inoltre create le variabili : 
* &CO.APMO :  applicazione del modulo
* &CO.MOBA :  in riferimento ai moduli naturati identifica il modulo di riferimento base dato dai primi sei caratteri del modulo
* &CO.NTMO :  in riferimento ai moduli naturati identifica la natura del modulo
* &CO.PMK :  se è un modulo che prevede il parametro (es. la BRR per il BRRISO), il parametro di riferimento è memorizzato anche in questa variabile, che viene tipizzata. Tramite essa è quindi possibile sfruttare gli attributi di tale riferimento (es. nel caso BRRISO se voglio utilizzare la natura della risorsa posso scrivere la variabile &CO.PMK%I/T$BRRF)

## Voci di menù preferite
Dal menù, passando l'apposito parametro PRF, è possibile attivare la gestione dei preferiti. Questa implica due aspetti : 
* Nel menù in fondo apparirà la voce "Gestione Voci di Menù Preferite", richiamandola sarà possibile selezionare le voci preferite.
* Quale sono state selezionate delle voci come voci preferite, il menù presentarà inizialmente solo tali voci e solo a richiesta esplicita dell'utente sarà possibile accedere alle voci del menù completo.
Questa funzionalità non è supportata sul mobile.

## Personalizzazione
Alle voci di menù proposte possono essere fatte delle aggiunte tramite l'utilizzo del file SCP_MNUPER.  Le voci aggiuntive devono essere inserite, con le stesse modalità del file SCP_MNU, in questo file, che va posto nella libreria di personalizzazione.
Questo script va compilato con le stesse regole di un menù standard del file SCP_MNUPER, con la sola differenza di avere in più in aggiunta gli attributi : 
* Ord - Ordinamento :  per fissare la posizione del nodo personalizzato all'interno del menù standard
* PoR - Posizione Riferimento :  per fissare il nodo standard a cui si vuole agganciare il nodo personalizzato
* PDR - Prima/Dopo Posizione Riferimento :  per  indicare se rispetto al precedente campo il nodo personalizzato deve essere posto prima o dopo di esso.
NOTA BENE :  al fine di evitare la sovrapposizione con i codici standard si consiglia di utilizzare per codificare le voci personalizzate i caratteri minuscoli (esclusa la "y" di primo livello in quando già utilizzata per l'inclusione "My Smeup")

## Autorizzazioni
Le voci di menù sono autorizzabili in base a questa struttura : 
* All'interno dello script possono essere indicati dei livelli di autorizzazione tramite gli attributi "Au" e "Usr" del tag C.MNU. Il primo viene utilizzato per la classe/funzione di riferimento dello script, mentre il secondo sulla classe USRLVL con funzione **.
* La classe di riferimento è LO.MNU e la funzione è il nome dello script. Tramite il tag S.MNU è possibile sostituire la funzione con l'attributo "Fun" o overridare la classe e la funzione con gli attributi "ClO" e "FuO". Quest'ultime due veranno utilizzate solo se è stato inserito un'impostazione specifica per questi due attributi
Nella determinazione del livello di autorizzazione vengono inoltre applicate le seguenti considerazioni : 
* Il livello impostato con codice 1 = "nome script" e codice 2 = "**" viene applicato come default a tutte le voci di menù dello script.
* La mancata autorizzazione di voce menù padre implica la disabilitazione di tutte le voci figlie
Operativamente i parametri sono gestibili tramite il modulo smeup dei parametri o sono immediatamente richiamabili tramite l'azione di popup disponibile sul menù stesso (tasto destro su una voce - "Gestione Autorizzazioni").
Le definizione degli elementi di tabella necessari (riportati di seguito) possono essere ripresi dal modello : 
 :  : DEC T(TA) P(B£P) K(LO.MNU)






