# Necessità soddisfatte
 - _2_Conoscere gli utenti connessi a WEBUP e LOOC.UP;  è possibile vedere gli utenti attivi
 - _2_Conoscere il numero di accessi effettuati;  Viene reso disponibile un elenco di tutte le connessioni effettuate per data e la loro durata
 - _2_Conoscere gli utilizzi delle specifiche funzioni;  ** In sviluppo ***  Viene tenuta traccia solo di alcune specifiche funzioni, quando sono state utilizzate e che oggetti coinvolgono
 - _2_Sintesi di tutte le informazioni;  Analizzare tutti i dati memorizzati in modo da conoscere gli utilizzi di funzioni, il numero di collegamenti  e la loro durata

# Flusso logico
## Prefazione
Ogni funzione eseguita in Web.up e alcune di Looc.up passa da  un programma di interfaccia chiamato JAJAC0.
 :  : DEC T(OJ) P(*PGM) K(JAJAC0)

Ogni volta che viene chiamato il programma JAJAC0, è possibile tenere traccia della comunicazione effettuata. Questo programma viene chiamato con diverse funzioni, ognuna delle quali può essere tracciata nel log.

Queste funzioni sono visibili dal TSTJAC
 :  : DEC T(OJ) P(*PGM) K(TSTJAC)

Le principali sono : 
 * DATSES= Collegamento sessione Looc.up
 * DATUSR= Collegamento Web.up
 * LISHTM= Lista oggetti generata da AS400 di Web.up
 * LISOGG= Lista oggetti Web.up/Looc.up

Tutte le operazioni loggate vengono scritte in un file
 :  : DEC T(OJ) P(*FILE) K(JALOGT0F)

## Attivazione
Per attivare la funzione di log e necessario impostare le seguenti tabelle : 
* Attivazione funzione
 :  : DEC T(ST) K(JA1)

 * Funzione da tracciare
 :  : DEC T(ST) K(JAL)

(Per Web.up) Definire per quali utenti non intendo tenere traccia
 :  : DEC T(ST) K(JAU)

### Dettagli tabella JAL
Nella tabella JAL è necessario specificare la singola funzione da loggare

Esistono funzioni di 2 tipi principali : 
 * Funzioni tramite le quali apro una nuova sessione su as400(collegamento)
Esempio DATSES,DATUSR
 * Funzioni tramite le quali chiedo dei dati
Esempio LISHTM,LISOGG

### Funzioni di tipo 1 (T$JAL1='C')
Queste funzioni vengono chiamate una volta sola al collegamento as400. Scrivono un record attivo che si chiude allo scollegamento**

### Funzioni di tipo 2 (T$JAL1<>'C')
Queste funzioni vengono chiamate tutte le volte che necessito di dati. Scrivono un record attivo che si chiude alla chiusura del relativo record di collegamento

## Modalità di scollegamento**
Lo scollegamento avviene in due modalità diverse per Looc.up e Web.up.

### Web.up
Lo scollegamento avviene quando la sessione as400 non è più attiva al richiamo di uno specifico programma di fasatura (JALOG1)
 :  : DEC T(OJ) P(*PGM) K(JALOG1)

Questo programma attribuisce una data e ora di chiusura uguale alla data ultima operazione + il time out specificato nel campo T$JAL2.

### Looc.up
Viene richiamato il programma jajac0 in una modalità di sconnessione. In questa modalità vengono chiusi tutti i record della sessione.
La mancata chiamata di scollegamento comporta un funzionamento simile all'altra modalità.

## Documentazione Tabella
Per ulteriori riferimenti sui campi Fare Riferimento a help tabella
- [JAL - Log collegamento webup loocup](Sorgenti/MB/DOC_OGG/TA_JAL)

## Aggiornare la data ultima operazione
Nel file di log è presente una data ultima operazione effettuata per una determinata sessione. Questa data può essere aggiornata quando viene effettuata ogni specifica operazione. Per attivare questo aggiornamento è necessario scrivere la funzione nella tabella jal e specificare "aggiorna collegamento :  Sì".

# VARI ESEMPI DI LOG
## Premesse
Per ognuno di questi esempi è necessario abilitare il log(JA1)

## Abilitare il log di loocup
>Set. JAL Funzioni Client/Server Log
Ele. DATSES
Descrizione          Log loocup
Tipologia messaggio  C                  Collegamento
Time out Secondi        60
Modalita Log Rid/Com C                  Completo
Modalita coll        L                  LoocUp
Agg collegamento     1                  SI


## Caratteristiche
Se una sessione viene chiusa im modo anomalo il log dichiara chiusa la Sessione 60 sec dopo l'ultima operazione effettuata

## Abilitare il log di webup
>Set. JAL Funzioni Client/Server Log
Ele. DATUSR
Descrizione          Log webup Collegamento
Tipologia messaggio  C                  Collegamento
Time out Secondi        60
Modalita Log Rid/Com C                  Completo
Modalita coll        W                  WebUp
Agg collegamento     1                  SI


>Set. JAL Funzioni Client/Server Log
Ele. LISHTM
Descrizione          Lis htm
Tipologia messaggio
Time out Secondi
Modalita Log Rid/Com C                  Completo
Modalita coll        W                  WebUp
Agg collegamento     1                  SI


>Set. JAL Funzioni Client/Server Log
Ele. LISOGG
Descrizione          Lisogg
Tipologia messaggio
Time out Secondi
Modalita Log Rid/Com C                  Completo
Modalita coll        W                  WebUp
Agg collegamento     1                  SI


## Caratteristiche
lo scollegamento avviene 60 sec dopo l'ultima operazione effettuata Le operazioni considerate sono : LISOGG e LISHTM Che vengono a loro volta tracciate in webup
