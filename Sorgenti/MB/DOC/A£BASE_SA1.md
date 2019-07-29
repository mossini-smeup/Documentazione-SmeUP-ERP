È possibile suddividere le librerie di Sme.up in tre tipologie : 
 - Librerie standard
 - Librerie dell'ambiente di sviluppo
 - Librerie dei clienti

## Standard

| Libreria | Descrizione |
| ---|----|
| SMESRC | Sorgenti standard all'ultimo rilascio di tutti i programmi e dei file video. |
| SMESTD | Sorgenti standard all'ultimo rilascio di tutto ciò che non sono programmi o file video (file fisici, logici, dizionari, /COPY ecc.) |
| SMEUP_OBJ | Tutti gli oggetti compilati all'ultimo rilascio |
| SMEDEV | Sorgenti e Oggetti di tutto ciò che è stato modificato e rilasciato dopo l'ultimo rilascio |
| SMEUP_FIL | Tutti i file con impostazioni da modello |
| SMETRD | File con traduzioni |
| SME_xx00 |  oggetti compilati per l'utilizzo di una determinata lingua (es. file video, xx è il codice iso di una lingua) |
| 


## Ambiente di sviluppo

| Libreria | Descrizione |
| ---|----|
| SMEUP_SVI | Sorgenti e Oggetti in alpha Test |
| SMEUP_TST | Sorgenti e Oggetti in beta Test |
| SMEUP_DAT | File con dati di test |
| SMETAB | File Tabelle con le definizioni standard delle tabelle ed elementi di test |
| W_xx | Libreria utente (dove xx sta per l'account utente) |
| P_nnnnnn | Libreria di branch (dove nnnnnn sta per il codice del branch) |
| 


## Librerie dei clienti installate su server di sviluppo

| Libreria | Descrizione |
| ---|----|
| PER_xxx | Libreria del cliente (dove _xxx_ indica il cliente), contentente le personalizzazioni. Vengono salvate ogni sera. |
| XPER_xxx | Libreria del cliente (dove _xxx_ indica il cliente), portate in SME.up come ambienti di test. Non ne vengono eseguiti backup. |
| 

