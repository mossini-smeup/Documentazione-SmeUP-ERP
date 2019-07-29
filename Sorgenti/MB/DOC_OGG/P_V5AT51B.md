# Crea righe work da R/F (colli esterni)
Il programma carica in un file di WORK le righe che andranno a comporre il documento di rientro del C/Lavoro.

Nella tabella di lancio B£JXX è ncessario impostare nel campo "parametri aggiuntivi" : 
 * Tipo riga
 * Ubicazione
 * Unità di Movimentazione
 * Tipo Collo

## Formato video
![P5PMFP_56](http://localhost:3000/immagini/MBDOC_OGG-P_V5AT51B/P5PMFP_56.png)
## Scrittura file di lavoro
In questo programma di esempio il codice letto con il terminale R/F è il barcode di un collo esterno alla gestione MFP da cui sono derivati i campi fornitore e articolo : 
 * fornitore :  caratteri dal  1 al 15
 * articolo :  caratteri dal 16 al 30

La quantità deve essere inserita manualmente

Il fornitore deve corrispondere a quello della testata del documento in costruzione

Il barcode letto costituirà l'alias del contenitore che sarà generato nel passo successivo di creazione del documento. Il campo BTFL01 deve essere = '1' in modo che venga creato il contenitore MFP mentre il codice alias viene messo nel campo BTKEY1. Il campo BTCD20 contiene l'UdM del contenitore

## Visualizzazione file di lavoro
Con F8 si lancia il programma V5AT51W di visualizzazione del file di lavoro che usa i campi :  BTCD01, BTCD02, BTCD03 come righe di visualizzazione.
![P5PMFP_57](http://localhost:3000/immagini/MBDOC_OGG-P_V5AT51B/P5PMFP_57.png)
## Scrittura righe documento
Per avere la scrittura delle righe documento, e la creazione dell'alias, deve esistere un successivo passo di flusso che richiama il programma V5AT51Z.
