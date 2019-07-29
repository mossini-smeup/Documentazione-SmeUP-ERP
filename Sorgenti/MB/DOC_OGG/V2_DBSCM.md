# DBSCM     -  SCELTA COMPONENTI IN DISTINTA BASE
Definisce il modo in cui nell'esplosione di distinta base vengono selezionati i legami in funzione della loro
validità.
In un legame di distinta base si può impostare un campo che lo rende : 
-    sempre valido
-    valido se l'assieme viene prodotto internamente
-    valido se l'assieme viene prodotto esternamente

## VALORI POSSIBILI

### ' ' INTERNI
Sono ritornati i legami sempre validi e quelli validi per interno.

### 'X' ESTERNI
Sono ritornati i legami sempre validi e quelli validi per esterno.

### '*' ENTRAMBI
Sono ritornati tutti i legami.

### 'P' DA POLITICA PIANIFICAZIONE
Per ogni assieme non fittizio viene determinato il tipo politica master (dai suoi parametri di pianificazione) : 
-    se la politica è di produzione si riconduce al caso ' '
-    se la politica è di lavorazione si riconduce al caso 'X'
-    se la politica è di acquisto nessun legame è valido
In questo modo, nelle esplosioni a più livelli (di produzione totale, riepliogata, ai materiali di base, ecc..)
vengono ritornati i componenti effettivamente utilizzati nelle situazioni reali.
