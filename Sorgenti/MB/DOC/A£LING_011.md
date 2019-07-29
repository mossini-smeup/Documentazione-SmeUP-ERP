# 1. Cosa fare per vedere tradotto un singolo oggetto

Per tradurre un qualsiasi oggetto in ambiente in lingua occorre effettuare 4 passaggi fondamentali : 
A) Estrazione
B) Preparazione
C) Traduzione
D) Creazione Oggetti

## Estrarre le frasi in Italiano

Per prima cosa bisogna estrarre le frasi in italiano che occorre tradurre, in modo tale che vadano a popolare il database A£TROR0F.
E' possibile effettuare questa operazione con il comando LI sul singolo programma.
Le opzioni a disposizione sono 2 :  EST (estrazione) e ESP (estrazione e preparazione)
Nel primo caso vengono estratte dal programma tutte le frasi in italiano sul file A£TROR0F.
Nel secondo caso, oltre alle funzioni dell'opzione EST, viene anche preparato il record sul file A£TRDE0F, a seconda delle impostazioni scelte.

## Preparare le frasi estratte

La preparazione delle frasi consiste nella creazione di record sull'A£TRDE0F in base a contesto, Ambito e lingua.
Per effettuare la preparazione si può usare il comando LI con funzione ESP, come spiegato precedentemente;
oppure lanciare l'apposita voce di menù "Preparazione frasi da tradurre", in cui occorre specificare il contesto, ambito e lingua da preparare.

## Tradurre le frasi

La traduzione delle frasi può avvenire a diversi livelli.
Se impostate correttamente le tabelle, la traduzione può avvenire già in fase di preparazione andando in risalita su frasi già tradotte, in base alle seguenti regole : 
1. Contesto simile, ambito più alto e lunghezza rispettata
2. Stessa applicazione, ambito più alto e lunghezza rispettata
3. Qualunque applicazione, ambito più alto e lunghezza rispettata

Altrimenti lo si può fare manualmente dopo l'estrazione.
Purtroppo non è possibile al momento selezionare un singolo oggetto, per cui è necessario specificare una lingua e un ambito (opzionale) e verranno completate tutte le traduzioni possibili.
Questa modalità è usufruibile usando la voce di menù "Completa trad da stessa lingua"

C'è anche la possibilità di completare una lingua partendo da un'altra, in questo caso è necessario specificare lingua di partenza e lingua di destinazione.
Questa modalità è usufruibile usando la voce di menù "Completa trad da altra lingua"

Infine è possibile completare le traduzioni delle singole frasi tramite la scheda "Traduzione" dal menù A£LING.
E' possibile raggiungere le frasi da tradurre di uno specifico oggetto partendo dalla navigazione dell'oggetto stesso.
Nel Fly c'è la voce "Supporto Multilingua" che permette di accedere alla scheda di traduzione con già preimpostato il contesto.


## Creare oggetti in lingua (solo per display file, message file e printer file)
Per Display file, Message File e Printer File è necessario ricreare gli oggetti direttamente in lingua, dopo aver completato i passi precedenti.
Per creare il singolo oggetto è possibile usare il comando LI con l'opzione GEN, specificando lingua e libreria (se necessario).
Nota :  per Looc.UP non è necessario generare i Display file in lingua, vengono tradotti run time.
      Resta comunque la necessità per Printer e Message file

# 2. Cosa fare per vedere tradotti oggetti in massa

Per tradurre una serie di oggetti in ambiente in lingua occorre effettuare 4 passaggi fondamentali : 
A) Estrazione
B) Preparazione
C) Traduzione
D) Creazione Oggetti

## Estrarre le frasi in Italiano

Per prima cosa bisogna estrarre le frasi in italiano che occorre tradurre in modo tale che vadano a popolare il database A£TROR0F.
Opportunamente preparate le exit e specificate nella tabelle A£1, è possibile estrarre tutte le frasi di una serie di oggetti tramite la voce di menù "Estrazione italiano"
In questa modalità è possibile estrarre tutte le frasi relative ai seguenti tipi oggetto : 
* TAB= tabelle (elementi, settori, campi)
* MSG= File di messaggi
* DB= File di database (tranne le tabelle), (es. campi, OAV, ...)
* SRC= File Video, file stampa, programmi (DSPF, PRTF, PGM)
* SCP= Script

relativi ad un file di una libreria.

Oppure tramite l'opzione exit è possibile definire una serie di tipi oggetto, file e librerie da estrarre consecutivamente.

## Preparare le frasi estratte

La preparazione delle frasi consiste nella creazione di record sull'A£TRDE0F in base a contesto, Ambito e lingua.
Per effettuare la preparazione occorre lanciare l'apposita voce di menù "Preparazione frasi da tradurre" specificando il contesto, ambito e lingua da preparare.

## Tradurre le frasi

La traduzione delle frasi può avvenire a diversi livelli.
Se impostate correttamente le tabelle, la traduzione può avvenire già in fase di preparazione andando in risalita su frasi già tradotte, in base alle seguenti regole : 
1. Contesto simile, ambito più alto e lunghezza rispettata
2. Stessa applicazione, ambito più alto e lunghezza rispettata
3. Qualunque applicazione, ambito più alto e lunghezza rispettata

Altrimenti lo si può fare manualmente dopo l'estrazione.
Questa modalità è usufruibile usando la voce di menù "Completa trad da stessa lingua"

C'è anche la possibilità di completare una lingua partendo da un'altra, in questo caso è necessario specificare lingua di partenza e lingua di destinazione.
Questa modalità è usufruibile usando la voce di menù "Completa trad da altra lingua"

Infine è possibile completare le traduzioni delle singole frasi tramite la scheda "Traduzione" dal menù A£LING.
E' possibile raggiungere le frasi da tradurre di uno specifico oggetto partendo dalla navigazione dell'oggetto stesso. Nel Fly c'è la voce "Supporto Multilingua" che permette di accedere alla scheda di traduzione con già preimpostato il contesto.


## Creare oggetti in lingua (solo per display file, message file e printer file)
Per Display file, Message File e Printer File e solo in emulazione 5250 è necessario ricreare gli oggetti direttamente in lingua, dopo aver completato i passi precedenti.
E' possibile generarli di massa attraverso la voce di menù "Generazione oggetti in Lingua".
In questa modalità è possibile estrarre tutte le frasi relative a Display File, Message File e Printer File, singolarmente, specificando file, libreria e lingua.
Oppure è possibile specificare nella exit A£TR01_xx una serie di tipi oggetto/file/librerie da cui generare gli oggetti.

