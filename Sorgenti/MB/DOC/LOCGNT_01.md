# Obiettivo
I servizi AS/400 che forniscono dati al componente GNT di LOOC.up hanno l'obiettivo di scrivere in XML tabelle di dati dove esistono almeno delle colonne di data/ora inizio e data/ora fine.
La struttura XML è quella standard delle tabelle
Il componente riordina le attività secondo una chiave e le dispone graficamente nel tempo permettendo tutte le funzioni grafiche tipiche di uno schedulatore
## Come scrivere un programma
I servizi sono caratterizzati dal nome xxGNTnn_y dove
  - xx = applicazione SME.up
  - nn = codice del servizio
  - y  = codice del sottoservizio

Ad esempio lo schedulatore standard SME.up sarà SFGNT01 e avrà i seguenti sottoservizi
  A = Lettura/Scrittura                        -> Crea la memoria
  B = Schedulazione                            -> Modifica il contenuto della memoria
  C = Lista funzioni in POPUP / Setup / Ecc
  D = Indici                                   -> Estrae informazioni dal contenuto
Ogni servizio potrà leggere i dati da posti diversi (usando dove possibile le funzioni SME.up) e fornire tabelle di dati con formati tipici

## Come partire
Potremo partire da un oggetto o richiedere le attività di tutti gli oggetti. Ad esempio se specifico un agente intendo richiedere tutti gli appuntamenti di quell'agente oppure gli appuntamenti di tutti gli agenti.

## Cosa posso chiamare dal GANTT
All'interno del GANTT, possiamo avere le seguenti categorie di funzioni
### Funzioni proprie del componente
  OPN - Carica la memoria
  WRI - Salva le modifiche eseguite
  CLO - Chiude il servizio
  MOD - Indica la modifica di una riga
### Passaggio ad altre funzioni di LOOC.up
  - Schede degli oggetti (risorse/articoli/Commesse/Ecc.)
  - Accessi all'emulazione 5250
### Funzioni associate ad eventi grafici
  - Spostamento di una attività nel tempo
  - Cambio di risorsa e spostamento
### Funzioni che restano all'interno del servizio stesso
  - Matrice degli indicatori per commessa
  - Schedulazione (in memoria) di un centro.
  Queste sono caratterizzate dal bollino azzurro
## Come estendere le funzioni

## Come applicare le logiche specifiche di schedulazione
Il programma di schedulazione può implementare le logiche desiderate leggendo i dati del sistema, utilizzando script specifici ecc.
Essendo isolato può essere personalizzato facilmente

## Ulteriori funzioni
### Disegno griglia di sfondo da istante a istante (singola cella o intero Gantt)
Per migliorare la lettura del Gantt e' possibile inserire una griglia di sfondo per marcare alcune aree
o segnalare l'aggregazione di alcune celle.

Si possono specificare tre tipi di griglie di sfondo : 
![03COMGNT01](http://localhost:3000/immagini/LOCGNT_01/03COMGNT01.png)Lo sfondo a livello di Gantt serve per evidenziare dei periodi temporali fissi e indipendenti dalle
attivita', esempio i periodi di chiusura per festivita' o semplicemente perche' ore notturne.
![03COMGNT02](http://localhost:3000/immagini/LOCGNT_01/03COMGNT02.png)E' possibile abilitare uno sfondo che comprenda tutte le attivita' che hanno la stessa chiave di
raggruppamento, cosi' e' possibile rendere piu' evidente il legame che unisce un gruppo di attivita'.
![03COMGNT03](http://localhost:3000/immagini/LOCGNT_01/03COMGNT03.png)Per ogni singola riga si possono specificare una serie di intervalli che prenderanno uno sfondo
particolare.

### Possibilita' di definire i colori a livello AS
Le attivita' all'interno del Gantt sono rappresentate da riquadri colorati, e' possibile specificare il colore
di queste celle affinche' tutto il grafico sia piu' facilmente interpretabile.

### Attivazione riquadro che cattura e passa ad AS un insieme di celle
All'interno della visualizzazione del GANTT c'e' la possibilità di selezionare piu' celle attraverso due
strumenti : 

- Seleziona attivita'
- Seleziona intervalli di tempo

![03COMGNT04](http://localhost:3000/immagini/LOCGNT_01/03COMGNT04.png)Tramite il selettore di intervalli di tempo si possono selezionare attivita' slot disegnando un riquadro
rettangolare all'interno del Gantt. Tutte le celle nel riquadro verranno selezionate, anche le celle
selezionate parzialmente. Il selettore di attivita' permette invece di selezionare piu' attivita' tenendo
premuto il tasto shift e cliccando una volta su di esse.
Se le attivita' selezionate sono temporalmente contigue allora si possono raggruppare in un gruppo
temporaneo attraverso il tasto 'Crea Gruppo temporaneo'.
![03COMGNT05](http://localhost:3000/immagini/LOCGNT_01/03COMGNT05.png)Per sciogliere un gruppo temporaneo e' sufficiente cliccare su un'attività del gruppo col tasto destro
e scegliere dal menu' 'azioni su gruppi temporanei' la voce appropriata.
![03COMGNT06](http://localhost:3000/immagini/LOCGNT_01/03COMGNT06.png)La selezione multipla di attivita' puo' essere disabilitata nel caso i programmi non siano allineati alla
versione dello schedulatore grafico.
