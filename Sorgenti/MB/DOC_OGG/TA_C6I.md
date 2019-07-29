# C6I - Indici di Bilancio
 :  : DEC T(ST) K(C6I)
## OBIETTIVO
Definire la struttura di definizione degli indici di bilancio.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrive l'insieme degli indici
 :  : FLD T$C6IA Contesto
Va indicato il contesto da utilizzare. Deve corrispondere a CNAZI (o in alternativa AZ)
 :  : FLD T$C6IB Tema Indici
Definisce il tema finale in cui verranno memorizzati gli indici finali calcolati.
E' importante che questo tema come tutti gli altri preveda come chiave 1 TAC6I&&.
Data/Periodo deve essere valorizzata a "P".
 :  : FLD T$C6IC Tema Fattori
Definisce il tema in cui verranno riportati i fattori da impiegare per il calcolo degli indici. Possono corrispondere direttamente a valori di bilancio, o a formule applicate su di essi e/o parametri numeri (possibilmente datati) sull'azienda.
E' importante che questo tema come tutti gli altri preveda come chiave 1 TAC6I&&.
Data/Periodo deve essere valorizzata a "P".
 :  : FLD T$C6ID Tema Valori di Bilancio
Definisce il tema in cui verranno ricodificate le riclassifiche di bilancio da utilizzare come fattori per il calcolo degli indici.
E' importante che questo tema come tutti gli altri preveda come chiave 1 TAC6I&&.
Data/Periodo deve essere valorizzata a "P".
 :  : FLD T$C6IE Riclassifica
E' la riclassifica di riferimento presa in considerazione per la costruzione del tema dei valori.
 :  : FLD T$C6IF Tema Riclassifica
Definisce il tema in cui verrà memorizzata l'intera riclassifica utilizzata per il calcolo degli indici.
Questo tema, a differenza degli altri, deve prevedere come chiavi : 
* Chiave 1 :  elemento TAC6I&&
* Chiave 2 :  elemento TAC5Nxx dove xx è il sottosettore della riclassifica presa come riferimento (es. sul CEE è normalmente TAC5NCE).
* Chiave 3 :  elemento TAC5B&&
Data/Periodo deve essere valorizzata a "P".
 :  : FLD T$C6IG Pertinenza Gestionale
Indica la combinazione di pertinenze che vuole essere presa in considerazione quando gli indici vengono interrogati infra-annualmente. A fine esercizio viceversa vengono prese in  considerazione sempre solo le pertinenze fiscali e comuni.
 :  : FLD T$C6IH Condizione Gestionale
Indica la combinazione di condizioni che vuole essere presa in considerazione quando gli indici vengono interrogati infra-annualmente. A fine esercizio viceversa vengono presa in  considerazione sempre solo le condizione attiva.
 :  : FLD T$C6IJ Filtro Intercompany
Permette di applicare dei filtri ai saldi, sulla base della condizione intercompany : 
* Con valore 1 vengono esclusi tutti i movimenti intercompany
* Con valore 2 vengono esclusi tutti i movimenti che non sono considerati intercompany

