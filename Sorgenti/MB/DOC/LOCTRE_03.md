## Miglioramenti ai movimenti della tastiera
CTRL + SPAZIO per la selezione della foglia e, muovendomi con le frecce e ripetendo l'operazione,
posso selezionare piu' foglie
   - Navigando con le frecce tra le varie foglie dell'albero, con lo spazio e' possibile eseguire la
     stessa azione che verrebbe eseguita con il click del mouse

## Funzioni di ricerca , filtro e selezione : 
a) Su un albero e' possibile, premendo ALT+F9, aprire la barra di ricerca (evidenziata in rosso);
inserendo una stringa e premendo INVIO vengono evidenziate le foglie dell'albero che
contengono la stringa da cercare.
![03COMTRE01](http://localhost:3000/immagini/LOCTRE_03/03COMTRE01.png)Inoltre scegliendo Filtro(K : ) al posto di Cerca(F : ) nella barra di ricerca, e' possibile visualizzare
solo i nodi dell'albero che contengono la stringa ricercata. Ad esempio : 
![03COMTRE01](http://localhost:3000/immagini/LOCTRE_03/03COMTRE01.png) In rosso e' evidenziata la barra di ricerca e, appena sopra, la stringa appena cercata;
nell'albero vengono visualizzati solo i nodi contenenti 'MA'. Aggiungendo un nuovo filtro,
quest'ultimo va in AND come si puo' notare nell'immagine successiva.
![03COMTRE03](http://localhost:3000/immagini/LOCTRE_03/03COMTRE03.png)b) E' possibile impostare lo script in modo che venga visualizzata la casella di selezione
che permette un'azione contestuale di ricerca+selezione+esecuzione azione come si
evince dall'esempio seguente : 
![03COMTRE04](http://localhost:3000/immagini/LOCTRE_03/03COMTRE04.png)![03COMTRE05](http://localhost:3000/immagini/LOCTRE_03/03COMTRE05.png)digitando nella casella di selezione la stringa da ricercare nell'albero e premendo la barra spaziatrice, si ottiene il risultato seguente : 
![03COMTRE06](http://localhost:3000/immagini/LOCTRE_03/03COMTRE06.png)Ovvero il focus viene posizionato sul nodo che ho ricercato e viene anche eseguita l'azione associata al nodo.
Per attivare la casella di selezione occorre impostare lo script con il tag apposito
__TreeType='Menu'__
Ad esempio : 
![03COMTRE07](http://localhost:3000/immagini/LOCTRE_03/03COMTRE07.png)
## Selezione foglie
a. definire una foglia come evidenziata :  attributo Focused dell'XML per selezionare il nodo e dare anche focus al nodo.
    Mettendo nell'XML della foglia l'attributo '**FOCUSED=YES**'
![03COMTRE08](http://localhost:3000/immagini/LOCTRE_03/03COMTRE08.png)il risultato sara' : 
![03COMTRE09](http://localhost:3000/immagini/LOCTRE_03/03COMTRE09.png)b. Attributo Selected in Leaf marca la foglia come selezionata senza dare il fuoco al nodo
Mettendo nell'XML della foglia
![03COMTRE10](http://localhost:3000/immagini/LOCTRE_03/03COMTRE10.png)il risultato sarà
![03COMTRE11](http://localhost:3000/immagini/LOCTRE_03/03COMTRE11.png)c. Definire una foglia come non selezionabile :  l' attributo NoSelect Indica un nodo non
selezionabile quindi visualizzato nell'albero in grigio. Mettendo nell'XML della foglia
![03COMTRE12](http://localhost:3000/immagini/LOCTRE_03/03COMTRE12.png)Il risultato sarà : 
![03COMTRE13](http://localhost:3000/immagini/LOCTRE_03/03COMTRE13.png)
## Selezione multipla
Tenendo premuto CTRL e selezionando diverse foglie, si ottiene una selezione multipla
![03COMTRE14](http://localhost:3000/immagini/LOCTRE_03/03COMTRE14.png)