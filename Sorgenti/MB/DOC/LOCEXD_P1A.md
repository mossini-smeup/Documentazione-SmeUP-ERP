# Servizio su AS/400
## Versione 1.0.a
 - Introdotta istruzione I.IF.ESI che testa l'esistenza di un oggetto specificato nella forma standard T() P() K(). Vera se l'oggetto esiste.

# Componente grafico
## Versione 1.0.a
 - Aggiunto Componente Label (G.SUB.LAB, G.SET.LAB, D.LAB.STD)
 - Aggiunto Gestione Setup in Componenti Albero, TabAlbero, Label
 - Modificata Gestione Targets. Ora sono descritti in appositi nodi nel documento Xml di Definizione Scheda
 - Definita Icona per visualizzazione in "Task Manager"

## Versione 1.0.b
 - Modificata sintassi Xml di definizione Setup Componente "Grafico". Il parametri con valore = "1|0" sono stati sostituiti con valore = "Yes|No"
 - Corretto Errore in refresh. Non veniva impostato il secondo oggetto!

## Versione 1.0.c
 - Modifica richiamo JASEP (SnP Scheda) per passare anche gli oggetti 2,3,4
 - Aggiunta Possibilità di non visualizzazione titolo TabSheet se passato *NONE come titolo e il PageControl presenta un unico Tabsheet
 - Inserita gestione Attributo Inv in Gauge :  consente di invertire l'ordine di presentazione dei colori della scala da Verde-Giallo-Rosso a Rosso-Giallo-Verde

## Versione 1.0.g
 - Eliminato refresh se ingrandimento/riduzione di un tabsheet contenente un albero con funzioni "dinamiche"

## Versione 1.0.h
 - Modificata Gestione Immagini/Icone per ricerca immagini ed icone anche a livello di Ambiente. Se esiste un direttorio ..\loocup_img\<ambiente> la ricerca delle immagini (icone se ..\loocup_ico\<ambiente>) avviene al suo interno. Se non esiste la ricerca delle immagini/icone avviene nei direttori standard (loocup_img e loocup_ico)
 - Corretto errore in modifica immagine/icona se tipo o parametro o codice conteneva caratteri illegali per il filesystem
 - Aggiunta possibilità di specificare componente di destinazione se "Esecuzione Funzione Origine" da Matrice. E' ora possibile selezionare se l'Xml deve essere elaborato da Matrice, Grafico o Excel
 - Modificata routine di gestione oggetti dinamici in Matrice. E' ora possibile specificare classi sia parzialmente fisse che parzialmente dinamiche (Es :  TA[XAOGG])

## Versione 1.0.i
 - Corretto errore in risalita immagini per ambiente
 - Corretto errore visualizzazione icone "fisse" su matrice
 - Inserita gestione sostituzione attributi dinamici nel caption del tabsheet
 - Aggiunta possibilità caricamento immediato o differito di un tabsheet dinamico

## Versione 1.0.j
 - Aggiunta Gestione Variabili di Sezione

## Versione 1.0.k
 - Aggiunta Gestione Variabili di Sezione,Scheda,Componente,Loocup
>N.B. :  Attualmente la gestione delle variabili Loocup coincide con quella di Componente
 - Inserita gestione eventi Click e DblClick su Albero
 - Inserita gestione eventi Click, DblClick, Change su TabAlbero
 - Inserita gestione eventi DblClick,Change,ChangeRow,ChangeCol su Matrice
All'atto dell'esecuzione dell'evento vengono inserite nelle variabili della sezione di destinazione, il "Tipo, Parametro, Codice" della cella sulla quale l'evento si è scatenato. Vengono inoltre inseriti i valori di tutti i campi della matrice.

## Versione 1.0.l
 - Modificata Gestione Caption del Tabshett di sottosezione
Viene determinata secondo la seguente regola : 
 -- Se esiste la Variabile Ti viene utilizzata
 --- Altrimenti Se esiste la Variabile Tx viene utilizzata
 --- Altrimenti viene utilizzato il tipo specificato nella sottosezione
 - Aggiunta Visualizzazione Valore in "Semaforo"
 - Aggiunta Visualizzazione Valore in "Gauge"
 - Corretto errore AV se click o doppioclick su albero "vuoto"
 - Monitorato errore se Xml di definizione scheda non presenta i nodi Layout o Popup
 - Implementata Gestione UI_Popup

## Versione 1.0.m
Aggiunta "Impostazione Variabili di Sezione" dall'elenco delle variabili della sezione precedente

## Versione 1.0.n
 - Corretto errore nell'"Impostazione Variabili di Sezione" introdotto in 1.0.m (Index Out of Range)
 - Inseriti, nel Setup di Chart le seguenti opzioni : 
 -- Dta = Visualizza Tabella Dati
 -- Ser = Visualizza Tabella Serie
 -- Cmd = Visualizza ToolBar
 - Inserita la possibilità di variare serie ed assi
 - Inserita Creazione Schede "Virtuali" nel caso di ricezione di Xml "Grafico"
 - Eliminato DNA

## Versione 1.0.o
 - Corretto Errore in Refresh Scheda se presenti Oggetti da 2 a 5.
 - Monitorato AV in Distruzione Oggetto TargetOnEvents
 - Aggiunto Attributo NomeScheda e richiamo a Funzione "Editor della Scheda"

## Versione 1.0.p
 - Corretto errore nella gestione Stack Finestre
 - Aggiunto Parametro NFI nel richiamo dell'editor scheda

## Versione 1.0.q
 - Aggiunta Impostazione Variabili su Eventi del Componente Albero anche per i nodi qualificati dall'attributo "Nome".
 - Corretto errore in Ingrandimento/Ripristino di una sottosezione contenente una Label
 - Implementato Componente ImageList (IML)
 - Corretto errore mancata impostazione variabile di sezione Ti da Matrice

## Versione 1.0.r
Corretto Errore GPF introdotto in 1.0.q

## Versione 1.0.s
Modificato Nome Attributo da Orientation a Direction nella definizione del setup del sottocomponente ListaImmagini

## Versione 1.0.t
 - Al Refresh della Scheda (F5) vengono ora cancellati i valori assegnati alle variabili di scheda
 - Corretto errore in Caricamento Tabella da Xml se presenti nodi diversi da Righe/Riga
 - Nel caso in cui esistano Sottosezioni con lo stesso nome, la ricerca della sottosezione nella quale indurre il dinamismo viene adesso effettuata con precedenza alla scheda corrente.

## Versione 1.0.u
 - Corretto errore per evitare refresh di sottosezioni dinamiche nel caso in cui il componente sorgente gestisca il dinamismo su più sottosezioni con caricamento Differito. L'attivazione del tabsheet avviene ora solo se il caricamento del tabsheet dinamico viene effettuato immediatamente
 - Modificata Visualizzazione Numeri in Matrice. Se il Numero è a zero non viene visualizzato   o

## Versione 1.0.v
Inserita possibilità di gestione Tabelle Correlate in Matrice

## Versione 1.0.w
 - Sostituito Componente Matrice.
 - Attivato Setup su Matrice con la seguente sintassi : 
 -- ShowTotal="Yes|No"
 -- Yes = Visualizza Totali
 -- No  = Non Visualizza Totali
 -- ShowGroup="Yes|No"
 -- Yes = Visualizza Area per "Droppare" le colonne soggette a raggruppamento
 -- No  = L'area non viene visualizzata per cui non è possibile raggruppare
 -- ShowFilter="Yes|No"
 -- Yes = E' possibile filtrare le righe
 -- No  = Non e' possibile filtrare le righe
 -- DftGroup="<nomecampo1>sep<nomecampo2>sep.....sep<nomecampoN>"
Indicare facoltativamente l'elenco dei campi sui quali effettuare il raggruppamento
Es. :  DftGroup="C$RIS0|£CIRST"
 -- DftTotal="<funz1>(<nomecampo>)sep<funz2>(<nomecampo>)sep...sep<funzN>(<nomecampo>)"
Indicare facoltativamente l'elenco delle funzioni di totalizzazioni riferendole ai campi
 - Le funzioni ammesse sono : 
 -- COUNT
 -- MAX
 -- MIN
 -- AVG
 -- SUM
Es. :  DftTotal="Sum(£CRV01)|Avg(£CRV02)|Min(£CRV03)"
     . Columns="<nomecampo1>sep<nomecampo2>sep.....sep<nomecampoN>"
Indicare facoltativamente l'elenco e l'ordine delle colonne da visualizzare
Es. :  Columns="C$RISO|£CIRST|£CRV01"
     . Icone="Yes|No"
       Yes = Vengono visualizzate le icone di testata e di cella (oggetti variabili)
       No  = Vengono visualizzate le sole icone di testata

>N.B. :  sep equivale al carattere pipe "|"

## Versione 1.0.x
 - Inserita Funzione *CLEAR() per abblencare le variabili di un certo scope.
La funzione *CLEAR() deve essere implementata come una variabile. Il suo scopo è quello di azzerare tutte le variabili dello scope nel quale è presente l'istruzione.
Deve essere specificata all'interno delle variabili "esplicite"

Es. :  *CLEAR() NumFat(12)
Vengono cancellati tutti i valori delle variabili e successivamente viene assegnato il valore 12 alla variabile NumFat

 - E' stato modificato l'ordine di assegnazione delle variabili.
Versioni Precedenti : 
 * Copia Variabili di Sezione
 * Impostazione Variabili "implicite" di sezione
 * Impostazione Variabili "esplicite"

Versioni dalla 1.0.x in avanti : 
 * Impostazione Variabili "esplicite"
 * Copia Variabili di Sezione
 * Impostazione Variabili "implicite" di sezione
Questo potrebbe portare dei cambiamenti nel caso in cui una variabile con lo stesso nome sia stata impostata in "posti" diversi

 - Inserito Attributo FontSize nel setup del componente Label.
Se è presente un valore, viene disattivato il dimensionamento automatico del font in base alle dimensioni della sezione
 - Aggiunto Evento OnClick nel componente Label e Gestione Popup Menu.
 - Implementato nel setup del componente "Chart" la possibilità di forzare i nomi dei campi da utilizzare come asse e come serie di dati

Sintassi : 
 * Axe="<nomecampo>"
 * Series="<nomecampo1>sep<nomecampo2>sep...sep<nomecampoN>"
>N.B. :  sep equivale al carattere pipe "|"

 - Inibito il dinamismo se la sezione origine è massimizzata per evitare AV

## Versione 1.0.y
 - Corretto errore che generava AV se specificato ordinamento e visibilità colonne nella matrice ma il dataset collegato con conteneva dati
 - Inserita Funzione "Help della scheda" nel popup menu della scheda
 - Corretto Errore in ordinamento Date all'interno di una matrice

## Versione 1.0.z
 - Corretto AV se non presente direttorio Icone
 - Aggiunti Tasti Funzionali mappati su UIPopup 'J1-GRA-EXD'
 - Aggiunta Possibilità di Collassamento Matrice con Raggruppamento
 - Modificato Formato Xml TrafficLight e Gauge. conservata Compatibilità con versioni precedenti
 - Sostituito Componente tAbcButton con tSpeedButton standard
 - Corretto visualizzazione errata Tabsheet se da nascondere (Title=*NONE)
 - Attivata (da perfezionare) visualizzazione dinamica pulsanti in funzione del componente sul quale è posizionato il fuoco.
 - Corretto errore AV se presenti caratteri non UTF-8 nell'XML statico definito all'interno della scheda stessa. Viene automaticamente inserito, se mancante, un nodo di "Processing Instructions"

## Versione 1.1.a
 - Impostata Gestione Valori di Default Variabili
 - Corretto errore AV in assegnazione variabili se una variabile precedente non ha valore
 - Modificato Formato Xml Label e Image. conservata Compatibilità con versioni precedenti
 - Impostato Retrieve codice finestra da Xml ricevuto in modalità refresh per evitare la "mappatura statica e preventiva" dell'handle della finestra chiamante

## Versione 1.1.b
 - Modificato Schema XML per l'impostazione delle Variabili di Scheda
Prima era in :  UISmeup/SetVar
Ora è in :      UISmeup/Setup/Variables/SetVar
E' inoltre possibile specificare nodi multipli
 - Inserita Visualizzazione Totali di Raggruppamento anche nella riga di intestazione del raggruppamento in matrice
 - Corretto errore "Data Invalida" se Tipo Dati diverso da D8*DMYY o D8*YYMD  in matrice
 - Corretto errore in gestione tabelle correlate. Precedentemente venivano presentate vuote
 - Abilitata possibilità Multisort sulle intestazioni di colonna.
Si abilita tenendo premuto il tasto <Shift> quando si seleziona la colonna.
 - Attivata possibilità di specificare nel Setup i campi di ordinamento, mediante la seguente sintassi : 
  . DftSort="<nomecampo1>[,A|D]<sep><nomecampo2>[,A|D]sep.....sep<nomecampoN>[,A|D]"
Indicare facoltativamente l'elenco dei campi sui quali effettuare l'ordinamento
E' possibile, facoltativamente specificare anche il tipo di ordinamento desiderato : 
 -- A - Ordinamento Ascendente (Default)
 -- D - Ordinamento Discendente
Es. :  DftSort="C$RIS0|£CIRST,D"

>N.B. :  sep equivale al carattere pipe "|"

## Versione 1.1.c
 - Corretto errore su mancata distruzione pulsanti da uiPopup nel caso di emissione scheda sullo stesso livello stack
 - Corretto errore su mancata visualizzazione in primo piano della finestra scheda se già presente nello stack
 - Corretto errore mancata Gestione Valori di Default Variabili nel caso di Sottoscheda
 - Aggiunto parametro SelFirst in Setup Matrice,Albero,TabAlbero :  consente di selezionare immediatamente il primo record scatenando l'evento OnChange associato

Sintassi : 
* SelFirst="Yes|No"
* Yes = Il primo record di una matrice o il primo nodo di un albero vengono automaticamente selezionati e viene automaticamente scatenato l'eventuale evento onchange associato
 * No  = Nessun elemento viene automaticamente selezionato  (default)
 - Introdotta Visualizzazione del nodo selezionato di un albero anche se il fuoco è su un altro componente
 - Aggiunto Parametro ToExcel in Setup Matrice per consentire l'inibizione dell'esportazione di una matrice in Excel.

Sintassi : 
 * ToExcel="Yes|No"
 * Yes = Esportazione consentita (default)
 * No  = Esportazione non consentita

## Versione 1.1.d
Implementata gestione azioni da effettuare (ACTIONS) al richiamo di una funzione con parametro TO(*REQ)

## Versione 1.1.e
 - Implementata mappatura tasti funzionali su funzioni da UIPopup se : 
   . Tipo = J1
   . Parametro = KEY
   . Codice    = *F1..*F24
>N.B. :  Se l'attributo Exec del nodo contiene il valore *NONE, l'effetto è quello di disabilitare il tasto funzionale associato

 - Corretto errore di disabilitazione funzioni di Massimizzazione Sezione se si ritornava indietro di un livello avendo un Sezione Massimizzata.

## Versione 1.1.f
 - Impostata in matrice determinazione automatica del numero di decimali.
Il numero di decimali viene impostato al numero massimo di decimali presenti nell'Xml relativamente ai campi di tipologia NR o NP
 - Corretto errore in visualizzazione icone in un campo tipizzato mediante oggetti variabili nel caso in cui la variabilità era determinata da più campi.
Es :  CN[K§TIEN] oppure [K§TODI][K§PADI]
 - Modificato comportamento in caso di FullExpand di un Albero. Per evitare che venga selezionato un nodo non visibile, nel caso di FullExpand viene selezionato e posizionato l'albero sul primo nodo
 - Inserita possibilità di gestione Refresh Automatico di una Sezione
E' attivabile in qualunque sezione e viene definito nel nodo di Setup con la seguente sintassi : 
Refresh="<intervalloinsecondi>"
L'intervallo in secondi è da considerarsi come tempo intercorrente tra la fine dell'ultima esecuzione della funzione e l'inizio della successiva, non come intervallo tra due esecuzioni.
Questo comportamento inibisce la possibilità che nel caso in cui il tempo di esecuzione della funzione risulti maggiore del tempo di intervallo specificato, si giunga ad un accodamento di richieste.
Se l'intervallo è pari a zero il Refresh è disabilitato
In caso di sottosezione a caricamento "ritardato" (Load="D") il refresh si abilita all'attivazione della sottosezione
 - Implementato Drag and Drop da FileSystem verso componente Albero. (BETA)
Occorre definire un evento "DROP" con attributo Exec="<nomeFunzione>"
I Nomi comprensivi di percorso vengono passati nel campo "contenuto" separati da ';'
Cfr :  il programma JATRE_22C

## Versione 1.1.g
 - Aggiunta Proprieta Align nel Setup di una Label. Sintassi :  Align="RIGHT|LEFT|CENTER".
Il default è CENTER

## Versione 1.1.h
 - Aggiunto Evento RETURN gestito in ogni componente di scheda
L'evento RETURN consente di aggiornare una sottosezione quando è terminata una funzione richiamata mediante popup.
Ciò consente di effettuare "refresh" alle sottosezioni quando l'azione del popup implica un aggiornamento della sezione stessa o di qualunque altra sezione della scheda
La sintassi è la stessa utilizzata per specificare qualunque altro evento
Esempio :   :  : G.DIN When="RETURN" Where="Elenco Clienti"

>N.B. :  E' possibile effettuare un "refresh" anche al termine del richiamo di funzioni non richiamate in un popup, inserendo nella stringa di richiamo della funzione un ulteriore parametro con la seguente sintassi (es :  azioni di UI_Popup) :  NOTIFY(<Nome della sottosezione da aggiornare>)
Questa sintassi, permette la notifica del completamento dell'azione scatenata alla sottosezione interessata

>N.N.B. :  NOTIFY deve essere scritto in maiuscolo

 - Aggiunta funzione Stampa Matrice (F24)
 - Aggiunto Richiamo Funzione Stampa Scheda (F23)
 - Inserita Creazione Schede "Virtuali" nel caso di ricezione di Xml "Matrice" :  come il Grafico una matrice equivale a una scheda di una sola sezione.

## Versione 1.1.i
 - Modificata Funzione per richiamo Help Scheda da F(HTM;*EDTLET;VIS.SCH) a F(HTM;JATRE_34C;DOC.SCH) per evitare Lock arbitrari da parte delle funzioni AS/400
 - Corretto errore AV se richiamo PopupMenu come prima operazione su Icona Oggetto/Componente
 - Monitorati errori nel caso di ricezione Xml errato in luogo di Xml di Definizione Scheda / Matrice / Grafico
 - Corretta Caption errata nell'"hint" del bottone di Stampa Scheda
 - Inserita Possibilità di definire a "run.time" funzion di totalizzazione su Matrice
 - Eliminato Componente Matrice da Linking

## Versione 1.1.j
 - Eliminata Componente Editor RPG da linking
 - Trasformato Litteral "Esecuzione Funzione Origine" in "Visualizza come ..."
 - Aggiunta a "Visualizza Come ...." la possibilità di trasformare : 
 -- Grafico in Excel
 -- Grafico in Matrice
 -- Html in Editor
 -- Html in Browser
 -- Albero in Stella
 - Inserita in Matrice Possibilità Intestazione su Righe Multiple (separatore di riga :  |)
 - Eliminata in Matrice Visualizza Icona se Oggetto di tip NR o NP
 - Le larghezza delle colonne della matrice viene ora determinata automaticamente in BestFit
 - Inserito Attributi FontName,FontColor,FontSize,BackColor nel setup del componente Label.
 - Inserito nel setup del componente Albero l'attributo NodeText che consente di specificare cosa visualizzare nella descrizione di un nodo di un albero.
I valori ammessi sono : 
 -- Code = Viene visualizzato il solo codice dell'elemento
 -- Text = Viene visualizzata la sola descrizione dell'elemento
 -- Both = Viene visualizzato il codice e la descrizione dell'elemento [DEFAULT]
Es. :  NodeText="Text"

## Versione 1.1.k
 - Modificato Richiamo Funzione "Visualizza come... Editor". Il parametro passato causava l'apertura del documento in modalità "read-only". Ora il documento viene aperto in modalità "modifica".
 - Aggiunta (cosi come era precedentemente gestito nelle versioni sino alla 1.1.i compresa) la possibilità di richiamare da una matrice o da un grafico all'interno di una scheda il componente specifico.
- Poichè il richiamo delle funzioni "Visualizza come..." può adesso (oltre al passaggio dell'XML tra componenti) richiamare funzioni, è stato modificato il controllo di applicabilità della pressione dei tasti [CTRL,ALT,SHIFT] al richiamo della funzione stessa. E' ora inibito l'uso dei tasti alle soli funzioni di scambio XML tra componenti, mentre è abilitato nel caso di richiamo funzioni.
 - E' ora possibile gestire sottosezioni dinamiche anche per funzioni di tipo F(HTM;......). In precedenza una sottosezione dinamica di tipo HTML poteva essere generata solo da funzioni di tipo F(EDT;......)
 - Attivata gestione Alberi (e TabAlberi) ad Espansione Dinamica.
Un Albero ad Espansione Dinamica è un normale albero in cui il caricamento dei rami avviene al momento dell'espansione del loro genitore. Poichè al momento non è possibile determinare se un nodo di un albero dinamico è nodo "foglia", tutti i nodi sono inizialmente caratterizzati dal simbolo di espansione + sino a quando non viene effettuato un tentativo di espansione.
Solo a quel punto è infatti possibile determinare con precisione se trattasi di nodo "foglia".
E' bene precisare che un Albero ad Espansione Dinamica non deve necessariamente essere un insieme di alberi monolivello, ma può essere composto da alberi a livelli multipli, così come i nodi che vengono aggiunti dinamicamente all'espansione del genitore.
La definizione di un albero dinamico coinvolge tre aspetti : 
 * Caratterizzazione dell'albero come "albero dinamico"
 * Definizione (facoltativa) della massima profondità raggiungibile in caso di espansione globale (fullexpand) dell'albero stesso per evitare problemi di "loop"
 * Definizione della funzione da richiamare al tentativo di espansione di un nodo

I Parametri quindi aggiunti al setup di un componente albero sono : 
 * DynExpand="Yes|No"
 * Yes = Albero ad Espansione Dinamica
 * No  = Albero "standard" (Default)
 * MaxDepth=<livellomassimo> Identifica (mediante un numero) il livello massimo sino al quale sarà possibile espandere automaticamente l'albero per evitare problemi di "loop" (Default=5)
E' stato inoltre definito un evento Expand al quale associare la funzione da eseguire all'espansione di un nodo i cui figli non sono ancora stati tentativamente caricati.
In questo evento non deve essere specificato l'attributo Where, in quanto il destinatario del risultato della funzione è lo stesso componente che ha effettuato il richiamo
Es : 
 :  : G.DIN When="Expand" Exec="F(TRE;JATRE_34C;OGG.MBR) 1(MB;DOC;[K1]) P(1)"

 - La visualizzazione di una Matrice (xml di Matrice con Definizione Automatica di una Scheda Virtuale) non consentiva le totalizzazioni.
 - La visualizzazione dei totali adesso avviene con il numero corretto di decimali (precedentemente era fissato a 2)

## Versione 1.1.l
 - Attivata possibilità di espansione livelli ulteriori di alberi ad espansione dinamica anche nel caso di raggiunto "MaxDepth". Viene espanso il livello successivo o anche i livelli ulteriori nel caso in cui l'Xml di definizione del sottoramo dell'albero sia multivello
 - Corretto errore su mancata espansione dinamica di un albero in una sottosezione massimizzata
 - Corretto errore "Access Violation" in caso di gestione eventi legata al componente TabAlbero
 - Aggiunto Attributo "Recursive" su Setup Albero. Esso consente di bloccare l'espansione di nodi figlio nel caso in cui esista un Antenato avente stesso Tipo,Parametro,Codice. Sono esclusi dalle valutazioni (e vengono quindi sempre espansi) i nodi che hanno Tipo non valorizzato.
L'espansione del nodo riguarda sia gli alberi ad Espansione Dinamica che gli alberi ad Espansione Convenzionale. Nel caso di visualizzazione dell'albero attraverso altri componenti (es : Visualizza come... Albero/Stella) viene inviato l'Xml già normalizzato secondo il valore impostato nel parametro "Recursive" : 
 * Recursive="Yes|No"
 * Yes = Albero con ricorsione (Default)
 * No  = Albero senza ricorsione

## Versione 1.1.m
 - Inserito nuovo componente PDF. Consente di visualizzare documenti PDF all'interno di una scheda senza istanziare Internet Explorer. Ciò si è reso necessario per problemi di stabilità di Adobe Acrobat Reader 6.0 all'interno di Internet Explorer all'interno di una sottosezione di una scheda.
Es : 
 :  : G.SUB.PDF Tit="Esempio PDF"
::D.PDF.URL http://172.16.2.13/cubi/A.PDF

>N.B. :  L'Istruzione URL può contenere sia percorsi di rete che URL. Se trattasi di URL è obbligatorio inserire l'URL comprensiva di http://

 - Modificato criterio di espansione alberi ad espansione dinamica. Quando si preme il tasto "Espandi Tutto", se vi sono nodi figli già caricati vengono ora espansi tutti (fino all'ultimo livello
  caricato) ed ogni ulteriore espansione (nodi non ancora caricati) implica l'espansione fino al livello massimo presente nell'xml ricevuto da includere nell'albero oggetto.
 - Corretto errore su mappatura tasti funzionali da F13 a F24 sulla bottoniera costruita da UIPOPUP (J1 KEY *Fxx)
 - Monitorato errore in caso di distruzione componente prima della ricezione dell'xml a lui destinato
L'errore (comunque non bloccante) occorreva quando l'utente scatenava eventi multipli (i.e. selezione dei nodi di un albero con eventi) più velocemente del tempo necessario al sistema AS/400 per la generazione e l'invio dell'Xml. Quando il documento Xml veniva ritornato al componente richiedente, il componente richiedente era già stato distrutto causando un AV
 - Corretto errore in alberi ad espansione dinamica nel caso in cui l'albero contenesse il solo root node

## Versione 1.1.n
 - Corretto errore AV se "doppio click" su di un Tabsheet non ancora caricato
 - Ripristinata (era stata eliminata nella versione 1.1.m) la sostituzione delle variabili di scheda all'interno di un Xml "Dati" presente nell'Xml di definizione Scheda. La sostituzione delle variabili tuttavia non avviene nel caso in cui l'Xml "Dati" sia relativo ad una Matrice, poichè la simbologia di definizione degli "oggetti variabili" per record coincide con la simbologia di definizione delle variabili di scheda.
 - Eliminato tasto "Refresh (F5)" nel caso in cui l'Xml di scheda non provenga da un servizio, ma sia stato generato da un "programma client". L'identificazione avviene mediante l'esame della stringa di Funzione nella quale il secondo parametro identifica il servizio. Se esso è vuoto non è possibile effettuare il "Refresh".
Es :  F(EXD;*SCO;) --> Refresh Consentito
     F(EXB;;)     --> Refresh Disabilitato

## Versione 1.1.o
 - Eliminato AV se Richiamo "Visualizza come..." su di un componente il cui Xml è definito all'interno dello script della scheda e non era presente un nodo Service con la funzione associata. Il nodo Service viene ora costruito automaticamente per consentire la funzionalità di "Visualizza come..."
 - Inserita Risoluzione Nomi/Valori variabili nel richiamo di funzioni associate a bottoniera, a eventi DragAndDrop su Albero, ad Azioni definite nel Nodo Actions di un documento Xml
 - Inserita Gestione Evento Click su Bottoniera
 - Inserita Gestione Evento Click su Matrice
 - Inserita Gestione Notify anche in richiamo azioni da Componenti (es :  Bottoniera, Label)
 - Inserita possibilità di specificare eventi RETURN multipli

>N.B. :  Il titolo del tabsheet specificato nell'attributo Where o nel parametro Notify NON DEVE comprendere il carattere di backslash "\". La limitazione occorre ovviamente solo per gli eventi RETURN.
Comportamenti Dinamici su altri eventi (CLICK,DBLCLICK,...) non sono soggetti a questa restrizione.

 - Inserito Popup in Bottoniera

## Versione 1.1.p
 - Aggiunta la funzione DoPopUp per la gestione centralizzata del PopUp di componente.
 - Inserita Gestione Evento doppio Click su Immagine
 - Inserita Gestione Evento doppio Click su Testo (componente Label)
 - Ripristinata la gestione del "fuoco" di finestra di Smetray corretta. Smetray non perdeva mai il fuoco anche in caso di creazione di una finestra Java

## Versione 1.1.q
 - Corretto errore in mancata visualizzazione Popup se assente o Tipo o Parametro o Codice.
Prima il popup veniva visualizzato solo se erano presenti tutti e tre i valori
 - Aggiunta Gestione Popup in componenti Image e ImageList
 - La ricerca del TabSheet di una scheda è ora "case insensitive"
 - Aggiunta gestione su tutti gli eventi di tutti i componenti del parametro "Exec" che può essere associato ad un evento G.DIN. L'Exec scatena il richiamo di un'azione ed è alternativo alla
  specifica del parametro Where. Può quindi essere utilizzato per richiamare (ad esempio) una nuova scheda allo scatenarsi di un evento su di un componente.
 - Corretto Errore di Access Violation su pressione Pulsanti di Espansione/Collassamento Alberi introdotto nella versione 1.1.o
 - Inserita possibilità di stampare la singola sottosezione mediante il componente "Form"
 - Evidenziato il Tabsheet Attivo

## Versione 1.1.r
 - Migliorata la politica di gestione dei fuochi delle finestre.
 - Aggiunta la gestione degli eventi Click e DblClick da script di scheda per il componente Grafico. E' stato anche definito un comportamento di default per i medesimi eventi in assenza di specifica nello script di scheda.
 - Aggiunto il popup alla pressione del tasto destro del mouse per le serie del componente Grafico.
 - Aggiunta la possibilità di definire un tipo di grafico a punti tramite lo script di scheda (Immettere "POINT" come tipo).
 - Rimossa la barra a fondo tabella che rimaneva anche in assenza di filtri.
 - Corretto un errore che richiedeva "Asse" e "Serie" anche se esplicitamente definiti nel componente Grafico.
 - Corretto un errore che impediva la visualizzazione di tabelle in caso di data non nulla ma formata da tutti zeri.
 - Ricostruito il modulo per l'esportazione in Excel : 
 -- L'esportazione consente sempre di generare un file xls (non formattato), anche in assenza di una "suite" di office di qualsiasi tipo. E' stata realizzata l'integrazione con Openoffice e Office per qualsiasi versione. In caso fosse rilevata la presenza di una "suite office" il file xls generato viene automaticamente formattato (autofit colonne, grassetto, ecc...).

## Versione 1.1.s
 - Modificato il modulo di esportazione in Excel : 
L'esportazione in assenza di una "suite" office avviene in SpreadSheetML (XML) già formattato, così come se è rilevata la presenza di Office 2003/OpenOffice 2.0 o superiori.
 - Corretto un errore nel componente Grafico che non consentiva la lettura delle colonne da usare come serie in caso di specifica di serie multiple.

## Versione 1.1.t
 - Corretto un errore sulla esportazione di celle numeriche in Excel
 - Ora se è già attivo un processo di excel o openoffice il documento excel esportato viene aperto tramite questo
 - Aggiunto il setup al semaforo. Ora è possibile specificare le seguenti opzioni sul testo : 
 -- FontName (Default Arial)
 -- FontColor (Default Black)
 -- Text (Permette di stabilire se rendere visibile la label sul semaforo con Yes|No. Default Yes)
 -- FontSize (Default Autoset)
 - Aggiunto un modulo di System Information. E' in grado di recuperare informazioni sulla versione di Office, Openoffice, Acrobat Reader, Java, IBM Client Access e Sistema operativo.
 - Corretto un altro errore che impediva la visualizzazione di tabelle in caso di data mal formata.

## Versione 1.1.u
 - Aggiunto Attributo Id nella definizione delle sottosezioni (G.SEZ). L'attributo Id identifica la sottosezione. E' facoltativo e, se mancante, viene impostato al valore dell'attributo Tit che identifica la descrizione che viene visualizzata sul Tabsheet. Nelle istruzioni G.DIN occorre quindi fare riferimenti all'attributo Id (se presente) e non più a Tit
 - Eliminato Flickering durante caricamento Matrice
 - Corretto Errore Aggiornamento Multiplo di sottosezioni albero se Ingrandimento o Riduzione di una sottosezione di tipo Scheda in cui gli alberi erano contenuti

## Versione 1.1.v
 - Ricostruita la funzionalità di Autofit per la matrice in modo da tenere in considerazione la presenza di icone nei campi e nelle intestazioni, dei cambi di font su singola colonna, della presenza o meno di oggetti tipizzati indiretti e delle barre del filtering.
 - Aggiunta l'opzione Autofit nel Setup della matrice (Autofit=Yes/No. Default :  Yes)
 - L'attributo Lun presente nell'Xml della matrice ora può essere presente privo di valore.
Se l'opzione Autofit della matrice è disabilitata, le colonne della medesima saranno dimensionate sul numero di caratteri passati nel campo Lun dell'Xml della matrice o, se la lunghezza della intestazione è superiore a quel numero, sulla lunghezza della stessa intestazione.
Se per una colonna non è presente un valore per l'attributo Lun, per quella colonna sarà attivato l'autofit.
 - E' stata forzata l'interpretazione delle intestazioni delle colonne di una matrice come testo durante l'esportazione in excel.
 - E' ora possibile non specificare un valore per l'attributo Where per inizializzare cmq le variabili senza indurre dinamismo su alcuna sezione.
 - Aggiunta la risoluzione delle variabili su Popup. Le variabili possono essere SOLO variabili di scheda e non di sezione.
 - Fissato un problema sull'xml all'inserimento di un nuovo record tramite una matrice.

## Versione 1.1.w 01/04/2005
 - Ristrutturata la parte di inserimento da matrice. Ora molto più stabile.
 - Gestita la cancellazione, l'inserimento e l'editing dei record da matrice tramite comunicazione con AS. Introdotta una semplice e temporanea gestione degli errori.
 - Aggiunta la gestione della "ricerca" nei campi tipizzati, per la modifica e l'inserimento tramite matrice.
 - Modificato il meccanismi di comunicazione SINCRONA Xml. Customizzato il timeout per la risposta.
 - Variabili nei PopUp :  Nel popup si possono ora usare anche variabili di Loocup, Componente e SEZIONE. Il comportamento delle voci di menù di popup può quindi essere diverso a seconda della sezione in cui viene richiamato.
 - Risolto l'annoso problema "sulla lentezza" alla pressione del tasto destro del mouse in caso di componenti nidificati in delphi 5.
 - Aggiunto l'aggiornamento dell'Xml della scheda in caso di editing, inserimento e cancellazione di un record.
 - Risolto un problema sul passaggio delle variabili tra [].

## Versione 1.1.z 06/04/2005
 - Risolto un baco sulla replicazione dell'XML in inserimento, editing e cancellazione da matrice.
Ora vengono gestiti correttamente anche decimali e date.
 - Modificata lievemente la gestione dei fuochi delle finestre della scheda di Looc.up.
Il fuoco della tastiera viene passato correttamente alla finestra aperta.
 - Modificato il modulo di esportazione delle matrici in excel, in modo da lasciare in primo piano l'applicazione che ha aperto il foglio di calcolo.
 - Modificato il componente HTM che è ora in grado di visualizzare un xml di qualsiasi tipo.
 - Aggiunto l'attributo "Lib" nel nodo "Layout" dell'xml della scheda in modo che si possa specificare la libreria in cui è inclusa la scheda. Il valore del nuovo attributo deve avere lo stesso formato dell'attributo "NomeScheda".
 - La risoluzione delle variabili è ora in grado di discernere tra nomi di variabili e valori numerici tra parentesi []. La sostituzione con BLANK viene eseguita solo se si tratta di nomi di variabili inesistenti o non ancora assegnate.
 - Inserimento tramite matrice :  Aggiunta la gestione degli errori, la differenziazione dei campi tramite colore, autofocus su campi editabili, autoset del "case" di un campo e comunicazione del setup da parte del servizio di updating associato alla matrice.
 - Risolto un grosso memory leak inerente al componente matrice.
 - Componente matrice :  abilitazione del tasto enter per confermare l'editing o l'inserimento di un nuovo record.
 - Inserimento tramite matrice :  Aggiunta la possibilità di definire dei valori di default per i campi, oltre al significato del campo (KEY, altro). Se un valore di default è specificato per un campo all'atto dell'inserimento di un nuovo record, il campo verrà inizializzato con il suo valore di default.
 - Componente Matrice :  aggiunto l'attributo "Context" nel Setup del componente. Indica al servizio di updating a quale tabella/contesto deve applicare le modifiche e il setup.
 - Componente Grafico :  aggiunto l'attributo "Stack" nel Setup del componente per grafici di tipo VBAR e HBAR. I valori possono essere :  NONE|STACKED|STACKED100|SIDEALL

## Versione 1.2.a 06/04/2005
 - Sistemata la nuova gestione dei fuochi. Smetray ora è in grado di mettere a fuoco anche finestre delle altre parti di Looc.up.
 - Sistemato un problema che bloccava l'utilizzo dei tasti funzione sulla scheda.
 - Limitato a 1000 il numero di colonne della matrice in memoria nel caso di Inversione Righe/Colonne del componente grafico. Il limite fisico del componente è 1024 colonne.
 - Smetray riprende il fuoco anche in caso di utilizzo del metodo GetSyncronousXml.

## Versione 1.2.b 08/04/2005
 - Modificata la gestione della risoluzione delle variabili.
 - Risolto un problema sull'autofocus nei campi editabili della matrice.

## Versione 1.2.c 13/04/2005
 - Matrice :  risolto un problema che bloccava la matrice in caso di ricerca in un campo.
 - Matrice :  Aggiunta una barra che raccoglie gli errori nel caso di inserimento.
 - Matrice :  Il pannello di debug per le matrici di inserimento è nascosto. Per mostrarlo si può premere Ctrl-F6.
 - Matrice :  Aggiunto un subcomponente per la gestione degli errori, uno per la gestione degli stili delle singole celle. In caso di errore in inserimento i campi "sbagliati" vengono marcati in rosso.
 - Matrice :  Sistemati i distruttori delle liste di stile per evitare memory leaks.
 - Modificata la risoluzione delle variabili di scheda, sezione, componente in modo da prevedere fino a 10 livelli di annidamento. Prima non era previsto alcun livello di annidamento.
 - Menù :  Aggiunta una prima gestione dei menù unificati tra scheda e Looc.up-java.

## Versione 1.2.d 14/04/2005
 - Risolto un baco sulla matrice. In caso di assenza di tutti i campi nelle righe ora vengono aggiunti i campi mancanti vuoti.
 - Risolto un piccolo baco in un servizio AS sul caricamento delle *TBL.
 - Aggiunta al progetto una dll di servizio fuoco finestre.
 - Primo restyling della grafica della scheda per uniformarsi alla main window di Looc.up.
 - La scheda di base del componente EXD viene ora creata dinamicamente.
 - Modifica dell'identificazione della finestra tramite codice dello stack. Oltre che al codice finestra e stack viene usato anche l'id di sessione.

## Versione 1.2.e 15/04/2005
 - Risolti dei bachi sullo stile delle finestre della scheda. In particolare la header bar visualizza correttamente gli oggetti e i titoli.
 - Risolto un problema sui menù unificati. Vengono gestite anche le voci in disable.
 - Matrice :  Aggiunta la gestione dei record pendenti in aggiornamento. Chiamando un refresh di sezione dinamico, le modifiche non vanno perse ma viene generato un messaggio di avvertimento.
 - Matrice :  Aggiunta la risoluzione delle variabili all'interno del setup della matrice. E' prevista l'estensione di questa caratteristica a tutti i componenti, date le potenzialità.
 - Conclusa ed estesa la dll di servizio fuochi in Delphi.
 - Smetray utilizza ora la stessa libreria per gestire i fuochi delle sue finestre in apertura.

## Versione 1.2.f 18/04/2005
 - Risolto un problema sull'evento changing degli alberi. Doveva scattare solo in presenza di matrici di inserimento.
 - Completato il restyle della header bar della scheda :  Titoli, e 4 icone oggetto come nella main window.
 - Completato il restyle della matrice. I colori e gli stili compresi dei bordi sono stati uniformati alla matrice Java.
 - Aggiunta l'apertura della scheda oggetto sulle iconcine della header bar della scheda. Facendo click sulle icone o sulle label nella header bar, sono abilitati i popup menù e l'apertura della scheda dell'oggetto di destinazione.
 - Aggiunto un setup alla bottoniera : 
 -- Flat, che consente di avere bottoni piatti senza bordo (Valori :  Yes/No. Default :  No)
 -- FillSpace, che forza la altezza dei bottoni in modo che occupino tutta la sezione della bottoniera (Valori :  Yes/No. Default :  No)
 -- ShowText, che indica la presenza del testo su bottone (Valori :  Yes/No. Default :  Yes).
 -  Estesa ad ogni componente la possibilità di introdurre variabili nel setup.
Le funzionalità sono così molto ampliate. E' possibile usare ogni tipo di variabile a livello di nodo di setup. Verranno tradotte come nei casi normali.

## Versione 1.2.g 21/04/2005
 - Completa gestione messaggi di avvertimento nel caso di aggiornamenti di sezioni nelle quali vi è una matrice in corso di editazione
 - Ridotto il numero di bordi visibili in caso di schede indentate (schede di schede)
 - Corretto errore (index out of bounds) nel caso di tabulazione su matrice con alcuni campi non editabili
 - E' ora possibile visualizzare correttamente Menù di Popup anche su celle non editabili
 - E' ora possibile utilizzare il parametro TO(*REQ) anche nei Popup di oggetto e negli UI_popup correlati
 - Ottimizzata gestione fuochi finestre

## Versione 1.2.h 27/04/2005
 - Sistemata l'inversione dei colori per i cruscotti.
 - Aggiunta l'inversione delle soglie e colori per i semafori.
 - Conclusa una versione dell'updater che non sostituisce i caratteri speciali nell'xml.
 - Risolto un fastidioso Access Violation degli alberi dinamici sull'evento onchange in alcune condizioni.
 - Sistemato un baco sull'autofit dei bottoni della bottoniera.
 - Aggiunta una voce di setup nel bottone per rimuovere l'icona.
 - Aggiunte le voci di setup relative al Font nella bottoniera.
 - Risolto un "vecchio" baco sulla scelta dei colori nello script di scheda.

## Versione 1.2.i 02/05/2005
 - Risolto un problema di loop nella "risalita" dei componenti in cerca di matrici di aggiornamento.
 - Cambiato il componente del browser integrato.
 - Aggiunta la progress bar al componente browser con relativo setup.
 - Aggiunto la barra degli indirizzi al componente browser.
 - Aggiunto un pulsante di Start della navigazione del browser.
 - Aggiunte le voci di Setup al componente Browser :  ShowBar (Yes/No Default :  No) che mostra la footer bar del nuovo browser, Browsing (Yes/No Default : No) che abilita/disabilita la barra di navigazione, FixedSize (Yes/No Default :  No) che abilita disabilita la presenza delle barre di scorrimento, Zoom (Yes/No Default :  No) che mostra una "tracking bar" per ingrandire il carattere nel browser e ZoomStart (0-4 Default :  0) che impone la dimensione del carattere nel browser alla partenza.
 - Risolto un altro Access Violation dell'albero dinamico che si presentava a causa del message handler del vecchio browser.

## Versione 1.2.j 09/05/2005
 - Risolto un errore nel caso di matrice/grafico/excel con campi numerici con decimali specificati nel formato iii;ddd dove iii=cifre intere, ddd=cifre decimali (facoltative).

## Versione 1.2.k 10/05/2005
 - Velocizzato carimento matrice
 - Eliminato AV nel caso di presenza di oggetti variabili riferiti a campi inesistenti
 - Risolto un problema di excel sulle celle numeriche che venivano esportate con allineamento a sinistra.
 - Rimossi gli apici in assenza di dati nella cella nell'esportazione in excel.
 - Il nuovo componente browser gestisce ora correttamente la barra di scorrimento risolvendo anche un memory leak.
 - Sistemato l'autofit delle colonne delle matrici in caso di "default sorting" attivato. Viene ora considerato anche il "triangolino" di visualizzazione ordinamento per determinare la larghezza della colonna.
 - Introdotta una prima versione della formattazione condizionale degli stili delle matrici a livello di colonna, riga e cella.
I dettagli sulla sintassi non vengono forniti in quanto non definitiva.

## Versione 1.2.l 11/05/2005
 - Introdotta la possibiltà di sottostringare le variabili. La sintassi è la seguente :  [<nomevariabile> : <posizioneiniziale> : <posizionefinale>], dove : 
<nomevariabile> 	= E' il nome della variabile a cui si fa riferimento
<posizioneiniziale>	= E' la posizione iniziale della stringa (facoltativa :  se non indicata verrà ritornata la stringa completa)
<posizionefinale>	= E' la posizione finale della stringa  (facoltativa :  se non indicata verranno ritornati tutti i caratteri a partire dalla posizione iniziale)

ATTENZIONE!!! La sintassi è cambiata. Quella corretta è definita nella versione 1.2.m

## Versione 1.2.m 12/05/2005
 - Sistemato un problema sull'autorefresh delle sezioni. La scheda riprendeva sempre il fuoco.
 - Modificata la sottostringatura delle variabili. La nuova sintassi è la seguente :  [<nomevariabile> : <posizioneiniziale> : <numerocaratteri>], dove : 
<nomevariabile> 	= E' il nome della variabile a cui si fa riferimento
<posizioneiniziale>	= E' la posizione iniziale della stringa (facoltativa :  se non indicata verrà ritornata la stringa completa)
<numerocaratteri>	= E' il numero dei caratteri da ritornare (facoltativa :  se non indicata verranno ritornati tutti i caratteri a partire dalla posizione iniziale)
 - Risolto un problema sullo zoom del webbrowser.
Al massimizzare e minimizzare della sezione che contiene il componente il contenuto non appariva.
 - Standardizzato i componenti matrice ed excel per utilizzare le impostazioni internazionali su separatori di Data, Decimali e Migliaia.
 - Ristrutturato il codice del componente HTML per renderlo più efficace.

## Versione 1.2.n 18/05/2005
 - Sistemato un Access Violation se in una formattazione condizionale veniva utilizzato uno stile senza definizione di font.
 - Aggiunto un attributo di setup che consente l'inversione nella sequenza di presentazione dei Tabsheet di un tabalbero.
Sintassi : 
 * InvertTabs="Yes|No"
 * Yes=Viene invertito l'ordine di presentazione dei tabsheet
 * No (default)=L'ordine di presentazione dei tabsheet viene mantenuto

 - Risolto un problema in esportazione in Excel. Le celle alfanumeriche mancanti di dati venivano riempite con il valore precedente.
 - Aggiunta una bottoniera laterale al componente grafico. Aggiunti due pulsanti, uno per la visualizzazione della bottoniera in testa al grafico, l'altro per l'apertura del selettore di assi e serie. La visualizzazione della bottoniera laterale è condizionata dall'attributo ShowCommands che precedentemente condizionava la bottoniera superiore. Non è più possibile quindi condizionare l'emissione della bottoniera superiore da script, ma l'apertura è a richiesta dell'utente attivando il corrispondente bottone nella bottoniera laterale.
 - Aggiunta la funzionalità di selezione/deselezione di tutte le serie nel selettore del componente grafico.
 - Modificata la visualizzazione nel grafico. Ora viene eseguita attraverso paginazione dei punti delle serie.
E' presente anche una barra di scorrimento la cui posizione dipende dal tipo di grafico e dalla pagina corrente.
 - Aggiunto un algoritmo di selezione dinamica dei punti per serie visualizzabili in una singola pagina del componente grafico.
 - Aggiunti due attributi di setup del grafico. FitAll per non avere la paginazione e PointsPerPage per impostare un numero fisso di punti per serie per pagina.
Sintassi : 
 * FitAll="Yes|No"
 * No (default)=viene utilizzato l'algoritmo di determinazione del numero di punti serie per pagina
 * Yes=tutti punti i punti serie vengono visualizzati su di una singola pagina
 * PointsPerPage="Numero intero"
 * Numero intero :  rappresenta il numero di punti per serie visualizzati in ogni pagina. Se il valore è superiore a 0 non viene applicato l'algoritmo di determinazione del numero di punti.
In caso contratio viene applicato l'algoritmo.

 - Risolti alcuni Access Violation relativi alla pressione del tasto sinistro su bordi e header del componente matrice.
 - Aggiunta la possibilità di richiamare un menù contestuale dall'header di colonna per selezionare assi e serie.
 - Trovato e risolto un problema sull'autorefresh delle sezioni. Il fuoco passava a loocup quando la sezione refreshante era di tipo scheda.
 - Trovato e risolto un problema nella identificazione generale delle serie e degli assi nei grafici : 
Se due colonne avevano una parte del nome uguale venivano inserite serie non corrette.

## Versione 1.2.o 19/05/2005
 - Corretto dinamismo indotto automaticamente in caso di alberi multipli in sottosezioni diverse della stessa sezione. All'atto della selezione di un elemento di un componente di una sottosezione, negli alberi delle altre sottosezioni della stessa sezione veniva erroneamente selezionato automaticamente il primo elemento anche se non era stato specificato il parametro SelectFirst.
 - Corretto AV e comportamenti anomali ed imprevedibili nel caso in cui una sottoscheda venisse contemporamente aggiornata da più componenti.
 - Migliorata la gestione del contatore Richieste/Risposte. Ora anche le risposte non gestibili poichè il componente di destinazione è inesistente incrementano il contatore risposte.
 - Invertito il default del Setup FitAll del grafico. Se non specificato ora il default è il valore 'Yes'. Per attivare la divisione in pagine del contenuto del grafico è quindi NECESSARIO specificare l'attributo FitAll valorizzato a 'No'.
 - Conclusa la gestione del colore da Setup di scheda. Ora è possibile specificare diversi formati : 
  -- il formato già in uso
  -- i valori letterali del tipo D.NOMECOLORE dove nomecolore è il nome di un colore di sistema
  -- il nuovo formato non posizionale del tipo 'RnnnGnnnBnnn' dove con 'nnn' si indica un numero di tre cifre rappresentante l'intensità del colore sul canale indicato dalla lettera che precede il numero.
 - Implementata la gestione degli stili nella matrice  In ogni scripd di scheda è possibile definire più stili semplicemente includendo un XML del tipo : 
 Styles
    Style Name="..." BackColor="..." FontName="..." FontSize=".." FontColor="..." FontItalic="..." FontULine="..." FontBold="..."
    Style Name="..." BackColor="..." FontName="..." FontSize=".." FontColor="..." FontItalic="..." FontULine="..." FontBold="..."
 Styles
 -- Ogni voce è facoltativa fatta eccezione per il Nome dello stile che deve essere presente. Per le voci Fontitalic, FontUline, FontBold è possibile specificare Yes o No. Nel caso in cui venga specificato Yes, all'applicazione dello stile su una cella verrà aggiunto l'attributo corrispondente (ad esempio se la cella è già in corsivo, e si definisce uno stile che ha Yes nell'attributo Grassetto, la cella verrà visualizzata in Corsivo e Grassetto). Nel caso non venga specificato nell'XML una voce relativa ad uno di questi attributi quell'attributo non verrà applicato. Nel caso in cui venga specificato No, all'applicazione dello stile su una cella, l'attributo verrà rimosso (Ad esempio se la cella è già in grassetto, e si definisce uno stile che ha No nell'attributo Grassetto, la cella verrà visualizzata con carattere normale).
 -- E' possibile specificare gli stili anche usando la sintassi G.STY.
Sono presenti alcuni stili di default : 
 * '*ERROR' Visualizza una cella con sfondo rosso.
 * '*BOLD' Visualizza il testo in grassetto.
 * '*UNDERLINE' Visualizza il testo sottolineato.
 * '*ITALIC' Visualizza il testo in corsivo.
 -- E' possibile sostituire i valori di default di questi stili, semplicemente rimappandoli creando uno stile con lo stesso nome nello script di una scheda. Come già precedentemente accennato gli stili sono "addiditivi".
 - Ultimata la formattazione condizionale delle celle delle matrici. La sintassi, da utilizzare nel setup della matrice è la seguente : 
 -- Styles="NomeStile" dove NomeStile può essere un nome di uno stile precedentemente definito, oppure, può essere una formula condizionale che restituisce uno o nessuno stile.
 -- Le formule condizionali sono del tipo :  "Campo={CondizioneStile}|Campo2={CondizioneStile2}" dove, 'Campo' rappresenta un campo di una matrice o *ALL per indicare tutti i campi, 'CondizioneStile' rappresenta una espressione condizionale, '|' è il carattere che divide l'applicazione di uno stile da un altro. Gli stili vengono applicati in sequenza e quelli prima definiti hanno la priorità
 -- Le espressioni condizionali sono del tipo :  "Valore1 Operatore Valore2;StileTrue;StileFalse" dove, 'Valore1' e 'Valore2' possono essere valori numerici o i valore dei campi della matrice (tra parentesi quadre), 'Operatore' è un operatore logico tra :  AND, OR, NOT, EQ (uguale), GT (maggiore), LT (minore), NE (diverso), LE (minore o uguale), GE (maggiore o uguale).
'StileTrue' (facoltativo) è il nome dello stile che verrà ritornato quando la condizione è vera , 'StileFalse' (facoltativo) è il nome dello stile che verrà ritornato quando la condizione è falsa.

Esempio di formattazione condizionale : 
Styles="£RITDS=DEFAULT|*ALL={[£RITEL] EQ XXX;*ERROR}|T$V5DS={[£RITEL] EQ FAT;Test01;Test02}|*ALL=Test04"

 - E' stata aggiunta la possibilità di definire direttamente uno stile nell'XML della matrice. Nei nodi "Riga" e "Colonna" è sufficiente aggiungere l'attributo Style="Nomestile", dove Nomestile è il nome di uno stile di default o definito nella scheda.
 - E' stato aggiunta la possibilità di specificare *ALL nella sintassi dell'attributo "DftTotals" per indicare di mostrare i totali per tutte le colonne possibili.
