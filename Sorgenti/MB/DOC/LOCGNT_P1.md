# Servizio su AS/400
# Componente grafico
## Versione 1
Primo rilascio del modulo schedulatore.
Funzioni di base

- Visualizzazione delle attività su asse temporale
- Raggruppamento per chiave
- Associazione automatica colore per chiave
- Associazione chiave per testo
- Spostamento e resize delle celle (solo grafico, senza salvataggio)
## Versione 2

- (DF) Applicazione effettiva delle modifiche (scrittura su AS/400)
- (DF) Evidenziazione attività modificate
- (DF) Funzioni di ottimizzazione della visualizzazione di pagina e di riga
- (DF) Visualizzazione delle date di fine richiesta e di fine schedulata.
- (DF) Attività con visualizzazione a livelli.
- (DF) Gestione di base dei messaggi di errore (da completare)
- (DF) Integrata gestione richieste a programmi di tipo 5250 (richieste di tipo R)
- (DF) Stampa (solo pagina corrente, come visualizzata da schermo)

## Versione 3

- (DF) Gestione dei filtri di visualizzazione
- (DF) Esportazione verso tabella
- (DF) Esportazione verso Excel (da sistemare)
- (DF) Gestione delle viste
- (DF) Persistenza dei colori (da completare)
- (DF) Identificazione del modulo grafico di schedulazione con il nome Fine.Up
- (DF) Visualizzazione on/off dell header con tasto F20

## Versione 4


- (DF) Separazione dei filtri in filtro di visualizzazione e filtro dati.
- (DF) Possibilità di attivare un filtro anche dal menù di popup associato ad una attività
- (DF) Migliorata la gestione dei colori.
- (DF) Migliorata la gestione delle viste. Definita la vista di default.
- (DF) Migliore gestione del reload alla pressione del tasto F5. Le modifiche non vengono più perse.
- (DF) Primo abbozzo di carrello per gestione delle operazioni su attività multiple.

## Versione 5 (13 ottobre 2004)


- (DF) Corretto errore di visualizzazione delle note associate ad una attività.  Le note mostrate in alcuni casi
erano riferite ad una attività diversa da quella selezionata.
- (DF) Inserita nuova chiave di Flag. Permette di attivare un marcatore grafico sulla cella utile per segnalare
una particolare condizione operativa della attività rappresentata dalla cella stessa. Ad esempio,
consente di marcare le celle che hanno una nota associata.

## Versione 6 (25 novembre 2004)


- (DF) Inserita la possibilità di attivare/disattivare il salvataggio, lo spostamento e il resize degli impegni.
- (DF) Possibilità di definire da XML il colore del marcatore di flag
- (DF) Visualizzazione automatica dei messaggi in funzione del livello di gravità (modifica temporanea
in attesa che sia pronta la gestione messaggi a livello globale).
- (DF) Migliorata la gestione del refresh dello schedulatore dopo l'applicazone delle modifiche.

## Versione 7 (3 dicembre 2004)


- (DF) Gestione dei messaggi di modifica di tipo MOD (modifica delle celle esistenti) e di tipo NEW (cancellazione
dele celle esistenti e loro sostituzione con quelle passate)
- (DF) E' possibile forzare la partenza dello schedulatore con tutti i gruppi espansi
- (DF) Possibilità di definire un flag di evidenziazione su tutti e quattro gli angoli della cella dell'impegno.

## Versione 8 (10 dicembre 2004)


- (DF) Modificata la parte di setup del XML del Gantt. Ora è stata allineata al formato
usato anche per altri moduli
- (DF) Nuova tipologia di istanti. Inserita la possibilità di identificare istanti di tempo con un
marcatore grafico a forma di freccia (dx o sinistra). Il meccanismo è una estensione
del campo D00R e D00S
- (DF) Migliorata la gestione di messaggi (anche se non è ancora in forma
definitiva)
-(DF) Corretto passaggio da visione per gruppo a visione per dettaglio. Nel passaggio
venivano perse alcune delle informazioni di base, passate nel XML originario.
-(DF) Inserita la possibilità di disattivare da XML alcune funzioni dello schedulatore : 
In particolare : 

* Possibilità di disabilitare la modalità dispostamento delle celle
* Possibilità di disattivare la modalità di ridimensionamento delle celle
* Possibilità di disattivare il SAVE su As/400 all'uscita dello schedulatore
* Possibilità di disattivare la funzione di dettaglio di un gruppo

## Versione 9 (17 dicembre 2004)


-(DF) Nuove forme per rappresentazione grafica delle celle del Gantt.
Inserito nuova chiave S01 che definisce il campo da utilizzare come
chiave di forma.
A seconda del valore, la cella viene disegnata con una forma diversa.
Tabella forme : 

S01 = 0 Cella rettangolare standard (default)

S01 = 1 Cella ovale

S01 = 2 Cella rettangolare con angoli arrotondati

S01 = 3 Cella a rombo

S01 = 4 Cella triangolare crescente

S01 = 5 Cella triangolare decrescente


-(DF) Nuovo flag di setup per attivare/disattivare la visualizzazione del
pannello di header. Di default la visualizzazione è disabilitata.

-(DF) Corretto la gestione della richiesta interna di dettaglio. Ora
al Gantt di dettaglio vengono passati tutti i valori e i campi corretti.

## Versione 9 bis (20 dicembre 2004)


- (DF) Modificata rappresentazione grafica multiforma. Ora le
celle mostrano sempre il rettangolo del contorno, anche
quando non sono rettangolari

-(DF) Nuovo indicatore di tempo legato alla coppia di flag D00T e H00T.
L'indicatore ha per default il colore verde e forma a freccia destra.

## Versione 10 (21 dicembre 2004)


Esteso il meccanismo di definizione degli istanti di tempo da
visualizzare graficamente nelle righe di dettaglio.
Adesso il numero di istanti di tempo definibili è libero e
definito dalle chiavi impostate nella definizione della griglia.

Per definire un singolo istante di tempo è necessario
definire una tripletta di chiavi : 

D00? = Identifica la colonna che contiene la data (obbligatorio)

H00? = identifica la colonna che contiene l'ora esatta

F00? = identifica la colonna che contiene il formato

Il carattere ? può essere un qualsiasi carattere alfanumerico e deve essere
lo stesso per le tre chiavi (ad esempio, D00R, H00R e F00R per identificare
le colonne che definiscono un istante R). Il carattere usato nella
posizione ? rappresenta il codice identificativo dell'istante
di tempo che si sta definendo.

Il campo F00? identifica il formato del segnatempo grafico ed
è composto da due caratteri : 


F00? = XY

dove : 

X = codice forma del segnatempo

0 per rombo
1 per rettangolo
2 per cerchio
3 per freccia con punta a destra (default)
4 per freccia con punta a sinistra

Y = codice colore del segnatempo

1 per giallo
2 per verde
3 per blu
4 per bianco
5 per nero
6 per ciano
7 per rosso (default)
8 per grigio
9 per arancio

## Versione 10 (11 gennaio 2005)


-(DF) Gestione delle note associate ad un impegno. E' stata creata una
nuova chiave N01 che identifica il campo contenitore delle note.
Gli impegni che hanno delle note associate sono visualizzati con
una piccola icona che identifica la presenza delle nota.

-(DF) Possibilità di avviare il Gantt con la modalità di resize o di
move abilitate di default.

-(DF) Corretta la visualizzazione delle note associate ad un oggetto.
In alcuni casi (impegni visualizzati nella parte centrale del componente
grafico) la nota finiva al di fuori dello schermo e diventava di fatto
non leggibile. Introdotto un controllo più sofisticato sul posizionamento
della finestra delle note. Permangono invece i malfunzionamenti per
finestre delle note visualizzate su impegni che occupano le posizioni
centrali dello schermo (sfarfalio e errore nella visualizzazione del
contenuto delle note)

## Versione 11 (12 gennaio 2005)


-(DF) E' ora possibile dichiarare alcune colonne come "hidden". Le
colonne hidden vengono lette dallo schedulatore e memorizzate a
livello dati ma non sono visualizzate nell'interfaccia grafica. Le
colonne hidden sono usate per passare allo schedulatore dei
dati necessari alla sua definizione ma che non hanno alcun
significato per l'utente. Le colonne hidden non possono nemmeno
essere usate come chiave di raggruppamento o come chiave per
i filtri di visualizzazione. Possono però essere usate come chiave
colore o chiave testo per l'impegno.

## Versione 12 (15 gennaio 2005)


-(DF) Inserita la possibilità di settare da XML la tipologia di
reggruppamento degli impegni. Sono state inserite tre
nuove modalita'

1) visualizzazione del dettaglio e del riepilogo di gruppo
2) visualizzazione del solo riepilogo di gruppo
3) visualizzazione delle sole righe di dettaglio

Il set puo' essere fatto solo da XMl iniziale. In futuro è
prevista la possibilità di modificare al volo la modalita'
di visualizzazione.

## Versione 13 (28 gennaio 2005)


-(DF) Corretto problema su apertura albero del Gantt forzata
da XML. Se il numero di gruppi era pari a uno l'apertura non
avveniva.
-(DF) Corretto malfunzionamento del refresh del grafico in
uscita da un popup. Se il popup veniva chiuso con il tasto
ESC, spariva l'impegno associato all'impegno su cui si era
premuto il mouse (problema segnalato da SIL)
-(DF) Nuovi tipi di indicatori di istante di tempo. I tipi inseriti sono
la doppia freccia a destra, la doppia freccia a sinistra, la tripla
freccia a destra, la tripla freccia a sinistra, la freccia con punta
in alto e la freccia con punta in basso. I nuovi codici forma
definiti sono 5, 6, 7, 8, 9, A.
-(DF) Inserito nella toolbar un nuovo bottone per la cancellazione
rapida di tutti i filtri. Il bottone azzera sia il filtro sui dati che il filtro
di visualizzazione.

## Versione 13.1 (5 marzo 2005)


-(DF) Corretto problema di gestione delle finestre. In alcune condizioni
particolari il Gantt si apriva in secondo piano rispetto alla scheda  da cui
era stato richiesto. La correzione ha richiesto anche delle modifiche alla
parte della scheda.

## Versione 14 (2 maggio 2005)


-(DF) Corretto errore di memoria esaurita su richiamo multiplo del Gantt. La
 correzione ha richiesto modifiche al meccanismo di base di gestione della
 memoria con conseguente miglioramento delle prestazioni di tutti i componenti
 grafici complessi.
-(DF) Corretto errore su gestione delle note. Se si dichiarava un campo come
 contenitore di note e lo si lasciava vuoto il gantt andava in errore e creava delle
 visualizzazioni senza senso.

## Versione 15 (13 maggio 2005)


-(DF) Gestione memorizzaizone chiavi di ordinamento. In caso di "raggruppa per" la
lista di celle viene riordinata per la chiave. Le successive operazioni si raggruppamento
andranno ad operare sulla lista ordinata. In questo modo si ha una memoria delle
operazioni di ordinamento effettuate. In pratica, le celle sono visualizzate ordinate e
raggruppate per la chiave attuale, il contenuto di un gruppo è ordinato per la chiave
k-1, k-2 ecc. ecc.

## Versione 16 (16 maggio 2005)


- (DF) Migliorata sensibilmente la gestione della stampa. Ora è possibile estendere la
stampa su più pagine e quindi avere un maggiore dettaglio e più possibilità di
controllo sull'output. Rimane ancora il limite di poter stampare solo quello che si vede
a schermo e non in base ad un intervallo di tempo prefissato.

## Versione 17 (25 maggio 2005)


- (DF) Inserito mantenimento delle impostazioni di visualizzazione sul refresh del gantt.
Qunado si preme il tasto F5 vengono memorizzate le impostazioni di visualizzazione attive
al momento della richiesta e vengono applicate al gantt dopo che è stato ricaricato.

- (DF) Nuovi menù di popup scrollabili. I menu di popup che contengono molte voci in
precedenza finivano fuori schermo e rendevano quindi non selezionabili alcune delle
voci del menu. Ora è stato creato un nuovo componente di popup che consente lo
scrolling e quindi in grado di gestire popup anche più grandi dello schermo.
