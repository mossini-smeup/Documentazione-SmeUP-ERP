## Impengo in corso
>Se l'origine è IM (impegno in corso)
Parametro 1 : 
-    Pos.1/3   Tipo impegno (opzionale);
-    Pos.4/5   Tipo origine (opzionale);
-    Pos.6/6   Tipo quantità (significativo se impegno esterno) : 
.              ' '  :  quantità totale dell'impegno;
.              'I'  :  quantità interna :  è la quantità ancora da spedire;
.              'E'  :  quantità esterna :  è la quantità già spedita e non ancora
.              consumata.
.              Queste due ultime opzioni sono attive solo se è stata eseguita la
.              spedizione per ordine.
-    Pos.7/7   Data impegno. Se impostato, per gli impegni di produzione (origine
.              'PP') si assume come data l'inizio dell'operazione in cui viene
.              impiegato. Va ricordato che l'operazione è sempre presente nella riga
.              di impegno materiale (la si deriva dall'informazione presente nel
.              legame di distinta base; se assente si imposta la prima operazione
.              in assoluto).
.              La data viene assunta dal record dello scenario base '**' se esso è
.              presente e se la data non è a zero. In caso contrario si mantiene la
.              data di impegno. Si può impostare uno dei seguenti valori : 
.              _7_'1' - data inizio schedulazione a capacità finita.
.              _7_'2' - data inizio schedulazione a capacità infinita al più
.                 presto.
.              _7_'3' - data inizio schedulazione a capacità infinita al più
.                 tardi.
.              _7_'4' - come 1, se assente si assume 3.
.              _7_'5' - come 1, se assente si assume 4.
.              Con queste ultime impostazioni è possibile una datazione migliore : 
.              se all'inserimento dell'ordine si imposta di eseguire una
.              schedulazione a capacità infinita, se ne assume la data fino alla
.              prima schedulazione a capacità finita a cui si sottopone l'ordine.
Parametro 2 : 
-    Pos.1/1   Se impostato tratta solo righe compatibili con l'azione (se non
.              impostato i recuperi sono considerati come impegni negativi, se
.              impostato non vengono considerati se l'azione è '-', ma si possono
.              trattare come una fonte specifica di disponibilità, con azione '+').

