# OBIETTIVI

Questo programma si pone l'obiettivo di controllare/riallineare il regime iva delle registrazioni  di documenti iva, in funzione dei valori previsti in queste due informazioni : 
* Parametro azienda, "Regime per cassa"
* Campo anagrafico cliente, "Iva per Cassa"

Questa funzione dovrebbe quindi essere eseguita a seguito di una variazione dei sopracitati dati, al fine di allineare le registrazioni inserite, precedentemente, a tale variazione.

Tecnicamente questo si tradurrà nell'aggiornamento del flag 25 di testata delle registrazioni contabili e del flag 25 delle scadenze della corrispondente partita.

**NOTA BENE** :  qualsiasi sia il periodo indicato, vengono escluse dall'elaborazione le registrazioni precedenti all'ultima liquidazione definitiva.

