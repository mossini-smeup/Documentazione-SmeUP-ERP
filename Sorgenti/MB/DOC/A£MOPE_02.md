
I test funzionali mirano a verificare che le funzionalità di un prodotto stabilite dai suoi requisiti siano state realizzate correttamente.

All'interno di Sme.UP vengono effettuati a livello automatico o manuale varie tipologie di test di funzionalità.

A livello automatico ad esempio è possibile citare : 
- unit test e integration test lato Web.UP
- unit test delle API e dei servizi RPG

## Unit test e integration test lato Web.UP

Il client Web.UP è un'applicazione scritta con la tecnologia java ee. Al suo interno sono presenti sia test unitari delle singole classi java sia test di integrazione in grado di testare ad alto livello l'applicazione. Vengono controllati quindi sia il corretto comportamento dei singoli componenti dell'applicazione sia le relazioni tra componenti, nonchè le chiamate a sistemi esterni quali il provider o il sistema as400. Pertanto i test di integrazione di Web.UP oltre a testare il client testano indirettamente tutto il sistema. Ciò viene realizzato simulando il comportamento finale dell'utente, in particolare automatizzando determinati percorsi utente sul browser e verificando di ottenere i risultati visivi e procedurali attesi.

Entrambe le tipologie di test (unitari e di integrazione) vengono eseguite periodicamente più volte al giorno sulla versione di sviluppo di Web.UP in maniera tale da individuare tempestivamente possibili regressioni o malfunzionamenti. Sono inoltre eseguite in fase di rilascio di ogni nuova versione pubblicata, prima di produrre la release.

Per aggiungere test unitari o di integrazione basta operare a livello del progetto java del client Web.UP, nelle cartelle src/test/java per i test unitari e nella cartella WebUP/src/it per i test di integrazione.

## Unit test delle API e dei servizi RPG

Tutti gli Unit Test devono essere sviluppati collegandosi all'ambiente definito nello script A£MOPE_02, questo ambiente permette di avere una base dati stabile e di conseguenza un test ripetibile.
 :  : DEC T(MB) P(SCP_SET) K(A£MOPE_02)

### API
Prima di poter procedere all'automazione del collaudo del software bisogna realizzare i seguenti componenti : 
**Script di configurazione (SCP_CFG)**
Guida il programmatore alla stesura degli Unit Test
**Script degli Unit Test (SCP_SIM)**
Qui vengono descritti gli Unit Test da eseguire definendo l'input e l'output atteso
**Esecutore degli Unit Test (JASRC/B£SIM0_xxx)**
E' il programma che esegue lo script degli Unit Test e memorizza gli esiti degli stessi

Per rendere più veloce la realizzazione dei componenti sopra citati sono stati resi disponibili degli strumenti che realizzano dei semilavorati, più o meno affidabili.
Tutte le funzioni sono accessibili attraverso il menù della scheda dell'API stessa all'interno del Dashbord nel menu Unit Test.

 :  : T04 Script di configurazione
Attraverso il menu dello Unit Test è possibile generare un semilavorato dello script di configurazione, la generazione segue queste regole : 
**Campi derivati dalla API**
Tutti i campi dichiarati nella specifica PARM presente nella API aventi lunghezza saranno riportati nello script come campi di input  e di output, la loro descrizione viene assunta dal commento e non saranno oggettivati.
Viene fatta eccezzione per i campi con descrizione Funzione e Metodo in cui rispettivamente saranno oggettivati come lista interna e V3 della funzione
Se si riscontra un campo senza lunghezza, viene aggiunto il finale "0F" e verificata la sua esistenza come database, se esistente tutti i campi del database saranno riportati come campi di input e output, in questo caso saranno oggettivati.
**Campi derivati dalla DS della API**
Tutti i campi presenti nella DS della API che contengono la stringa I_ saranno riportati come campi di input, assunta la descrizione dal commento e non oggettivati
Tuitti i campi presenti nella DS della API che contengono la stringa O_ saranno riportati come campi di output, assunta la descrizione dal commento e non oggettivati
Tutti i campi che iniziano con il nome della API e non contengono il carattere '_' sono riporatti come campi di input  e di output.
**Campi schiera**
I campi delle schiere devono essere seguiti dal carattere "." e l'indice della stessa.

**Attenzione**, il semilavorato sarà generato nella libreria richiesta solo e soltanto se non già presente nella lista di libreria, anche se assente nella libreria richiesta.

**Attenzione 2** :  lo script di configurazione viene creato con impostata l'exit dell'A08 A£MOPE_A08. E' possibile però creare un'exit specifica per l'API, creando un pgm avente nome SIM_xxx_A8. Questo pgm verrà automaticamente chiamato, con la stessa exit prevista dalle exit dell'A08, dal pgm A£MOPE_A08.

 :  : T04 Esecutore degli Unit Test
Attraverso il menu dello Unit Test è possibile generare un semilavorato dell'esecutore degli Unit Test, la generazione segue queste regole : 

Deve essere stato già generato lo script di configurazione, input per la definizione dei campi di input e output durante il processo di esecuzione.
Saranno inseriti sempre le copy di dipo DS e E presenti, non saranno aggiunte le definizioni esterne dei database.

**Attenzione**, il semilavorato sarà generato nella libreria e file sorgente richiesto solo e soltanto se non già presente nella lista di libreria, anche se assente nella libreria richiesta.
La generazione dell'oggetto è a carico dello sviluppatore, per poter rigenerare il codice deve essere cancellaro sia l'oggetto che il sorgente.

 :  : T04 Script degli Unit Test
Attraverso il menu dello Unit Test è possibile gestire lo script degli Unit Test

Deve essere stato già generato lo script di configurazione, input per il wizard da utilizzare per stendere gli Unit test desiderati.

**Nota**L'output dello Unit test può essere generato automaticamente alla prima esecuzione dello Unit Test, una volta generato per poter essere rigenerato deve essere eliminato manualmente dallo scipt degli Unit Test.

 :  : T04 Esecuzione
Attraverso il menu dello Unit Test è possibile eseguire lo script degli Unit Test.
Questa azione si abilita solo in presenza dello script degli Unit Test.
Verrà richiesto se si vuole completare lo script degli Unit Test con l'ouput di esecuzione degli stessi.

 :  : T04 Esecuzione della api senza script di simulazione
Attraverso il menu dello Unit Test è possibile eseguire l'esecuzione estemporanea dell'API.

### SERVIZI
A differenza delle API non necessita la preparazione di componenti aggiuntivi.

### Script degli Unit Test
Attraverso il menu dello Unit Test è possibile gestire lo script degli Unit Test
Qui verrà definita la F di esecuzione, all'inserimento verrà eseguita la F e memorizzato il risultato per le sucessive operazioni di confronto, è data la possibilità di rigenerare l'immagine all'occorrenza
l'oggetto può essere derivato attraverso le seguenti keyword : 
*LAST - Viene mantenuto il valore precedente
*RND - Viene generato un codice randon utilizzando l'oggettivazione del campo stesso
*RND.xxx - Viene generato un codice randon utilizzando l'oggettivazione descritto dopo il "."

 :  : T04 Esecuzione
Attraverso il menu dello Unit Test è possibile eseguire lo script degli Unit Test.
Questa azione si abilita solo in presenza dello script degli Unit Test.

**Nota**L'output, l'atteso e la differenza è accessibile solo se lo UNit Test è fallito
