# BRMIL     -  TIPO MILESTONE IN RIGHE CICLO
Definisce le modalità della dichiarazione automatica di alcune righe di ciclo.
Si definisce milestone una riga di ciclo la cui dichiarazione induce la dichiarazione di altre righe.
Si definisce automatica una riga di ciclo che non viene dichiarata autononomamante, ma la cui dichiarazione viene
indotta da una dichiarazione di una riga milestone.
I caratteri alfabetici sono riservati per le righe automatiche, quelli numerici per le righe milestone.
E' da tener presente che un'operazione che ha rilevanza operazione a '1' (non portata in P5IRIS), non viene
considerata un'operazione automatica, anche se è stata dichiarata tale.

## VALORI POSSIBILI

### ' ' NESSUNO
La riga di ciclo viene dichiarata autonomamente

### 'P' OPERAZIONE AUTOMATICA PRECEDENTE ALLA MILESTONE
Essa verrà dichiarata contemporaneamente alla milestone successiva.

### 'S' OPERAZIONE AUTOMATICA SUCCESSIVA ALLA MILESTONE
Essa verrà dichiarata contemporaneamente alla milestone precedente.

### '1' OPERAZIONE MILESTONE CON DICHIAR.STANDARD AUTOMATICHE
Le operazioni automatiche verranno dichiarate nel seguente modo : 
-    le precedenti per la quantità buona + scarto
-    le successive per la quantità buona
I tempi saranno calcolati applicando le aliquote standard.

### '2' OPERAZIONE MILESTONE CON DICHIAR.STANDARD AUTOMATICHE SOLO QTÀ
E' simile al valore 1, con la differenza che i tempi, per le operazioni automatiche, vengono lasciati a zero. Può
servire quando si dichiarano operazioni di cui non si conosce esattamente la quantità ma solo il tempo impiegato :  in
un'operazione successiva (milestone 2) si determina la quantità effettiva, che viene assunta anche per le operazioni
precedenti automatiche.

## MODO DI COLLEGAMENTO MILESTONE -> AUTOMATICHE
Il legame tra milestone e automatiche si interrompe quando si incontra un'altra milestone o l'inizio o la fine del
ciclo.
Eventuali operazioni normali, o automatiche non concordi al senso di percorrenza verranno trascurate.

Esempio : 
                               Operazioni collegate
Operaz.   Autom.    Milest.   Precedenti     Successive
    020      P
    030
    040      P
   **050                **      020 e 040      060 e 080
    060      S
    070      P
    080      S
    090
   **100                **      070            110 e 130
    110     S
    120
    130      S
