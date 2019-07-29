# Analisi evadibilità estesa
## Obettivo
Permette di verificare la evadibilità dei materiali richiesti dagli impegni (vendita, conto lavoro, produzione).

La differenza rispetto alla disponibilità è che viene data una indicazione di "stato" : 

- pronto
- disponibile dal
- non disponibile


## Formato di lancio
![V5SP10_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5SP10/V5SP10_01.png)
## Compilazione
### Funzione
Definisce la modalità di elaborazione e presentazione del risultato : 
 * _1_PRE = Al più presto, la funzione controlla l'evadibilità alla data del fabbisogno e presenta sia la quantità richiesta che quella evadibile ciascuna con la propria data
 * _1_DAT = Alla data, la funzione controlla l'evadibilità alla data del fabbisogno e presenta sia la qtà richiesta che quella evadibile alla data della richiesta
 * _1_MDV = Esecuzione con MDV reperita in Cond.Lib., la funzione viene utilizzata solo per le elaborazioni batch, in questo caso le impostazioni vanno memorizzate con MDV e inserite nella condizione libera utente

### Metodo
Definisce l'origine dei fabbisogni di cui calcolare l'evadibilità : 
 * _1_RIG = Righe del documento, si vuole calcolare l'evadibilità di fabbisogni dovuti a documenti del ciclo esterno (normalmente documenti di vendita)
 * _1_COM = C/lavoro, si vuole calcolare l'evadibilità dei fabbisogni del conto lavoro
 * _1_OPR = Produzione,  si vuole calcolare l'evadibilità dei fabbisogni degli ordini di produzione
 * _1_ALL = C/lavoro e produzione,  si vuole calcolare l'evadibilità di tutti i fabbisogni
### Tipo documento
Valido solo per la funzione RIG, richiede il tipo documento a fronte del quale cercare i fabbisogni.
### Gruppo fonti base
Da utilizzare per l'analisi disponibilità
### Gruppo fonti eccedenza
Da utilizzare per il calocolo delle eccedenze
### Disponibilità parzializzata per ente
Se si vuole parzializzare per ente
### Disponibilità separata per ente
Se si vuole mantenere la disponibilità separata per ente
### Stampa di controllo
Emette la lista dei documenti (righe documento / testate ordini produzione) che vengono presi in considerazione
### Limiti
I campi presentati servono per impostare dei filtri sui fabbisogni
### Esplosione/Implosione impegni
Determina la forma della stampa
