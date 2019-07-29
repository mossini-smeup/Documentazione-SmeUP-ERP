# B£G - Griglia controllo 3 oggetti
 :  : DEC T(ST) K(B£G)
## OBIETTIVO
>>>>>>>>>>>>Da completare<<<<<<<<<<<<
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 **Codice 1**
Ogni codice descrive uno degli oggetti noti al sistema, come caratterizzati nella tabella associata al campo stesso (*CNTT).
 :  : FLD T$KYC2.T$KYC1 **Codice 2**
 :  : FLD T$KYC3.T$KYC1 **Codice 3**
 :  : FLD T$PAR1 **Parametro**
Utilizzato solo per alcuni tipi di oggetto. Se l'oggetto è una tabella, il parametro caratterizza il codice della tabella stessa.
 :  : FLD T$PAR2.T$PAR1 **Parametro**
 :  : FLD T$PAR3.T$PAR1 **Parametro**
 :  : FLD T$DES1 **Descrizione specifica**
Normalmente la descrizione, se richiesta, viene ripresa dalla tabella *CNTT in funzione dell'oggetto. Se è una tabella sarà la descrizione della tabella.  È possibile qui indicare una descrizione da utilizzare in sostituzione.
 :  : FLD T$DES2.T$DES1 **Descrizione specifica**
 :  : FLD T$DES3.T$DES1 **Descrizione specifica**
 :  : FLD T$OBB1 **Valore obbligatorio**
Indica al programma di restituire un errore se il campo indicato risulta non immesso.
 :  : FLD T$OBB2.T$OBB1 **Valore obbligatorio**
 :  : FLD T$OBB3.T$OBB1 **Valore obbligatorio**
 :  : FLD T$ACA1 **Accetta codici che iniziano con ****
Indica al programma di accettare come validi i codici che iniziano con **. Ciò al fine di poter inserire anche codici generici non presenti nel DATABASE.
 :  : FLD T$ACA2.T$ACA1 **Accetta codici che iniziano con ****
 :  : FLD T$ACA3.T$ACA1 **Accetta codici che iniziano con ****
