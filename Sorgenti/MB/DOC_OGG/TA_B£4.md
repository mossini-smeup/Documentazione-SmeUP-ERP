# B£4 - Date particolari
 :  : DEC T(ST) K(B£4)
## CONTENUTO DEI CAMPI
 :  : FLD T$B£4A **Forzature particolari**
1 =  Porta in negativo il valore della data se appartiene al 1900
2 =  Toglie 50 anni alla data se appartiene al 1900
 :  : FLD T$B£4B **Tipo comparazione**
Definisce il metodo con cui trattare le date manuali immesse.
 :  : FLD T$B£4C **Data manuale 1**
Valore di data immesso dall'utente
 :  : FLD T$B£4D **Data manuale 2**
Valore di data immesso dall'utente
_9_Esempi
Per i movimenti di magazzino sono valide solo le date successive al 31/12/1999.
-    Operatore      GT
-    Data 1         31121999
-    Data 2         Bianca
Per i movimenti contabili si accettano solo date registrazione appartenenti al mese corrente
-    Operatore      RG
-    Data 1         &OMI
-    Data 2         &OMF
