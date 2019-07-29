## Documenti applicativi

E' possibile schedulare l'acquisizione cambi giornalieri.

Questo può avvenire sia depositando il file UIC_CambiGiornalieri.csv nella cartella IFS oppure su una cartella del server ove è installato SmeUp Provider.

## Prerequisiti

* Configurare le seguenti variabili nel SCP_CLO : 
** BRCAMB.FLR001 :  Path ove verrà depositato e letto il file UIC_CambiGiornalieri.csv
** BRCAMB.FLR002 :  SmeUp Provider, indicare '1' se il file si trova sul server ove è installato Smeup Provider
** BRCAMB.FLR003 :  Coda utilizzato per lo Smeup Provider

* Configurare il LOA27_BR con le credenziali per la schedulazione tramite Smeup Provider

* Lanciare la schedulazione tramite il seguente comando :  CALL PGM(LOA27_BT) PARM('BR.BR.CAM').


