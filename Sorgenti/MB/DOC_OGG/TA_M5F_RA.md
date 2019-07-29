## Richiesta acquisto
>Se l'origine è RA (richiesta d'acquisto)
Parametro 1 : 
-    Pos.1/4   Tipo Richiesta (opzionale).
-    Pos.5     Data rettificata :  se impostato, la data della fonte verrà avanzata
.              dei giorni di rettifica. Verranno usati i giorni di rettifica di
.              acquisto o lavorazione, reperiti dai dati di pianificazione per
.              articolo, in base alla caratteristica della riga (flag 3 del record
.              di riga). Verrà usato il magazzino su cui si sta eseguendo l'analisi
.              disponibilità, sia per reperire i dati di pianificazione sia per
.              reperire il calendario (posto che non si sia impostato, in tabella
.              M51, di trattare giorni solari). Con questa rettifica si interpone una
.              'sicurezza' tra la data di consegna del materiale e quella del suo
.              utilizzo. Inoltre, dato che la pianificazione propone ordini che
.              tengono conto di questo tempo, se, dopo il loro rilascio, non se ne
.              continuasse a tenerne conto, la pianificazione successiva suggerirebbe
.              un anticipo, del tutto superfluo, pari al tempo di rettifica.

