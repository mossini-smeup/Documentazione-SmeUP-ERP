# Obiettivo
Interrogare gli indici statici, modificarli e confrontarli con indici di livello superiore

## Formato guida
![CQ_VEND_13](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR70/CQ_VEND_13.png)
Compilando uno o una coppia dei campi di input il programma presenta la lista degli indici corrispondenti, se tutti i campi sono bianchi viene presentata la lista completa : 

## Formato lista
![CQ_VEND_14](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR70/CQ_VEND_14.png)
## Formato dettaglio indice
![CQ_VEND_15](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR70/CQ_VEND_15.png)Ogni riga di questo elenco corrisponde ad un indice statico utilizzato nel calcolo dell'indice complessivo (nel caso dell'esempio è IVVG ma potrebbe essere qualsiasi altro indice). Il programma in sostanza elenca tutti gli indici statici che appartengono all'architettura dell'indice globale ed accanto ad ogni indice statico riporta il peso ad esso attribuito e la corrispondente valutazione (sono visualizzati anche i codici dei sottosettori delle tabelle degli indici e delle valutazioni).

Nella colonna "?" vengono visualizate le varie valutazioni, se si è entrato in modifica si possono anche modificare, viene richiesta anche la data della valotazione, con F21 si può impostare la data odierna.

In funzione del modo in cui si entra nel dettaglio (ovvero del numero di codici definiti nella maschera di ingresso) viene presentata la valutazione corrispondente alla combinazione specificata, e nelle colonne   "C1/C2/**", "C1/**/**", "**/**/**", vengono mostrate, se presenti le valutazioni ai livelli superiori.

Vediamo di chiarire il concetto con l'esempio considerato in cui sono state specificate due chiavi : 
 * codice del fornitore;
 * codice dell'articolo;
 * il terzo codice legato alla fase ed esponente di modifica, è stato impostato a (**).

Il programma attiva una ricerca di "risalita", come si diceva prima, e recupera dall'archivio le valutazioni relative al : 
 * fornitore generico (**/**/**) riportandole nell'ultima colonna
 * le valutazioni relative allo specifico fornitore (C1/**/**) nella penultima colonna
 * le valutazioni della combinazione (C1/C2/**) accanto all'indice con la relativa descrizione della valutazione.

Con l'opzione 02 modifica, l'Ente della Qualità responsabile della gestione degli indici può impostare o aggiornare le valutazioni riportate con nuovi valori tabellati. Ad ogni indice statico infatti é legata una tabella (Tabella CRI) di possibili valutazioni da assegnare (il cui riferimento si trova nella tabella del'indice) :  ad ogni singola  valutazione sono associati i valori che vengono poi moltiplicati per il peso dell'indice.

Il programma prevede la possibilità di assegnare automaticamente i valori del livello di definizione superiore utilizzando l'opzione "F15 = Assegna Livello Sup." .

### Confronti tra livelli
Si possono anche eseguire confronti tra i diversi livelli, in altre parole è possibile vedere come il livello di qualità di un fornitore per un dato articolo si discosta dal profilo del generico fornitore oppure dalla valutazione complessiva attribuita in generale a quel fornitore.
Basta indicare la colonna con la quale si vuole eseguire il confronto con un carattere di spunta.
![CQ_VEND_16](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR70/CQ_VEND_16.png)
Visualizzazione del confronto
![CQ_VEND_17](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR70/CQ_VEND_17.png)
Riassumiamo quanto visto sul modulo di "Gestione degli Indici Statici della Qualità"  tramite il seguente schema : 
![CQ_VEND_18](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR70/CQ_VEND_18.png)