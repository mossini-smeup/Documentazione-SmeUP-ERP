 ### UTILIZZO RICHIESTA CONFIGURAZIONE

In queste schede vengono evidenziate le possibilità previste dall'utilizzo della richiesta configurazione, in tutte le modalità grafiche previste dall'attributo UirMGr - Modalità Grafica : 
 * C :  Richiedi ed Esegui in Subsezione (Assunto)
 * B :  Richiedi in Finestra, Esegui in Subsezione
 * D :  Richiedi in Subsezione, Esegui in Nuova Finestra
 * E :  Solo Richiesta in Subsezione

 ### NOTE OPERATIVE

 :  : R01 Struttura di Richiamo

Tramite i Tag G.SUB.UCF, G.SET.UCF e D.FUN.UCF è possibile lanciare una funzione, ponendo prima all'utente la richiesta di compilazione (che può essere obbligatoria o meno) di un questionario di domande.

* Il tag G.SUB.UCF serve solo per identificare la subsezione, come una un subsezione che presenterà le sopracitate caratteristiche.
* Il tag G.SET.UCF serve per indicare quale sarà il questioni che si andrà utilizzare e varie caratteristiche grafiche tramite le quali, il questionario e la funzione stessa verranno posti all'utente.
* Il tag D.FUN.UCF serve per indicare quale funzione deve essere infine eseguita. Questo tag non si differenzia dal normale tag di funzione D.FUN.STD se non che per un aspetto :  tutte le risposte alle domande del questionario verranno automaticamente passate come parametri di INPUT alla funzione indicata in questo formato "codicedomanda(valorerisposta)", ma è inoltre possibile indicare un utilizzo specifico di tali parametri all'interno della funzione tramite la seguente dicitura $IN.codicedomanda. Quindi ponendo di avere come unica domanda con codice domanda "CD", mi viene richiesto un cliente, se in D.FUN.UCF specifico "F(EXD;*SCO;) 2(MB;SCP_SCP;XXX)" mi verrà eseguita la funzione "F(EXD;*SCO;) 2(MB;SCP_SCH;XXX) INPUT(CD(valorerisposta))", viceversa se specifico "F(EXD;*SCO;) 1(CN;CLI;$IN.CD) 2(MB;SCP_SCP;XXX)" mi verrò eseguita la funzione "F(EXD;*SCO;) 1(CN;CLI;valorerispostaCD) 2(MB;SCP_SCH;XXX) INPUT(CD(valorerisposta))"

Esempio 1)
 :  : PAR F(04) L(MON)
G.SEZ Pos(1)
G.SUB.UCF Tit="*NONE"
G.SET.UCF UirTRe="LOA08/A" UirMGr="C" UirCtx="M_LOSUIR"
D.FUN.UCF F(EXD;*SCO;) 2(MB;SCP_SCHESE;LOSUIR) 4(;;EXDPAR)


Esempio 2)
 :  : PAR F(04) L(MON)
G.SEZ Pos(1)
G.SUB.UCF Tit="*NONE"
G.SET.UCF UirTRe="LOA08/A" UirMGr="C" UirCtx="M_LOSUIR"
D.FUN.UCF F(EXD;*SCO;) 1(TA;$IN.ST; $IN.CD)  2(MB;SCP_SCHESE;LOSUIR) 4(;;EXDPAR)


 :  : R01 Le Domande della Configurazione

Per il dettaglio sulle possibilità grafiche si rimanda all'help del wizard G.SET.UCF, mentre ci si sofferma sulla definizione del questionario. Quest'ultimo può essere definito in varie modalità, ma viene qui data indicazione di come opportunamente definirlo per l'utilizzo nell'UIR.

* Il questionario va definito all'interno di uno script di SCP_CFG. Per il nome di quest'ultimo si consiglia di far riferimento al nome del "modulo" (standard o meno) in cui il questionario verrà poi impiegato. Se non si vuole utilizzare il codice di un modulo è comunque vincolo non eccedere i sei caratteri (per vari motivi, qui non esplicitati, ma che comunque impongono tale limite) ed attribuire un nome che non si sovrapponga a quello di un modulo.
* All'interno di questo script si possono utilizzare i seguenti TAG di definizione (per una immediata comprensione si consiglia poi di dare un'occhiata allo script utilizzato per gli esempi ed accessibile dalla voce corrispondente nella parte finale del menù) : 
** A08 :  tramite esso è possibile specificare l'eventuale exit da utilizzare manipolare in modo più specifico domande e risposte del questionario. Per il nome di questo pgm si consiglia di adottare la dicitura nomescript_A08.
** SEZ :  permette di definire un elenco di questionari le cui domande verranno poi dettagliate nella sezione dello script definita dal tag RIG. Le sezioni hanno il vincolo di avere un codice della lunghezza di un carattere. Questo vincolo e quello della lunghezza del nome lo script sono necessario al fine di poter identificare le configurazioni come oggetti. La configurazione verrà infatti tipizzata in questo modo Tipo Oggetto CF, Parametro Oggetto :  S-Nomescript/Letterasezione (es. CFS-C5D010/A)
** RIG :  permette di definire le varie domande attribuibili ad ogni sezione. Per la compilazione si rimanda al wizard, tenendo sottocchio il questionario utilizzato per gli esempi. Ci si sofferma qui solo sull'utilizzo della tipizzazione ".V" che permette di sfruttare i valori fissi indicabili nella sezione dello script definita dal tag LIS.
** LIS :  permette di definire elenchi di valori fissi che possono essere poi utilizzati nelle domande poste nei questionari.

Qui di seguito viene riportato lo script LOA08, utilizzato per gli esempi.

 :  : PAR F(04) L(MON)
 :  : I.INC.MBR Fil(SCP_CFG) Mem(LOA08)


 ### NOTE SU ESEMPI

* La funzione che viene eseguita alla compilazione del questionario è sempre una matrice in cui vengono evidenziati i parametri ricevuti.
* Gli esempi sono suddivisi in due categorie : 
** Nella prima vediamo l'utilizzo del configuratore con varie tipologie di domanda che è possibile utilizzare : 
*** Campo a tipizzazione dinamica, cioè un campo la cui tipizzazione dipende dal valore di un altro campo. Negli esempi abbiamo "Settore" come campo di riferimento ed "Elemento" come dipendente :  il codice indicando nel campo "Elemento" punta alla tabella indicata nel campo "Settore".
*** Nei suddetti campi è stato espresso anche l'attributo di obbligatorietà che costringe all'indicazione obbligatoria per entrambi di un valore valido.
*** Campo con valore di default. Da script è possibile indicare una valorizzazione di default per un campo, questo significa che al primo caricamento il campo verrà automaticamente riempito con tale valore. Come esempio di questo tipo è stato utilizzato il campo data, nel quale è stata forzata come default la data dinamica odierna. In questo campo è quindi possibile verificare anche l'utilizzo di questa funzionalità, specifica delle date.
*** Valori fissi :  dallo script di configurazione è possibile tramite indicazione ".V" come tipo oggetto, seguito dal codice di una sezioni indicate sotto il tag "LIS", esprimere la scelta di una valore con corrispondente significato, senza che a tali scelte sia necessario far corrispondere un oggetto definito. Questa possibilità nell'esempio è espresso nel campo "Scelta Valore".
*** Campi di varia lunghezza :  la lunghezza del campo di input può arrivare fino ad una lunghezza di 2560. Nell'esempio viene semplicemente riportato nel campo "Descrizione" un campo lungo 30.
*** Per questioni di spazio per i valori nelle domande normalmente è prevista l'indicazione della decodifica. E' però possibile poter specificare una forzatura a livello di campo, per far si che per questo venga presentata la decodifica. Nell'esempio, questa possibilità è stata applicata al campo "Elemento". Non è esemplificato, ma se lo si ritiene opportuno è altresì possibile tramite l'attributo del setup "UirDec" forzare la presentazione delle decodifice di tutti i campi.
** Nella seconda categoria vediamo invece l'applicazione di un pgm di exit. A livello di script è infatti possibile specificare un pgm di controllo di exit. Nell'esempi viene semplicemente indicato come è possibile condizionare tre domande a seguito di una prima domanda che identifica una griglia. Quindi i tre campi successivi alla prima domanda prenderanno la tipizzazione e l'obbligatorietà a partire da quanto definito nell'elemento della B£G indicato nel primo campo. Attraverso esso è possibile : 
*** Modificare le definizioni delle domande : 
**** attributo di visualizzazione (B, O, H)
**** obbligatorietà
**** intestazione
**** non è invece possibile modificare il tipo oggetto. E' necessario che questo rimanga identico a quello previsto dal configuratore. Per questo è necessario che per questa casistica, il campo che deve cambiare tipizzazione appoggi semplicemente la propria tipizzazione ad un campo esterno.
*** Intervenire sulle risposte : 
**** Modificando il valore della risposta stesso
**** Aggiungendo segnalazioni che esulano i semplici controlli di consistenza ed obbligatorietà dell'oggetto.





