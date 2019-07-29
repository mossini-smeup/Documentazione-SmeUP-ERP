# Esempio di applicazione
Immaginiamo di voler legare delle caratteristiche alle commesse di produzione macchina (commesse tipo P). Questa scheda tecnica dovrà contenere una serie di parametri che vanno a caratterizzare la macchina che viene abbinata alla commessa in questione.
Tra questi parametri vi sono quelli che identificano il Cliente ed il costruttore della specifica macchina costruita con la commessa.

Vediamo come impostare tale struttura : 

1) Definiamo l'elemento CM della B£G dove associamo la categoria di parametri all'entità commesse di produzione : 

![C£_05_02](http://localhost:3000/immagini/C£PARA_ESE/CX_05_02.png)
2) Creiamo il sottosettore B£NCM della tabella B£N i cui elementi saranno i parametri associati all'entità commesse di produzione : 

![C£_05_03](http://localhost:3000/immagini/C£PARA_ESE/CX_05_03.png)
3) Creiamo nel sottosettore B£NCM della tabella B£N gli elementi che rappresentano i parametri associati all'entità commesse di produzione : 

![C£_05_04](http://localhost:3000/immagini/C£PARA_ESE/CX_05_04.png)
In particolare inseriamo il parametro X60 che specifica l'articolo associato ad una commessa : 

![C£_05_05](http://localhost:3000/immagini/C£PARA_ESE/CX_05_05.png)
4) Creiamo la categoria di parametri "Commesse Macchine"; a tale scopo definiamo l'elemento CM all'interno della tabella C£E dove specifichiamo che il contenitore dei parametri sarà il sottosettore B£NCM della B£N e che la griglia di controllo sarà definita dall'elemento CM della tabella B£G : 

![C£_05_06](http://localhost:3000/immagini/C£PARA_ESE/CX_05_06.png)
Il risultato finale sarà il seguente : 

![C£_05_07](http://localhost:3000/immagini/C£PARA_ESE/CX_05_07.png)