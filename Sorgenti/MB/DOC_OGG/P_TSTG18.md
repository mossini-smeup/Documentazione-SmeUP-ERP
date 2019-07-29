# GESTIONE VISUALIZZATORE

## OBIETTIVI

Visualizzare informazioni in formato video 5250 e gestire eventualmente
l 'esecuzione di azioni previste per ogni riga del subfile, spool di stampa e PDF.

## CONSIDERAZIONI AGGIUNTIVE PER STAMPA E PDF

Essendo nata solo per visualizzare i formati video 5250, vengono qui riportate alcune considerazioni aggiuntive relative alle novità introdotte per la produzione dei formati di file di spool e file PDF.

- Modello X :  con impostato tale modello si può sfruttura la lunghezza fisica massima disponibile per ogni formato :  198 per file di spool, 132 per video 5250, fino a 30000 caratteri per PDF. In questo caso tutti i dati comprese le intestazioni dovranno essere passati attraverso il campo £G18RE che essendo un campo Varying di 30000 caratteri dovrà essere sempre valorizzato con l'istruzione EVAL. Per il passaggio delle intestazioni si veda quando esposto di seguito.
- Stile :  per uniformare lo stile dell'output in funzione del significato dei dati è stato introdotto
il concetto di stile da indicare a livello di £G18CR (si veda quanto riportato di seguito per   il dettaglio). Lo stile a differenza degli attributi video viene preso in considerazione in ogni formato di output. Ciò non toglie che posso cmq utilizzare gli attributi, che a questo punto verrano presi in considerazione solo per i formati di output che li gestiscono.
- Salto Pagina :  Per i formati PRTF, PDF l'informazione relativa all'esecuzione del salto pagina, viene ritornata tramite il campo messaggio valorizzato con "OVF"
- Intestazioni :  Le instestazioni possono essere aggiornate tramite la funzione AGI, questa per i formati PRTF/PDF implica automaticamente il salto pagina. Può perciò essere utilizzata anche solo per questo scopo.
- Informazioni standard :  alcune informazioni standard (utente, sistema informativo, data/ora, numero pagina), possono essere omesse valorizzato la posizione 9 del campo £G18MO.
- Formati dei printer :  vengono assunti questi formati a seconda del modello E=132 caratteri, X=198 caratteri, 80 caratteri per tutto gli altri casi.
- £GPE :  tramite la £GPE ed il relativo comando UP GPE possono essere condizionate anche le modalità di produzione del PDF. Per fare questo in modo corretto nel programma che richiama la £GPE deve essere valorizzato il campo £UDTPS con valore 999.
Inoltre per quel che riguarda le stampe, quest'ultime di default sono in formato AFPDS, ma  nel caso vi sia necessità è possibile passare ad un formato *SCS tramite l'apposita opzione della GPE. Se nel formato video si possono selezionare più formati, quello del PDF va identificato dal codice "7".
- L'ubicazione e la denominazione dei file PDF prodotti :  per i file PDF è previsto un default sia per l'ubicazione che per la denominazione dei file PDF prodotti. Tali default sono sovrascribili tramite il comando UP GPE con la possibilità di poter utilizzare anche variabili d'ambiente (es. &AM.UT).
-- Ubicazione :  vengono posti nella cartella /SMEDOC/UTE/NomeUtente/ il suo utilizzo implica l'attivazione della condivisione della cartella SMEDOC
-- Denominazione File :  NomeProgramma-Lavoro-Data-Ora.PDF
-E possibile anche forzare alcuni parametri da pgm nella chiamata INZ, compilando i campi :  (se compilati sovrascrivono eventuali valori della GPE)
-- £G18P1  :  Tipo Elaborazione (server, client, ecc)
-- £G18P2  :  Formato (A4, A3, ecc)
-- £G18P3  :  Orientamento (H Orizzontale o V verticale)
-- £G18P4  :  Directory File (percorso IFS di destinazione del PDF, ad esempio /PDF/ORDINI/)
-- £G18P5  :  Nome file (nome completo con estensione del PDF, ad esempio PRO_P0900100.pdf)
- Apertura file PDF :  Se l'esecuzione avviene in modo interattivo, alla conclusione dell' elaborazione verrà aperto sia in 5250 che da loocup il file PDF prodotto. Può essere     inibita l'apertura immediata (anche se interattiva) se nella fase di INZ viene valorizzato il campo £G18P0.
- Accesso ai documenti dell'utente :  nella B§1 come azione utente è implementabile il richiamo
al pgm B£UT51I che sia da loocup che da 5250 permette di aprire la cartella standard dell'utente
in modo del tutto simile al quale l'utente accede ai suoi file di spool.
- Modalità di esecuzione del PDF :  nella £GPE è possibile decidere se l'elaborazione del PDF deve essere seguita dal Server (cioè l'AS400) o dal Client (cioè Loocup) quando l'interfaccia grafica è Loocup. Ognuna delle due presenta degli svantaggi/vantaggi che possono essere valutati :  -- Server :  posso lanciare l'elaborazione in batch, posso sfrutture le memorizzazione della GPE, l'aggiornamento del componente di elaborazione del PDF è legato all'aggiornamento del componente SMEDG installato sull'AS.
-- Client :  posso pilotare il formato di stampa (verticale/orizzontale, A4/A3 ecc.), posso  sfruttura le immagini di loocup, l'aggiornamento del componente di elaborazione è legato all'aggiornamento di loocup.
- Immagine Azienda se elaborazione Server :  l'unica immagine utilizzabile se l'elaborazione è di tipo server è l'immagine azienda che viene automaticamente posta in nelle intestazioni sulla sinistra. Per poter essere utilizzata tale immagine deve essere obbligatoriamente posta nella cartella '/SMEDOC/IMG/AZ/' con denominazione CodiceAzienda.jpg
- Test :  tramite l'elemento della tabella PGM B£G18H è possibile condizionare che la produzione del file PDF al solo file .inv che solitamente viene cancellato in post-elaborazione. Per fare questo è necessario indicare il flag "Solo simulazione".
Indicando invece il campo "Stampa Log" per l'elemento B£G53H è possibile avere invece la stampa dello stesso.


## FUNZIONI/METODI

**- INZ/INZE -**
Inizializzazione e pulizia della routine, con definizione del formato di output.
La differenza fra INZ/INZE consiste nel fatto che con la INZE si dichiara l'intenzione
di volte utilizzare la stringa di dati estesa (£G18RE, lunga 30000) più capiente rispetto
alla stringa standard (£G18RI di 132 caratteri), ma che comporta un maggior impiego di risorse.
Nella inizializzazione con metodo PRTF o PDF si possono caricare i campi della £G18DS contenuta nella copy £G18E, per sfruttare alcune funzioni specifiche.
    -       -
Dichiaro che voglio produrre i dati in un video 5250 senza attivazione del DROP.
    - DROP  -
Dichiaro che voglio produrre i dati in un video 5250 con attivazione del DROP.
    - PRTF  -
Dichiaro che voglio produrre un file di spool
    - PDF  -
Dichiaro che voglio produrre un file PDF.
**- WRI -**
Scrittura di una riga del subfile
    - ALL   -
Con il metodo blanks il subfile verrà caricato tutto NON A
PAGINE senza essere presentato
    - blank -
Utilizzato per caricare il subfile A PAGINE, per cui ad ogni
scrittura del sufile si verifica se è stata riempita una pagina ed
in tal caso viene presentata.
    - PRE   -
Ad ogni scrittura seguirà la presentazione attuale del subfile
aggiornata all'ultima scrittura
**- PRE -**
Fine caricamento e presentazione del subfile
    - INI   -
Presenta il subfile posizionandosi sulla prima pagina
    - ULT   -
Presenta il subfile riposizionandolo alla precedente posizione in cui si trovava.
Se si desidera forzare l'attivazione della paginazione in avanti (utile in caso di riposizionamento nel corso di un
caricamento a pagine non completato), occorre valorizzare il campo £G18CM (input solo in questo caso) con il valore
del tasto £PAGEDN (da /copy £KEY).
    - blank-
Presenta il subfile posizionandosi sull'ultima pagina
**- LAS -**
Lettura azione successive (vedi più avanti). E' impostato dalla £G18
    - AGG   -
Aggiornamento della riga elaborata. La riga del subfile viene riscritta utilizzando i dati eventualmente modificati
dalla £G18SR. Questo metodo deve essere impostato dalla subroutine £G18SR presente nel pgm chiamante.
    - AGF -
Aggiorna la riga e alla fine delle azioni restituisce il controllo al programma chiamante (che per esempio potrebbe
aggiornare l'intestazione tramite la funzione AGI).
    - AIG   -
Come AGG con la differenza che vengono aggiornate anche le intestazioni
    - AIF -
Come AGF con la differenza che vengono aggiornate anche le intestazioni
**- FIN  -**
Normalmente dopo la lettura dell'ultima azione viene ripresentato il S/File. Impostando questo metodo (all'interno
della routine £G18SR) dopo la lettura di tutte le azioni il controllo viene invece restituito al programma chiamante.
Un utilizzo può essere il seguente :  una o più azioni forzano la rigenerazione del S/File, con la scrittura di
ulteriori righe successive a quella in cui è stata digitata l'azione, e si vuole che queste azioni abbiano effetto
contemporaneamente.
**- AGI -**
Aggiornamento delle intestazioni. Utile nel caso contengano dei totali.
E' da notare che nel caso il formato di output sia PDF o PRTF, questa funzione implica
il salto pagina.
**- UPD -**
Aggiornamento riga del subfile :  il numero di record del subfile da aggiornare viene impostato nel £G18PO. Il nuovo
valore impostato nel record è la £G18RI corrente.
    - PRE   -
Presenta il subfile dopo l'aggiornamento
**- READ -**
Funzione per la gestione della rilettura del subfile.
    - FIRST -
Legge e restituisce il primo record del subfile.
    - NEXT -
Da utilizzare in un ciclo dopo una READ/FIRST per leggere i successivi record del subfile.
    - *BLANKS -
Legge e restituisce il record impostato nel campo £G18PO.
    - POSI -
Legge e restituisce il primo record dell'ultima pagina visualizzata
Svolge la funzione di chain sul record del subfile.
OSS. Le funzioni UPD e READ ripristinano il n°relativo di record precedente alla loro chiamata.
**- POSI -**
Funzione per il posizionamento (e visualizzazione) del subfile alla riga specificata in £G18PO.
**- PRT  -**
Funzione per la stampa della lista caricata.

## MODELLO

La struttura del modello è la seguente : 
Prima posizione :  modalità di presentazione
- E  esteso :  presentazione subfile in video 27x132. Se il video non supporta questo formato, viene automaticamente assunto il formato successivo. La stampa viene prodotta a 132 caratteri.
- X  massimizzato :  per ogni formato può essere sfruttata la lunghezza massima. Il subfile viene è presentato a 132, la stampa 198, per il PDF si possono utilizzare fino a 30000 caratteri.
E' da tenere conto che in questo caso i dati vanno passati nella stringa estesa £G18RE e che
in questo caso le intestazioni vanno in essa definita come riportato nell'esempio di seguito.
Es. £G18RE='£18I01="xxxxx" £18I02="xxxx"'
- C  completo :  presentazione a tutto schermo in video 24x80
- H  alta intensità :  mostra la riga in alta intensità (se funzione WRI)
Seconda posizione :  campo di posizionamento
- P  viene attivato, in alto a sinistra, il campo di I/O di posizionamento, il cui contenuto viene ritornato al
chiamante, che può decidere se eseguire il riposizionamento in base ad esso.
Si può tipizzare questo campo, in modo da rendere attiva la ricerca alfabetica, impostando, nella funzione 'INZ', il
campo £G18CR (che normalmente ha lo scopo di condizioni di riga) : 
Posiz.  1 -  2 :  tipo oggetto
Posiz.  3 - 12 :  par. oggetto
Questa tipizzazione dell'oggetto non ne implica il controllo formale di esistenza :  si può comunque digitare la radice
del codice.
Terza posizione :  posizione cursore
- C   se in seconda posizione è previsto il campo di posizionamento, il cursore viene posizionato sul campo di
posizionamento, in caso contrario viene invece posizionato sull'opzione.
Nona posizione :  ometti utente/data/ora/sistema informativo/pagina in formato PDF/Printer File.

## AMBIENTE

E' dello stesso tipo di £PDSNP ed è utilizzato nella gestione autorizzazioni.

## SCRIPT/SUFFISSO PDF

Questi campi vengono impiegati sono per la produzione dei PDF e vanno valorizzati quando viene eseguita  la funzione di inizializzazione.
Tramite il primo è possibile utilizzare uno script del file SCP_G53 in sostituzione rispetto a quelli assunti come default.
Tramite il secondo invece è possibile aggiungere uno suffisso che concatenato al nome definito dalla £GPE permette di determinare il nome effettivo del file che verrà prodotto. Questo campo torna utile qualora nella medesima elaborazione si vogliano produrre più file.

## AZIONI AMMESSE

E' una lista di azioni ammesse (max 200) nella gestione del subfile.
La schiera associata deve essere compilata nel pgm che utilizza £G18.
Ogni riga di azione ammessa è così strutturata : 
- 1° e 2° carattere :  codice azione
- 3° carattere :  '='
- dal 4° al 33°  :  descrizione azione
- 34° e 35° carattere :  tipo azione (viene confrontato con il tipo riga)
- 36° e 37° carattere : 
'SC' per azione che può essere solo scelta e quindi eseguibile dal solo programma chiamante.
'ES' per azione eseguibile direttamente dal subfile
'EN' come ES lanciando in un nuovo gruppo di attivazione, per evitare ricorsioni.
- 38° e 39° carattere :  codice di autorizzazione associato all'azione.
La classe di autorizzazione è ABILITA ed è associata all'AMBIENTE !!
- dal 40° al 49°  :  programma associato all'azione
- dal 50° al 59°  :  funzione associato all'azione
- dal 60° al 69°  :  metodo associato all'azione
Programma, funzione e metodo saranno gestiti dalla £FUN
- al 70°  :  Flag che indica l'obbligatorietà del tasto di conferma F06 alla scelta delle opzioni.
- al 71°  :  Flag che imposta il parametro £FUNP4 (es. "M" per impostare la modalità manutenzione per i programmi che lo
prevedono come BRFU01X)
- dal 72° al 74°  :  per reimpostare le chiavi che verranno utilizzate nel richiamo di azioni eseguibili internamente
(funizzate); ad esempio se la funzione richiamata ha come oggetto il secondo (£FUNK2), nella posizione 73 si imposterà
1 per caricare in £FUNK1 il contenuto di £FUNK2; ricordiamo che in std viene eseguita la funizzata con i dati passati
da £FUNDS1 (dati nascosti nel subfile).
ATTENZIONE!! se oltre alle azioni ammesse si vogliono abilitare quelle del flusso (B£H) è necessario aggiungere alle
precedenti azioni la particolare azione "! " per la quale, in luogo della descrizione dell'azione si inserisce il
codice della tabella B£H.

## COMANDI ATTIVI

E' una tasti funzionali ammessi per il subfilelista di azioni ammesse (max 200) nella gestione del subfile.
La schiera associata deve essere compilata nel pgm che utilizza £G18.
Ogni comando ammesso è così strutturato : 
- 1°, 2° e 3° carattere :  tasto funzionale
- 4° carattere :  '='
- dal 5° al 40° descrizione tasto funzionale
- dal 41° al 76° descrizione ridotta del tasto per visualizzazione in prima pagina
- dal 77° al 80° attributo video (vedi codici come da £ATRC) da assegnare al tasto funzionale.
I comandi ammessi, compresi quelli interni alla gestione subfile, sono reperibili attraveso il comando F24, nella
presentazione del subfile.

## INTESTAZIONI

Nella presentazione del subfile sono disponibili 5 righe : 
Prima riga :  titolo
Seconda riga :  sottotitolo
Terza e quarta riga :  libere
Quinta riga :  testata subfile

## CONDIZIONI DI CONTESTO

Caratterizza ogni riga con i parametri della £FUND1 impostati dall'utente, e saranno riportati nei campi nascosti del
subfile.

## RIGA

E' la riga del subfile che sarà scritta. Essendo di 132 caratteri, se la stringa supera i 76 caratteri (limite max
della modalità completa), i restanti saranno inseriti nella riga gestita dal DROP (F08)

## CONDIZIONI DI RIGA

E' possibile definire le caratteristiche di ogni riga mediante la compilazione della variabile £G18CR. Vengono analizzate le posizioni della stringa secondo il criterio seguente.

### "V" Abilitazione della scelta opzioni di riga (1° carattere)
- ' ' se per la riga è consentito il campo OPZIONI
- '1' se per la riga non sono ammesse le OPZIONI

### "Ti" Tipo riga per identificazione opzioni (2° e 3° carattere)

### "A" Azione dopo l'esecuzione dell'azione sulla riga (4° carattere)
- '1' se dopo l'azione impostata nelle posizioni precedenti non si deve emettere il S/File.

### "Str" Struttura della riga (Dal 5° al 7° carattere)
Permette di associare una struttura (tipo griglia di LOOC.up) al fine di consentire la trasformazione di tali righe in matrici e/o in ExCEL

### "Gr" Gruppo di tipi riga (8° e 9° carattere)
 identifica un gruppo di tipi riga per i quali le opzioni sono comuni. Viene impiegato nell'applicazione delle azioni di massa, se valorizzato solo sulle righe che presentano in medesimo gruppo l'azione verra eseguita

### "Sty" Stile (Dal 10° al 12° carattere)
Permette di specificare un tipo riga per caratterizzare in modo standard gli attributi della riga. I codice stili sono così strutturati : 

- 1° Posizione :  Tipo Stile
-- N :  nota
-- L :  riga di livello
-- T :  riga di totale
-- M :  riga di rottura
-- G :  riga di grassetto (valida solo per i printer file interni)
- 2° Posizione :  Livello
-- Assume valore da 1 a 6 ed indica il livello di evidenza dello stile, più il numero è basso più lo stile viene evidenziato.

Per verificarne e funzionamento e possibilità utilizzare i relativi tasti funzionali del TST.

## AZIONE/TIPO

Rappresentano rispettivamente il codice dell'azione scelta nella riga del subfile, e se l'azione è tra quelle ammesse
(tipo = blanks) oppure tra quelle della B£H (tipo = B£H).
