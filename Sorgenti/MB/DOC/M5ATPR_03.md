## Struttura tecnica ATP


##  Introduzione
L'ATP, dato un articolo, una quantità ed un profilo di disponibilità libera, risponde alla domanda :  a che data questa quantità potrà essere consegnata, senza mettere in crisi nessun'altro fabbisogno precedentemente inserito?
Per far questo deve scorrere ripetutamente, in discesa ed in salita, la distinta base deill'articolo in esame.
Il procedimento è :  scendere di un passo, risalire fino all'assieme, scendere di un altro passo, fino as trovare copertura nella disponibilità libera oppure fino a raggiungere le foglie.
per questo motivo sono state realizzate delle repliche dei programmi di discesa e salita, ciascuno dei quali si preoccupa di elaborare un livello, che costituisce il suffisso della replica (da xxxxxx_00 a xxxxxx_20).
Ad oggi ci sono qundi ventun repliche, per cui il livello massimo trattato dall'ATP è venti (assumendo che il livello dell'assieme sia zero). L'estensione è comunque di semplice realizzazione.


##  Descrizione dell'algoritmo
Si parte impostando il record di fabbisogno dell'assieme, nel programma guida
 :  : DEC T(OJ) P(*PGM) K(M5M5H0)
si imposta il livello 00 e si lancia il programma di nettificazione rispetto alla disponibilità libera
 :  : DEC T(OJ) P(*PGM) K(M5M5HE_00)
che, se la disponibilità libera (entro il tempo di approvvigionamento) non copre la quantità richiesta, scrive un ordine a partire dalla data inizio atp.
Se non è un primo livello, avanza i livelli superiori a partire dalla fine dell'ordine (consumando la disponibilità libera che incontra)
 :  : DEC T(OJ) P(*PGM) K(M5M5HI)
ed eventualmente allineando i livelli inferiori (fino a quello in corso) se è stata trovata disponibilità libera nell'avanzamento.
 :  : DEC T(OJ) P(*PGM) K(M5M5HA_00)
Dopo di ciò, si aumenta di uno il livello in corso, e per ogni componente si  lancia la copia del programma di nettificazione del livello relativo, ed il processo riprende ciclicamente, fino a raggiungere le foglie, oppure quando un intero livello è coperto da disponibilità libera.

Come azione finale, è possibile eseguire un compattamento "al più tardi" che appiattisce i rami non critici alla data fine dei rami critici corrispondenti, con lo scopo di consumare un'eventuale disponibilità libera più avanti nel tempo, liberando quella più precoce (e quindi più preziosa per successivi ATP).

## Schema a blocchi

>.
.            M5M5H0 (guida)
.            - scrive il fabbisogno dell'assieme
.            - imposta il livello lv=0
.                 |
. ----------------|
. |               |
. |          M5M5HE_lv
. |          - avanza la data del lead time
. |          - scrive la disponibilità libera
. |          - nettifica :  se è coperto ---------> ** FINE **
. |          - passa il numero dell'assieme
. |               |
. |     --->-------
. |     |    - numero assieme = 0 (è al lv 0) (sì)------->----------
. |     |        (no)                                              |
. |     |         |                                                |
. |     |         ----->---- M5M5HI                                |
. |     |              - lead time > del precedente (no) ->--------|
. |     |                       |                                  |
. |     |                      (sì)                                |
. |     |                       |                                  |
. |     |              - avanza la data del lead time inferiore    |
. |     |              - nettifica il livello (M5M5HN)             |
. |     |              - torna il n.ro del suo assieme             |
. |     |                       |                                  |
. |     -----------<-------------                                  |
. |                                                                |
. |           -----------------------<------------------------------
. |           |
. |        - ha avanzato un assieme (sì)--->-----
. |          (no)                               |
. |           |               - loop di allineamento dei
. |           |                 livelli inferiori (M5M5HA_00/lv)
. |           |                                 |
. |           ----------------<------------------
. |               |
. |         - rilegge il record
. |         - se non c'è più
. |           o se ha quantità 0 ----> ** FINE **
. |             vuol dire che è stato tolto in discesa dall'assieme
. |             che ha trovato disponibilità nell'avanzamento
. |         - se è ancora valido
. |               |
. |               |
. |         - esplode la distinta a un livello
. |         - imposta lv = lv +1
. |         - per ogni componente
. |         - finiti i componenti (sì)---> ** FINE **
. |             (no)
. |               |
. -----<-----------
.
.
.          *** FINE ***
.              |
.          (è sempre in M5M5H0)
.          - calcolo disponibilità pronta
.          - eventuale correzione data
.          - eventuale appiattimento al più tardi (M5M5HS)
.          - eventuale controllo capacità (M5M5HC)
.              |
.          M5M5HF (azioni finali)
.          - eliminazione rami secchi
.          - correzioni se multiplant
.          - appiattimento quantità riservata
.

















