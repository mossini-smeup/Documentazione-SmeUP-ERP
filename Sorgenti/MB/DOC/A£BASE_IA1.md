Sme.UP è sostanzialmente IASP-izzabile. Bisogna però prestare alcune attenzioni.

La SMESYS non è IASP-izzabile (perché è in QSYSLIBL). Quindi deve stare in SYSBAS.
Quindi dentro questa libreria non ci devono essere riferimenti ad oggetti in IASP (altrimenti il sistema non è in grado di partire senza IASP in linea).
Il QSTRUP nella SMESYS va quindi scritto con attenzione (non posso ad esempio fare il CLRLIB di SMEUPUIDQ se quella libreria è in IASP).

Tutte le altre librerie sono IASP-izzabili.

Per replicare su sistema target la SMESYS ci sono varie tecniche : 
* fare un SAVF della libreria (ad esempio una volta al giorno) e : 
** metterlo in una libreria presente su IASP (così automaticamente viene replicato)
** spedirlo via FTP
* usare un software dedicato

Bisogna inoltre fare attenzione a eventuali connessioni DDM e ODBC (JDBC), potrebbe essere necessario modificare le stringhe di connessione per adattarsi al nuovo DatabaseName e anche per non avere problemi nel momento in cui viene fatto lo switch (take over) tra SYS1 e SYS2.

## Versioni di Sme.UP compatibili
Per avere un'installazione di sme.UP pienamente compatibile con lo IASP, è necessario avere una versione V4R1 almeno del 01/12/2014.

## Nota su IFS
Attualmente molti dei programmi e delle schede di sme.UP puntano (in modo non modificabile) a cartelle nella root dell'IFS (Smeext, Smedoc, ecc.). Le cartelle presenti nello IASP non figurano direttamente sotto la root, ma sotto la "cartella" con il nome dello IASP.
La tecnica che utilizziamo per risolvere questo problema è quella di mettere nella root dei link simbolici che puntano alla cartelle corrette nello IASP.
Ovviamente questa soluzione è percorribile solo in caso sia presente un solo IASP.

## Nota sulle stampanti
Ci sono problemi con gli overlay di Sme.UP. Le stampanti vegono avviate automaticamente all'IPL da un job che non ha lo IASP in linea. Questo crea problemi nel caso si cerchi di stampare con un overlay presente in DEVo o OBJ (che invece sono in IASP).
La soluzione attuale (peraltro consigliata da IBM) è quella di riavviare le stampanti da un job che ha in linea lo IASP.
