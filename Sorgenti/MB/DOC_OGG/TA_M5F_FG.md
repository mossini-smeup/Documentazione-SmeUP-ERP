## Fabbisogno giornaliero
Se l'origine è FG (fabbisogno giornaliero)
Per ogni giorno in cui sono presenti eventi di disponibilità, si determina la somma algebrica delle coperture  e dei fabbisogni. Se tale somma è negativa essa costituisce (cambiata di segno) il fabbisogno giornaliero.
Si assume che tale fonte sia futura, ma può ritornare anche fonti presenti (se la disponibilità presente è negativa, ad esempio a causa di una scorta minima).
Il segno di tale fonte è unicamente documentativo, in quanto tutti gli elementi ritornati avranno tale segno.
Questa fonte è stata mantenuta per compatibilità con il passato. Il suo comportamento è compreso nella fonte QG (quantità giornaliera) con il tipo filtro 'B' (fabbisogno netto).
>Parametro 1 : 
-    Pos.1/10  Gruppo fonti per calcolare il fabbisogno giornaliero.
Parametro 2 : 
-    Pos.1/1   Suddivisione per oggetto di rottura. Se impostato, se la
.              pianificazione è impostata per codice di rottura e l'articolo è
.              pianificato a rottura, viene eseguito il calcolo separato per ogni
.              oggetto di rottura (che viene ritornato dalla disponibilità nel campo
.              predisposto :  commessa, configurazione, ecc..)

