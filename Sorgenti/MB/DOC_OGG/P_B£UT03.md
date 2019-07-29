# Caricamento risorse esterne da SAVF
Mediante questa utility è possibile estrarre alcune risorse esterne da SAVF distribuiti con Sme.UP.

Queste risorse comprendono : 
- File con settori ed elementi di tabella
- Smens / Smedg
- Smepd
- Moduli
- Configurazioni esterne

Innanzitutto è necessario inserire la libreria in cui sono presenti i SAVF da cui estrarre le varie risorse (Libreria di partenza).

Successivamente va indicata quale risorsa si vuole restorare.

Per alcune risorse è necessario indicare il percorso in cui estrarre tali componenti.
Di default vengono presentati i percorsi standard che possono ovviamente essere modificati.
In caso il percorso indicato non abbia una struttura standard, verrà richiesta la conferma per
l'esecuzione.

In caso venga indicata una cartelle esistente, verrà impedita l'operazione di restore.
Questo per evitare possibili sovrascritture e perdite di dati.
Se la cartella esiste già, si consiglia di seguire i seguenti passi : 
* effettuare il restore in una cartella nuova
* salvare le informazioni personali presenti nelle cartelle "vecchie" (ad esmepio eventuali font   personalizzati)
* cancellare le corrispondenti cartelle originali (dopo averne fatta una copia di backup)
* copiare le cartelle nella posizione deisderata
* riportare nelle nuove cartelle le informazioni personali precedentemente salvate

## IASP libreria di destinazione
In questo campo va indicato l'eventuale IASP in cui è presente la libreria o le cartelle IFS di
destinazione. I valori accettati sono i seguenti : 

* Blank / *DFT verrà usato il default di sistema
* Nome dello IASP

## File con settori ed elementi di tabella
E' possibile restorare i file necessari per effettuare un allineamento dei file tabelle (settori ed elementi) già installati sul sistema.
Innanzitutto va indicata la libreria che conterrà i file restorati (Libreria destinaz.).
Successivamente vanno indicati queli file restorare : 
TABDS00F/TABDC00F e/o TABEL00F e/o TABELV0F e/o TABELA0F
Per quanto riguarda TABDS, TABDC, TABELV e TABELA è sufficiente mettere una X nel campo relativo e verranno restorati i file precedentemente salvati dal modello.
Per quanto riguarda il file TABEL00F è invece possibile effettuare una doppia scelta : 
* 1 per restorare il file salvato dal modello
* 2 per restorare il file salvato dall'ambiente di sviluppo
Il file salvato dall'ambiente di sviluppo contiene molti più elementi di quello del modello, però la bontà di tali elementi non è garantita.

## Smens / Smedg
E' possibile restorare tutti i file e le cartelle necessarie al corretto funzionamento dei componenti esterni Smens e Smedg. Ricordiamo che tali componenti sono quelli utilizzati dalla £G53 per creazione PDF, invio mail ecc.
E' necessario indicare nell'apposito campo quali componenti si vogliono ripristinare : 
* 1         Tutto (SMENS+SMEDG)
* 2         Solo SMENS
* 3         Solo SMEDG
Dato che tali componenti vanno installati sull'IFS, è obbligatorio specificare la cartella in cui andranno copiati.
Tale cartella deve avere una struttura particolare, quindi in caso venga indicato un percorso non standard, si verrà avvisati dei possibili malfunzionamenti.
Per ulteriori dettagli in merito consultare l'apposita documentazione : 
 :  : DEC

## SmePD
E' possibile restorare (sempre in una cartella dell'IFS) i file necessari all'installazione del componente SmePD.
Tale componente è necessario per la stampa di PDF direttamente su OUTQ.
Attualmente viene restorato un unico file contenente le istruzioni di installazione.

## Moduli
E' possibile restorare (sempre in una cartella dell'IFS) i file necessari per la stampa dei moduli standard in pdf (es. Moduli per la certificazione unica).
Viene restorata una cartella contenente tutti i pdf dei moduli standard attualmente gestiti.

## Configurazioni Esterne
E' possibile restorare (sempre in una cartella dell'IFS) i file necessari per i file di configurazioni esterne (utilizzabili ad esempio per l'invio delle notifiche su Device Mobile).
Viene restorata una cartella contenente i file di configurazione attualmente gestiti.

## API Json
E' possibile restorare la libreria specifica per il parsing Json, copyright di Scott C. Klement. Per ulteriori dettagli vedere qui : 
- [Parsing Json](Sorgenti/MB/DOC/WSBASE_01)
