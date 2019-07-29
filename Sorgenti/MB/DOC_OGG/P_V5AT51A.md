# Crea righe file di lavoro da radiofrequenza
Il programma carica in un file di WORK le righe che andranno a comporre il documento di uscita di C/Lavoro.

Nella tabella di lancio B£JXX è ncessario impostare nel campo "parametri aggiuntivi" : 
 * Tipo riga
 * Ubicazione

## Formato video
![P5PMFP_51](http://localhost:3000/immagini/MBDOC_OGG-P_V5AT51A/P5PMFP_51.png)Area di giacenza e tipo giacenza sono derivate dalla prima causale di movimentazione di scarico ("-") presente nel tipo riga. La giacenza deve essere univoca e di tipo MFP :  ubicazione / fase / contenitore.
Il contenitore in input deve essere presente nell'area / tipo giacenza e solo nell'ubicazione scelta.

## Scrittura file di lavoro
Dalla giacenza deriva magazzino, fase, quantità .
Dal contenitore deriva l'ordine di produzione
Dal ciclo del contenitore deriva il centro di lavoro della fase successiva, dal centro di lavoro deriva il fornitore che deve corrispondere a quello in testata documento.

## Visualizzazione file di lavoro
Con F8 si lancia il programma V5AT51W di visualizzazione del file di lavoro che usa i campi :  BTCD01, BTCD02, BTCD03 come righe di visualizzazione.
![P5PMFP_52](http://localhost:3000/immagini/MBDOC_OGG-P_V5AT51A/P5PMFP_52.png)
## Scrittura righe documento
Per avere la scrittura delle righe documento deve esistere un successivo passo di flusso che richiama il programma V5AT51Z.
