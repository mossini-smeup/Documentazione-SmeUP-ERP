# Funzioni e Metodi

##  CODICE IVA
Il metodo "CIV" ritorna le informazioni relative alla dichiarazione d'intento di un ente.
In input è necessario passare : 

- il codice azienda;
- un soggetto (tipo e codice);
- una data validità.

La funzione mi ritornerà : 

- se per l'ente è pervenuta o meno una dichiarazione d'intento valida alla data passata in input
- se pervenuta la dichiarazione, il codice di assoggettamento Iva (TA IVA) relativo alla dichiarazione stessa
- una DS contenente alcune informazioni relative alla dichiarazione d'intento per il soggetto passato in input


### Possibili utilizzi
Dato un cliente voglio sapere se mi ha mandato o meno la dichiarazione d'intento.
Dato un cliente voglio sapere che assoggettamento Iva verrà applicata sulle fatture da me emesse nei suoi confronti.


##  CALCOLO IMPORTO IVA
Il metodo "CAL" esegue un calcolo dell'importo Iva realtivo ad un documento.
In input è necessario passare : 

- un documento (tipo e codice);
- una data validità;

La funzione ritornerà : 

- l'ente cui il documento è intestato;
- se per l'ente è pervenuta o meno una dichiarazione d'intento valida alla data passata in input;
- se pervenuta la dichiarazione, il codice di assoggettamento Iva (TA IVA) relativo alla dichiarazione stessa;
- l'importo di Iva del documento;
- una DS contenente alcune informazioni relative alla dichiarazione d'intento per il soggetto passato in input


### Possibili utilizzi
Dato un documento voglio controllare l'Iva addebitata al soggetto.
Dato un cliente voglio sapere che assoggettamento Iva verrà applicata sulle fatture da me emesse nei suoi confronti.



