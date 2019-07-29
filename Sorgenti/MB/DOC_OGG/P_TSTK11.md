

# Obiettivo
Richiamare un web service esterno al fine di integrare dati in ingresso oppure di inviarli.

## Funzione SND metodo OUT. Invia messaggio a webservice - Da server a webservice
Permette di effettuare una richiesta webservice passando in input le schiere di variabili Nome (£K11S_NM) e Valore (£K11S_VA). Le variabili devono essere definite nel relativo script LOA38. Viene restituita la chiave per la lettura dei dati di output in matrice.

## Funzione SND metodo FIL. Invia messaggio a webservice - Da server a webservice
Permette di effettuare una richiesta webservice passando in input le schiere di variabili Nome (£K11S_NM) e Valore (£K11S_VA) e nel parametro PAYLOAD il file indicato. Le variabili devono essere definite nel relativo script LOA38. Viene restituita la chiave per la lettura dei dati di output CDATA.
Il file deve risiedere nell'IFS del server.

## Funzione GRI metodo SCH. Griglia - Restituzione schiere
Restituisce la griglia di definizione delle colonne in output dal webservice, necessita della chiave restituita dal SND.OUT.

## Funzione RIG metodo POS e LET. Righe - Posizionemento e lettura
Posiziona all'inizio e legge una riga alla volta l'output dal webservice, necessita della chiave restituita dal SND.OUT.

## Funzione DAT metodo POS e LET. Righe - Posizionemento e lettura
Posiziona all'inizio e legge una riga alla volta l'output dal webservice, necessita della chiave restituita dal SND.FIL.

## Funzione INI. Reinizializza Provider
Effettua la reinizializzazione del provider per l'istanza del webservice richiesta.

Per la definizione dei webservice si rimanda alla documentazione specifica del costruttore LOA38 : 
- [BASE Integrazione con webservice](Sorgenti/MB/DOC_OGG/V2LOCOSA38)
