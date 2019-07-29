# Come scrivere una /COPY di buona "qualità"
La corretta "procedura" di creazione di una /COPY si sviluppa in numerosi punti : 
* creazione della /COPY vera e propria
* creazione del "TST" (programma di simulazione che consente di testare in input e output il suo funzionamento) se necessario
* creazione dello unit test
** creazione della base
** creazione dello script con i test
* scrittura della documentazione attiva relativa (documentazione specifica nel file DOC_OGG, accessibile dal TST tramite la sequenza di tasti F2-F1)
* Inserimento del nome della /COPY nel programma BRAR19 (che contiene l'elenco di tutte le /COPY)
* Scrittura della NEWS relativa
Una volta soddisfatti tutti questi punti, la /COPY si può considerare "standard".

La misurazione della qualità di una /COPY è basata sulla soddisfazione dei precedenti requisiti

## Caratteristiche della /copy vera e propria
Denominazione : 
* Se la /COPY corrisponde all'interfaccia di un oggetto : 
** La /COPY va chiamata con codice £Ixx dove xx è il codice oggetto. Per le eventuali specifiche di D si usa la codifica £IxxDS. NOTA BENE :  in passato si è adottato il prefisso £IF concatenato ad un codice che riconducesse solo intuitivamente all'oggetto interessato (es. £IFCON per i CN o £IFCCO per i cicli di collaudo). Va altresi notato che a volte sorge l'esigenza di avere un'interfaccia su un archivio che non corrisponde ad un oggetto preciso (es. Note strutturate o parametri), in questi casi sono state adottate codifiche particolari, che vanno di volta in volta concordate.
* Se la /COPY corrisponde ad una procedura : 
** Se esiste anche una corrispondente /COPY di specifiche C, va denominata con lo stesso prefisso con aggiunto "P" per le specifiche P della procedura vera e propria e "PD" per le specifiche D di definizione della procedura
** Viceversa se è una procedura che non ha corrispondenti /COPY C, si segue la codifica £Pnnn, dove nnn indica il numero progressivo da aggiungere (es. se sono arrivato £P040, dovrò creare la £P041). Le specifiche di definizione assumeranno codifica £PnnnD (quindi es. £P041 e £P041D).
* Altrimenti
** Se la /COPY appartiene all'applicazione B£, va seguita la numerazione £Knn (es. se l'ultima /COPY inserita fosse la £K40, dovrei inserire la £K41). Le specifiche di definizione, qualora necessarie, assumeranno la codifica £KnnDS. NOTA BENE :  prima di utilizzare il prefisso K era in utilizzo il prefisso G.
** Se la /COPY appartiene ad un'altra applicazione, va seguita la codifica data dal prefisso corrispondente all'applicazione più una lettera o un numero (es. £BRA è la prima /COPY dell'applicazione BR). NOTA BENE :  in alcuni casi sono state usate tutte le lettere possibili e sono state quindi create delle eccezioni (es. per l'applicazione C5 si è passati al prefisso C6). Nel caso sorga questa questione bisogna concordare con il laboratorio quale codifica adottare.

File di appartenenza : 
* QPROGEN per le /COPY che corrispondono a procedure
* QILEGEN per tutte le altre

Le nuove /COPY devono avere una struttura standard.
La nomenclatura prevede l'utilizzo di due DS. Una DS di input (con tutti i campi di input) e una Ds di output (con tutti i campi di output).
I nomi dovrebbero rispettare questa nomenclatura (ipotizzando una copy £xxx) : 
> DS di Input
D£xxxDI           DS           512
campi specifici di input
D £xxxI_yy                      yy
 DS di Output
D£xxxDO           DS           512
 campi specifici di output
D £xxxO_yy                      yy

Note : 
Se alcuni campi (di input o di output) sono rilevanti solo per alcune funzioni/metodo, indicarlo nella documentazione.
Se la stessa informazione deve essere presente sia in input che in output, creare due campi distinti (uno nella Ds di input e uno in quella di output).
La lunghezza della DS dipende dalle informazioni che deve contenere, il default è 512.

Questa dovrebbe essere la struttura del richiamo del programma di gestione della /COPY : 
>C     £xxx          BEGSR
C                   EVAL      £xxxPG='B£xxxG'
C                   CALL      £xxxPG
C                   PARM                    £xxxDI
C                   PARM                    £xxxDO
C                   EVAL      *IN35=£xxxO_35
C                   EVAL      *IN36=£xxxO_36

Il programma richiamato ha la struttura B£xxxG nel caso di /COPY generiche (le £Gxx, £Hxx e £Kxx).
Avrà invece la struttura yyxxx0 nel caso di /COPY specifiche di applicazione (yy= applicazione).
La /COPY £Hxx sono un'estensione della corrispondente £Gxx.

Non va condizionata la CALL mediante l'utilizzo di un indicatore (come avveniva invece in passato).

Al richiamo della /COPY va pulita la DS di output e all'uscita va pulita invece quella di input.

Per quel che riguarda la DS di input, va affrontata anche la questione dell'inizializzazione. Si possono porre due valutazioni differenti : 
* Se la DS non è molto lunga e/o viene chiamata molte volte si può valutare di definirla con attributo INZ. In questo caso sarà necessario nell'entry del pgm di gestione dalla /COPY sarà necessario far transitare la DS da una variabile d'appoggio (si veda l'esempio riportato a seguite).
* Viceversa si può valutare di non prevedere questa possibilità, con l'obbligo a quel punto di inizializzare la DS in ogni pgm che utilizza la /COPY interessata.

>C     £xxxDI        PARM      £xxxDI        §xxxDI
 


Sono presenti i 3 seguenti prototipi che vanno utilizzati in caso di creazione di una nuova /COPY (contengono infatti i campi obbligatori/facoltativi con la nomenclatura corretta).
 :  : DEC T(MB) P(QILEGEN) K(£XXX)
 :  : DEC T(MB) P(QILEGEN) K(£XXXDS)
 :  : DEC T(MB) P(QSRCGEN) K(B£XXXG)

## Caratteristiche del TST
Un buon programma di simulazione (TST) deve contenere : 
* Tempi in millisecondi :  è implementato il controllo delle performance di esecuzione in millisecondi.
* MDV multipla :  viene gestita la memorizzazione di dati video multipla.
* FEM controllo FU/ME :  la chiamata della /COPY avviene tramite l'utilizzo di Funzione e Metodo.
* F02=Navigazione :  la pressione del tasto F02 dal TST fa entrare nel menù navigazione.
* F03=Uscita :  la pressione del tasto F03 fa uscire dal TST.
* F04=Controllo Campi :  la pressione del tasto F04 dal TST mostra quali campi sono di inserimento obbligatorio.
* F05=Dati tecnici :  la pressione del tasto F05 dal TST visualizza il nome delle variabili associate ai campi.
* F10=Nessun controllo :  la pressione del tasto F10 dal TST elimina il controllo di correttezza sui campi, utile per effettuare test di funzionamento con input scorretti.
* F12=Ritorno :  la pressione del tasto F12 dal TST fa tornare alla schermata precedente.
* F16=Sorgente :  la pressione del tasto F16 dal TST mostra il sorgente della /COPY.
* F22=Messaggi :  la pressione del tasto F22 dal TST mostra i messaggi generati.
Nei TST più recenti è implementato anche il tasto **F14**, premendo il quale viene eseguito un test con dati randomizzati, i cui risultati sono visibili attraverso il _Trace'n Play_ di Looc.Up.

Ovviamente la soddisfazione di questi singoli punti concorre al miglioramento del punteggio di qualità complessiva della /COPY.

Esistono i seguenti due prototipi che vanno utilizzati in caso di creazione di una nuova /COPY
 :  : DEC T(MB) P(QSRCGEN) K(TSTXXX)
 :  : DEC T(MB) P(QSRCGEN) K(TSTXXX0V)

# Come Trovare Una /COPY  

| | **Obiettivo** | **Percorso** |
| ---|----|----|
| Elenco delle /COPY | Elenco completo delle /COPY documentate. | Da Looc.Up attraverso il menù _My Loocup_, voce _Servizi e Azioni_, scheda _API_ |
| A partire da un'applicazione | Elenco delle /COPY utilizzate nell'applicazione selezionata.| Da Looc.Up attraverso il menù _My Loocup_, voce _Applicazioni_, selezione di un'Applicazione (es. M5) nel treeview, scheda _Set'n play_, scheda _API_ |
| A partire da un programma | Elenco delle /COPY utilizzate da un programma specifico | Tramite il comando **UP FUN** , Tipo _OJ**, Parametro _*PGM**,  Codice _NomeProgramma** (es. A£FR15X) :  selezionando _Attributi_ dall'interfaccia dell'oggetto vengono visualizzate anche le /COPY utilizzate dal programma. |
| Ricerca nella Documentazione | Scheda di una /COPY specifica tramite le funzionalità di ricerca nella documentazione | Comando _cerca  "Stringa1  e Stringa2" DOC_ . Ad esempio _cerca "memorizzazione e input" DOC esegue una ricerca dei due termini in AND all'interno della Documentazione; è supportato anche l'operatore 'o' per la ricerca in OR) |
| 


## Scheda della /COPY
La scheda di una /COPY è uno strumento di loocup che permette di riassumere, in modo standard, tutte le caratteristiche salienti di una /COPY, nella figura seguente si può vedere un esempio di queste schede.

![A£BASE_023](http://localhost:3000/immagini/A£BASE_SI/AXBASE_023.png)
## Modello dinamico
Tramite il modello dinamico è possibile visualizzare le relazioni che la /COPY ha con il resto del mondo Sme.up (ad esempio in quali programmi è utilizzata.
Per una trattazione di dettaglio del Modello dinamico si rimanda allo specifico paragrafo del documento.

Nell'immagine seguente si possono vedere quali sono le informazioni che si possono trovare in questa scheda.

![A£BASE_024](http://localhost:3000/immagini/A£BASE_SI/AXBASE_024.png)
# Come provare una /COPY
Uno dei principali fattori di qualità di una /COPY è rappresentato dalla presenza o meno di un programma di test. Gran parte delle /COPY in Sme.up hanno associato un programma che  permette di testarne il funzionamento mostrando nel dettaglio, oltre ai valori, anche i nomi delle variabili di input e output che vengono lette o valorizzate. Il nome di questi programmi è solitamente standard ed è nella forma _TST+nome della /COPY senza il carattere £_.

Esempio : 
£G11 :  TSTG11
£OAV :  TSTOAV
£DEC :  TSTDEC

Fanno eccezione  alcuni programmi di test come ad esempio : 
£RITES :  TSTRIT
£DMSG :  TSTDMS
