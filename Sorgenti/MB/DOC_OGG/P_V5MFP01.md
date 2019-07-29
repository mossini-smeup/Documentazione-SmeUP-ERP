# Seleziona righe per invio C/Lavoro
Il programma costruisce la bolla di invio al fornitore a partire dalla giacenza. Il fornitore usato per filtrare la giacenza è quello indicato nella tabella del tipo riga (intestatario, spedizione, ..) e deve corrispondere all'ente responsabile della risorsa legata all'ubicazione ante.

Nella tabella di lancio B£JXX è ncessario impostare nel campo "parametri aggiuntivi" : 
 * Tipo riga
 * Ubicazione

Area di giacenza e tipo giacenza sono derivate dalla prima causale di movimentazione di scarico ("-") presente nel tipo riga. La giacenza deve essere univoca.
La giacenza deve essere di tipo MFP :  ubicazione / fase / contenitore.
Il contenitore in input deve essere presente nell'area / tipo giacenza e solo nell'ubicazione scelta.

Il programma presenta i colli in giacenza per essere spediti in conto lavoro.

## Scrittura righe documento
Dalla giacenza deriva magazzino, fase, quantità .
Dal contenitore deriva l'ordine di produzione
Dal ciclo del contenitore deriva il centro di lavoro della fase successiva, dal centro di lavoro deriva il fornitore che deve corrispondere a quello in testata documento.

## Formato video
![P5PMFP_54](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP01/P5PMFP_54.png)Con l'opzione "S" si seleziona la riga, mentre "D" serve per deselezionare. F15 per selezionare tutto.
![P5PMFP_55](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP01/P5PMFP_55.png)Alla fine si conferma con F6.
