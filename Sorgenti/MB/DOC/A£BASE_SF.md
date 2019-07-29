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

 :  : DEC T(ST) P() K(B£I)
