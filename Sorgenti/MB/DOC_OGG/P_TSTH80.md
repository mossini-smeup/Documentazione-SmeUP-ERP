# £H80 Gestione file di rete
# OBIETTIVO
Gestire (in lettura e scrittura) file e cartelle di rete da un programma RPG

Il percorso del file o della cartella di rete è relativo allo Sme.UP Provider a cui vengono inoltrate le operazioni da eseguire :  si tratta quindi di condivisioni di rete oppure di percorsi locali relativi alla macchina su cui è installato Sme.UP Provider.
Gli encoding attualmente supportati per i file di testo sono : 
 * Windows (CP1252)
 * Ascii (CP850)
 * ISO-8859-1 (Latin 1)
 * UTF-8

**PREREQUISITO : ** installazione di uno Sme.UP Provider V4R1M151024 "Sydney Harbour Bridge" Stable con upgrade del 25/07/2016 o successivo.
Per l'installazione e la configurazione del provider si rimanda alla documentazione del modulo
LOCSPR.
Si fa riferimento in questa sede ad una configurazione importante di Sme.UP Provider :  l'elenco
delle cartelle a cui è abilitato, definite dalla variabile PROVIDER_PATHS. La H80 potrà scrivere
e leggere solo in queste cartelle, e solo se le stesse sono abilitate all'UTENTE WINDOWS con cui
Sme.UP Provider è in esecuzione.

**N.B.**In lettura, file di testo con dimensione maggiore di 20/30 MB possono causare l'esaurimento della memoria disponibile della Java Virtual Machine di Sme.UP Provider e quindi originare un timeout.

**Esempio di utilizzo :  generare un file pdf con G53 e spostarlo su una cartella di rete**
In questo caso i passaggi saranno : 
CONFIGURAZIONE INIZIALE
 1- Configurare l'IFS in modo che sia visibile come condivisione Windows a Sme.UP Provider
 2- Abilitare l'utente windows all'accesso all'ifs senza autenticazione interattiva
RUNTIME
 1- Generare il file in un percorso IFS temporaneo
 2- Lanciare la funzione di copia della H80 dal percorso IFS, in notazione \\sistema\cartella\file
 3- Eliminare, se opportuno, il file temporaneo

## SIGNIFICATO DEI CAMPI DI INPUT
**N.B. :  I campi di input vengono puliti automaticamente dopo ogni esecuzione.**
### FUNZIONE E METODO
Funzioni e metodi ricalcano quelli della £G80 per la gestione dell'IFS.

. ***BLANKS**   Controllo esistenza
.. ***BLANKS**   Qualsiasi oggetto
. **READ**      Lettura
.. **FILE**      Contenuto File
.. **DIR**       Contenuto Directory
. **WRITE**     Scrittura
.. **FILE**      File (in append) - se non esiste crea il file
.. **DIR**       Directory
. **COPY**      Copia (con sovrascrittura)
.. **FILE**      File
.. **DIR**       Directory
. **DELETE**    Eliminazione
.. **FILE**      File
.. **DIR**       Directory (solo vuota)
. **EMPTYD**    Elimina contenuto directory
.. **ALL**       Tutto
. **CLOSE**     Chiusura

**N.B. :  La funzione COPY esegue la sovrascrittura del file se già presente. In caso di copia** **di una cartella, sovrascrive la cartella e i file eventualmente già presenti in essa **contenuti.**
**Qualora vi siano nella cartella di destinazione file non presenti nella cartella di origine** **essi NON vengono cancellati.**

**£H80I_PH**= Path
 - è il path completo del file o della cartella di rete. Il percorso è relativo allo Sme.UP provider a cui vengono inoltrate le operazioni da eseguire :  si tratta quindi di condivisioni di rete oppure di percorsi locali relativi alla macchina su cui è installato Sme.UP Provider.

**£H80I_PD**= Path destinazione
 - è il path completo del file o della cartella di destinazione della funzione di copia. Il percorso è relativo allo Sme.UP provider a cui vengono inoltrate le operazioni da eseguire :  si tratta quindi di condivisioni di rete oppure di percorsi locali relativi alla macchina su cui è installato Sme.UP Provider.

**£H80I_DQ**= Sme.UP Provider
 - è lo Sme.UP Provider a cui viene chiesto di eseguire l'operazione su file o cartelle. (oggetto V3LSE)

**£H80I_ST**= Stringa
 - è la stringa (record) da scrivere con la funzione WRITE/FILE

**£H80I_EN**= Encoding
 - è l'encoding del file in lettura e scrittura.
   In scrittura se non specificato assume UTF-8 con BOM (Byte Order Mark).
   In lettura se non specificato assume cp1252 a meno che il file non cominci con il BOM (nel cui    caso riconosce UTF-8)
   Gli encoding attualmente supportati per i file di testo sono : 
   * Windows (cp1252)
   * Ascii (Cp850)
   * ISO-8859-1 (Latin 1)
   * UTF-8

**£H80I_RL**= Lunghezza record
 - fissa la lunghezza di un record con la funzione WRITE/FILE. Se questa non viene indicata viene assunta la lunghezza della stringa trimmata a destra passata con la WRITE

**£H80I_EO**= Caratteri fine record
 - fissa i caratteri che vengono aggiunti alla fine record con la funzione WRITE/FILE. Se il parametro non viene passato vengono assunti i caratteri CR/LF che identificano l'"a capo".
Se invece voglio che non venga aggiunto alcun carattere va passata come costante '*NONE'.

**£H80I_AT**= Timeout Attesa
 - attesa in secondi della risposta di Sme.UP Provider prima di andare in timeout. Se 0 assume 60 secondi.

## SIGNIFICATO DEI CAMPI DI OUTPUT

**£H80O_CO**= contenuto
  - è il contenuto dell'oggetto specificato con la funzione READ.
    .se il metodo è FILE contiene il record del file
    .se il metodo è DIR  contiene il nome dell'oggetto contenuto nella cartella

**£H80O_OG**= oggetto
  - è il path completo dell'oggetto letto con la funzione READ o *blanks

**£H80O_TO**= tipo oggetto
 - è il tipo oggetto dell'oggetto letto con la funzione READ o *blanks (J1PATHFILE o J1PATHDIR)

**£H80O_D2/£H80O_H2**= Data e ora della modifica del contenuto dell'oggetto

**£H80O_SZ**= size
 - dimensione in byte dell'oggetto restituita dalla funzione *blanks

**£H80O_SD**= Presenza Sottocartelle
 - Se presenti sottocartelle restituisce 1 (funzione READ/DIR)

**£H80O_35= indicatore di errore
 - impostato a '1' nei seguenti casi : 
   .oggetto non trovato (funzione *blanks)
   .fine file/file cartella (funzione READ)
   .errore generico (tutte le funzioni)
