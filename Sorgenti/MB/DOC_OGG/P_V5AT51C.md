# Crea righe work da R/F (colli MFP)
Il programma carica in un file di WORK le righe che andranno a comporre il documento di rientro del C/Lavoro.

Nella tabella di lancio B£JXX è ncessario impostare nel campo "parametri aggiuntivi" : 
 * Tipo riga
 * Ubicazione
 * Unità di Movimentazione
 * Tipo Collo

## Formato video
![P5PMFP_58](http://localhost:3000/immagini/MBDOC_OGG-P_V5AT51C/P5PMFP_58.png)
## Scrittura file di lavoro
In questo programma di esempio il codice letto con il terminale R/F è il barcode di un collo MFP.

La quantità deve essere inserita manualmente

Il fornitore deve corrispondere a quello della testata del documento in costruzione

Il campo BTFL01 deve essere = ' ' in modo che non vengano creati nè un nuovo contenitore MFP nè l'alias. Il campo BTCD20 contiene l'UdM del contenitore.

## Visualizzazione file di lavoro
Con F8 si lancia il programma V5AT51W di visualizzazione del file di lavoro che usa i campi :  BTCD01, BTCD02, BTCD03 come righe di visualizzazione.
![P5PMFP_57](http://localhost:3000/immagini/MBDOC_OGG-P_V5AT51C/P5PMFP_57.png)
## Scrittura righe documento
Per avere la scrittura delle righe documento, e la creazione dell'alias, deve esistere un successivo passo di flusso che richiama il programma V5AT51Z.
