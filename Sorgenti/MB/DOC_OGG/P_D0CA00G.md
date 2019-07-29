# Impianto di calcolo
## Introduzione
L'elaborazione del calcolo di costi può essere così riassunta : 
 - Nel formato di lancio deve essere impostato il tipo costo da elaborare, nonchè tutta la serie di parametri e parzializzazioni che ne condizionano l'esecuzione.
 - Una volta lanciato, vengono elaborati tutti gli articoli che non vengono filtrati dalle parzializzazioni.
 - Per ognuno degli articoli vengono riprese le politiche di riferimento e, in rapporto ad esse, calcolati i costi di acquisto, conto lavoro e produzione.
 - Il risultato del calcolo del costo del singolo articolo viene memorizzato nel file dei costi per oggetto (D5COSO0F), in funzione del tema previsto per tipo costo utilizzato.

L'elaborazione non è affidata ad un unico pgm, ma è stata suddivisa tra più programmi, ognuno dei quali svolge una determinata funzione standard.
Tali pgm sono identificabili dalla radice D0CA, cui si aggiunge un numero che definisce la funzione svolta dal pgm e la desinenza '_' più un numero di due cifre che identifica la versione del pgm da utilizzare (la standard ha desinenza 00).
Tale costruzione, oltre a permettere il mantenimento di personalizzazioni, dà anche la possibilità di tenere contemporanamente attive più versioni alternative dello stesso pgm, che potranno essere facilmente interscambiate, come spiegato di seguito, al momento del lancio del calcolo.


## Programma di lancio del calcolo
Il pgm di lancio del calcolo dei costi standard è D0CA00G, tramite cui è possibile lanciare l'esecuzione del calcolo in funzione di un particolare tipo costo, la modalità di esecuzione del calcolo è alquanto complessa e oltre che dai campi delle tabelle del modulo è condizionata da una serie di parametri che sono stati raggruppati in due categorie di seguito dettagliate.

### Formato di lancio
![D0BASE_02](http://localhost:3000/immagini/MBDOC_OGG-P_D0CA00G/D0BASE_02.png)
_7_Richiamo pgm di calcolo
 :  : INI
 :  : CMD CALL D0CA00G
 :  : FIN

## Parametri dI impostazione
### Formato di impostazione parametri
![D0BASE_03](http://localhost:3000/immagini/MBDOC_OGG-P_D0CA00G/D0BASE_03.png)
Sono i parametri che condizionano le modalità di esecuzione del calcolo. Fra i parametri facoltativi è importante il parametro "Memorizzare", senza la cui impostazione non può avvenire la memorizzazione del calcolo che di default non avviene. Le varie configurazioni di tali parametri sono memorizzabili con ambiente D0CA00A1.

_7_Gestione MDV - D0CA00A1
 :  : INI
 :  : CMD CALL B£MDV0
 :  : FIN

 - _2_Tipo costo aliquote - Obbligatorio. Indica il tipo costo da utilizzare per la determinazione delle aliquote necessarie alla valorizzazione dei costi delle fasi interne (D5OCC).
 - _2_Tipo costo Lavorazioni esterne - Obbligatorio. Indica il tipo costo da utilizzare per la determinazione dei costi delle lavorazioni esterne.
 - _2_Tipo costo Materiali - Obbligatorio. Indica il tipo costo da utilizzare per la determinazione dei costi d'acquisto.
 - _2_Data validità - Facoltativo. Indica la data di riferimento del calcolo in caso differisca dalla data odierna.
 - _2_Quantità - Facoltativo. Indica la quantità utilizzata nei calcoli relativi ai cicli e alla distinta base. Se non viene valorizzata, verrà usata come default quantità 1.
 - _2_Senza esplosione distinta - Facoltativo. Indica se nel calcolo dei costi relativi alla distinta, questo debba appoggiarsi ai risultati di elaborazioni precedenti o se la distinta debba essere interamente rielaborata (cioè ricalcolo a loro volta il costo di ogni singolo articolo della distinta).
 - _2_Esplosione - Facoltativo. Se impostato fa in modo che nella selezione degli articoli da elaborare vengano selezionati anche tutti i componenti della distinta base dell'articolo.
 - _2_Implosione - Facoltativo. Se impostato fa in modo che nella selezione degli articoli da elaborare vengano selezionati anche tutti gli articoli di cui l'articolo è componente.
 - _2_Ricalcolo Low Level Code. Indica se deve essere eseguito il ricalcolo del low level code della distinta e il tipo esplosione.
 - _2_Memorizzazioni - Facoltativo. Gestisce l'aggiornamento dei costi dopo il calcolo (DI DEFAULT I COSTI NON SONO AGGIORNATI). Può assumere valore ' '= non aggiorna, 'T'= aggiorna sempre, 'C'= aggiorna solo senza errori.
 - _2_Lista serie oggetti - Facoltativo. Implica la stampa della lista di tutti gli articoli che vengono elaborati nel calcolo.
 - _2_No Costi alla fase - Facoltativo. Fa in modo che la sequenza del calcolo non esegua il calcolo alla fase anche se ne è stato specificato il tema nella tabella TCO.
 - _2_Tipo Calcolo - Facoltativo. Quando è impostata la memorizzazione del calcolo, permette di attivare un filtro sui costi da aggiornare in base alla loro pre-esistenza :  ' '= nessun filtro, 'M'= solo costi non ancora memorizzati, 'P'= solo costi già memorizzati.

## Parametri di funzione
### Formato di impostazione programmi
![D0BASE_04](http://localhost:3000/immagini/MBDOC_OGG-P_D0CA00G/D0BASE_04.png)
Premettendo che il calcolo standard presuppone obbligatoriamente l'utilizzo del sottosettore standard della tabella IGI£C (Indici di gestione/Costi articolo standard), queste sono le sue peculiarità : 
 * _2_D0CA01_00, di ogni articolo presente nel file di work vengono lette le politiche e, in funzione di esse, viene calcolato il costo nel seguente modo :  in presenza di politica d'acquisto viene letto il costo del materiale (in base al tipo costo materiale passato) e relativa ricarica, in presenza di politica di c/lavoro viene letto il costo di c/lavoro, relativa ricarica e viene scandita la distinta di c/lavoro, in presenza infine della politica di produzione vengono scanditi il ciclo e la distinta di produzione. Alla fine, in base al tema definito nel tipo costo, i risultati verranno memorizzati su D5COSO e, se non specificato diversamente, in presenza di una politica di produzione verranno memorizzati anche i costi progressivi di ogni fase.
 * _2_D0CA04_00, le politiche vengono lette tramite 3 OAV dell'articolo
 * _2_D0CA03_00, le ricariche vengono attribute in base alla famiglia ricariche collegata all'articolo tramite la tabella della classe materiale e al metodo di attribuzione della tabella CSA.
 * _2_D0CA05_00, la scansione del ciclo avviene in base al tipo ciclo indicato nel tipo costo tramite la /COPY £CIR e, a seconda che la fase sia interna o esterna, il costo viene così calcolato : 
 ** _3_Fase interna, determinato il centro di costo dalla risorsa della fase se ne leggono le aliquote (cioè il costo orario) in base al tipo costo aliquote, ottenendo il costo della fase moltiplicando le aliquote per le componenti di costo ritornate dalla £CIR in base alla £BRT (possono essere al massimo 6), seguendo i criteri definiti dalla tabella CSB indicata nella tabella del tipo costo dell'articolo.
 ** _3_Fase esterna, si legge semplicemente il costo della fase dell'articolo in base al tipo costo delle lavorazioni esterne.
 * _2_D0CA06_00, la scansione della distinta avviente tramite la /COPY £DIB in base al tipo distinta indicato sul tipo costo. A seconda poi che sia prevista l'esplosione distinta o meno, viene letto o ricalcolato il costo di ogni singolo componente.

I parametri di funzione definiscono i suffissi (ultimi due caratteri) dei pgm di calcolo che si utilizzeranno.
Per ogni pgm è possibile inoltre indicare un parametro che nei pgm standard è usato solo in casi particolari, ma che può risultare utile in caso di personalizzazioni.

A standard i parametri sono utilizzati nel pgm D0CA03_XX, in cui il parametro indica il sottosettore di riferimento della tabella CSR (Famiglie Ricariche) e nel pgm D0CA09_XX, in cui il parametro indica la interrogazione da utilizzare; a questo proposito è da tener conto che, valorizzando il parametro, bisognerà utilizzare il pgm standard D0CA09_01, mentre lasciandolo vuoto bisognerà utilizzare il pgm D0CA09_00.

Le varie configurazioni di tali parametri sono memorizzabili con ambiente D0CA00A2.

_7_Gestione MDV - D0CA00A2
 :  : INI
 :  : CMD CALL B£MDV0
 :  : FIN

### Attributi articolo
 :  : DEC T(OA) P(AR) K(J/P03) I(_9_  % Politica produzione) L(1)
 :  : DEC T(OA) P(AR) K(J/P04) I(_9_  % Politica acquisti) L(1)
 :  : DEC T(OA) P(AR) K(J/P05) I(_9_  % Politica lavoraz.) L(1)

### Tabelle interessate
 :  : DEC T(ST) K(CLS) L(1)
 :  : DEC T(ST) K(CSR) L(1)
 :  : DEC T(ST) K(CSA) L(1)
 :  : DEC T(ST) K(BRT) L(1)
 :  : DEC T(ST) K(CSB) L(1)
 :  : DEC T(ST) K(BRL) L(1)

### Scansioni ciclo, tempi e distinta base
 :  : INI
 :  : CMD CALL TSTCIR
 :  : CMD CALL TSTBRT
 :  : CMD CALL TSTDIB
 :  : FIN
