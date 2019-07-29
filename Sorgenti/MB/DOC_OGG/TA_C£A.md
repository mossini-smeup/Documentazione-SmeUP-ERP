# C£A - Categoria regole
 :  : DEC T(ST) K(C£A)
## OBIETTIVO
Permettere di raggruppare delle regole in una categoria. Ad una categoria di regole possono essere associati due tipi di oggetti.
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 **Tipo codice 1**
Specifica di che tipo è il primo codice associato alla categoria. È un elemento della tabella *CNTT.
 :  : FLD T$PAR1 **Parametro tipo codice 1**
Se indicata una tabella nel tipo, permette di definire il nome di tale tabella.
 :  : FLD T$KYC2 **Tipo codice 2**
Specifica di che tipo è il secondo codice associato alla categoria. È un elemento della tabella *CNTT.
 :  : FLD T$PAR2 **Parametro tipo codice 2**
Se indicata una tabella nel tipo, permette di definire il nome di tale tabella.
 :  : FLD T$SSRE **Sottosettore regole**
È il sottosettore della tabella C£T nel quale sono elencate le regole appartenenti alla categoria definita.
 :  : FLD T$C£AR **Modalità di risalita per codice 1**
.    A = Solo se assente
La risalità sul  codice 1 viene effettuata solo se il codice specifico non ha associata nessuna regola. In questo caso vengono restituite le regole collegate al codice generico.
.    B = Sempre
La risalità sul  codice 1 viene effettuata sempre, anche se il codice specifico ha associate delle regole. In questo caso vengono restituite le regole collegate sia al codice generico che a quello specifico.
 :  : FLD T$C£AS **Modalità di risalita per codice 2**
.    A = Solo se assente
La risalita sul  codice 2 viene effettuata solo se il codice specifico non ha associata nessuna regola. In questo caso vengono restituite le regole collegate al codice generico.
.    B = Sempre
La risalita sul  codice 2 viene effettuata sempre, anche se il codice specifico ha associate delle regole. In questo caso vengono restituite le regole collegate sia al codice generico, che a quello specifico.
.    C = Tutti
Questa opzione viene applicata solo se, nella richiesta delle regole associate a una categoria e a dei codici specifici, il secondo codice è diverso da blanks.
La risalita viene effettuata per tutti i codici 2 che hanno delle regole associate in corrispondenza della categoria e del codice 1 definiti.
