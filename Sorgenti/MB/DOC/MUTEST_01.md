## Obiettivo
Il modulo MUTEST, è creato creato per permettere la consultazione di tutti i programmi di test che vengono registrati nel file MUTEST.

## Sviluppo RPG
Un programma che presenta delle annotazionidi tipo MU* e compilato in un modalità 'MT' (da definire), popolerà il file MUTEST con le esecuzioni dei test.
I test al momento sono di uguaglianza, quindi viene valutato il valore di una variabile confrontandolo con un valore dato.
Questo tipo di test serve per valutare la consistenza dei dati e delle varie tipologie di variabili.
Sono stati realizzati diversi programmi di esempio in cui vengono analizzati i comportamenti delle varie tipologie di variabile (carattere, numero, data, indicatore)
con i relativi codici operativi.
Nella matrice si può visualizzare per programma l'esito del test.

![MUTEST_01A](http://localhost:3000/immagini/MUTEST_01/MUTEST_01A.png)

## Esecuzione multipiattaforma
In ambiente multipiattaforma il comando di riferimento è  :  : DEC T(OJ) P(*CMD) K(RUNTEST) con i seguenti parametri di esecuzione : 

| 
| .COL Txt="Nome" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| 
| .COL Txt="Valore" LunAut="1" A="L" |
| COMP|Componente| *ALL, *OTHER |
| RUNNER|Runner|asup : /omac/myPlugin/runnerName |
| OUTPUT|Output| *, *PRINT, *FILE, *MEMO |
| 


Esempi di chiamata : 
* RUNTEST COMP(Database) OUTPUT(*PRINT)
* RUNTEST COMP(*ALL) OUTPUT(*FILE)
* RUNTEST RUNNER(asup : /omac/com.smeup.erp.test.gen/com.smeup.erp.test.gen.runner.MUTE01_01)


