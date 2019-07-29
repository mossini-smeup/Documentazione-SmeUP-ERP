# MU1 - Personalizzazioni MULT
 :  : DEC T(ST) K(V5D)
## OBIETTIVO
Impostazioni base ambiente multipiattaforma
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM
Elemento Fisso

 :  : FLD T$DESC
Descrizione generica tabella

 :  : FLD T$MU1B
Release di compilazione, viene effettuato un test di confronto quando si incontrano le specifiche di
precompilazionie DEFINED

 :  : FLD T$MU1A
Questo è il campo che definisce la cartella dell'IFS in cui vengono depositati i file prodotti dalla
conversione.
Se tale campo è blank, l'estrazione depositerà i file nel percorso : 
**/SmeMult/
Se tale campo non è blank, allora l'estrazione depositerà i file nel percorso : 
**/SmeMult/xxxxxxxxxxxxxxxxxxxx/

 :  : FLD T$MU1C
Determina il contesto di esecuzione dell'estrazione
