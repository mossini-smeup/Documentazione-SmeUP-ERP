# Interrogazione Giacenze
## Generalità
L'interrogazione giacenze permette di visualizzare la quantità giacente di un articolo nelle varie aree e nei vari magazzini (plant) di un'azienda.
Si possono interrogare sia la quantità giacente che quella allocata e quella attesa.
Se in un'area la giacenza di un articolo è ulteriormente dettagliata (es. per ubicazione, per fornitore, ...) è possibile avere anche la qtà sommarizzata.

## Formato di lancio
L'interrogazione giacenze parte dal seguente formato di lancio : 

![GM_11_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_01.png)In questo formato si impostano : 

- Forma di presentazione
- Totalizzazione
- Visualizzazione estesa
- Dati per selezione


### Forma di presentazione
Determina come sarà visualizzata la lista giacenze che sarà presentata, dalla forma di presentazione dipendono anche i campi che vengono visualizzati per l'inserimento dei dati di selezione, la forma di presentazione è un elemento della tabella GMF : 

![GM_11_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_02.png)In funzione di come è stata impostata l'elemento la forma di presentazione può predefinire alcuni dati di selezione ed anche renderli non modificabili.

### Totalizzazione
Permette di avere la qtà totale ad esempio nell'area di accettazione di un articolo su tutti i lotti : 

![GM_11_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_03.png)Con le impostazioni di qui sopra la lista si presenta nel modo seguente : 

![GM_11_04](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_04.png)Nella riga corrispondente all'articolo viene mostrata la qtà totale, nelle altre righe si vede la qtà per ciascun lotto.

### Visualizzazione estesa

![GM_11_05](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_05.png)Se non è selezionata in lista si vede la sola quantità in giacenza, se invece è selezionata allora vengono visualizzate anche la quantità allocata e la quantità attesa : 

![GM_11_06](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_06.png)Quantità allocata e quantità attesa, vengono usate se sono attive le liste di prelievo (richieste di movimentazione).
La quantità allocata rappresenta la qtà che è stata prenotata, nella giacenza di partenza, a fronte di una o più liste di prelievo e normalmente è minore o al massimo uguale alla giacenza.
La quantità attesa viene imposta, come contraltare di quella allocata, nella giacenza di destinazione (es. se nell'area di magazzino per un articolo alloco (prenoto) una quantità di 100 per la spedizione ad un fornitore, contemporaneamente mi troverò 100 come quantità attesa per lo stesso fornitore nell'area attesa spedizione).

## Lista giacenze
La lista giacenze si presenta in modi diversi in funzione della forma di presentazione dei dati di selezione impostati nel formato di lancio.

Indipendentemente dalla presentazione, nella lista abbiamo delle caratteristiche comuni : 

- _2_posizionamento, serve per spostarsi nella lista in corrispondenza del valore più prossimo a quanto inserito nel campo di posizionamento.
_3_Nota bene, il posizionamento opera sul primo campo di ordinamento impostato nella forma di presentazione, nella figura di esempio è il plant
- _2_parzializzazioni articolo, permette di filtrare gli articoli che vengono mostrati in lista attraverso le parzializzazioni dell'articolo
- _2_opzione di riga, generalmente si usa l'opzione 05 che permette di interrogare il dettaglio della giacenza. Sono possibili altre opzioni ma solo a chi ne è autorizzato.


![GM_11_07](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_07.png)## Dettaglio giacenza
Attivato dalla lista giacenze attraverso l'opzione 05, presenta la situazione di dettaglio della giacenza : 

![GM_11_08](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_08.png)Facendo riferimento ai campi di input di destra : 

- quelli senza (*), inserendo un carattere qualsiasi, premettono di vedere il dettaglio del dato di riga (es. se c'è della qtà allocata si può vedere l'elenco delle richieste di movimentazione che hanno allocato quella qtà, mentre nel magazzino si aprono le funzioni oggetto del magazzino 09)
- quelli con (*) oltre al tipo di interrogazione valido anche per le altre righe, se il carattere è "M" mostra i movimenti dell'oggetto (es. i movimenti dell'articolo, oppure i movimenti del lotto)


## Movimentazione da lista giacenza
Per chi è autorizzato, oltre all'opzione 05 per l'interrogazione di dettaglio, sono disponibili opzioni che permettono di eseguire della movimentazione : 

![GM_11_09](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_09.png)

 :  : PAR L(TAB)
- R+| Rettifica + | permette di rettificare la giacenza in aumento
- R- | Rettifica - | permette di rettificare la giacenza in diminuzione


### Rettifica positiva
Si attiva con l'opzione R+ si presenta un formato con la causale di rettifica che può essere cambiata o confermata, con invio di prosegue e si presenta il formato di inserimento manuale rettifiche : 

![GM_11_10](http://localhost:3000/immagini/MBDOC_OGG-P_GMQU01/GM_11_10.png)Inserire la qtà da aggiungere e confermare con F6.

### Rettifica negativa
Come rettifica positiva.
