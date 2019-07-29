## Movimentazione
In Sme.up ogni movimentazione che crea un'incremento o un decremento di una giacenza in un'area viene eseguita attraverso l'elaborazione di una causale di movimentazione.

La causale di movimentazione esegue un movimento elementare di carico o scarico su un'area.

In Sme.up esistono molte funzioni che lanciano l'esecuzione di causali di movimentazione : 

- esecuzione delle richieste di movimentazione (o liste prelievo)
- spedizione o ricevimento di una bolla materiali
- versamento di un ordine di produzione
- avanzamento produzione con scarico componenti alla fase
- elaborazione rettifiche da liste inventario fisico
- ......

La gestione di queste funzioni è descritta in altri documenti.

Esistono anche delle funzioni di lancio manuale di causali di movimentazione : 

- versamenti e prelievi estemporanei
- rettifiche manuali
- trasferimenti manuali (esempio tra 2 ubicazioni del magazzino)

Nel seguito trattiamo le movimentazioni manuali e le funzioni di interrogazione e revisione movimenti.

### Esecuzione Attività
Per eseguire un'attività manuale di movimentazione si una la seguente funzione : 

![GMMOVI_01](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_01.png)
nella finestra vengono presentate tutte le attività di movimentazione previste, esistono 2 tipologie di movimentazione : 

- _2_causale singola, viene eseguita una sola causale. Ad esempio un prelievo estemporaneo, una rettifica di giacenza, un versamento non pianificato, ...
- _2_doppia causale, vengono eseguite in sequenza 2 causali una di scarico ed una di carico, tipicamente trasferimenti all'interno della stessa area oppure trasferimenti tra aree diverse


### Attività a causale singola
Si utilizzano azioni, scritte nella tabella B£J come nell'esempio seguente : 

![GMMOVI_02](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_02.png)
il programma GMMV01I è quello delle attività a singola causale e la causale da eseguire è quella scritta nel campo Parametri aggiuntivi.

Quando viene selezionata questa azione all'utente si presenta il seguente formato : 

![GMMOVI_03](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_03.png)
devono essere inseriti :  articolo, quantità, campi chiave della giacenza (in questo caso ubicazione).

Con F6 si conferma la movimentazione.

### Attività a doppia causale
Si utilizzano azioni, scritte nella tabella B£J come nell'esempio seguente : 

![GMMOVI_04](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_04.png)
il programma GMMV02I è quello delle attività a doppia causale e le causali da eseguire sono quelle scritte nel campo Parametri aggiuntivi.

Quando viene selezionata questa azione all'utente si presenta il seguente formato : 

![GMMOVI_05](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_05.png)
deve essere inserito l'articolo, la data di registrazione viene assunta oggi, manualmente si può inserire una data diversa, la visualizzazione estesa mostra oltre alla giacenza anche la quantità allocata : 

![GMMOVI_06](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_06.png)
dalla lista delle giacenze dell'articolo si seleziona la giacenza da cui si vuole spostare la quantità : 

![GMMOVI_07](http://localhost:3000/immagini/MBDOC_OPE-GMMOVI01/GMMOVI_07.png)
deve essere impostata la quantità, i campi chiave della giacenza in base al tipo giacenza della causale di destinazione (in questo caso l'ubicazione).

Con F6 si conferma la movimentazione.
