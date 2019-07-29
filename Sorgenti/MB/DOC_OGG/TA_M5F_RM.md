## Richiesta di movimentazione
>Se l'origine è RM (richiesta di movimentazione)
Parametro 1 : 
-    Pos.1/3   Tipo Riga movimentazione (opzionale).
-    Pos.4/5   Origine Riga (opzionale).
-    Pos.6/8   Tipo documento origine (opzionale) :  va impostato assieme all'origine
.              riga. Se quest'ultma identifica un documento V5 o un impegno esterno,
.              è possibile ottenere un'ulteriore parzializzazione.
-    Pos.9     Indica se considerare la quantità in unità di misura interna o
.              esterna.
-    Pos.10    Indica quale data della richiesta considerare come data fonte : 
.              -- 'R'  Data richiesta;
.              -- 'D'  Data disponibilità prevista;
.              -- ' '  Data a zero (fonte presente).
Parametro 2 : 
-    Pos.1/2   Area origine (opzionale);
-    Pos.3/4   Tipo giacenza origine (opzionale);
-    Pos.5/6   Area destinazione (opzionale);
-    Pos.7/8   Tipo giacenza destinazione (opzionale);
-    Pos.9     Definisce il modo di trattare le richieste secondo l'assegnazione : 
.              -- ' '  Tutte le richieste;
.              -- '1'  Solo richieste assegnate;
.              -- '2'  Richieste assegnate e da non assegnare;
-    Pos.10    Definisce se ritornare l'ente legato all'eventuale documento V5
.              presente nella riga della richiesta di movimentazione.
.              Il recupero di questo tipo di informazione comporta un rallentamento
.              dell'esecuzione del programma di analisi disponibilità. Questo
.              parametro NON deve essere utilizzato in caso di fonti deviate.
.              -- ' '  No  (non viene restituito nessun ente)
.              -- '1'  Ente Intestatario
.              -- '2'  Ente spedizione

