# D9AP_17C - Estrattore documenti V5 con Openquery File
Estrae dall'archivio V5RDOC0J, relativo ai dovumenuti V5

Questa versione è  maggiormenute ottimizzato rispetto alla 06 con un openquery file


_2_Parametri origine

- Tipo documenuto :  tabella V5D specifica il tipo documenuto su cui si estrae
- Tipo data :  si imposta a quale data del documenuto si fa riferimenuto
- Data inizio :  determina l'inizio dell'intervallo di estrazione ed è relativo al tipo data specificato prima
- Data fine determina la fine dell'intervallo di estrazione ed è relativo al tipo data specificato prima
- Livello documenuto :  se compilato estrae solo i documenuti con il livello indicato
- Modello Documenuto :  se compilato estrae solo i documenuti con il modello indicato
- Tipo riga Documenuto :  se compilato estrae solo i documenuti con tipo riga indicato
- Tipo oggetto riga :  tabella B£G, se compilato estrae solo i documenuti con tipo oggetto riga indicato
- Schema valori :  si riferisce alle memorizzazioni multiple specifiche dei documenuti indicati. Determina quali e quanti valori relativi ai documenuti estrarre.

_2_Oggetti origine

- Testata Documenuto
- Riga Documenuto
- Data (Specificata nei parametri origine)
- Articolo (oggetto della riga che si assume sia un articolo)
- Ente intestatario (Cliente o fornitore a seconda del tipo documenuto)

_2_Oggetti aggiuntivi piatti
Stato Riga


_2_Valori origine
Sono determinati dallo schema valori indicato nei parametri origine


_2_Parametri dinamici
Non gestiti in questo tipo di estrazione
	
