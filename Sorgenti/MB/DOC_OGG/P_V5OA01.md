## Stampa modulo documento
La funzione permette di stampare il modulo del documento (o dei documenti selezionati attraverso le parzializzazioni), il programma di stampa del modulo è definito nella tabella V5D, quando esiste un unico programma di stampa per tipo documento, altrimenti in tabella V5D è defnito il sottosettore della tab. B£Q dove si troverranno i vari programmi di stampa utilizzabili.

## Formato di lancio
![V5OA01_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5OA01/V5OA01_01.png)
## Funzioni possibili : 
 * _2_Stampa, il sistema controlla che il documento non sia già stato stampato (in testata il Flag 6 deve essere blank), dopo la stampa il flag 6 viene portato a "1".
 * _2_Prestampa, il sistema esegue la stampa senza cambiare il valore del flag 6.
 * _2_Ristampa,  il sistema esegue la stampa solo se il flag 6 = "1".
## Azioni
Se il campo "Singolo documento" è compilato viene stampato solo questo, altrimenti vengono stampati tutti i documenti compresi nelle parzializzazioni, se le parzializzazioni non sono state impostate esce un messaggio di warning che richiede una conferma esplicita per lanciare la stampa di massa.

_1_ATTENZIONE per stampe di più documenti inserire SEMPRE le parzializzazioni.

Attraverso i parametri di esecuzione (F11) si possono modificare le caratteristiche dell'elaborazione (es. stampante, elaborazione batch/interattiva, ecc..); (cfr. doc. B£GPE2)
- [Parametri di esecuzione](Sorgenti/MB/DOC_OGG/P_B£GPE2)
