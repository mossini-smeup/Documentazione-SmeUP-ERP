TabSheet
Questo elemento grafico viene usato in alcune applicazioni, come ad esempio la gestione enti.
E' possibile selezionare il TabSheet desiderato utilizzando i tasti ALT + (Lettera Sottolineata) oppure
cliccando sul TabSheet desiderato.
Il TabSheet attivo viene visualizzato in blu.
Function Bar
La Function Bar è una barra verticale che viene visualizzata attraverso l'uso di una variabile descritta
nel formato video.
Le funzioni riportate nella Function Bar sono contestuali all'applicazione.

La tastiera
La tastiera è lo strumento principale con cui interfacciarsi con l'emulatore. La maggioranza delle
funzioni attivabili con il mouse possono essere effettuate anche attraverso la tastiera :  nel seguito sono
illustrate le combinazioni di tasti ed il loro significato.
Le motivazioni che stanno alla base di questa scelta sono essenzialmente : 
 * velocità di interazione :  l'utilizzo della tastiera permette una maggiore efficienza rispetto all'uso del
mouse
 * l'interfaccia segue il concetto di "grafica in più" e non " grafica invece", l'utente SME.up si è gia
creato un proprio legame mentale tra i tasti da utilizzare e le funzioni, si ha una key-recognition tra
la funzione voluta e la tastiera.
Il mouse rappresenta, invece, il punto di partenza per gli utenti nuovi che possiedono un background
culturale di stile Windows.
All'inizio a questi risulterà più naturale e semplice l'uso del mouse. Poi, acquisiranno anche loro propri
stili di interazione con un utilizzo maggiore della tastiera, accorgendosi di poter effettuare le stesse
operazioni in maniera più efficiente e veloce.
Utilizzo della tastiera
In questa sezione vengono presentate le combinazioni di tasti che vengono utilizzate nell'emulatore.
Primo tasto Secondo tasto Funzionalità
CTRL F01 Apre XML Origine
CTRL F02 Apre XML Normalizzato
CTRL F03 Apre Buffer Video
CTRL F04 Apre Log Performance
CTRL F05 Apre Log Socket Data
CTRL F06 Apre tabella grafica da lista (subfile)
CTRL F07 Apre Foglio Elettronico da lista (subfile)
CTRL F10 Pulisce la cache dei formati video
CTRL F11 Abilita/disabilita icone su lista (subfile)
CTRL F12 Abilita/disabilita icone su campo (subfile)
CTRL PageUp Ripristina a finestra
CTRL PageDown Ingrandisce a tutto schermo
CTRL Freccia Su Sale di una riga all'interno di una lista
Manuale base LOOC.up Cod. LOA0003_02 56
Sme.up
CTRL Freccia Giù Scende di una riga all'interno di una lista
Freccia Giù Su un campo tipizzato, permette di visualizzare la storia dei valori
Tab Si sposta sul campo successivo
Shift Tab Si sposta sul campo precedente
Tasto PopUp
Apre PopUp menu su oggetto/elemento grafico
ALT F04 Chiude finestra corrente, consentita se abilitati tasti F03 e/o F12
ALT Barra spaziatrice Apre System Menu della Title Bar
ALT [Lettera sottolineata] Nei TabSheet, nelle Function Bar e negli Option Button, permette di
passare alla sezione contraddistinta dalla lettera sottolineata
ESC Apre una sessione emulazione 5250 a caratteri per la gestione delle
stampe e stampanti
La configurazione dell'Emulatore
Questa sezione è dedicata alla raccolta degli elementi di configurazione dell'Emulatore di LOOC.up.
Per il reperimento della configurazione si legga la sezione Dove risiedono i file di configurazione .
Icone
Questa sezione si trova in :  (/Application/Module[@Name=Main]/Images)
E' la sezione nella quale si definiscono le impostazioni di visualizzazione e reperimento delle icone
oggetto.
Attributo Namespace Valore/Descrizione
Direttorio Icone Oggetti LocalPath Il nodo radice del percorso che contiene le icone degli oggetti. Il percorso può
essere specificato sia relativamente alla posizione di avvio del programma, che
in modo assoluto.
Topologia di Archiviazione NameType Tree = le icone vengono archiviate in una struttura ad albero.
Flat = le icone vengono archiviate in una struttura piatta.
Nome icona di Default DefaultName
Estensione Icone IconExtension Viene espressa nel formato <estensione>.
(Es :  .gif)

Gestione Cache Icone IconCache Yes=Le icone vengono memorizzate all'avvio dell'applicazione.
L'applicazione è più lenta nella fase di avvio, ma più veloce nel disegno delle
videate.
No=Le icone vengono caricate al momento del loro utilizzo. L'applicazione è
più veloce nella fase di avvio, ma più lenta nel disegno delle videate.
Generale
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/General)
E' la sezione che contiene i parametri "generali" che principalmente configurano l' "apparenza"
estetica dell'emulatore.
Attributo Namespace Valore/Descrizione
Memorizzazione
Posizione/Dimensione Finestre
RestoreFromPos Yes = Viene memorizzata la posizione e la dimensione
di ogni finestra; alle visualizzazioni successive la
finestra verrà visualizzata secondo le impostazioni
memorizzate.
No = Ogni emissione di una finestra avviene secondo le
coordinate specificate nel DSPF iSeries.
Font Campi di Emissione FontName Nome del font utilizzato per i campi di Output e i Campi
Costante.
Font Campi di Immissione FontNameGet Nome del font utilizzato per i campi di Input/Output.
Font Campi di Emissione su
Subfile
FontNameGrid Nome del font utilizzato per i campi di Output e i Campi
Costante su Subfile.
Font Campi di Immissione su
Subfile
FontNameGetGrid Nome del font utilizzato per i campi di Input/Output su
Subfile.
Dimensione Carattere FontSize Dimensione (in punti) dei caratteri.
Visualizzazione Icone Oggetto DisplayObjIcon5250Field Yes = Vengono visualizzate le icone oggetto.
No = Non vengono visualizzate le icone oggetto.
E' possibile attivare/disattivare questa opzione a runtime
mediante il "System Menu".
Visualizzazione Icone Oggetto
su Subfile
DisplayObjIcon5250SubfileField Yes = Vengono visualizzate le icone oggetto su Subfile.
No = Non vengono visualizzate le icone oggetto su
Subfile.
E' possibile attivare/disattivare questa opzione a runtime
mediante il "System Menu".
Le colonne del subfile, non venendo ridimensionate,
potrebbero visualizzare solo parzialmente i dati
contenuti se l'opzione viene attivata.
Colore Sfondo Finestra StandardColor/BackgroundColor Inserire il colore nel formato R;G;B.
Colore Caratteri Finestra StandardColor/CharacterColor Inserire il colore nel formato R;G;B.

Colore Sfondo Campi di
Immissione
InputColor/BackgroundColor Inserire il colore nel formato R;G;B.
Colore Caratteri Campi di
Immissione
InputColor/CharacterColor Inserire il colore nel formato R;G;B.
Suono su Errore AudioErrorFile Inserire (opzionalmente) il nome di un file .wav che
verrà riprodotto ogni volta che viene visualizzato un
messaggio di campo non vuoto.
Modalità visualizzazione Riga
Subfile selezionata
MarkSelectedRow Yes = La riga Subfile selezionata viene visualizzata con
caratteri bianchi su Sfondo Blu.
No = La riga Subfile selezionata viene evidenziata
mediante una bordatura blu.
Visualizzazione Opzioni in
Combobox
OptionsInCombo Yes = I campi opzione presenti sulle videate vengono
visualizzati mediante combo box.
No = I campi opzione vengono visualizzati come
normali campi di input.
Autocompletamento Campi di
Immissione
AutoComplete Yes = Viene attivata la memorizzazione della storia dei
valori immessi nei campi di input.
No = I valori immessi nei campi di input non vengono
memorizzati.
Proposta Automatica
Autocompletamento
AutoCompleteAutoProposal Yes = Durante la digitazione del contenuto di un campo
viene automaticamente visualizzato e proposto l'elenco
dei valori precedentemente utilizzati per il campo ed
aventi la stessa radice.
No = Per richiamare l'elenco dei valori occorre premere
il tasto "frecciagiù".
Numero Massimo Voci di
Proposta Automatica
AutoCompleteHistoryLength Inserire il numero massimo di valori da memorizzare per
ogni campo od oggetto. I valori vengono comunque
sempre memorizzati in ordine FIFO ma presentati in
ordine alfabetico.
Lista (Subfile)
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/Grid/Default|G18)
Consente di configurare l' "apparenza" delle griglie. E' possibile impostare un' "apparenza" generale,
ed un' "apparenza" per tutte le griglie di tipo "G18".
Attributo Namespace Valore/Descrizione
Visualizzazione a Schermo Intero FullScreen Yes = Le finestre contenenti le griglie specificate vengono
massimizzate.
No = Le finestre contenenti le griglie specificate vengono visualizzate
così come definito nel DSPF iSeries.
Visualizzazione Righe di
Separazione
GridLine Yes = Le celle della griglia sono separate da righe.
No = Non vi è alcuna separazione tra le celle della griglia.
Manuale base LOOC.up Cod. LOA0003_02 59
Sme.up
Attivazione Lettura Facilitata AlternateRowColor Yes = Le righe vengono visualizzate in modalità "lettura facilitata"
(bianco/giallo a righe alternate).
No = Tutte le righe presentano uno sfondo neutro.
HeaderBar
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/HeaderBar)
Consente di specificare la configurazione dell'HeaderBar.
Attributo Namespace Valore/Descrizione
Visualizzazione Display Yes = L'Header Bar viene visualizzata (solo se almeno una
"regola" valida).
No = L'Header Bar non viene mai visualizzata.
Visualizzazione Icone Oggetti DspDftObjIco Yes = Vengono visualizzate le icone relative ai seguenti
oggetti :  emulatore, programma, formato video.
No = Non vengono visualizzate le suddette icone.
Visualizzazione Informazioni "Ambiente" DspEnvInfo Yes = Vengono visualizzate le immagini associate a : 
Sistema, Ambiente, Utente.
No = Non vengono visualizzate le suddette immagini.
HeaderBar - Regole
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/HeaderBar/Rules/Rule)
Le Regole sono un'elenco di voci di configurazione che consentono di definire le modalità con le quali
alcuni campi possono essere rimappati nell'HeaderBar.
Attributo Namespace Valore/Descrizione
Titolo Pannello Regola @Title Descrive il titolo del pannello che conterrà il campo rimappato
nell'Header Bar.
Dimensione Bordo Pannello @BorderWitdth Dimensione (in pixel) del bordo del pannello.
Nome Controllo Ocx @XmlNodeName E' il nome del controllo ActiveX che si vuole attivare(opzionale).
Nome Nodo Xml E' il nome del Nodo Xml che deve essere rimappato.
Nome e Valore Attributo Xml E' il nome ed il valore che un eventuale attributo deve contenere
perché il campo venga rimappato nell'Header Bar.
Viene espresso nel formato <NomeAttributo>=<ValoreAttributo>.
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm

ToolBar
Questa sezione si trova in : 
(/Application/Module[@Name=Emulator]/CommandBar/Left|Center|Right/CommandButton)
E' divisa in 3 sezioni :  Left, Center, Right. In ogni sezione è possibile definire un'elenco di tasti
funzionali da visualizzare.
La sezione Right descrive i tasti funzionali "standard", cioè quei tasti funzionali che non hanno
bisogno di una descrizione per essere compresi.
La sezione Center non è al momento utilizzata.
La sezione Left descrive i tasti funzionali "non standard", cioè quei tasti funzionali che hanno bisogno
di una descrizione per essere compresi.
Attributo Namespace Valore/Descrizione
Identificatore Tasto Key E' l'identificatore del tasto associato.
I tasti funzionali da F1 a F24 sono rappresentati nell'intervallo -1..-24.
Altri Codici di Tastiera sono : 
13 = Invio;
33 = Pagina Su;
34 = Pagina Giu;
99999 = Qualunque Tasto non definito;
Testo Tasto Txt Il testo da visualizzare se nell'Xml di definizione del formato non è presente alcun testo
(opzionale).
Icona Tasto Ico Il percorso ed il nome dell'icona che rappresenta graficamente il tasto stesso
(opzionale).
Il percorso può essere specificato sia relativamente alla posizione di avvio del
programma, che in modo assoluto.
FunctionBar
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/FunctionBar)
Definisce la visualizzazione delle FunctionBar.
Attributo Namespace Valore/Descrizione
Visualizzazione Display Yes = Se definita nell'Xml di definizione del formato viene visualizzata.
No = Non viene mai visualizzata alcuna Function Bar anche se definita nell'Xml del
formato.
Logging
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/Logging)
Definisce l'attivazione delle funzionalità di Logging.
Attributo Namespace Valore/Descrizione

Attivazione Traccia Dati Comunicazione SockDataTrace Yes = Ogni dato ricevuto/trasmesso viene "loggato".
No = Il log dei Dati è disabilitato.
Dimensione Massima nel File di
Configurazione
SockDataTraceSize E' la dimensione massima del file di traccia dati
comunicazione.
La dimensione è espressa in KB ed il default è 1024.
Quando viene raggiunta la dimensione massima, il file di
log esistente viene ridenominato con estensione .bak e
viene creato un nuovo file.
Attivazione Memorizzazione Errori ErrorTrace Yes = Ogni errore emesso dall'applicazione viene
"loggato".
No = Il log degli errori è disabilitato.
RunTimeAttributes
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/RunTimeAttributes)
Consente di definire il significato da attribuire agli attributi video runtime (cioè quei caratteri
esadecimali immessi forzatamente in un campo di Immissione/Emissione di un formato video che nel
flusso di un'emulazione 5250 condizionano la rappresentazione grafica del campo stesso).
Attributo Namespace Valore/Descrizione
Colore di Default del
Subfile
DefaultSubfileBackgroundColor E' il colore (espresso nel form R;G;B) che viene
definito come colore di default per inibire
l'applicazione dei colori di sfondo degli Attributi
Run Time aventi colori di sfondo "non significativi".
Sostituzione Colore di
Default Subfile
SubstituteDefaultSubfileBackgroundColor Yes = Se il colore di sfondo di un Attributo Run
Time è uguale al colore di Default del Subfile, il
colore di sfondo non viene applicato.
No = Il colore di Sfondo di un Attributo Run Time
viene sempre applicato.
Attributo di Default DefaultAttribute E' il codice dell'Attributo Video RunTime da
utilizzare nel caso in cui un campo contenga degli
Attributi Video RunTime ma tali attributi non
comprendono la specifica del primo carattere del
campo stesso. L'attributo di Default viene quindi
automaticamente inserito come l'Attributo Video da
applicare ai primi caratteri.
RunTimeAttributes - Attributi
Questa sezione si trova in : 
(/Application/Module[@Name=Emulator]/RunTimeAttributes/Attributes/Attribute)
E' l'elenco degli attributi video runtime e l'associazione della loro rappresentazione.
Attributo Namespace Valore/Descrizione


Codice @Cod E' il codice (corrispondente alla conversione mediante tabella
ASCII/EBCDIC del carattere esadecimale utilizzato nel buffer video 5250)
dell'attributo video.
FontName @FontName E' il nome del Font da applicare.
Dimensione Carattere @Size E' la dimensione (in punti) del carattere.
Corsivo @Italic Yes = Il carattere viene visualizzato in corsivo.
No = Il carattere non viene visualizzato in corsivo.
Grassetto @Bold Yes = Il carattere viene visualizzato in grassetto.
No = Il carattere non viene visualizzato in grassetto.
Sottolineato @Underline Yes = Il carattere viene visualizzato sottolineato.
No = Il carattere non viene visualizzato sottolineato.
Colore del Carattere @CharacterColor Inserire il colore nel formato R;G;B.
Colore dello Sfondo @BackgroundColor Inserire il colore nel formato R;G;B.
ObjectActions
Questa sezione si trova in : 
(/Application/Module[@Name=Emulator]/ObjectActions/ObjectAction)
Sono le azioni che devono essere "aggiunte" sistematicamente al Popup menu di un oggetto o di un
campo di immissione.
Attributo Namespace Valore/Descrizione
Codice @Codice E' il codice dell'azione utilizzato come riferimento di
identificazione.
Tipo di Azione @Azione Update5250Field = L'azione aggiornerà il contenuto del
campo di immissione 5250 associato.
ExecuteProgram = L'azione provocherà l'esecuzione di
un'azione esterna.
Azione di Default @Default Yes = E' l'azione da richiamare se viene effettuato un click
sull'icona associata.
No = Non è l'azione di default.
Applicabile a Non Oggetti @NoObject Yes = L'azione è valida anche se il campo non è un oggetto.
No = L'azione è valida solo se il campo è un oggetto.

Azione Alternativa Se Campo Vuoto @SeVuoto Immettere il codice dell'azione alternativa da eseguire se il
campo non contiene alcun valore o contiene solo caratteri
speciali di ricerca.
Testo @Testo E' il testo che appare nel popup menu associato e che descrive
l'azione.
Valore 5250 @Valore5250 E' il valore da immettere nel campo 5250 (Valido solo se
@Azione=Update5250Field).
Modalità di Riempimento 5250 @FillMethod5250 Pre = Il Valore5250 viene prefissato al valore eventualmente
già presente nel campo stesso.
Post = Il Valore5250 viene aggiunto al valore eventualmente
già presente nel campo stesso.
Over = Il Valore5250 viene sostituito al valore
eventualmente già presente nel campo stesso.
Enter @Enter5250 Yes = Dopo aver immesso il valore nel campo viene simulata
la pressione del tasto Invio.
No = Non viene simulata la pressione del tasto Invio
(Valido solo se @Azione=Update5250Field).
Tipo @Tipo E' il tipo dell'oggetto se differente da quello associato
(Valido solo se @Azione=ExecuteProgram).
Parametro @Para E' il parametro dell'oggetto se differente da quello associato
(Valido solo se @Azione=ExecuteProgram).
Codice @Codi E' il codicedell'oggetto se differente da quello associato
(Valido solo se @Azione=ExecuteProgram).
Azione @Exec E' la funzione esterna da eseguire
(Valido solo se @Azione=ExecuteProgram).
ErrorMail
Questa sezione si trova in :  (/Application/Module[@Name=Emulator]/ErrorMail)
Definisce l'attivazione delle funzionalità di Logging.
Attributo Namespace Valore/Descrizione
Attivazione Active Yes = Viene inviata una mail nel caso di errori riscontrati nei documenti XML di
definizione dei formati iSeries.
No = Nessuna mail viene inviata in caso di errore.
Mittente Sender E' l'indirizzo e-mail che figura come mittente del messaggio.
Destinatari Recipients E' l'elenco dei destinatari ai quali viene indirizzato il messaggio (separati da punto e
virgola).

Server di Posta SmtpServer E' l'indirizzo del server di posta in uscita che viene utilizzato per l'invio dei messaggi.
Titolo Messaggio Subject E' l'oggetto del messaggio che viene inviato.
