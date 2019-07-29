# V5T - Tipo viaggio
 :  : DEC T(ST) K(V5T)
## OBIETTIVI
-    Caratterizzare la tipologia dei viaggi per poterla utilizzare per impostare comportamenti e classificazioni comuni a viaggi dello stesso tipo
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
Per ogni viaggio si possono definire caratterizzazioni che verranno utilizzate per tutti i viaggi dello stesso tipo.
## CONTENUTO DEI CAMPI
 :  : FLD T$V5TA **Natura viaggio**
È un elemento fisso V2/NAVIA e definisce in modo univoco la natura del viaggio. Questo campo, avendo un significato prefissato, può essere usato dalle applicazioni in modo esplicito.
 :  : FLD T$V5TC **Tipo/parametro oggetto esecutore**
Individuano il tipo di oggetto che eseguirà i viaggi di questo tipo.
 :  : FLD T$V5TD.T$V5TC
 :  : FLD T$V5TF **Tipo documento origine**
È un elemento della tabella V5D :  individua il tipo di documento che origina i viaggi di questo tipo.
 :  : FLD T$V5TH **Tipo documento spedizione**
È un elemento della tabella V5D :  individua il tipo di documento che, a sua volta, individua le spedizioni di viaggi di questo tipo.
 :  : FLD T$V5TI **Livello di nascita**
Se, in inserimento del viaggio, non viene specificato uno stato, viene assunto questo livello, con il suo stato principale.
 :  : FLD T$V5TJ **Gruppo flag**
È un elemento della tabella B£Y. Se valorizzato, all'atto dell'inserimento del viaggio vengono assegnati i flag di questo elemento.
 :  : FLD T$V5TK **Priorità assunta**
È un elemento della tabella B§A che viene proposto all'atto dell'inserimento dei viaggi.
 :  : FLD T$V5TL **Categoria parametri**
È un elemento della tabella C£E che definisce i parametri esterni collegabili al viaggio.
 :  : FLD T$V5TM **Parametri impliciti**
È un elemento della tabella C£I che definisce i parametri collegabili al viaggio, contenuti all'interno dell'archivio.
 :  : FLD T$V5TN **Contenitore note**
È l'elemento della tabella NSC che contiene le note dei viaggi di questo tipo.
 :  : FLD T$V5TO **Numeratore viaggi**
È l'elemento della tabella CRN (sottosettore VG), che viene usato per assegnare il numero al viaggio.
 :  : FLD T$V5TB **Percorsi**
È un elemento della tabella C£I che definisce i percorsi collegabili al viaggio, contenuti all'interno dell'archivio (si usano i campi alfanumerici di questa tabella).
