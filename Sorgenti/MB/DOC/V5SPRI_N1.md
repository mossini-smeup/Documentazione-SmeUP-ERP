# Struttura richiamo PGM in V5AT15L
Nel PGM V5AT15L (passaggio documenti) si imposta il programma di aggiustamento : 
 - **V5AT15_xy**, dove "**x**" è la forma (1/9),  "**y**" è il suffisso impostato nel metodo di passo del flusso. Questo PGM, lanciato in più punti, con funzioni particolari permette di arricchire le funzionalità del passaggio documenti
 - **V5AT16_xy**
La prima volta che si lancia il PGM 1) esso verifica la presenza del 2), se presente lo lancia tutte le volte che è chiamato, prima di eseguire alcunchè, trasferendo tutti i dati ricevuti in input. Nel programma 2) impostando il campo £V5TOK (che riceve blank) fa si che il PGM 1) vada a fine esecuzione (per lo specifico richiamo). Si può quindi decidere che le funzioni più generali si eseguono in 1), mentre opzioni utente particolari invece si eseguono in 2).

## Nomenclatura
Il suffisso è : 
 * **numerico**, per programmi personali
 * **alfabetico**, per programmi aggiuntivi forniti da Sme.UP (in questi ultimi per personalizzazioni utente si abilita il V5AT16_xy)

## Nomenclatura opzioni
 * **alfabetiche**, interne a V5AT15L o al singolo suffisso standard (non devono sovrapporsi alle precedenti, tra di loro possono sovrapporsi in quanto non sono mai presenti insieme)
 * **N. righe**, interne al singolo suffisso personalizzato (15 + numero, oppure 16)
Le opzioni sono così definite in V5*/OE si codifica l'elemento XY dove x è il suffisso del programma e y è l'opzione.
**Nota Bene**, nella descrizione si mette in prima posizione l'opzione e dalla posizione 11 in poi la decodifica, il campo prosegue nei parametri, in posizione 11 si imposta il condizionamento riga ("blank" sulle righe compatibili, "T" su tutte, "N" non compatibili, "F" non compatibili con ammessa forzatura)
