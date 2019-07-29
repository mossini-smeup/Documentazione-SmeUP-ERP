## Contenuto
Stesso tracciato del file GMMOVI0F con in coda i seguenti quattro campi : 
 * M§BATC     Lotto transazione
 * M§NRTR     Numero transazione
 * M§CDMS     Codice messaggio di errore
 * M§FIMS     File messaggi

M§BATC e M§NRTR servono per identificare e raggruppare i records relativi a una transazione.
M§CDMS e M§FIMS descrivono eventuali errori.

Il file è utilizzato come driver di scrittura dei movimenti di magazzino che saranno applicati all'ambiente definito in tabella B£1. Nel caso in cui l'ambiente movimenti di magazzino sia Sme.up l'applicazione dei movimenti avverrà col programma GMTR00_SM.

## Codice Oggetto (in TA/*CNTT)

## Chiave primaria

## Altri condizionamenti facoltativi in ricerca

## Ulteriore chiave primaria

## Tabella guida
Le impostaziooni che condizionano questo archivio sono contenute nel settore di tabelle GMC (Causale movimento) : 
 :  : DEC T(ST) K(GMC)

## Autorizzazioni

## Note strutturate (Tabella NSC)

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
Il visualizzatore del dettaglio del movimento viene definito in Tab. GMC.
Nella movimentazione manuale a 2 causali (PGM -  GMMV02I) esiste una seconda possibilità di definire il programma di visualizzazione :  impostato nella tabella B££xx.

## Programmi di controllo
Esiste la pissibilità di intervenire sui movimenti di magazzino tramite il programma di aggiusamento definito in tabella GMC (vedi es.GMTR00K_ES)

## /COPY
Gestione e applicazione movimenti di magazzino (£G24) : 
 :  : DEC T(MB) P(QILEGEN) K(£G24)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
N.A.

## CONTENUTO DEI CAMPI

 :  : FLD M§NURE **Numero registrazione**
Si assume il numeratore definito in tabella GM1, (tabella CRN, sottosettore GM).

 :  : FLD M§TIMO **Tipo movimento**
Viene copiato per motivi di prestazioni (e non è modificabile) dal campo omonimo di tabella GMC.
 :  : DEC T(CS) P(T/GMC) K(T$GMCM) R(1)

 :  : FLD M§TIGC **Area giacenza**
Viene copiato per motivi di prestazioni (e non è modificabile) dal campo omonimo di tabella GMC.
 :  : DEC T(CS) P(T/GMC) K(T$GMCA) R(1)

 :  : FLD M§SOGC **Tipo giacenza**
Viene copiato per motivi di prestazioni (e non è modificabile) dal campo omonimo di tabella GMC.
 :  : DEC T(CS) P(T/GMC) K(T$GMCT) R(1)

 :  : FLD M§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) imserito in tabella GMC.
 :  : FLD M§COD2.M§COD1 **Codice 2**
 :  : FLD M§COD3.M§COD1 **Codice 3**
 :  : FLD M§COD4.M§COD1 **Codice 4**
 :  : FLD M§COD5.M§COD1 **Codice 5**

 :  : FLD M§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) imserito in tabella GMC.
 :  : FLD M§NUM2.M§NUM1 **Numero 2**
 :  : FLD M§NUM3.M§NUM1 **Numero 3**
 :  : FLD M§NUM4.M§NUM1 **Numero 4**
 :  : FLD M§NUM5.M§NUM1 **Numero 5**
