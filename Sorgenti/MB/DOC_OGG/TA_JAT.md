# Funzioni grafiche
## OBIETTIVO
Gestire la corrispondenza fra un servizio codificato ed il programma che ne implementa funzioni e metodi.
La tabella era importante nella prima versione di LOOC.up. Attualmente si fa coincidere il servizio con il nome del programma. I pochi servizi restanti (alcuni di questi quali *SCO *TBL ecc) molto importanti, hanno una associazione fissa dentro LOOC.up, quindi tutto deve funzionare anche in mancanza della tabella JAT.
## CONTENUTO DEI CAMPI
 :  : FLD T$JATA __Costruttore__
È un elemento V3/PJ1 ed indica il suffisso del pgm che gestisce la funzione grafica, il cui nome viene definito nel seguente modo :  "JATRE_"+T$JATA+"C".
 :  : FLD T$JATB __Parametro costruttore__
È un campo libero che definisce, in pratica, il metodo di richiamo del costruttore.

