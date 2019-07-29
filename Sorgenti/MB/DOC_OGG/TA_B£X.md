# B£X - Deviazione attributi
 :  : DEC T(ST) K(B£X)
## OBIETTIVO
Poter deviare il programma di calcolo di un attributo interno (I) o intrinseco (J) su un programma utente.
## UTILIZZO
Questa tabella viene usata all'atto della costruzione dell'archivio di definizione degli attributi (B£SLOT0F).
## SOTTOSETTORI
Si imposta il tipo oggetto dell'attributo (AR/RI/CN).
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
Si imposta il codice dell'attributo
 :  : FLD T$B£XA **Programma di deviazione**
Si imposta il programma specifico di calcolo dell'attributo :  è un campo obbligatorio.
 :  : FLD T$B£XB **Parametro programma**
Si imposta, opzionalmente, il parametro del programma specifico di calcolo dell'attributo.
