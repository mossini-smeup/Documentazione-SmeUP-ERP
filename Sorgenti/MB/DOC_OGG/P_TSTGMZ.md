# Obiettivo
Inizializzare il record del file GMRRIM0F : 

# Funzioni e metodi
 * Funzione - "CLEAR"   :  inizializzazione totale del record
 * Funzione - "CLEARN"  :  inizializzazione totale del record senza testata
 * Funzione - "DERIV"   :  derivaz.riga esistente senza pulizia campi "origine" e "destinazione"
 * Funzione - "DERIVI"  :  derivaz.riga esist.senza pulizia campi e con incremento dumero di riga
 * Funzione - "DERIVA"  :  derivaz.riga esistente con pulizia campi "origine" e "destinazione"
 * Funzione - "DERIVO"  :  derivaz.riga esistente con pulizia campi "origine"
 * Funzione - "DERIVD"  :  derivaz.riga esistente con pulizia campi "destinazione"

Tutte le funzioni possono essere richiamate con due metodi : 
 * Metodo   -  blanks   :  il record verrà scritto dal pgm chiamante
 * Metodo   - "WRI"     :  il record verrà scritto dalla funzione £GMZ

_2_Nota Bene : 
Con la dicitura campi "origine" e "destinazione" si intendono i campi chiave corrispondenti a quelli del file GMQUAN0F (quattro campi chiave, piu' i campi del plant e del contenitore).
Essi sono duplicati in "origine" e "destinazione" :  i primi corrispondono al tipo giacenza previsto per il movimento di prelievo (se presente), i secondi a quello del movimento di versamento (se presente).

In dettaglio, si tratta dei seguenti campi : 
>     origine        destinazione
     -------        ------------
     R£ORMG            R£DEMG           Codice Magazzino
     R£ORC1            R£DEC1           Ubic./Forn./Cliente
     R£ORC2            R£DEC2           Lotto/Ord./Agente
     R£ORC3            R£DEC3           Matricola/Fase
     R£ORC4            R£DEC4           Commessa/Data FIFO
     R£ORCO            R£DECO           Numero collo


# Input
 * £GMZFU :  funzione
 * £GMZME :  metodo
 * £GMZNR :  numero di RdM. Se si sta creando una riga senza testata (funzione CLEARN), in questo campo deve essere indicato il tipo di richiesta (tabella GMO)
 * £GMZTR :  tipo RdM. Deve essere presente in tabella GMZ. Se è lasciato a blanks, si assume quello di dft specificato in tabella GMO.
 * GMRRIM :  record del GMRRIM0F :  se si sta usando una delle funzioni "DERIVx", deve essere il record origine da cui derivare quello nuovo

# Output
 * GMRRIM :  record inizializzato della DS del record del GMRRIM0F
 * £GMZMS :  Codice messaggio
 * £GMZFI :  File messaggio
 * £GMZCM :  Ultimo comando
 * £GMZ35 :  Indicatore 35
 * £GMZ36 :  Indicatore 36

# Prerequisiti
Definizione del record del file : 
>D GMRRIM        E DS                  EXTNAME(GMRRIM0F) INZ


# Esempio di chiamata
>C                   EVAL      £GMZFU='CLEAR'
C                   EVAL      £GMZME=''
C                   EVAL      £GMZNR=<numero richiesta>
C                   EVAL      £GMZTR=<tabella GMZ>
C                   EXSR      £GMZ

