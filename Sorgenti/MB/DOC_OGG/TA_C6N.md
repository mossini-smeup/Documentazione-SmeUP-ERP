# C6N - Non Conformità controllo fatture
 :  : DEC T(ST) K(C6N)
## OBIETTIVO
Definisce le possibili non conformità nel controllo fatture di acquisto aperte, ecc.. nelle analisi di disponibilità.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È il codice della "NON CONFORMITA"
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$C6NA **Codice Default**
È un elemento della tabella CQD, è necessario per la scrittura del record nel file CQNCOG0F (non conformità di Q9000)
 :  : FLD T$C6NB **Causale**
È un elemento della tabella CQC, è necessario per la scrittura del record nel file CQNCOG0F (non conformità di Q9000)
 :  : FLD T$C6NC **Prog.Dest.Msg.Definito**
È un campo facoltativo. Indica il programma specifico per il recupero automatico della "Destinazione" della non conformità (Suffisso XX del programma C5CF71_XX).
 :  : FLD T$C6ND **Param.  "**
Si può indicare un parametro da legare al programma di attribuzione destinazione
 :  : FLD T$C6NE **Progr. Gest.Az.Corr.**
È un campo facoltativo. Indica il programma specifico di gestione delle azioni correttive della Non Conformità. (Suffisso XX del programma C5CF72_XX)
 :  : FLD T$C6NF **Param.  "**
Si può indicare un parametro da legare al programma di gestione
 :  : FLD T$C6NG **Progr. Esec.Az.Corr.**
È un campo facoltativo. Indica il programma specifico di esecuzione delle azioni correttive della Non Conformità. (Suffisso XX del programma C5CF73_XX)
 :  : FLD T$C6NH **Param.  "**
Si può indicare un parametro da legare al programma di esecuzione
 :  : FLD T$C6NI **Progr. Esec.Az.Corr.**
