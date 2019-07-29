## Valorizzazioni WIP
Calcola il WIP alla data e valorizza gli ordini in corso in base all'avanzamento della produzione
## Formato di lancio
Questa funzione produce una stampa valorizzate del WIP ad una certa data per gli ordini di produzione compresi nelle parzializzazioni di lancio.

La valorizzazione può variare in funzione delle impostazioni sul tipo e livello costo utilizzati per i materiali e le operazioni.

Il formato di impostazione è il seguente : 

![P5_03_02](http://localhost:3000/immagini/MBDOC_OGG-P_P5OR95/P5_03_02.png)
Il sistema, in base alle dichiarazioni di produzione si calcola la giacenza in WIP alle varie fasi di lavoro e valorizza ciascuna giacenza alla fase considerando per i componenti la distinta ed il tipo costo / livello impostato per i materiali e per le operazioni il ciclo di lavorazione e le aliquote orarie sia per il tempo macchina che per il tempo uomo.

A seconda di come è impostato il campo 'Dettaglio' avremo una stampa più o meno dettagliata.
