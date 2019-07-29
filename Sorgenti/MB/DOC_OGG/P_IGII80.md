## Formato guida
![IG_REPT_10](http://localhost:3000/immagini/MBDOC_OGG-P_IGII80/IG_REPT_10.png)
 * '!' collegamento con le tabelle IGA, IGT, IGS
 * '/'  collegamento con archivio Q9000. Il programma mostra tutti i dati che ha in archivio corrispondenti alla combinazione Area/Tema/Livello, parzializzando per una data combinazione di elementi la cui griglia è funzione del livello.

## Selezione area, tema, livello di sintesi con modalità '/'
![IG_REPT_11](http://localhost:3000/immagini/MBDOC_OGG-P_IGII80/IG_REPT_11.png)
## Formato per scelta ordinamento interrogazione
![IG_REPT_12](http://localhost:3000/immagini/MBDOC_OGG-P_IGII80/IG_REPT_12.png)
## Formato interrogazione indici
![IG_REPT_13](http://localhost:3000/immagini/MBDOC_OGG-P_IGII80/IG_REPT_13.png)
 * i valori che vengono visualizzati RIQD, RIDC, QAUC,.... dipendono dall'associazione tema codice indice che si crea con l'opzione "02 Associazione di indici ad un tema"
 * in base all'ordinamento scelto (Periodo, Fornitore) il programma ha prelevato dall'archivio i  record.
 * l'opzione F07 consente di selezionare di tutti gli indici inclusi in un tema solo quelli più interessanti :  verranno visualizzati solo quelli indicati nella finestra che si apre.
 * l'opzione F08 permette la decodifica dei dati
 * l'opzione F15 sblocca per modifiche ai valori degli indici
 * l'opzione F18 che consente di scegliere i periodi per i quali far calcolare al programma i totali dei valori degli indici del tema in oggetto :  è possibile quindi vedere lil numero di non conformità rilevato su un articolo fornito da un certo fornitore nei mesi di Gennaio e Febbraio oppure nell'intero arco dell'ultimo anno.
 * l'opzione F19 sposta la videata a sinistra
 * l'opzione F20 sposta la videata a destra
 * l'opzione F14 di generazione dell'archivio, consente di creare un file (Documento di una Cartella ) in cui possono essere parcheggiati i dati riportati in visualizzazione. Disponendo di un'opportuno strumento di trasferimento dati da AS400 a PC, mediante fogli elettronici come Excel, si possono ottenere tutti i grafici possibili. Èpossibile impostare un "Modello" di formattazione personalizzato per i grafici importati su PC, diverso da quello di default.

## Esempio di output ottenuto automaticamente attraverso l'interfacciamento con EXCEL
![IG_REPT_14](http://localhost:3000/immagini/MBDOC_OGG-P_IGII80/IG_REPT_14.png)