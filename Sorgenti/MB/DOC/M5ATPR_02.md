## Giorni di distanza dalla criticità


## Descrizione applicativa

Quando la data ATP non è soddisfacente in quanto il cliente non è disposto ad accettare il lungo tempo di attesa, si pone la necessità di analizzare come questa data potrebbe essere anticipata.
Ovviamente bisogna lavorare sui tempi di approvigionamento, interni ed esterni, in modo da accorciarli rispetto al leadtime standard che è quello utilizzato nel calcolo della data ATP.

Si comincia dall'analisi del percorso critico, ossia dal ramo più lungo per vedere di sollecitare la produzione o i fornitori a consegnare in tempi più ristretti.

Quando la analisi ATP si compone di diversi rami, perchè il prodotto ha una distinta complessa , è opportuno analizzare anche gli altri rami per individuare quali altri rami diventerebebro critici dopo che il principale è stato risolto.

A questo scopo è stato introdotto per ogni ramo dell'anaisi ATP,  l'indice " giorni di distanza dalla criticità" che indica l'efficacia, per la riduzione della data atp, della compressione dei tempi di approvvigionamento relativi agli ordini ancora da emettere suggeriti dall'atp stesso.
Un indice basso indica che il ramo è prossimo a quello critico, un indice alto indica che il ramo è relativamente corto rispetto al ramo critico.
Ovviamente, una analisi ATP che contenga solo rami con indici alti indica che se si risolve la lungehzza del percorso critico , tramite sollecitazioni ai fornitori o alla produzione, c'è buona probabilità di anticipare la data ATP in modo considerevole.
Viceveresa, una analisi ATP con tanti rami con indice basso indica che neanche risolvendo il percorso critico si può ottenere una sensibile miglioramento della data ATP.


NOTA :  Esso non entra nel merito della compressione di ordini in corso che avrebbero un'efficacia nell'arretramento della disponibilità libera.

## Descrizione tecnica
Si parte dalle foglie :  per ciascuna di esse si determinano i giorni di distanza dalla foglia con data più bassa, che costituisce il punto di partenza del percorso critico, per il quale questo numero vale 0.
Risalendo, tutti i rami di un percorso ereditano il valore della loro foglia :  quando più rami si incontrano in un punto, il ramo superiore assume il valore più basso tra quello dei rami che in esso si ricongiungono.






