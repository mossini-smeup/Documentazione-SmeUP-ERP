# MMO - Codici interventi
## OBIETTIVO
Classificare i vari interventi e definire le caratteristiche
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Codice
 :  : FLD T$DESC Descrizione
Descrizione
 :  : FLD T$MMOA  __Obbligo tempi dich.__
Se non è blank, indica che i tempi sono obbligatori
 :  : FLD T$MMOB  __Riclassifica__
Codice libero per classificare i codici interventi
 :  : FLD T$MMOC  __Obblig. 1° Esecutore__
Se non è blank, indica che il primo esecutore è obbligatorio
 :  : FLD T$MMOD  __Obblig. dell'Esito__
Se non è blank indica che l'esito è obbligatorio
 :  : FLD T$MMOE  __Suff.pgm ripresa materiali__
Se specificato un valore, alla scelta dell'opzione 13=Ripresa nel formato
di gestione dei materiali di un intervento verra' richiamato il programma
MMAM23E_x (con x=valore specificato) per il reperimento personalizzato dei
materiali di un intervento.
In assenza di tale suffisso verra' invece richiamato il pgm MMAM23E che
permettere di derivare i materiali da quelli dichiarati sull'intervento
programmato.
