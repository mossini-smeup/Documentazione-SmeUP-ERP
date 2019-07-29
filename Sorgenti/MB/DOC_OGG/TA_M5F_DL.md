## Disponibilità libera
>Se l'origine è DL (disponibilità libera)
Parametro 1 : 
-    Pos.1/10  Gruppo fonti per calcolare la disponibilità libera alla data
.              (obbligatorio)
Parametro 2 : 
-    Pos.1     Se impostato, verranno trascurati, nel computo della
.              disponibilità libera, gli impegni con data superiore al lead time
.              cumulato dell'articolo.
-    Pos.2/3   Se impostato, è un numero di giorni di sicurezza, che si somma al
.              lead time, nella determinazione della data massima in cui si
.              considerano gli impegni.
-    Pos.4/6   Se impostato, è un elemento della tabella modelli di ATP (M5H) :  la
.              data di partenza del calcolo non sarà oggi ma la data di partenza
.              dell'ATP (se presente). Il modello ATP deve essere, al massimo, di tre
.              caratteri
-    Pos.7/7   Se impostato, il gruppo fonti di calcolo della disponibilità libera
.              non utilizzerà il gruppo plant in esso definito, ma quello ricevuto.
.              Questa impostazione è utile in caso di applicazioni multiplant, in
.              cui si passa il plant di calcolo, senza dover codificare gruppi fonte
.              diversi per i vari plant.
-    Pos.8/10  Se impostato, è il tipo distinta (Tabella BRL) che viene usato per il reperimento del
.              lead time cumulato. Se non impostato, viene assunto 'ART'.
.              Questo campo viene preso in considerazione se è stato scelto (in posizione 1) di
.              escludere gli impegni oltre il lead time cumulato.

