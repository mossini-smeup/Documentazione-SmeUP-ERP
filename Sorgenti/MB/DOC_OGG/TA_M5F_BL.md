## Fonte bilanciata
>Se l'origine è BL (bilanciamento)
Parametro 1 : 
-    Pos.1/10  Gruppo fonti per calcolare la disponibilità alla data (obbligatorio).
.              Esso deve contenere almeno una fonte MPS negativa, che costituirà la
.              fonte guida (riferirsi al paragrafo in cui si descrive l'origine 'MP'
.              per il modo di definire una fonte guida in modo esplicito, e come
.              vengono risolte eventuali ambiguità nella scelta della fonte guida).
.              Le rimanenti fonti future negative costituiscono un vettore di altre
.              fonti, raggruppate secondo la periodicità derivata dal piano della
.              fonte guida.
.              Viene eseguito un confronto, per ogni data, tra gli elementi di
.              questi due vettori (fonte guida e altre fonti), in base al criterio
.              definito del tipo bilanciamento :  il risultato sarà un elemento della
.              fonte alla data.
.              Viene ritornata la data di inizio o di fine periodo a seconda di
.              quanto impostato nella fonte guida.
.              *** Attenzione
.              Particolare cura deve essere prestata quando si utilizza una fonte
.              bilanciata, non a livello di prodotto finito, all'interno dell'MRP.
.              In questo caso possono essere presenti impegni pianificati (a fronte
.              di un ordine pianificato a livello superiore) che, in funzione del
.              tipo di bilanciamento scelto potrebbero essere considerati 2 volte.
.              In questi casi bisogna impostare che essi vengano chiusi dalla
.              politica (flag "Elimina impegni pianificati in Tab. M5A), per non
.              essere compresi nella scansione di disponibilità della pianificazione
.              Devono essere invece considerati nel gruppo fonti di questa metafonte
.              Per far ciò si deve codificare una seconda fonte futura, di impegno
.              pianificato, che ha l'impegno come fonte origine, nella quale si
.              imposta che il livello trattato sia '8'.
.              ***
Parametro 2 : 
-    Pos.1     Tipo bilanciamento (obbligatorio)
-    Pos.2     Primo periodo :  se impostato, trascura la fonte guida fino al periodo
.              in cui è presente un'altra fonte.
.                 Esempio (con bilanciamento per maggiore, e con partenza dal primo
.                 periodo presente).
.                 Fonte guida    Altre fonti    Fonte bilanciata
.                          12            20                  20
.                          10             0                  10
-    Pos.3     Modo di trattamento delle altre fonti scadute
.              ' '  Trascurate
.              '1'  Portate al primo periodo
-    Pos.4     Modo di trattamento delle altre fonti oltre periodo
.              ' '  Trascurate
.              '1'  Portate all'ultimo periodo
-    Pos.5     Suddivisione per oggetto di rottura
.              Se impostato, se la pianificazione è impostata per codice di rottura
.              e l'articolo è pianificato a rottura, viene eseguito un bilanciamento
.              separato per ogni oggetto di rottura (che viene ritornato dalla
.              disponibilità nel campo predisposto :  commessa, configurazione, ecc..)
-    Pos.6     Bilanciamento progressivo
.              Vale solo per il tipo bilanciamento '1' :  se impostato, il confronto
.              tra le fonti non viene fatto per ogni periodo, ma progressivamente
.              dall'inizio.
-    Pos.7     Gruppo plant
.              E' significativo nel caso di applicazione multiplant.
.              Stabilisce il modo di impostare il gruppo plant per l'analisi
.              disponibilità "locale" con cui si determinano i valori di questa
.              fonte.
.              Può assumere i seguenti valori
.              ' ' - Viene assunto il plant in scansione nell'analisi disponibilità
.                    "originale". Ad esempio, se essa viene eseguita con i plant
.                    P1, P2 e P3, l'analisi disponibilità "locale" viene eseguita
.                    tre volte, rispettivamente con il plant P1, P2 e P3.
.              '1' - Viene assunto il gruppo plant contenuto nel gruppo fonti
.                    impostato in questa tabella
.              '2' - Viene assunto il gruppo plant dell'analisi disponibilità
.                    "originale".
.                    In questo modo si evita di dover codificare diverse fonti per
.                    diversi gruppi plant.
.              NOTA TECNICA
.              Nei casi '1' e '2' l'analisi disponibilità "locale" viene eseguita una
.              sola volta, ed i suoi valori vengono assegnati al primo plant del
.              gruppo fonti.

