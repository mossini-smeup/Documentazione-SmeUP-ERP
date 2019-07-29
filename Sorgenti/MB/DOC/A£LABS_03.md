## Obiettivo
Controllare che i campi dei formati video siano ordinati. Ciò serve ad evitare che su LOOC.up il movimento del cursore salti in modo diverso dall'atteso (che normalmente è il campo successivo).
La verifica è vivamente consigliata prima di ogni rilascio.

## Impostazione
Richiamando il programma B£UT11 (compilazione di massa) e scegliendo l'opzione 4 si ottengono i servizi relativi al riordinamento dei formati.

Normalmente se si indica un file di una libreria vengono creati i membri riordinati in un file di una libreria definiti dall'utente.

Quando si sceglie *ALL (Tutti i files) si ottengono le strutture di controllo.
Per ogni membro vengono evidenziati : 
- Libreria
- File
- Membro
- Numero di campi in disordine
- Suggerimento di correggere (se > 3 o non in SMESRC)
I dati vengono salvati in due luoghi (se e solo se questi esistono)
1. Documentazione del programma B£UT35A (Quindi in DOC_OGG il membro P_B£UT35A)
2. Nella tabella XVD (da creare appositamente) e che dovrà contenere i seguenti campi
   - T$XVDA  Libreria
   - T$XVDB  File
   - T$XVDC  Numero campi errati   NR         In SMESRC
   - T$XVDD  Numero campi errati   NR         In altri files
   - T$XVDE  Correggere?           V2 SI/NO   Se > 3 o non in SMESRC
   - T$XVDF  Estratto?             V2 SI/NO   Se esiste il membro nella libreria W_SL/libreria

## Come procedere

1. Consultare la tabella costruita (ad esempio in XVD)
2. Richiamare il membro con l'SDA ed eseguire il riordinamento (12 sul formato F4 F6)
3. Segnalare la PTF sul programma e ricompilare






