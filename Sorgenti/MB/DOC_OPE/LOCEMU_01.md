# Emulatore
L'emulatore ha funzione di consentire l'utilizzo dei programmi Sme.Up dotati di interfaccia 5250. Il layout della finestra si mostra molto simile al formato video tradizionale 5250 : 
![LOCEMU_00](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_00.png)
Come tutte le finestre di Looc.Up anche la finestra emulatore può essere suddivisa in zone ciascuna con proprie caratteristiche perculiari

# Le funzioni della Title Bar
![LOCEMU_01](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_01.png)
La "Title Bar", oltre a visualizzare il titolo ed il sottotitolo dell'applicazione, consente l'esecuzione di una serie di funzioni mediante l'attivazione del "System Menu", tramite : 
 * ALT + BARRA SPAZIATRICE;
 * Click (tasto sinistro) su icona Emulatore della Title bar;
 * Click tasto destro del mouse sulla Title Bar : 

![LOCEMU_02](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_02.png)
Suddividiamo il "System Menu" in sette aree : 
 * _2_Gestione Finestra :  sono le funzioni standard di Windows di gestione delle finestre;
 * _2_Analisi della Comunicazione :  è un menu tecnico che consente, mediante l'attivazione di un sottomenu, l'accesso e la visualizzazione degli oggetti utilizzati per la comunicazione tra il server iSeries ed il Client;
 * _2_Icone :  permette la visualizzazione delle icone;
 * _2_Cache Locale dei formati video :  permette di gestire la cache dei formati video che vengono mantenuti sul client;
 * _2_Elenco Valori Memorizzati :  permette di gestire l'elenco dei Valori Memorizzati dei campi dei formati video, che vengono mantenuti sul client;
 * _2_File Configurazione :  permette la gestione del file di configurazione;
 * _2_Gestione Memorizzazioni Aspetto :  consentono la gestione delle memorizzazioni dell'aspetto (appearance) delle finestre e delle liste;
 * _2_Invio segnalazione errori :  permette di inviare al laboratorio la segnalazione di un errore.

## Gestione Finestra
Significato delle voci : 
 * Ripristina :  voce che permette, quando la finestra è minimizzata o massimizzata, di ripristinare la finestra a video;
 * Sposta :  permette di spostare con i tasti freccia o con l'ausilio del mouse la finestra;
 * Riduci a Icona :  permette di minimizzare sulla barra delle applicazioni la finestra;
 * Ingrandisci :  permette di portare a tutto schermo la finestra;
 * Chiudi :  chiude la finestra, questa voce è consentita solo se sono abilitati i tasti funzionali F03 o F12, e ne viene simulata la loro pressione.

## Analisi della Comunicazione
La funzione di queste opzioni è quella di permettere la comprensione della comunicazione tra l'emulatore 5250 e il server iSeries.

Significato delle voci : 
 * XML Sorgente :  permette di visualizzare l'XML che l'emulatore riceve dal server iSeries;
 * XML Normalizzato :  permette di visualizzare l'XML sorgente dopo avergli applicato le funzioni di normalizzazione e d'aver integrato i buffer video ricevuti;
 * Buffer Video :  permette di visualizzare l'XML del buffer video ricevuto dal server iSeries;
 * Dati Performance :  permette di visualizzare l'elenco dei dati di performance che vengono salvati durante l'interazione;
 * Traccia Comunicazione :  permette di visualizzare i dati della comunicazione tra il server iSeries e l'emulatore;
 * Traccia errori :  permette di visualizzare il log degli errori non gestiti.

Si possono compiere le stesse azioni anche attraverso short-cut (comandi tastiera); si faccia riferimento all'immagine per la loro definizione.

## Icone
La funzione di queste opzioni è di permettere la scelta di visualizzare o meno le icone nell'uso dell'emulatore 5250.
L'inibizione di quest'opzione dà la possibilità di velocizzare l'interazione con l'emulatore. Vediamo quali sono i componenti di quest'area : 
 * Icone Oggetto su Campo :  permette di abilitare/disabilitare la visualizzazione delle Icone vicino ai campi (icone oggetto);
 * Icone Oggetto su Subfile :  permette di abilitare/disabilitare la visualizzazione delle Icone all'interno delle liste (icone oggetto su subfile);
_2_Nota; l'attivazione di questa funzionalità può portare ad una visualizzazione parziale del contenuto delle colonne.

Si possono compiere le stesse azioni anche attraverso short-cut (comandi tastiera); si faccia riferimento all'immagine per la loro definizione.

## Cache Locale dei formati video
La funzione di queste opzioni è di permettere la gestione della cache dei formati video : 
 * Visualizzazione :  consente di "esplorare" la cartella nella quale vengono memorizzati i documenti XML che descrivono i formati video iSeries.
 * Cancellazione :  consente la cancellazione della cache dei documenti XML che descrivono i formati video iSeries. Ciò può rendersi necessario nel caso in cui l'applicazione iSeries venga modificata.
_2_Nota; ad ogni esecuzione di LOOC.up la cache dei formati video XML viene automaticamente svuotata.

Si possono compiere le stesse azioni anche attraverso short-cut (comandi tastiera); si faccia riferimento all'immagine per la loro definizione.

## Valori Memorizzati
I valori memorizzati sono quei valori che sono stati usati in precedenza per un determinato tipo di campo. _2_Nota; l'attivazione delle funzionalità di memorizzazione valori è configurabile nei parametri _3_Completamento automatico e _3_proposta, mentre il numero massimo di valori memorizzabili è configurabile nel parametro _3_lunghezza. (cfr. Configurazione).
I valori memorizzati sono visualizzabili posizionandosi su un campo (Es. :  un codice articolo) e premendo il tasto freccia giù; a questo punto compare una finestra in cui sono presenti tutti i campi utilizzati in precedenza.
_2_Nota; se il campo di input è classificato come oggetto, la "storia" dei valori è condivisa tra tutti i campi relativi alla stessa classe. Se il campo di input è "neutro", la "storia" dei valori è condivisa tra tutti i campi di input aventi lo stesso nome (indipendentemente dal formato video).
 * Visualizzazione :  consente di "esplorare" la cartella nella quale vengono memorizzati i valori storici dei campi video di input.
 * Cancellazione :  permette di cancellare l'elenco dei valori memorizzati.

## Gestione Memorizzazioni Aspetto
I componenti di quest'area sono : 
 * visualizzazione elenco aspetto e posizionamento finestre, consente la gestione delle memorizzazioni dell'aspetto (appearance) delle finestre e delle liste. Per ogni finestra viene memorizzato quanto segue : 
 ** le sue coordinate x e y
 ** la sua Larghezza ed Altezza
 ** se la finestra è dotata di Subfile vengono inoltre memorizzate le larghezze delle singole colonne;
 * cancellazione globale aspetto e posizionamento finestre, cancella le impostazioni memorizzate per tutte le finestre;
 * cancellazione aspetto e posizionamento finestra corrente, cancella le impostazioni memorizzate solo per la finestra corrente.

## Configurazione
 * Carica / Gestisci :  consente la modifica;
 * Ricaricamento :  consente di ricaricare una configurazione aggiornata dopo eventuali modifiche.

La funzione di queste opzioni è quella di gestire la configurazione dell'emulatore 5250. La configurazione avviene attraverso l'editazione di un file XML che è assistita dalla gestione dei setup.
Selezionando la gestione della configurazione si apre la finestra seguente : 
![LOCEMU_03](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_03.png)dove si sceglie se intervenire sul livello di configurazione (es. specifica dell'utente oppure comunte a tutto l'ambiente :  utente "**").

Il click sul bottone "Modifica" apre il formato per le impostazioni di configurazione : 
![LOCEMU_04](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_04.png)Per il significato di tutti i campi si rimanda alla documentazione specifica.

### Dove risiedono i file di configurazione
ll reperimento della configurazione avviene mediante "risalita" secondo i seguenti criteri (il primo trovato viene ritenuto valido) : 
 - (LoocupDir)\LOOCUP_SET\CFG\EMU\(Ambiente)\(Utente)\SmeuiClt.xml
 - (LoocupDir)\LOOCUP_SET\CFG\EMU\DEFAULT\(Utente)\SmeuiClt.xml
 - (LoocupDir)\LOOCUP_SET\CFG\EMU\(Ambiente)\DEFAULT\SmeuiClt.xml
 - (LoocupDir)\LOOCUP_SET\CFG\EMU\DEFAULT\DEFAULT\SmeuiClt.xml
 - (LoocupDir)\LOOCUP_SET\CFG\EMU\EMU\SmeuiClt.xml

## Invio segnalazione errori
Questa funzione apre un formato per l'invio di una mail di segnalazione allo "Sviluppo", è possibile scrivere un breve commento : 
![LOCEMU_05](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_05.png)
# Le funzioni della Header Bar
![LOCEMU_06](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_06.png)Nell'emulatore la header bar permette, in maniera grafica, di : 
 * Identificare : 
 ** il sistema a cui si è collegati;
 ** l'ambiente in cui si sta lavorando;
 ** l'utente connesso.
 * Accedere a funzionalità su : 
 ** il componente;
 ** il programma;
 ** il video;
 ** elementi variabili.

La "Header Bar" è suddivisa in tre aree distinte : 
 * Area Ambiente;
 * Area Oggetti;
 * Area Dinamica.
_2_Nota; l'aspetto e la visualizzazione della barra è condizionata dalla configurazione.

## Area Ambiente
In quest'area possono essere visualizzate delle immagini rappresentanti : 
 * il sistema;
 * l'ambiente;
 * l'utente.

![LOCEMU_07](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_07.png)_2_Nota, le immagini possono venire mostrate o meno a seconda che siano presenti le relative icone nella cartella LOOCUP_ICO

## Area Oggetti
![LOCEMU_08](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_08.png)In questa area vengono visualizzate le icone relative ai seguenti oggetti : 

| 
| .COL Txt="_2_Oggetto" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="_2_Parametro" Lun="0" A="L" |
| 
| .COL Txt="_2_Descrizione" Lun="0" LunAut="1" |
|  - J1 | GRA EMU | Emulatore |
|  - OJ | *PGM ....... | Programma |
|  - OJ | *FILE ....... | File video |
| 

Da ogni icona, con il tasto destro, è possibile accedere alle funzioni ed ai metodi propri di ogni oggetto che permettono di gestire e identificare : 
 * il componente che è attualmente in uso;
 * il programma;
 * il video.

## Area Dinamica
In questa area possono essere dinamicamente rimappati dei campi di I/O presenti nel formato video dell'Emulazione 5250.
![LOCEMU_09](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_09.png)
## Icone
La visualizzazione delle icone è sottoposta a : 
 * attivazione dal System Menu della Title Bar;
 * la tipizzazione del campo.

Nei campi tipizzati il tasto destro sull'icona o sul campo apre il PopUp dell'oggetto, mentre il click sull'icona lancia la funzione associata in sede di configurazione :  tab "Object actions" (generalmente la ricerca per codice "!").

# Le funzioni della Tool Bar
## Sinistra
In questa area vengono rappresentati i tasti funzionali standard (cioè quei tasti funzionali aventi la stessa funzionalità in tutta l'applicazione) e che quindi possono essere rappresentati anche solo con un'icona.
L'evidenziazione in giallo di un pulsante di paginazione vuole sottolineare che la lista (subfile) non è interamente caricata.
![LOCEMU_10](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_10.png)
## Destra
In questa parte vengono rappresentati i bottoni corrispondneti ai tasti funzionali non standard specifici del programma.

## Le funzioni della Status Bar
Le funzioni della Status Bar sono principalmente due : 
 * visualizzazione dei messaggi informativi;
 * reperimento di informazioni sul programma;

Posizionandosi sopra e apettando alcuni secondi verrà presentato un riquadro di riepilogo informazioni sul programma ILE-RPG attualmente in esecuzione (Hint).

## Il corpo dell'emulatore
Definiamo corpo dell'emulatore quella parte di finestra che riproduce la schermata 5250 del server iSeries.

### Significato dei colori di sfondo
Ad ogni tipo di campo viene associato un colore; questo per facilitarne l'identificazione. Nella seguente tabella vediamo i colori e i loro significati : 

| 
| .COL Txt="_2_Colore" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="_2_Significato" Lun="0" LunAut="1" |
|  - Bianco Campo Neutro | Non sono associate le funzionalità avanzate di LOOC.up. **Nota**, il colore del campo neutro è definito in configurazione. |
|  - Giallo | Campo Tipizzato |
|  - Verde | Campo Numerico Positivo |
|  - Azzurro | Campo Numerico Negativo |
|  - Rosso | Campo Errato |
| 


### La storia dei valori
La storia dei valori è uno strumento utile che permette di visualizzare le ultime digitazioni effettuate in quel campo (cfr. Configurazione).

### Campi Tipizzati
Questi campi sono contraddistinti da : 
 * sfondo giallo o, se all'interno di un subfile, dal colore giallo dell'intestazione della colonna;
 * icona associata al campo, l'icona cambia in relazione al tipo di oggetto applicativo a cui fa riferimento. Il click sull'icona lancia la funzione definita in configurazione (di solito la ricerca).

Sul campo tipizzato il tasto destro apre un menu di popup con le funzioni previste per l'oggetto : 

![LOCEMU_11](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_11.png)
# Lista (Subfile)
La lista è fondamentalmente suddivisa in due tipologie di campi : 
 * campi di visualizzazione
 * campi di inserimento/modifica

![LOCEMU_12](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_12.png)Lo spostamento all'interno delle righe nella lista avviene attraverso l'uso dei tasti freccia su e giù. Per spostarsi tra i campi della lista (relativamente allo stesso record) vengono utilizzati i tasti di
tabulazione.

## Utilizzo del PopUp in lista
All'interno della lista è possibile ottenere il PopUp solo sulle colonne (e quindi i campi) tipizzate; queste vengono presentate con l'intestazione gialla.
Posizionandosi con il mouse su una colonna di questa tipologia è possibile richiamare il PopUp specifico dell'oggetto che si è selezionato. Inoltre, abilitando la visualizzazione delle icone all'interno della lista (subfile) è possibile effettuare la stessa procedura sulle icone.

## Selezione di un elemento della lista
Per selezionare un codice all'interno di una lista (subfile), sono a disposizione quattro possibili modalità : 
 * Doppio click con il mouse sul codice (mette una X sul campo opzione)
 * Immissione di una X di selezione sul campo opzioni
 * ALT + (Lettera assegnata del pulsante relativo) se sono presenti i bottoni di opzione
 * Right-Click + seleziona voce

## Configurazione del formato
Le opzioni che permettono la configurazione del formato di visualizzazione sono raccolte nel tab "Griglia" della scheda del setup emulatore.

## TabSheet
Questo elemento grafico viene usato in alcune applicazioni, come ad esempio la gestione enti. E' possibile selezionare il TabSheet desiderato utilizzando i tasti ALT + (Lettera Sottolineata) oppure
cliccando sul TabSheet desiderato.
![LOCEMU_13](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_13.png)Il TabSheet attivo viene visualizzato in blu.

## Function Bar
La Function Bar è una barra verticale che viene visualizzata attraverso l'uso di una variabile descritta nel formato video. Le funzioni riportate nella Function Bar sono contestuali all'applicazione.

![LOCEMU_14](http://localhost:3000/immagini/MBDOC_OPE-LOCEMU_01/LOCEMU_14.png)
## La tastiera
La tastiera è lo strumento principale con cui interfacciarsi con l'emulatore. La maggioranza delle funzioni attivabili con il mouse possono essere effettuate anche attraverso la tastiera :  nel seguito sono
illustrate le combinazioni di tasti ed il loro significato.

Le motivazioni che stanno alla base di questa scelta sono essenzialmente : 
 * velocità di interazione :  l'utilizzo della tastiera permette una maggiore efficienza rispetto all'uso del mouse
 * l'interfaccia segue il concetto di "grafica in più" e non " grafica invece", l'utente SME.up si è gia creato un proprio legame mentale tra i tasti da utilizzare e le funzioni, si ha una key-recognition tra la funzione voluta e la tastiera.

Il mouse rappresenta, invece, il punto di partenza per gli utenti nuovi che possiedono un background culturale di stile Windows.
All'inizio a questi risulterà più naturale e semplice l'uso del mouse. Poi, acquisiranno anche loro propri stili di interazione con un utilizzo maggiore della tastiera, accorgendosi di poter effettuare le stesse operazioni in maniera più efficiente e veloce.

## Utilizzo della tastiera
In questa sezione vengono presentate le combinazioni di tasti che vengono utilizzate nell'emulatore.

| 
| .COL Txt="_2_Primo tasto" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="_2_Secondo tasto" Lun="0" A="L" |
| 
| .COL Txt="_2_Funzionalità" Lun="0" LunAut="1" |
|  - CTRL | F01 | Apre XML Origine |
|  - CTRL | F02 | Apre XML Normalizzato |
|  - CTRL | F03 | Apre Buffer Video |
|  - CTRL | F04 | Apre Log Performance |
|  - CTRL | F05 | Apre Log Socket Data |
|  - CTRL | F06 | Apre tabella grafica da lista (subfile) |
|  - CTRL | F07 | Apre Foglio Elettronico da lista (subfile) |
|  - CTRL | F10 | Pulisce la cache dei formati video |
|  - CTRL | F11 | Abilita/disabilita icone su lista (subfile) |
|  - CTRL | F12 | Abilita/disabilita icone su campo (subfile) |
|  - CTRL | PageUp | Ripristina a finestra |
|  - CTRL | PageDown | Ingrandisce a tutto schermo |
|  - CTRL | Freccia Su | Sale di una riga all'interno di una lista |
|  - CTRL | Freccia Giù | Scende di una riga all'interno di una lista |
| -  | Freccia Giù | Su un campo tipizzato, permette di visualizzare la storia dei valori |
|  -  | Tab | Si sposta sul campo successivo |
|  - Shift | Tab | Si sposta sul campo precedente |
|  - Tasto PopUp |   | Apre PopUp menu su oggetto/elemento grafico |
|  - ALT | F04 | Chiude finestra corrente, consentita se abilitati tasti F03 e/o F12 |
|  - ALT | Barra spaziatrice | Apre System Menu della Title Bar |
|  - ALT | [Lettera sottolineata] | Nei TabSheet, nelle Function Bar e negli Option Button, permette di passare alla sezione contraddistinta dalla lettera sottolineata |
|  - ESC |   | Apre una sessione emulazione 5250 a caratteri per la gestione delle stampe e stampanti |
| 

