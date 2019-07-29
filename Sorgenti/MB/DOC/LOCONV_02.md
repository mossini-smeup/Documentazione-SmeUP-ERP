## Convertitore
### Prerequisiti
 :  : DEC T(MB) P(DOC) K(JALOC_13)  I(_7_Ricompilazioni              >>)

## Problemi nella ricompilazione.
### Formati video
Le specifiche dei formati video devono essere conformi allo standard SDA. Non sono ammesse quindi più **Key** sulla stessa riga.
 * _9_Soluzione, Attaverso l'SDA entrare nei vari formati e riaggiornare il sorgente.

### Formati video
Le specifiche dei formati video devono essere ordinate per riga e colonna.
 * _9_Soluzione, Attaverso l'SDA effettuare l'ordinamento.

### Limitazioni del convertitore
- [Limitazioni su convertitore](Sorgenti/MB/DOC/LOCONV_026)

## Oggetti trattati
 * **Command**, Sono i tasti funzionale CFxx e CAxx, durante la conversione viene ricercata la loro descrizione nel video attraverso le costanti Fx= o Fxx=, se non trovata ne viene assegnata una di default. Tutte le costanti rimanenti contenti le costanti Fx= o Fxx= sono trasformate in "CommandText" anche in assenza della sua definizione.

## Descrizioni di default
    F01=Help
    F02=Funzione
    F03=Fine Lavoro
    F04=Decodifica
    F12=Ritorno
    F22=Informazioni Programma

## Funzionamento emulatore
Nei subfile, l'emulatore fonderà i comandi inviati dalla write del piede.
 * **Free**, E' la definizione di variabile sia di Input, Output o nascosta.
 * **Intestazione**, E' la costante o la varibile definita titolo della finestra, viene assunta per le finestre la prima riga e i soli campi presenti prima della 20 colonna, altrimenti le prime due righe con solo i campi compresi fra la colonna 9 e 70 con esclusione dei campi £RAS* e £PDS* e la costante <-- e £G00AZ, £G00DV e £G00ES
 * **Intestazione di colonna**, Sono derivate dalle due righe precedenti alla prima riga del subfile, vengono inclusi i campi di output e le label. Sono esclusi i campi che iniziano con C$D* ma non con C$DAT*, C£*, £AUA* ed escludo i label con tenenti il carattere '=' inferiori all'ottava riga. Sono escluse le righe che contengono campi di input. Per ridefinire le righe di intestazione inserire un elemento nella tabella JAF con il seguente formato :  Codice = <Nome sorgente>.<Nome formato> e nel campo libero utilizzare i primi cinque caratteri i primi due identificano la riga più vicina al subfile mentre gli altri due la riga più lontana ed il quinto se si tratta di un'unica intestazione (Drop). E' considerata la seconda riga di intestazione solo se possiede un campo nei primi 10 caratteri. Es. BRAR01L.SFL1 0504 oppure BRAR01L.SFL1 0505 oppure BRAR01L.SFL1 05041 Se la colonna possiede un oggetto l'intestazione di colonna diviene l'intestazione di oggetto.
 * **Label**, E' definita una costante. Sono escluse le costanti <--, <->, /, >,  >, >> se si troma nelle prime 3 righe o dalla 23.
 * **Message**, E' la variabile contenete il messaggio di errore che verrà esposto nella barra di stato. Si assumono i campi senza decimali con nome W$M130, W2MES1, W$MES* con esclusione di W$MESE e W$MESG
 * **CommandText**, Testo di un comando.

### Funzionamento emulatore
Se presente un tasto funzionale senza descrizione viene assunto dal CommandText.
 * **Option**, E' il campo contenente l'opzione, viene riconosciuto attraverso i nomi campi W$OPZ*, S$OPZ*, W$MODA

### Funzionamento emulatore
Viene presentato una listbox contenente le sole opzioni sceglibili.
 * **OptionList**, E' l'elenco dei valori possibili per l'opzione. Viene indicato a quale opzione si riferisce, sono riconosciuti i campi £AUAS*, UI£OPZ e le stringhe contenenti il carattere uguale nelle prime otto righe. Per ora sospeso la ricerca nelle prime otto righe
 * **Tab**, E' il campo contenente la scelta del tab, viene riconosciuto dal nome campo WX$FMT, trasformato in campo nascosto.

## Funzionamento emulatore
Viene presentato un tab contenente i formati sceglibili.
 * **TabList**, E' l'elenco dei formati possibili per il tab, viene indicato a quale tab si riferisce, è riconosciuto dal nome campo WX£FMT oppure da tutte le costanti contenente il carattere uguale presenti sulla stessa riga del TAB.
 * **Button**, E' il campo contenente il risultato della pressione del bottone, è il campo lungo un carattere che precede la stringa >>
 * **ButtonList**, E' il valore restituito alla pressione del tasto, viene indicato a quale button si riferisce, riconosciuto dalla costante >> e sostituita in ?=..
 * **Action**, E' il campo contenente il risultato della lista di azioni, **Non gestito**
 * **ActionList**, E' l'elenco delle azioni disponibili, viene indicato a quale azione si riferisce,**Non gestito**
 * **Intestazioni di subfile**, Sono intese intyestazioni di subfile le prime due righe precedenti la prima riga del subfile, vengono esclusi i campi £AUAS e W£C e W$D

## Barra di testata
Gestita del file di configurazione, viene distribuito con le seguenti impostazioni
 * **Azienda**, Riconosciuta dai campi £RASDI e £G00AZ
 * **Posizionamento**, Riconosciuto dal campo C$POSI, C$POS1
 * **Memorizzazione Dati Video**, Riconosciuta dai campi W$RISC e C$RISC e WX$MDV
 * **Note Strutturate**, Riconosciuta dal campo £RPRF1, £RPRF2
 * **Divisione**, Riconosciuta dal campo £G00DV
 * **Esercizio**, Riconosciuto dal campo £G00ES

## Forzatura oggetti
E' possibile forzare il tipo oggetto tramite le seguenti parole chiavi da inserire nel SDA sulla chiave INDTXT. La chiave INDTXT è utilizzata per la documentazione dell'indicatore, non si può utilizzare nello stesso video più volte lo stesso indicatore, se si dovesse fare alla prima modifica del video ne viene mantenuto solo uno.
 * **£OGGHID**, Il campo o costante è definito nascosto
 * **£FMTINT**, Deve essere seguita dal nome del formato contenente le intestazioni del subfile, dalla prima e seconda riga dell'intestazione. Deve essere inserita a livello di control. La prima riga deve essere la maggiore fra le due. **Es.** £FMTINT FMT1 04 o £FMTINT FMT1 04 03
 * **£SFLINT**, Deve essere seguta dal nome della variabile o dalla costante che sarà utilizzata per documentare la colonna del subfile. Deve essere inserita sul campo del subfile desiderato. La variabile deve essere preceduta dalla ecommerciale e può essere sottostringata. **Es.** £SFLINT Scelta o £SFLINT [eW$INT1] o £SFLINT [eW$TITO : 3 : 5]
 * **£CMDTXT**, Il campo o costante contiene un testo di un comando. La variabile deve contenere la stringa Fxx=, se definito "F6=Conferma" non verrà riconosciuto.
 * **£TESTO**, Il campo o costante non deve essere esaminato per le intestazioni di subfile.
 * **£NOINT**, Il campo o costante non deve essere portato nell'intestazione della finestra come titolo, nonostante sia inserito nelle righe 1 e 2 della videata.
 * **£ACT**, Il campo contiene il risultato dell'azione. Deve essere seguito da un codice identificativo per la molteplicità. **Es.** £ACT 01
 * **£ACTLST**, Il campo o costante contiene l'elenco delle azioni utilizzabili. deve essere seguito dal codice identificativo per la molteplicità. **Es.** £ACTLST 01
 * **£OPZ**, Il campo contiene il risultato delle opzioni. Deve essere seguito da un codice identificativo per la molteplicità. **Es.** £OPZ 01
 * **£OPZLST**, Il campo o costante contiene l'elenco delle opzioni utilizzabili. Deve essere seguito dal codice identificativo per la molteplicità. **Es.** £OPZLST 01
 * **£BUT**, Il campo contiene il risultato del bottone. Deve essere seguito da un codice identificativo per la molteplicità. **Es.** £BUT 01
 * **£BUTLST**, Il campo o costante contiene il risultato della pressione del bottone. Deve essere seguito da un codice identificativo per la molteplicità. **Es.** £BUTLST 01
 * **£TAB**, Il campo contiene il risultato della navigazione dei formati. Deve essere seguito da un codice identificativo per la molteplicità. **Es.** £TAB 01
 * **£TABLST**, Il campo o costante contiene l'elenco dei formati navigabili. Deve essere seguito dal codice identificativo per la molteplicità. **Es.** £TABLST 01.

## Determinazione Oggetto dal programma
Se non è definito l'oggetto, ne viene derivato dalla ricerca attivata sul campo. Questa funzione è attiva solo se il programma si chiama come il video senza la**V**finale.
