# £G80 FUNZIONI SU IFS
# OBIETTIVO
 Gestire i file e le cartelle dell'IFS dell'AS400 da un programma RPG

## SIGNIFICATO DEI CAMPI DI INPUT
### FUNZIONE E METODO
1. La funzione WRITE richiede che dopo la scrittura dell'ultimo record venga effettuata una chiamata alla £G80 con funzione CLOSE.
2. Prima della DELETE eseguire la G80 con funzione e metodo *BLANKS per farsi restituire il tipo oggetto da cancellare (da mettere nel metodo della DELETE)
*blanks  :  controlla l'esistenza di un oggetto dell'ifs.
.**WRITE** :  crea o scrive un oggetto dell'ifs.
..**'*STMF'** :  scrive il contenuto di £G80ST nel file specificato in £G80PH. Se il file non esiste lo crea, altrimenti accoda il contenuto a quello esistente.
..**'*DIR'** :  crea la cartella specificata in £G80PH.
..**'*PAT'** :  crea l'intero percorso specificato in £G80PH.

.**READ** :  legge il contenuto di un oggetto dell'ifs.
..**'*STMF'** :  legge il contenuto del file specificato in £G80PH, un record alla volta
..**'*DIR'** :  legge il contenuto della cartella specificata £G80PH, un oggetto alla volta.

.**DELETE** :  cancella un oggetto dell'ifs. Prima della DELETE eseguire la G80 con funzione e metodo blanks per farsi restituire il tipo (*STMF o *DOC o *DIR) dell'oggetto da cancellare. Questo tipo oggetto andrà messo poi nel metodo della funzione DELETE.
..**'*STMF'** :  cancella il file specificato in £G80PH (questo file deve essere di tipo *STMF)
..**'*DOC'** :  cancella il file specificato in £G80PH (questo file deve essere di tipo *DOC)
..**'*DIR'** :  cancella la cartella specificata £G80PH, solo se è vuota.

.**CLOSE**   :  chiude (termina l'elaborazione) di un oggetto dell'ifs.
..**'*STMF'** :  va specificato dopo la scrittura dell'ultimo record scritto (funzione WRITE/*STMF), oppure dopo l'ultimo record letto, nel caso si voglia ripetere il ciclo di lettura.
..**'*DIR'** :  va specificato dopo la lettura dell'ultimo record letto (funzione READ/*DIR), nel caso si voglia ripetere il ciclo di lettura.

.**SETAUT**   :  Imposta le autorizzazioni per l'oggetto
Eredita le autorizzazioni della cartella superiore impostando le autorizzazioni di controllo completo per l'utente di creazione (il proprietario) dell'oggetto

**£G80PH**= Path
 - è il path completo dell'oggetto ifs da gestire. Il primo byte deve essere il carattere '/'.
   Esempio di oggetto *STMF :  /tmp/prova.txt
   Esempio di oggetto *DIR  :  /tmp/

**£G80CP**= Code page di creazione
 - è la code page dell'oggetto *STMF da creare.
 Se il campo è lasciato *blanks, assume il valore impostato nel campo T$V§NN (Code page client  windows) della tabella V§N, per l'elemento corrispondente alla nazione impostata nel campo ££B£2H  (Nazione assunta) nella tabella B£2.
 Questo valore è usato SOLO in creazione dello streamfile. In lettura e in scrittura questo
 parametro viene ignorato.

**£G80CC**= Code page dati
 - è la code page dei dati presenti in £G80ST.
 Quindi è la codepage dei dati che mi vengono restituiti in lettura o la codepage dei dati che
 voglio scrivere se sono in scrittura.
 Questa codepage è indipendente dalla codepage effettiva dello streamfile.
 Se lo streamfile ha una codepage diversa da quella indicata per i dati, il sistema effettua
 la conversione in modo automatico.

 Se il campo è lasciato *blanks viene utilizzato il ccsid del JOB.

**£G80ST**= Stringa
 - è la stringa (record) da scrivere con la funzione WRITE/*STMF

**£G80RL**= Lunghezza record
 - fissa la lunghezza di in record con la funzione WRITE/*STMF. Se questa non viene indicata viene assunta la lunghezza della stringa trimmata a destra passata con la WRITE

**£G80EO**= Caratteri fine record
 - fissa i caratteri che vengono aggiunti alla fine record con la funzione WRITE/*STMF. Se il parametro non viene passato vengono assunti i caratteri ASCII CR/LF (cioè i valori esadecimaili 0D/0A) che indificano l'"a capo". Se invece voglio che non venga aggiunto alcun carattere va passata  come costante '*NONE'.

**£G80UN**= Unicode
 - indica che si vuole creare un file con encoding UTF-8, con o senza Byte Order Mark (BOM).
Tale parametro viene **pulito dopo l'esecuzione** dell'api e considerato solo in creazione di un nuovo file (quindi sulla prima esecuzione della funzione WRITE con metodo *STMF).
Se il file è in UTF-8 il parametro £G80CP è ignorato.

E' stata inoltre aggiornata la funzione blank (Controllo esistenza) per restituire i due nuovi parametri di output £G80CS (CCSID) e £G80BM (BOM).
**Il CCSID corrispondente all'encoding UTF-8 è il 1208.**

La £G80 è in grado di riconoscere automaticamente se un file è in UTF-8 basandosi sul CCSID del file e/o dalla presenza del BOM. Copiando file su IFS tramite Gestione Risorse o FTP il CCSID non viene impostato correttamente. Per questo si consiglia quando possibile di utilizzare file in UTF-8 con BOM, in quanto il Byte Order Mark è scritto nei primi 3 byte del file ed è sempre identificabile in modo certo.

### AUTORIZZAZIONI IN CREAZIONE DI FILE E CARTELLE
In creazione di un file o una cartella vengono ereditate le autorizzazioni della cartella superiore, impostando le autorizzazioni di controllo completo per l'utente di creazione (il proprietario) del nuovo oggetto.

## SIGNIFICATO DEI CAMPI DI OUTPUT

**£G80CO**= contenuto
  - è il contenuto dell'oggetto specificato con la funzione READ.
    .se il metodo è *STMF contiene il record del file
    .se il metodo è *DIR  contiene il nome dell'oggetto contenuto nella cartella

**£G80OG**= oggetto
  - è il path completo dell'oggetto letto con la funzione READ o *blanks

**£G80TO**= tipo oggetto
 - è il tipo oggetto dell'oggetto letto con la funzione READ o *blanks

**£G80D1/£G80H1**= Data e ora della modifica dello stato dell'oggetto
**£G80D2/£G80H2**= Data e ora della modifica del contenuto dell'oggetto
**£G80D3/£G80H3**= Data e ora dell'ultimo accesso all'oggetto

**£G80CS**=CCSID
**£G80BM**=Presenza Byte Order Mark (BOM)

**£G8035/*IN35**= indicatore di errore
 - impostato a '1' nei seguenti casi : 
   .oggetto non trovato (funzione *blanks)
   .fine file/file cartella (funzione READ)
   .errore generico (tutte le funzioni)
