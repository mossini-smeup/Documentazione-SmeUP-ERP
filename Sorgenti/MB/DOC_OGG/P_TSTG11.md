# Funzioni e Metodi

## VER       Verifica
La funzione di Verifica valida la valorizzazione delle schiere di input.
Metodi : 
   STD       standard
   TRA       Trasf.tipi dinamici in statici

## GES       Gestione
La funzione GES è la funzione che permette effettivamente di emettere la G11, i suoi metodi si distinguono
in due famiglie :  i metodi VIS e quelli di tipo MOD. I primi permettono la sola visualizzazione del dato, i
secondi ne consentono anche la modifica.
Metodi : 
   MOD       Modifica
   VIS       Visualizzazione
   MODF      Modifica (in finestra)
   VISF      Visualizzazione (in finestra)
   MODR      Modifica (RF)
   VISR      Visualizzazione (RF)
   MOD P     Modifica  Presenti
   VIS P     Visualizzazione Presenti
   MODFP     Modifica (finestra) Presenti
   VISFP     Visualizzazione (finestra) Presenti
   MODRP     Modifica (RF) Presenti
   VISRP     Visualizzazione (RF) Presenti

## MDV       Lettura MDV
La funzione MDV permette di caricare le schiere £11M e £11N utilizzando una memorizzazione video precedentemente
preparata.
Questa funzione ha come "metodo" il codice della memorizzazione multipla che si vuole caricare.

## FMT      Formattazione schiera
L'output della G11 riempie le schiere £11M e £11N, la prima con i valori alfanumerici la seconda con quelli numerici, e i
£G11CO, un campo di 300 byte nel quale vengono accodate le informazioni di output.
Riempiendo le schiere  £11M e £11N è possibile ottenere la stringa £G11CO grazie al metodo "S_D", il passaggio inverso
(da £G11CO a Schiere £11M e £11N) si effettua grazie al metodo "D_S".
Metodi : 
     S_D       Da schiere a DS
     D_S       Da DS a schiera

# METODO DI COSTRUZIONE DELLA SCHIERA £11A

**Descrizione                **Posizione 01-30** :  intestazione del campo
                                               COSTRUZIONE DELL'INTESTAZIONE DINAMICA
                                               Nella descrizione se si include _&_Dn viene
                                               inclusa la descrizione dell'n.esimo elemento
                                               ES : 'Pippo _&_D1 Pluto' è la descrizione
                                                  e nel primo elemento c'è un articolo la
                                                  cui descriz. è Artic_1
                                                  La descriz.diventerà'Pippo Artic_1 Pluto'

**TpParametro                **Posizione 31-50** :  Tipo+Parametro (lungh. 2+18)
                                               Se fisso viene gestito normalmente (es.£DEC)
                                               se variabile è tipo dinamico
                                               COSTRUZIONE DEL TIPO DINAMICO
                                               Definizione della schiera con cui va costruit
                                             - _&_ come primo carattere
                                             - C,D,E,G,H indicano se deve reperire le informaz
                                               rispettivamente dal codice,descriz., TTLIBE o
                                               oggetto di una griglia presente nel TTLIBE
                                               dell'n.esimo elem. della schiera d'ingresso
                                               L'H è identico al G solo che forza nell'intestazione
                                               del campo la decodifica del tipo oggetto della B£G.
                                         Esempio :  TA_&_C1,n,l indica che a TA concatena il Codice
                                               del primo elemento dalla pos 'n' per 'l' caratteri
                                             - numero indicante l'indice a cui puntare
                                             - , di separazione (ATTENZIONE : OBBLIGATORIA)
                                             - numero indicante la posizione d'inizio
                                               da cui iniziare a prendere l'elemento
                                               o nel caso G pos. d'inizio di dove è presente
                                               la griglia di oggetti (TAB£G)
                                               ES :  TA_&_C1,2,3  e il 1°elem.contiene PIPPO
                                               allora il sistema costruirà il tipo dinamico
                                               TAIPP
                                             - , di separazione (ATTENZIONE : OBBLIGATORIA)
                                             - numero indicante la lunghezza dell'elemento
                                               o nel caso G quale dei 3 oggetti presenti nella
                                               griglia considerare.
                                               Nel tipo dinamico è possibile inserire fino a
                                               3 _&_ puntando a 3 elementi differenti.
                                               VERIFICA LIMITI/VALORI                       -
                                             - Tipo = L per controllare i limiti
                                             - Tipo = V per controllare i valori
                                               Parametro = xxxyyy, dove xxx e yyy sono gli
                                               indici della schiera £11V, rappresentano il
                                               range in cui vengono controllati i lim. o
                                               valori
                                             - E' altresì possibile indicare variabili d'ambiente
                                               secondo la dicitura _&_AM.xx
**Lung.                      **Posizione 51-55** :  rappresenta la lunghezza (se tipo numerico)
**D                          **Posizione 56-56** :  indica il numero di decimali
**O                          **Posizione 57-57** :  O= indica l'obbligatorietà
                                               N= Nè obblig. nè controllo esistenza oggetto
                                               n= obblig. non controllato
                                               A= Non obbligatorio, ma accetta **
                                               a= obblig. ma accetta **
                                               Blank= Non obblig. con controllo esist. ogg.
**V                          **Posizione 58-58** :  numero per forzare  modalità
                                               (gestione=2,interrogazione=5,hidden=H)
                                               nel caso siamo in verifica e è presente 'R'
                                               allora il pgm fa apparire una finestra per
                                               ricercare il codice R=ricerca
**Au                         **Posizione 59-60** :  Autorizzazione
**D                          **Posizione 61-61** :  Se diverso da BLANKS forza nella descrizione
                                               della riga X il valore messo in £11D,X
                                               utile per descrivere campi numerici o **
                                               in un loop di immissione
                             N.B. !!           Non valido per
                                               righe dinamiche
**Pos                        **Posizione 62-64** :  Ordinamento
                                               Se diverso da BLANKS forza in visualizzazione
                                               la posizione indicata  :  le righe BLANKS si presentano alla fine,
                                               nell'ordine in cui sono nella schiera
**Nam                        **Posizione 65-66** :  Nome Campo
                                               Associa un nome di due caratteri all'elemento. Tale nome viene
                                               preso in considerazione nell'analisi della struttura (£IR1) ed
                                               ha un suo utilizzo su funzioni grafiche che sfruttano la definizione
                                               della G11 (Vedasi ad Esempio Costruttore LOA08)
