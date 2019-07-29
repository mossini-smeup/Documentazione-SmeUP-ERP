# STAMPA CICLI
## OBIETTIVO
Stampare tutti i cicli gestiti nella fabbrica secondo tecniche di implosione esplosione e scansione applicate a tipi ciclo diversificati.
Si potranno stampare cicli tecnici o di produzione con esposizione di componenti diverse quali tempo/costo/carico.
La stampa è applicabile a tutte le tipologie di ciclo a partire dai cicli su articoli/risorse ma estesa a qualsiasi tipo di ciclo l'azienda voglia gestire es. operazioni/risorse secondo la logica dei tipi oggetto.
La diversificazione di questi oggetti e' caratterizzata dal tipo ciclo (tabella BRT)
## PARAMETRIZZAZIONE
### Funzione

- Esplosione; permette l'esplosione del ciclo; in particolare riferendoci al tipo ciclo ART dato un articolo presenta tutte le sue operazioni.
- Implosione; permette l'implosione del ciclo; in particolare riferendoci al tipo ciclo ART dato una risorsa presenta tutti gli articoli che utilizzano il centro.
- Scansione; questa funzione ha senso applicata a un quantitativo di prodotto a partire da una certa data; sequenzia nel tempo le varie attività simulando la produzione del quantitativo richiesto prevedendo a fronte delle capacità delle risorse e degli eventuali tempi di spostamento e/o coda il termine delle singole operazioni e del ciclo.


### Tipo ciclo

- Tabella BRT; identifica la tipologia del ciclo gestito in particolare indica il significato del tipo codice es. AR articolo e del tipo risorsa es. RI CDL centri di lavoro.
- Codice; il campo codice assume significato in funzione dei due parametri precedentemente descritti infatti se viene richiesta l'esplosione sul tipo ciclo ART il codice si riferirà all'oggetto articolo (AR) viceversa se richiesta l'implosione il codice si riferirà all'oggetto risorsa (RI CDL) la scansione si comporta come l'esplosione.

