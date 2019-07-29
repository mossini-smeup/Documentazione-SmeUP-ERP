# Descrizione
* BLDSM51

# Fasi build

## Ricezione XMI origine
* RCVXMI RESTORE(*YES) DATE(*TODAY)

## Conversione orgine
* CRTXMIDBF
* CRTXMIDSPF
* CRTXMIPRTF
* CRTXMIMOD
* CRTXMIPGM

## Buid prodotto
* RUNMVNUNIT

Fasi del processo : 

* Inizializzazione della cartella di build
* Copia dei sorgenti dalla libreria di espostazione alla cartella di build
* Avvio compilazione sorgenti

Il risultato sarà : 

* Compilazione dei singoli moduli (DBF, DSPF, PRTF, MOD, PGM)
* In caso di errore in compilazione, produce un log di errore
* In caso di compilazione eseguita correttamente viene prodotto un sito P2 contenente i plugin aggiornati con gli utlimi sorgenti

## Deploy repository test
* SNDMVNUNIT
** smeup.github.io/com.smeup.erp.p2.test.site
** github.com/smeup/smeup-gen/tree/test

## Esecuzione test
* RCVMVNUNIT RESTORE(*YES)
** smeup.github.io/com.smeup.erp.p2.test.site
* RUNTEST COMP(*ALL) OUTPUT(*MEMO)

* SNDMVNUNIT
** smeup.github.io/com.smeup.erp.p2.prod.site
** github.com/smeup/smeup-gen/tree/master

