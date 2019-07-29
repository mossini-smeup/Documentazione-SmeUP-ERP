# TCO - Tipo costo
 :  : DEC T(ST) K(TCO)
## OBIETTIVO
Questa tabella serve a descrivere i Tipi Costo presenti nell'applicazione e di volta in volta utilizzati nelle varie elaborazioni.
## UTILIZZO
L'elemento "nnn" definisce il tipo di costo.
Alcuni campi della tabella sono gestiti dall'applicazione stessa, tuttavia l'utente può modificarne in ogni momento il contenuto, se necessario.
Questi campi mostrano alcuni parametri utilizzati nell'ultima esecuzione del ricalcolo costi. Per una maggiore comprensione degli stessi si rimanda alla documentazione del ricalcolo costi.
Questa tabella è comune all'applicazione dei costi standard (CS) e costi avanzati (D0). Per ogni campo sarà riportata la sigla dell'applicazione in cui è utilizzato
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC DESCRIZIONE
Si inserisce la descrizione del tipo di costo.
_9_Esempio : 
Ele. S92 = Costo STANDARD 1992
Ele. C91 = Costo CONSUNTIVO 1991
Ele. L91 = Costo LIFO 1991
 :  : FLD T$DULC **DATA ULTIMO CALCOLO**
Utilizzo :  CS - D0
Viene memorizzata la data dell'ultimo ricalcolo costi eseguito.
 :  : FLD T$TULC **TIPO ULTIMO CALCOLO (TOTALE/SELETTIVO)**
Utilizzo :  CS
Il contenuto di questo campo indica come è stato eseguito l'ultimo ricalcolo : 
T = ricalcolo totale, ossia eseguito per tutte le parti;
S = ricalcolo selettivo, ossia eseguito solo per alcune parti;
 :  : FLD T$SCLR **SUFFISSO RICARICO COSTI**
Utilizzo :  CS
Viene qui memorizzato il suffisso utilizzato nell'ultimo ricalcolo costi per l'attribuzione delle "ricariche".
 :  : FLD T$SALQ **SUFFISSO ALIQUOTE COSTI**
Utilizzo :  CS
Viene qui memorizzato il suffisso utilizzato nell'ultimo ricalcolo costi per le aliquote orarie dei centri di costo.
 :  : FLD T$TCOJ **COSTO TOTALE**
Indica, per i costi calcolati, se sono memorizzati a valori unitari o totali. Se totali deve essere presente in un indice della IGI un campo quantità, di tipo £Q,  dove viene memorizzata la quantità a cui fanno riferimento i costi. La £G55 ritorna sempre il valore unitario, per avere il valore totale è necessario usare il metodo "TOT".
 :  : FLD T$UTAU **UTENTE AUTORIZZATO**
Utilizzo :  CS - D0
Se questo campo è compilato, l'utente specificato è l'unico abilitato al calcolo del tipo costo che si sta definendo.
In tal modo ci si protegge, ad esempio, da sottomissioni accidentali che possano modificare il contenuto di un costo protetto (esempio il costo standard calcolato a inizio anno)
 :  : FLD T$TCOO **MEMORIZZAZIONE OPERAZIONI**
Utilizzo :  CS
Permette di mantenere, per questo tipo costo e su apposito archivio, il dettaglio del costo alla fase. Ciò, ad esempio, può risultare particolarmente utile per le valorizzazioni del WIP.
I valori possibili sono : 
- ' '  Non memorizza;
- '1'  Memorizza solo quando è richiesta anche la memorizzazione del costo stesso;
- '2'  Memorizza i nuovi valori ad ogni lancio del calcolo (anche se si richiede la sola stampa).
 :  : FLD T$TCOC **MEMORIZZAZIONE TEMPI PER CENTRO**
Utilizzo :  CS
Permette di mantenere su apposito archivio le ore lavoro e macchina totali, per centro di lavoro. Risulta, di conseguenza, possibile il riepilogo per centro di costo e quindi l'analisi degli effetti di un cambio aliquota di un centro su un prodotto.
Valori possibili come sopra.
 :  : FLD T$TCOL **MEMORIZZAZIONE COSTI PER CLASSE**
Utilizzo :  CS
Permette di mantenere su apposito archivio il riepilogo dei costi per classe. In tal modo, ad esempio, risulta  immediata la verifica di incidenza dei costi delle materie prime su un prodotto.
Valori possibili come sopra.
 :  : FLD T$TCOA **TIPO COSTO ASSUNTO**
Utilizzo :  CS - D0
Permette di indicare un tipo costo a cui l'applicazione deve passare ogni volta che non viene trovato il costo nel contenitore richiesto.
_9_Esempio : 
Se chiedo una valorizzazione con costi S93 (standard 93), posso specificare che in mancanza assumo S92 (standard 92) ecc. La tabella a cui rimando potrà a sua volta avere un tipo costo collegato.
Sono gestiti fino ad un massimo di 3 livelli se l'ambiente è SM. Se è S2 sono infiniti e quindi bisogna prestare attenzione a non creare un loop.
Un utilizzo particolare, che si rende possibile mediante questa tecnica, è quello di definire un contenitore di eccezioni (in cui pongo i pochi articoli che voglio modificare per una simulazione), e di associare a questo il contenitore normale, in cui sono contenuti tutti gli articoli. In questo modo il calcolo dei costi risulterà completo e potrò eseguire una simulazione significativa.
 :  : FLD T$MEME **TRACCIA ERRORI**
Utilizzo :  CS
Specifica se si vogliono memorizzare, nell'archivio apposito, gli errori riscontrati durante il calcolo, in modo da poterli poi trattare opportunamente con le funzioni predisposte a tale scopo.
I valori possibili sono : 
- ' ' = non memorizza;
- '1' = memorizza un solo record per ogni assieme che ha errori, con il totale errori rilevati ed i dati relativi all'errore più grave;
- '2' = memorizza un solo record per ogni assieme e un solo record per ogni componente che ha errori, entrambi con il totale errori rilevati ed i dati relativi all'errore più grave.
 :  : FLD T$TCSB **STRUT. ATTR. ALIQU.**
Utilizzo :  CS - D0
È un elemento della tabella CSB che gestisce l'applicazione delle aliquote orarie ai tempi del ciclo. Questo campo è alternativo al campo 'STRUT. ATTR. ALIQU.VAR'.
La struttura, sia dei campi legati al lavoro (ciclo) che a tutti gli altri, ha una destinazione fissa che per i D0 è Tab. IGIxx : 
>- 01              LIV.VAR.Materiali;
- 02               "   "  lav.esterne;
- 03               "   "  Lavoro;
- 04               "   "  Macchina;
- 05               "   "  Attrezzaggio;
- 06               "   "  Scarto;
- 11              INF.VAR.Materiali;
- 12               "   "  lav.esterne;
- 13               "   "  Lavoro;
- 14               "   "  Macchina;
- 15               "   "  Attrezzaggio;
- 16               "   "  Scarto;
- 20              Totale Costo primo;
- 21              LIV.FIS.Materiali;
- 22               "   "  lav.esterne;
- 23               "   "  Lavoro;
- 24               "   "  Macchina;
- 25               "   "  Attrezzaggio;
- 26               "   "  Scarto;
- 31              INF.FIS.Materiali;
- 32               "   "  lav.esterne;
- 33               "   "  Lavoro;
- 34               "   "  Macchina;
- 35               "   "  Attrezzaggio;
- 36               "   "  Scarto;
- 39              Costi Diretti;
- 40              Totale Costo Diretto;
- 41              Industriali 1;
- 42                  "       2;
- 43                  "       3;
- 49              Costi Industriali;
- 50              Totale Costo Industriale;
- 51              Generali    1;
- 52                 "        2;
- 53                 "        3;
- 59              Costi Generali;
- 60              Totale Costo Pieno;
- 61              Ricariche   1;
- 62                  "       2;
- 63                  "       3;
- 69              Ricariche;
- 70              Prezzo Minimo di vendita.

 :  : FLD T$TCOD **STRUT. ATTR. ALIQU.VAR**
Utilizzo :  D0
È un sottosettore della tabella D0C ed è in alternativa al campo 'STRUT. ATTR. ALIQU'. Riempiendo questo campo, il programma standard utilizza la tabella D0C dell'attribuzione aliquote, al posto di utilizzare la tabella CSB.
Il valore di questo campo è anche l'elemento della tabella D0D, che è utilizzata per impostare la destinazione (tab.IGI) dei costi non legati al ciclo. La compilazione della tabella D0D NON è obbligatoria, in quanto il programma, in mancanza di quest'ultima, utilizza la struttura standard descritta nel help del campo 'STRUT. ATTR. ALIQU'.
 :  : FLD T$TCMG **GESTIONE ECCEZIONI**
Utilizzo :  CS - D0
È un elemento V2/CSECC :  determina il modo di derivazione del costo (da statistiche di magazzino, ecc..).
Se viene utilizzata una di queste eccezioni e, in concomitanza, vengono utilizzati i costi D0, è da tener ben presente che è necessario indicare il campo T$TCOI ('Indice costo eccezione'). Questo, infatti, determina il numero nel quale dovrà essere memorizzato il risultato della lettura.

>  AM        Acquisto medio
  AMR       Acquisto medio con risalita
  AU        Acquisto ultimo
  AUR       Acquisto ultimo con risalita
  VM        Vendita  medio
  VMR       Vendita  medio con risalita
  VU        Vendita  ultimo
  VUR       Vendita  ultimo con risalita

Per queste eccezioni la lettura del costo avviene tramite la lettura delle statistiche di magazzino (£GMS).

>  ULD       Ultimo da documenti
  MED       Medio da documenti

Per queste eccezioni la lettura del costo avviene tramite l'analisi dei documenti legati alla articolo. I parametri tramite i quali avviene la lettura dei documenti sono impostati nel parametro dell'eccezione.

>  LIS       Listino

Il costo viene letto dai listini. Anche qui la lettura è condizionata dal riempimento del parametro dell'eccezione.
Nel parametro di eccezione la "valuta listino" ha il seguente significato : 
* >*BLANKS Se non reperisce fornitore abituale va con fornitore generico (**) e forza la
  valuta presente nella tabella B£2
* >1 Se non reperisce fornitore abituale va con fornitore generico (**) e forza la
  valuta *BLANKS
* >2 Se reperisce fornitore abituale ricerca sul listino con quel fornitore e con la
  valuta della tabella B£2, se non reperisce il fornitore abituale usa il fornitore
  generico (**) sempre con la valuta della tabella B£2
* >3 Se reperisce fornitore abituale ricerca sul listino con quel fornitore e con la
  valuta *BLANKS, se non reperisce il fornitore abituale usa il fornitore generico (**)





>  RIC       Ricalcolato dinamicamente

Ad ogni lettura il costo viene ricalcolato dinamicamente. I parametri di esecuzione del calcolo devono essere memorizzati con ambiente D0CA00A gestibile tramite il pgm D0CA00A.

>  UTE       Deviazione utente

Il calcolo avviene tramite il pgm utente B£G55S_U
>

 :  : FLD T$TCOB **GEST. EFFICIENZA RIS.**
Utilizzo :  CS
Se viene digitato un carattere, il programma di calcolo dei costi utilizza l'efficienza standard della risorsa del ciclo per aumentare i tempi indicati (i costi terranno conto della efficienza/inefficienza standard)
 :  : FLD T$TCOF **TIPO DISTINTA LETTO**
Utilizzo :  CS - D0
Permette di associare ad un tipo costo un tipo distinta. Tale tipo distinta sarà utilizzato dalla scansione distinta nel calcolo del costo. Se bianco viene assunto "ART".
 :  : FLD T$TCOM **TIPO CICLO LETTO**
Utilizzo :  CS - D0
Idem come per tipo distinta letto
 :  : FLD T$TCOQ **PARAM. DEVIAZIONE**
Utilizzo :  CS - D0
È una caratterizzazione del valore impostato nella gestione eccezioni : 
_9_Esempio :  se metodo con £GMS (statistiche), potrebbe indicare se costo medio, ultimo, se mensile, annuale, ecc.
 :  : FLD T$TCOR **CODICE CARICO**
Utilizzo :  CS - D0
Indica il codice carico da utilizzare nell'esplosione dei cicli di lavoro.
 :  : FLD T$TCOT **TEMA COSTO**
Utilizzo :  D0
È un elemento della tabella D5O ed è il tema con cui il tipo costo archivia i contenuti nel file D5COSO0F. Questa gestione è la versione avanzata dei costi (S2). Pur gestendo i costi sul file D5COSO0F, se viene lasciato bianco questo campo il costo, si assume sia sul file COSAR00F (versione base 'CS' dei costi).
 :  : FLD T$TCOU **RISALI DATA/PERIODO**
Utilizzo :  CS - D0
Questo campo controlla le modalità di risalita sulla data o periodo, se non trovato l'elemento di costo per la data o il periodo ricevuto.
Valori ammissibili : 
- ' ' :  risale alla prima data/periodo precedente (per il periodo usa il codice alfabeticamente precedente).
- '1' :  se periodo, risale al primo periodo precedente usando la £PE8; se data, è equivalente al valore ' '.
- '2' :  non risale.
- '3' :  come ' ', ma controlla che il periodo trovato sia congruente con il tipo periodo impostato nella D5O. Nel caso in cui nella D5O non sia impostato il tipo periodo, questo metodo si comporta esattamente come il metodo ' '.
 :  : FLD T$TCOI **INDICE DA SCRIVERE**
Utilizzo :  D0
È un numero positivo. Questo numero è fondamentale nel caso in cui il costo sia calcolato esternamente (quando cioè ho impostato il campo "Gestione eccezioni", in modo che il costo venga derivato da documenti, listini ecc.). Tramite questo numero, infatti, viene determinato in quale elemento della schiera di valori, ritornata dalla routine di letturadei costi (£G55), verrà ritornato il costo. In questo modo si può sfruttare qualsiasi configurazione della tabella IGI,
collegata al relativo tema.
_7_ATTENZIONE :  se questo campo non viene impostato, il costo verrà calcolato ma non sarà ritornato.
 :  : FLD T$TCOE **TIPO COSTO 'CS'**
Utilizzo :  CS
Se impostato, il tipo costo è relativo all'applicazione di costi base, e quindi il tema deve essere obbligatoriamente bianco
 :  : FLD T$TCOG **TEMA COSTO ALLA FASE**
Utilizzo :  D0
È il tema con cui vengono eventualmente memorizzati i costi alla fase.
La sua presenza fa sì che nel lancio venga chiesto se memorizzare o meno i costi alla fase, e che nella richiesta di un costo alla fase (routine £G55) venga assunto come tema, se tra gli oggetti di input è presenta la fase.
 :  : FLD T$TCOP **LIVELLO COSTO**
È il livello costo usato in assenza di un codice inserito esplicitamente; ad esempio nella
determinazione dei numeri di un oggetto (routine £G37). Si consiglia vivamente di inserire il
livello che rappresenta il costo totale dell'articolo, in quanto questo è il livello utilizzato
per leggere i costi nelle routine di calcolo costi.
Si ricorda che per ottenere un costo bisogna sempre esplicitare sia il tipo costo sia il livello.
Se non presente risale al livello in tabella D01
