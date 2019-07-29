# Creazione mappe in breve
## Dove trovo le immagini delle mappe?
Le immagini delle mappe sono quelle che vengono aperte quando c'è una chiamata del tipo : 
 *  :  : G.SET.OBJ Tip="MB" Par="SCP_MAP" Cod="MIAMAPPA" Exec="F(MAP;LOSER_18;OPN) 1(MB;SCP_MAP;MIAMAPPA)"
 *  :  : G.SET.IMG Path="MB;SCP_MAP;MIAMAPPA2"

Il client LoocUp si aspetta di aprire un'immagune .jpeg del tipo MIAMAPPA.jpeg o MIAMAPPA2.jpeg
Al momento le immagini vengono risolte dal client andando sulla cartella....
## Servizio di lettura mappe
Il servizio che legge lo script di mappa(del tipo MP - SCPO_MAP) sull'AS400 è LOSER_18.
In questo servizio vengono eseguite 4 procedure principali : 
 * La lettura di uno script in cui sono definite delle variabili (in SCP_SET)
 * La trasformazioni di eventuali OAV(&OA) trovati nello script SCP_SET nel campo Val
 * La lettura dello script di mappa SCP_MAP con la sostituzione delle variabili
 * La lettura dell'ultima configurazione della mappa nel file B£MEDE

## Principali comandi nella mappa
### Creazione di un segnaposto nella mappa
Un segnaposto è il punto in cui viene inserita una mappa e può assumere varie forme : 
 * rettangolo (RECT)
 * poligono   (POLY)
 * cerchio    (CIRCLE)

Seguendo le relative coordinate come ad esempio  :  : G.SET.FRM Shp="RECT" Crd="100,770,40,100".
Dopo aver creato ils egnaposto si ha la possibilità di gestire altre 3 opzioni : 
 * Fill (ON/OFF) stabilisce il riempimento del segnaposto stesso di colore blu (svilupperemo anche altri colori)
 * Img  (OFF/MOUSEON/ALWAYS) stabilisce quando e come far apparire un'immagine
 * Txt  (OFF/MOUSEON/ALWAYS) stabilisce quando e come far apparire il testo

Vediamo un esempio :   :  : G.SET.LAY Fill="OFF" Img="ALWAYS" Txt="ALWAYS"

A questo punto restano solamente tre opzioni da poter essere completate : 
 *  :  : G.SET.OBJ che come già descritto sopra indica la funziona da eseguire relativa al segnaposto preso in considerazione
 *  :  : G.SET.IMG che indica tutte le opzioni su come e quale immagine far apparire
 *  :  : G.SET.TXT che indica tutte le opzioni su come e quale testo far apparire. Il contenuto vero e proprio può essere sia

il valore di una variabile che una parola qualsiasi; si ha la possibilità di selezionare la dimensione dei caratteri, il colore dello sfondo e del testo stesso, il Font e il modo in cui appare a video scegliendo tra una spaziatura forzata e non.

## In che modo la mappa può diventare dinamica?
Attraverso l'utilizzo del servizio LOSER_18 il quale a sua volta richiama un membro contenente delle variabili si ha la possibilità di visualizzare il valore delle stesse dipendenti da un servizio qualsiasi, rendendo appunto la mappa dinamica. Il refresh viene eseguito con il solito tasto F5, ma si ha anche la possibilità di renderlo automatico, stabilento un intervallo di tempo con la seguente istruzione : 
 *  :  : G.TIM Ref="numero millisecondi"

### Passaggio del parametro
Sempre attraverso l'utilizzo del servizio LOSER_18, come già avviene nelle schede di LoocUP, ora si ha la possibilità di passare un parametro qualsiasi dalla scheda chiamante alla mappa chiamata.
Per vedere un semplice esempio basta aggiungere nella scheda, alla riga di richiamo della mappa, la seguente sintassi : 

P(PIPPO(PLUTO))

Così facendo all'interno della mappa che verrà chiamata possiamo specificare la variabile &PA.PIPPO che avrà di conseguenza il valore "PLUTO"; queste variabile, avendo "PA" come radice, si distingue dalle altre variabili con radice "CO" che sono considerate di contesto.
