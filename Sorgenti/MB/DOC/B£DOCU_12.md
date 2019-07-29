## Struttura e contenuto documentazione operativa
Obiettivo della documentazione operativa è spiegare all'utente tutte le possibilità che ha a disposizione ogni volta che si trova di fronte a una qualsiasi finestra di SmeUP. Per raggiungere questo scopo si è deciso di strutturare la documentazione operativa in 4 capitoli principali con i relativi sottocapitoli : 
 * Obiettivo :  riporta la finalità dell'interrogazione
 * Formato guida :  all'interno del formato guida va specificato il significato di tutti i campi presenti. Inoltre al suo interno è necessario inserire i seguenti sottocapitoli : 
 ** Impostazioni :  riporta il dettaglio di tutti i campi presenti all'interno delle impostazioni
 ** Tasti funzionali :  riporta il significato di tutti i tasti funzionali disponibili
 ** Tips&tricks :  in questo paragrafo sono riportate tutte le possibilità presenti all'interno del formato guida e che non sono specificate nella parte sopra (es :  disponibilità mdv, disponibilità parzializzazioni, caratteri speciali per le ricerche, possibilità di inserire date dinamiche, ecc.). In questo sottocapitolo sono incluse, quindi, alcune possibilità 'generali' di SmeUP :  queste caratteristiche sono generalmente documentate all'interno del modulo B£ è, quindi, necessario inserire il riferimento alla documentazione specifica.
 * Formato lista :  all'interno del formato lista vanno specificate le informazioni riportate per ogni record. al suo interno è necessario specificare i seguenti sottocapitoli : 
 ** Opzioni :  vanno specificate tutte le opzioni disponibili per ogni record
 ** Impostazioni :  se non sono state documentate le impostazioni all'interno del formato guida (perché non presente) specificarle all'interno del formato lista; in caso contrario inserire un richiamo alla documentazione del formato guida
 ** Tasti funzionali :  se non sono stati documentati all'interno del formato guida (perché non presente) specificarli all'interno del formato lista; in caso contrario inserire un richiamo alla documentazione del formato guida
 ** Tips&Tricks :  in questo paragrafo sono riportate tutte le possibilità presenti all'interno del formato lista e che non sono specificate nella parte sopra (es :  ricerche di stringhe tramite F1, stampa delle liste tramite F4, utilizzo del campo posizionamento, parzializzazioni, ecc.). Se queste possibilità sono documentate riportare il link alla documentazione.
 * Formato dettaglio :  vanno specificate tutte le informazioni di dettaglio visualizzate. Sottocapitoli da documentare : 
 ** Tasti funzionali :  riportare il significato di tutti i tasti funzionali disponibili
 ** Tips&Tricks :   in questo paragrafo sono riportate tutte le possibilità presenti all'interno del formato dettaglio e che non sono specificate nella parte sopra (es :  accesso alle schede oggetti di LoocUP cliccando sulle icone, ecc).

 La struttura dello script della documentazione operativa deve seguire la seguente : 
![B£DOCU_001](http://localhost:3000/immagini/B£DOCU_12/BXDOCU_001.png)
## Inclusione di altri documenti
Il comando I.INC.MBR Fil(NomeFile) Mem(NomeMembro) permette di includere altri documenti all'interno di un testo. In particolare utilizzando questo comando il documento scritto nel membro indicato verrà esploso : 
Durante il processo di inclusione è possibile, attraverso opportuni parametri, l'importazione di una parte del documento richiesto : 
* Sec - Importa solo il tag richiesto
* SAt - Una volta incontato il tag richiesto, questo deve possedere l'attributo richiesto per poter essere imporato. Questi valori possono essere multipli (Separati da spazio) solo se trattasi di membri SCP_CFG.
* SeE - Una volta incontrato il tag richiesto, ferma l'importazione quando incontri il tag righiesto. Non attivo se trattasi di membgri SCP_CFG.
Vengono applicate le seguenti limitazioni : 
* Se presente l'attributo Id(...) il SAt(...)  deve corrispondere.
* Se titolo il SAt(...) deve corrispondere al titolo
* Negli altri casi il SAt(...) deve essere presente nella riga
L'importazione viene interrotta quando si incontra lo stesso Sec(...) di inizio.
L'importazione non viene interrotta al primo evento, ma viene scansionato l'intero membro dando così la possibilità di includere più elementi anche non sequenziali fra loro.
in alternativa si può utilizzare il parametro
* SeE - Importa tutto il documento fermandosi quando si incontra il tag impostato.

_3_Esempio di esplosione della voce Upper processes con comando INC.MBR Sec(VOC) SAt(UP) : 
 :  : I.INC.MBR Fil(DOC_VOC) Mem(GLO_ACR_01) Sec( :  : VOC) SAt(UP)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione dello Sviluppo personalizzazioni e interfacce e termine al primo sottotitolo con comando INC.MBR Sec(T02) SAt(Sviluppo personalizzazioni e interfacce) SeE(T03) : 
## Customizzazione tabelle
La customizzazione avviene con una modalità incrementale e di modifica a partire dal modello fornito in fase di installazione del Sw. Nelle librerie STD vengono forniti anche modelli diversi a cui attingere per implementare funzioni particolari. Quando si inseriscono gli elementi di tabella è possibile utilizzare le note per una breve spiegazione della ragione e del funzionamento del particolare elemento.

### Deliverables

- >Modello dinamico :  l'insieme delle customizzazioni eseguite sulle tabelle può essere estratto direttamente dal sistema attraverso l'utilizzo delle schede dei modelli dinamici, dove per ogni applicazione vengono presentate gli elementi di tabella interessate e le loro interrelazioni.

![A£BASE_028](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_028.png)

- Glossario
- Stato avanzamento attività
- Rapporti attività SME.up
- Verbale di chiusura della fase approvato dal Capo Progetto Cliente


## Sviluppo personalizzazioni e interfacce

- Sviluppo dei programmi richiesti.
- Approntamento delle eventuali schedulazioni (elaborazioni batch).
- Autorizzazioni per gruppo utenti :  attribuzione a ciascun gruppo utente, per classe / funzione delle autorizzazioni stabilite in fase di analisi tecnica.

### Deliverables

- Programmi (formato codice sorgente e codice oggetto)
- Documentazione tecnica ricavata dinamicamente dai tool Sme.up di documentazione (vedi esempi sottostanti).

Lancio programma documentazione : 
![A£BASE_025](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_025.png)
Esempio stampa : 
![A£BASE_026](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_026.png)
- Autorizzazioni previste per ciascun gruppo utente, ricavabile dalla scheda autorizzazioni (vedi esempio)

![A£BASE_030](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_030.png)
- Stato avanzamento attività
- Rapporti attività SME.up
- Verbale di chiusura della fase approvato dal Capo Progetto Cliente

## Sviluppo programmi conversione dati

- Sviluppo dei programmi richiesti.
- Compilazione eventuali tabelle alias di trascodifica.
- Predisposizione delle elaborazioni batch (preferibilmente con schedulazione giornaliera notturna) per la creazione dell'ambiente di test partendo dai dati presenti nel sistema corrente

### Deliverables

- Programmi (formato codice sorgente e codice oggetto)
- Documentazione tecnica ricavata dinamicamente dai tool Sme.up di documentazione
- Schedulazione elaborazioni batch
-- Alias per trascodifiche, ossia tabelle interne a Sme.up in cui vengono descritte le associazioni tra codice origine e codice di destinazione e che possono essere utilizzate in fase di migrazione dati oppure anche a regime nel passaggio informazioni tra il cliente ed enti diversi (es. EDI)
- Stato avanzamento attività
- Rapporti attività SME.up
- Verbale di chiusura della fase approvato dal Capo Progetto Cliente

SeE(###)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione della Customizzazione tabelle con termine al primo sottotitolo con comando INC.MBR Sec() SAt() SeE(T03) : 
## Customizzazione tabelle
La customizzazione avviene con una modalità incrementale e di modifica a partire dal modello fornito in fase di installazione del Sw. Nelle librerie STD vengono forniti anche modelli diversi a cui attingere per implementare funzioni particolari. Quando si inseriscono gli elementi di tabella è possibile utilizzare le note per una breve spiegazione della ragione e del funzionamento del particolare elemento.

### Deliverables

- >Modello dinamico :  l'insieme delle customizzazioni eseguite sulle tabelle può essere estratto direttamente dal sistema attraverso l'utilizzo delle schede dei modelli dinamici, dove per ogni applicazione vengono presentate gli elementi di tabella interessate e le loro interrelazioni.

![A£BASE_028](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_028.png)

- Glossario
- Stato avanzamento attività
- Rapporti attività SME.up
- Verbale di chiusura della fase approvato dal Capo Progetto Cliente


## Sviluppo personalizzazioni e interfacce

- Sviluppo dei programmi richiesti.
- Approntamento delle eventuali schedulazioni (elaborazioni batch).
- Autorizzazioni per gruppo utenti :  attribuzione a ciascun gruppo utente, per classe / funzione delle autorizzazioni stabilite in fase di analisi tecnica.

### Deliverables

- Programmi (formato codice sorgente e codice oggetto)
- Documentazione tecnica ricavata dinamicamente dai tool Sme.up di documentazione (vedi esempi sottostanti).

Lancio programma documentazione : 
![A£BASE_025](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_025.png)
Esempio stampa : 
![A£BASE_026](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_026.png)
- Autorizzazioni previste per ciascun gruppo utente, ricavabile dalla scheda autorizzazioni (vedi esempio)

![A£BASE_030](http://localhost:3000/immagini/A£BASE_P0G/AXBASE_030.png)
- Stato avanzamento attività
- Rapporti attività SME.up
- Verbale di chiusura della fase approvato dal Capo Progetto Cliente

## Sviluppo programmi conversione dati

- Sviluppo dei programmi richiesti.
- Compilazione eventuali tabelle alias di trascodifica.
- Predisposizione delle elaborazioni batch (preferibilmente con schedulazione giornaliera notturna) per la creazione dell'ambiente di test partendo dai dati presenti nel sistema corrente

### Deliverables

- Programmi (formato codice sorgente e codice oggetto)
- Documentazione tecnica ricavata dinamicamente dai tool Sme.up di documentazione
- Schedulazione elaborazioni batch
-- Alias per trascodifiche, ossia tabelle interne a Sme.up in cui vengono descritte le associazioni tra codice origine e codice di destinazione e che possono essere utilizzate in fase di migrazione dati oppure anche a regime nel passaggio informazioni tra il cliente ed enti diversi (es. EDI)
- Stato avanzamento attività
- Rapporti attività SME.up
- Verbale di chiusura della fase approvato dal Capo Progetto Cliente

_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione del Indipendenza dalla piattaforma  con comando INC.MBR Sec(T03) SAt(Tasti funzionali) : 
## Introduzione
Un'interfaccia è un contratto tra ogni classe che la implementa ed il mondo esterno :  l'interfaccia vincola le classi che la implementano a supportare le funzioni in essa dichiarate.
Notiamo che l'interfaccia non vincola in alcun modo l'implementazione delle classi.
In questo senso, l'uso delle interfacce è la chiave di volta per l'estendibilità del software :  oggetti di una qualunque classe C che implementi l'interfaccia I possono essere utilizzati in qualunque contesto operante su elementi di tipo I.
Come vedremo, l'uso accorto delle interfacce è anche una delle chiavi per la riusabilità del software (ricordiamo che riusabilità ed estendibilità sono fattori distinti, per quanto entrambi estremamente importanti).

Un'interfaccia può anche essere considerata un 'contratto di programmazione', utilizzabile per creare relazioni tra classi altrimenti non correlate. Ad esempio, si consideri una situazione di lavoro con un team di programmatori, ciascuno dei quali si occupa di una classe diversa della stessa applicazione. In fase di progettazione dell'applicazione, viene stabilito un set di metodi che le classi utilizzeranno per comunicare. Viene quindi creata un'interfaccia che dichiara questi metodi, i relativi parametri e tipi restituiti. Qualsiasi classe che implementa questa interfaccia deve fornire le definizioni per tali metodi; in caso contrario si verificherà un errore del compilatore. L'interfaccia è come un protocollo di comunicazione a cui devono aderire tutte le classi.

A tale scopo, è possibile creare una classe che definisca tutti questi metodi e far sì che ogni classe estenda questa superclasse o erediti dalla stessa. Tuttavia, dato che l'applicazione è costituita da classi non correlate, non è consigliabile inserire tutte le classi in una gerarchia comune. Una soluzione ottimale consiste nel creare un'interfaccia che dichiari i metodi utilizzati per la comunicazione e consentire quindi alle suddette classi di implementare (fornire la propria definizione per) questi metodi.

Generalmente è possibile eseguire una corretta programmazione senza l'uso delle interfacce. Tuttavia, se utilizzate correttamente, le interfacce consentono di ottimizzare la realizzazione dell'applicazione rendendola più piacevole, scalabile e aggiornabile in modo semplice.

## Up ver
### Indipendenza dalla piattaforma
La  gestione della definizione delle interfacce è il modulo Sme.up, che permette il dialogo con applicazioni di ambienti diversi da Sme.up.
Tutti i moduli Sme.up per il reperimento e la gestione delle informazioni, dialogano esclusivamente con questo componente, così, per ogni singolo programma, non è necessario specificare la natura dell'anagrafico interrogato. Il gestore delle interfacce elabora le informazioni ricevute dai vari ambienti e le traduce in uno standard comune, in modo che i programmi del mondo SME.up possano reperire le informazioni sempre nella stessa forma, in maniera indipendente dalla fonte.

Nella figura seguente si può vedere uno schema che esemplifica come il mondo Sme.up comunichi esclusivamente con il gestore delle interfacce, responsabile del trasporto e dell'elaborazione delle informazioni provenienti da tutti gli ambienti supportati.

![A£BASE_020](http://localhost:3000/immagini/A£BASE_SF/AXBASE_020.png)
Gli ambienti supportati ad oggi [22/01/08] sono : 
 * ACG IBM 5.0 (EXT)
 * ACG IBM 7.0 (EXT)
 * ACG IBM Versione 1
 * ACG IBM Versione 2
 * ADB IBM
 * AGAS/GIPROS - THERA V2R1
 * APPL. SELTERING
 * Applicazioni CTS
 * Applicazioni SVIB
 * BITECH
 * Bpcs
 * DataSys
 * ECON
 * Europa di CSB
 * Galileo - SanMarco
 * GI.PRO.S APS - THERA
 * Gipros V1R6 (EXT)
 * GIPROS/36
 * Golden Lake
 * Gruppo PRO J
 * Ibimec
 * MAPICS - Rilascio 2
 * MAPICS - Rilascio 3
 * MAPICS - Rilascio 4
 * MAPICS versione XA
 * PACKMAN 2 - DATASYS
 * Primerose
 * Query / EURO
 * Query versione 3
 * Query versione 5
 * SAP R.3
 * SAXAP - IBM
 * SICON/CATA
 * SIGECO
 * SIPE
 * SME_up
 * SME_up /Release precedente
 * SME_up DEMO
 * SME_up/V2
 * SMEUP_ Q9000
 * Star
 * SYSTEL
 * Tecnest Flex

Un'architettura di questo genere ha l'indubbio vantaggio che, come nel caso presentato di seguito, alla nascita dell'esigenza d'interfacciamento con un nuovo driver, l'unico modulo da modificare  è il gestore delle interfacce. Infatti, qualunque sia la modalità di comunicazione con il nuovo driver, questa sarà trasparente a tutti i moduli, che parlano direttamente solo con il gestore delle interfacce. Grazie a questa architettura è possibile evitare la modifica di qualsiasi altro modulo, con un risparmio di tempo e risorse senza eguali.

![A£BASE_021](http://localhost:3000/immagini/A£BASE_SF/AXBASE_021.png)
### Il comando in pratica
Nella figura seguente si può vedere un esempio di configurazione del gestore delle interfacce. Modificando il campo applicazione all'interno di questa griglia, tutto il sistema devierà il reperimento delle informazioni per quella specifica area, verso l'_applicazione_ selezionata.

![A£BASE_022](http://localhost:3000/immagini/A£BASE_SF/AXBASE_022.png)
Le righe visualizzate sono tutte e sole quelle definite nella tabella B£1. Il programma è solo una form di immissione meglio guidata e controllata, ma non permette di aggiungere driver di nuove interfacce.

**Opzione** :  Questo campo si presenta quando è attiva la possibilità di richiamare il programma di verifica cioè quando l'interfaccia descrive un oggetto applicativo (Es. articolo, cliente, ubicazione ecc.)
**Interfaccia** :  Descrizione dell'interfaccia definita per la tabella B£1
**Applicazione** :  Codice dell'applicazione.
**AP**Tale codice può essere associato mediante la B£1 a  due diverse tabelle : 
 1.   Tabella *CNAA :  Solo descrittivo, il campo tipo oggetto si presenta con inversione di fondo. Sono possibili le normali interrogazioni ma non i controlli.
 2.   Tabella B£Vxx (xx=tipo oggetto) :  Oltre alle normali interrogazioni è possibile inserire il carattere "/". In tal caso si presenta un formato di dettaglio che visualizza tutte le interfacce descritte per l'oggetto permettendo la selezione delle sole interfacce che non presentano errori, cioè per le quali è soddisfatta la disponibilità di file e programmi descritti nella specifica tabella.

### Tasti funzionali
F6   Controllo interfacce
Esegue per tutte le interfacce descritte in tabella B£V la verifica sopra descritta e presenta il campo lampeggiante se l'esito ha dato risultato negativo.

## Tabelle collegate
B£1   - Personalizzazione
*CNAA - Codici ambiente applicativo *CNTT - Codici oggetti applicativi
B£Vxx - Dettaglio interfacce applicative

un'altra scheda rilevante è TA _B£I

- [B£I - Deviaz. tabella](Sorgenti/ST//B£I)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione di documento con comando INC.MBR : 
 :  : I.INC.MBR Fil(DOC_OPE) Mem(B£_LIS)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

## Link ad altri documenti
Attraverso il comando DEC è possibile introdurre un link a un altro documento che sarà possibile esplodere o meno settando il parametro L (si veda il wizard per maggiori dettagli)
_3_Esempio di inserimento di un link a un documento con comando DEC : 
 :  : DEC T(MB) P(DOC_OPE) K(B£_LIS) I(Gestione liste oggetti) L(1)
_3_Fine esempio di inserimento di un link a un documento con comando DEC : 

## Elementi grafici del documento
Tutti gli elementi costitutivi del corredo grafico del documento che viene generato sono immagini di oggetti.
Per elementi costitutivi del corredo grafico del documento si intende :  la copertina prima pagina, il logo aggiuntivo della prima pagina, la copertina di fine documento, l'header di pagina ed il footer di pagina.
La loro eventuale personalizzazione passa per la personalizzazione delle immagini degli oggetti.
Gli elementi e gli oggetti SmeUP relativi sono : 
* Sfondo prima pagina :  oggetto VO; COD_SEL; SFO_000
* Sfondo ultima pagina :  oggetto VO; COD_SEL; SFO_002
* Logo prima pagina :  oggetto VO; COD_SEL; LOG_000
* Header di pagina :  oggetto VO; COD_SEL; HEA_000
* Footer di pagina :  oggetto VO; COD_SEL; FOO_000
