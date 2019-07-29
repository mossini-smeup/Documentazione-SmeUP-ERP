## Classificazione impegni e coperture

La classe di copertura stabilsce la criticità di un impegno e di una copertura.
La criticità di un impegno dipende dalle coperture che lo soddisfano.
La criticità di una copertura è di due tipi : 
- criticità intrinseca, dipendente dalla natura della copertura stessa (fonte presente, futura, ecc..)
- criticità derivata :  se la copertura è un ordine di produzione, di lavorazione o di trasferimento, dipende dalla classe di copertura degli imepgni che la soddisfano.

Dato che il calcolo è effettuato durante l'MRP, è necessario attivarlo (per evitare appesantimenti inutili se non si è interessati) impostando il campo opportuno dello scenario in tabella M5B : 
 :  : DEC T(VO) P(T.M5B) K(T$M5BS)

La classe di copertura è un valore V2M5_CM, secondo un criterio crescente di criticità
1 - Fonti presenti
2 - Fonti future rilasciate senza anticipo
3 - Fonti future rilasciate con anticipo
4 - Fonti future pianificate non scadute
5 - Fonti future pianificate scadute

## Classe di copertura "intrinseca" delle coperture.
E' memorizzata nel flag 10 dei consigli di pianificazione.
E' determinata considerando la natura della copertura.

## Classe di copertura degli impegni
E' memorizzata nel flag 10 dei consigli di pianificazione.
Essa si determina con la classe di copertura più alta tra quelle delle coperture (al suo livello) che lo soddisfano, scandite con la routine di analisi coperture : 
 :  : DEC T(MB) P(QILEGEN) K(£M5G).

## Classe di copertura "derivata" delle coperture (se ordini di produzione, di lavorazione o di trasferimento).
Viene ritornata nell'OAV J/I03 del consiglio, in quanto viene calcolata dinamicamente all'atto della richiesta, per non appesantire la durata dell'MRP.
Anch'essa ha come prerequisito l'impostazione dello stesso campo di M5B.
Si determina leggendo gli impegni (al livello inferiore che lo soddisfano) e prendendo la classe di copertura più alta tra di essi.
Impostando il seguente suffisso sulla tabella M5B
 :  : DEC T(VO) P(T.M5B) K(T$M5BT)
si può attivare un filtro che esclude eventuali impegni per la determinazione della classe di copertura degli ordini. Ciò può essere utile per escludere, ad esempio, alcuni articoli dal calcolo, non ritenendoli significativi.

## Considerazioni ulteriori
La classe di copertura "derivata" opera ad un livello :  non scende fino alle foglie :   ciò si può tradurre, ad esempio, nel fatto che una fonte futura pianificata non scaduta, scendendo nei livelli, sia soddisfatta da fonti future pianificate scadute.
Per ottenere questa informazione è necessaria un'esplosione ai materiali di base del consiglio di pianificazione in esame, da eseguire con la routine di navigazione : 
 :  : DEC T(MB) P(QILEGEN) K(£M5N).


