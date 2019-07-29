## Ordine pianificato
>Se l'origine è PN (ordine pianificato)
Parametro 1 : 
-    Pos.1/10  Scenario dei consigli (opzionale) :  se non impostato viene assunto lo
.              scenario ricevuto. Se anch'esso è bianco viene assunto '**'.
Parametro 2 : 
-    Pos.1     Deviazione oggetto di rottura. Se impostato, l'oggetto di rottura
.              sostituisce l'oggetto dello stesso tipo sia nella parzializzazione
.              sia nel ritorno dei dati della fonte. Se, ad esempio, è stato
.              impostato questo flag e l'ente è stato scelto come oggetto di rottura
.              della pianificazione, viene considerato come ente intestatario
.              dell'ordine l'oggetto di rottura e non quello presente nel campo ente
.              dell'archivio dei consigli. Questa modalità è utilizzata nella
.              pianificazione 'logistica' in cui, nell'ordine pianificato sono
.              contenuti due enti :  l'esecutore dell'ordine e il destinatario dello
.              stesso. A seconda della situazione, si deve considerare il primo
.              oppure il secondo.
-    Pos.2/4   Fonte origine :  se non impostata vengono inclusi solo gli ordini
.              pianificati la cui fonte (presente nell'archivio) è uguale a quella
.              che si sta scandendo. Se impostata la fonte origine, vengono inclusi
.              solo gli ordini pianificati la cui fonte è uguale ad essa.
-    Pos.5     Data ritornata come disponibilità
.              -- ' ' data fonte.
.              -- '1' data suggerimento (è la data a cui si deve emettere l'ordine.
.              -- '2' data fine pianificata.
-    Pos.6     Se impostato, verranno ritornati solo gli ordini pianificati a
.              disponibilità chiamata.

