# IGR - Codici di aggregazione
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
 :  : FLD T$DESC Descrizione
È la descrizione codice di aggregazione.
 :  : FLD T$IGR1 __Base della ripresa/Attributo__
Base della ripresa è uno dei campi dell'archivio Report.
Si suddividono in 3 tipolgie : 
-->**Sintesi** (identificate tramite la tabella IGS del livello di sintesi).
-->**Aggregazioni** (definite dalla tabella IGG).
-->**Campi liberi** (si differenziano in 20 campi alfanumerici e 10 numerici e sono, ad esempio :  N° fattura, Data fattura, Commessa, Configurazione, Lotto etc.).

La definizione del valore può essere di tipo primo o derivato. Se si tratta di tipo primo, costituisce il contenuto stesso del campo del file, se si tratta di derivato, costituisce un OAV, funzione dell'oggetto identificato dalla base della ripresa. L'attributo identifica di un oggetto il puntatore al valore selezionato.
_9_Esempi : 
 - Cliente  (Tipo primo)
Base della ripresa  S02  Cliente è funzione della IGS
 - Attributo
 - Tipo oggetto        CN
 - Parametro ogg.      CLI
 - N°fattura (Tipo primo)
 Base della ripresa  L02  Libero alfanumerico 2
 - Attributo
 - Tipo oggetto        **
 - Parametro ogg.
 - Classe materiale (Tipo derivato)
Base della ripresa  S03      Articolo è funzione della IGS
 - Attributo           I/10     Indice OAV classe materiale.
 - Tipo oggetto        TA
 - Parametro ogg.      CLS
 :  : FLD T$IGR2.T$IGR1 __Attributo di ripresa__
 :  : FLD T$IGR3 __Tipo oggetto__
Identifica il tipo oggetto risultato del calcolo per le decodifiche in fase di stampa.
_9_Esempio : 
Base della ripresa  S02      Cliente
 - Attributo           I/12     Agente
 - Tipo oggetto        TA       Tipo oggetto per decodifica
 - Parametro ogg.      AGE
 :  : FLD T$IGR4.T$IGR3 __Parametro del livello__
