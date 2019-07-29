# Obiettivo
Specificano i parametri guida per la pianificazione di ciascun articolo e possono essere definiti a livello di :  Articolo / Plant, Codice di classificazione (es. classe materiale) / Plant, Generico / Plant.
Il programma, nel ricercare i parametri di pianificazione per un articolo, utilizza il metodo della "risalita", cioè cerca il parametro a livello di articolo e, se non lo trova, lo cerca a livello di classe e, se anche in questo caso non lo trova, utilizza il default a livello generico.

Per gestire i parametri di pianificazione si usa il seguente formato di dettaglio : 

![M5_001_02](http://localhost:3000/immagini/MBDOC_OGG-P_M5ARTP/M5_001_02.png)
Si possono inserire : 
 * __Tipo e politica di riordino__, che definisce se l'articolo è di acquisto, produzione o conto-lavorazione (le politiche di riordino sono definite nella tabella M5A); nel caso di pianificazione multiplant completa si possono anche impostare le politiche di trasferimento utilizzate dal sistema quando pianifica un trasferimento dal plant di responsabilità a quello utilizzatore
 * __Percentuale di assegnazione__, se diversa da 100 pianifica la copertura del fabbisogno in funzione della precentuale assegnata (il totale deve essere 100)
 * __Tempi di riordino (lead time)__, che definiscono i tempi dal rilascio di un ordine materiale alla sua disponibilità.
Essi possono essere : 
 ** fisso (si applica nella definizione della data disponibilità dei componenti)
 ** variabile (si applica nella definizione della data disponibilità dei componenti, in base alla quantità da procurare)
 ** di rettifica (tempo aggiuntivo comprensivo dei tempi amministrativi di ricevimento e i tempi di collaudo)
 * __Quantità (lotto)__, che definisce, se indicata, l'arrotondamento o la suddivisione dei lotti da ordinare rispetto al fabbisogno netto.
Possono essere definiti i lotti : 
 ** minimo (maggiora il fabbisogno al lotto minimo)
 ** multiplo (arrotonda il fabbisogno a una quantità multipla del lotto)
 ** massimo (se il fabbisogno è superiore il sistema lo suddivide in più fabbisogni, ciascuno non superiore al lotto massimo).
