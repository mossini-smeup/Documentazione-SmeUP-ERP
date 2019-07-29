## Processo di esportazione e conversione

### Premessa
L'esportazione e conversione dei programmi RPG e CLP avviene in due momenti diversi.
La prima parte avviene su iSeries ed è la generazione di un file .xmi in cui si è
cercato di normalizzare il codice sorgente rendendolo neutro.
La seconda parte avviene su piattaforma As.Up dove viene generato un file .java ed un file .class.
Il processo di conversione prevede anche un'analisi dei sorgenti e la rilevazione di parti di codice non supportate.

### Descrizione conversione OS in XML
Il processo di esportazione ha origine con il comando "MU" (MUOS02C), eseguito su un oggetto presente in una libreria.
In base al tipo dell'oggetto del programma viene effettuato uno switch su un programma specifico.

 :  : DEC T(OJ)  P(*PGM) K(MUOS02)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_01)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_02)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_03)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_04)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_05)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_06)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_07)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_08)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_09)
 :  : DEC T(OJ)  P(*PGM) K(MUOS02_10)

Il risultato dell'esportazione, ovvero il file .xmi viene depositato in una cartella dell'IFS.
La cartella base è la "SmeMult", e nella tabella MU1 viene definito un path specifico di release.
Esiste un programma di utilità che restituisce il path iniziale : 
  :  : DEC T(OJ)  P(*PGM) K(MUUT01)
ES :  "/SmeMult/asup_x.x.x"

Tale cartella è organizzata in sottocartelle che prendono il nome della libreria dell'oggetto che si sta convertendo;
all'interno della cartella "libreria" sono presenti delle sottocartelle che prendono il nome dal tipo oggetto che si sta convertendo (PGM, USRPRF,DTAARA, etc),
ed in queste sottocartelle sono presenti infine i file .XMI convertiti.

### Descrizione parser RPG (MUPA03)
E' stato creato un programma __MUPA03__ che si occupa del parsing di un sorgente RPG.
Tale programma funziona similmente ad un parser SAX, ovvero attraverso una gestione ad eventi.
Sono stati creati una serie di tag che identificano diversi eventi.
Qualche esempio : 
* Datastructure;
* Annotazioni;
* File;
* If;
* etc;

Il programma MUPA03 è stato creato in maniera tale che possa rimanere neutro,
e preoccuparsi solamente di lanciare eventi mentre esegue la parserizzazione.
Sono stati creati dei "listener" al MUPA03 per la gestione degli eventi : 

 :  : DEC T(OJ)  P(*PGM) K(MUPA03_01)
 :  : DEC T(OJ)  P(*PGM) K(MUPA03_03)

__MUPA03_01__
Questo programma, di fatto, è quello che scrive il risutato della parserizzazione di un sorgente RPG.
Il risultato finale è un file .xmi che successivamente potrà essere importato in ambiente As.Up.
Questo programma, si preoccupa anche di verificare che le specifiche scritte in un programma siano supportate dal nuovo linguaggio.
I risultati di questa verifica sono scritti nel file MUCONV0F.

__MUPA03_03__
Questo programma è adibito al controllo dei "metadati" di un sorgente, vengono analizzate i codici operativi TAG e GOTO.

### Nuovi Comandi
**Comando MU**
E' stato creato un nuovo comando _b_MU (MUOS02C) che permette la conversione di un oggetto as400.
Il comando si applica agli oggetti presenti in una libreria ed alle librerie stesse.
Questo comando riceve : 
* una funzione ed un metodo (al momento è presente soltato la funzione "CON");
* il tipo oggetto;
* la libreria;
* il nome oggetto;
* il path IFS dove posizionare il file .XMI;
* la libreria destinazione (se diversa da quella originale);
* flag per conversione progressiva (un oggetto viene convertito solo se è stato modificato rispetto all'ultima conversione effetuata);

### Documentazione messaggi relativi alla conversione
**Validi per tutti i tipi oggetti**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00100   | Esportazione oggetto                                      | 30 |
| 


**Validi per OJ*CMD**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00332   | Errore reperimento informazioni comando                   | 30 |
| 


**Validi per OJ*MSGF**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00303   | Designazione file &1(&2) non supportata                   | 30 |
| 


**Validi per OJ*FILE**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00201   | Tipo campo &1 non supportato                   | 30 |
| MU00202   | Nome campo &1 non supportato                   | 30 |
| MU00203   | Nome file &1 non supportato                    | 30 |
| MU00204   | File logico &1, fisico in altra libreria       | 30 |
| MU00205   | Vista logica su campo materializzato           | 20 |
| MU00206   | Lunghezza campo &1 eccede il valore ammesso    | 20 |
| MU00309   | File &1 multimembro deprecato    | 30 |
| MU00330   | File logico multiformato non supportato    | 30 |
| 


**Validi per OJ*PGM e OJ*MODULE**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00319   | File sorgente &1 non trovato    | 30 |
| MU00321   | Errore nel parser MUPA03    | 30 |
| MU00322   | Tipo specifica non riconosciuta | 30 |
| 


**Relativi alle specifiche /precompilazione**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00329   | Specifica /FREE non supportata                            | 30 |
| MU00393   | Direttiva precompilazione da verificare :  &1               | 20 |
|  |
| 


**Relativi alle specifiche F**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00303   | Designazione file &1(&2) non supportata                   | 30 |
| MU00304   | Fine file &1 non supportata                               | 30 |
| MU00305   | Sequenza file &1 non supportata                           | 30 |
| MU00306   | Formato file &1 non supportato                            | 20 |
| MU00307   | Limite file &1 non supportato                             | 30 |
| MU00338   | File video definito internamente                          | 30 |
|  |
| 


**Relativi alle specifiche D**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00328   | Definizione variabile puntatore :  &1                       | 20 |
| MU00347   | DS con attributo non supportato                           | 20 |
| MU00348   | Lunghezza &1 per la DS di tipo &2 non supportata          | 30 |
| MU00392   | Puntatore in DS non supportato :  &1                        | 30 |
|  |
| 


**Relativi alle specifiche I**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00370   | Spec. I - Sequence "&1"                                   | 20 |
| MU00371   | Spec. I - Number "&1"                                     | 20 |
| MU00372   | Spec. I - Option "&1"                                     | 20 |
| MU00373   | Spec. I - Record identifying indicator "&1"               | 20 |
| MU00374   | Spec. I - Record identifying codes "&1"                   | 20 |
| MU00375   | Spec. J - Data Attributes "&1"                            | 20 |
| MU00376   | Spec. J - Datetime separator "&1"                         | 20 |
| MU00377   | Spec. J - Control level "&1"                              | 20 |
| MU00378   | Spec. J - Matching Fields "&1"                            | 20 |
| MU00379   | Spec. J - Field Record Relation "&1"                      | 20 |
| MU00380   | Spec. J - Field Indicators "&1"                           | 20 |
| MU00381   | Spec. I - And/Or non gestito                              | 20 |
| MU00382   | Spec. IX - Record identifying indicator "&1"              | 20 |
| MU00383   | Spec. JX - Control level "&1"                             | 20 |
| MU00384   | Spec. JX - Matching Fields "&1"                           | 20 |
| MU00385   | Spec. JX - Field Indicators "&1"                          | 20 |
| MU00386   | Spec. I - Utilizzo                                        | 20 |
| MU00387   | Spec. IX - Utilizzo                                       | 20 |
|  |
| 


**Relativi alle specifiche C**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00317   | Errore in compilazione modulo                             | 30 |
| MU00320   | Goto a Tag Main non ottimizzato                           | 30 |
| MU00323   | Codice operativo &1 non riconosciuto                      | 30 |
| MU00324   | Codice operativo &1 non supportato                        | 20 |
| MU00325   | Operazione su file non ottimizzata &1([&2][&3][&4])       | 30 |
| MU00327   | Operazione su puntatori non ottimizzata &1                | 20 |
| MU00336   | Fattore 2 per ENDDO non supportato                        | 20 |
| MU00337   | Chiusura annidamento IF/ELSEIF/ELSE anomalo               | 20 |
| MU00340   | Sostituzione carattere speciale EBCDIC                    | 30 |
| MU00349   | Codice operativo RETURN usato impropriamente              | 30 |
| MU00360   | Operator extender &1 da verificare                        | 20 |
| MU00394   | Verificare indicatori su codice operativo :  &1             | 20 |
| MU00395   | Operatore logico omesso per questo codice operativo (CAB/CAS)| 20 |
| MU00396   | Indicatore non ammesso su codice operativo :  &1([&2][&3][&4]) | 30 |
| MU00397   | Indicatore condizionale non ammesso su codice operativo :  &1  | 30 |
|  |
| 


**Relativi alle specifiche O**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00350   | Spec. O - Update                                          | 20 |
| MU00351   | Spec. O - Type "&1"                                       | 20 |
| MU00352   | Spec. O - Record ADD/DEL "&1"                             | 20 |
| MU00353   | Spec. O - Fetch Overflow/Release "&1"                     | 20 |
| MU00354   | Spec. O(P) - Edit Codes "&1"                              | 20 |
| MU00355   | Spec. O(P) - Blank after "&1"                             | 20 |
| MU00356   | Spec. O(P) - Data format "&1"                             | 20 |
|  |
| 


**Relativi alle specifiche P (procedure)**

|  Nam="Lista Messaggi" |
| 
| .COL Cod="A" Txt="Codice" Lun="10" A="L" |
| ---|----|
| 
| .COL Cod="B" Txt="Descrizione" Lun="50" A="L" |
| 
| .COL Cod="C" Txt="Gravità" Lun="5" A="L" |
| MU00362   | Procedura :  &1, Copy :  &2                                   | 20 |
| MU00363   | Procedura :  &1, Copy :  &2 non censita                       | 20 |
| MU00364   | Procedura :  &1, Copy :  &2 incompleta                        | 20 |
|  |
| 

