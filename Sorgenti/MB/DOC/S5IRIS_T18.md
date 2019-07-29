# NEWS
In questo documento sono registrate le modifiche eseguite nella schedulazione BCD.
Ricordo che ad ogni modifica della memoria (£S5SMDS) dovranno essere ricompilati tutti i programmi personaili di BCD.
Quando si modifica la memoria viene sempre modificato il pgm S5SMES_31 (di rappresentazione della memoria con £G11.

##  Data 05.07.06
1) Modificata memoria DSDEGR :  aggiunte data e ora fine attrezzaggio (per ora non calcolate)

2) Modificata memoria DSRISO :  aggiunti n.impegni in corso e n.impegni schedulati.
Vengono calcolati sia per la risorsa generale sia per la risorsa specifica (se diversa) e sono presentati nella scheda della schedulazione
Pgm :  S5SMES_20, S5SMES_D3

##  Data 11.07.06
Nel formato di impostazioni del dettaglio del gantt (accessibile con F17 da una zona libera) è stata aggiunta la possibilità di ingresso bloccato.
Se impostato questo campo, è necessario attivare esplicitamente la possibilità di spostamento all'ingresso di ogni sessione.

##  Data 13.07.06
Nel formato di impostazioni del dettaglio del gantt (accessibile con F17 da una zona libera) è stata aggiunta la possibilità di ingresso chiuso.
Se impostato questo campo, all'ingresso di ogni sessione, per ogni risorsa del gruppo viene presentata soltanto la riga riassuntiva.
E' possibile espanderla con il tasto  nel piede della finestra.
Ricordo che comunque le azioni sulla cella (spostamento, forzatura e congelamento) si possono esreguire anche sulla riga riassuntiva.

##  Data 13.07.06
E' stata realizzata una scheda di analisi della memoria, richiamabile dalla scheda di lista risorse.
In essa è possibile presentare le varie DS della memoria, scegliendo un puntatore (campo preceduto da un punto) si presenta. in verticale, la lista di tutti i campi dell'elemento di memoria individuato dal puntatore stesso.
Inoltre, scegliendo l'oggetto intestatario della schedulazione (ordine di preoduzione, riga di ciclo esterno, collo) si passa alla presentazione di una scheda in cui è riportato, per l'elemento scelto, l'insieme degli elememnti di memoria che lo descrivono (impegni, alternative, dettagli) con evidenziati i legami tra di essi.
E' possibile inoltre accedere ad una lista di statistiche, che riporta il riempimento di tutte le DS
della memoria.
Particolare attenzione va prestata ai primi due campi :  numero di righe schedulate e numero impegni.
Se non sono uguali (il secondo è maggiore del primo) è presente qualche errore nella consecutività del ciclo dell'ordine, per cui alcuni impegni non sono stati resi attivi. Ciò nmormalmente è dovuto ad un'errata impostazione degli impegni in corso :  su di essi deve essere presente la risorsa specifica su cui sono in esecuzione :  se non è così non è possibile determinare dove eseguirli, e e quindi il ciclo si interrompe.
E' possibile inoltre ottenere l'analisi della memoria anche della situazione iniziale. Ciò può risultare utile qualora il tempo di schedulazione sia lungo, oppure quando l'elaborazione termina in modo anomalo e quindi non si piò accedere alla scheda della memoria finale.
Per ottenere questo comportamento si deve : 
- modificare lo script nella parte di presentazione memoria iniziale conformemente a quanto presente
  nello script INT di SMEDEV
- inserire un elemento di BCD simile a FIN, impostando nella classe di esecuzione 'MI'
Lanciando la BCD con questo elemento, viene presentata la scheda della memoria come si presenta dopo che è stata caricata ma prima di aver eseguito qualsiasi passo di schedulazione.
Da questa scheda l'unica prosecuzione permessa è l'uscita dalla schedulazione.
Ricordo che per questa modifica è necessario installare l'ultima versione di B£BCD02 (operazione che è buona norma eseguire ad ogni nuovo rilascio di BCD.

##  Data 17.07.06
Sono stati introdotti alcuni migliramenti relativi all'attrezzaggio, guidati da impostazioni dello script di parametri, unicamente per le risorse a capacità finita.
Queste modifiche hanno comportato modifiche alle DS di memoria, quindi tutti i programmi personali o Si può impostare di calcolare la data/ora di fine attrezzaggio. Questo calcolo è reso opzionale, in personalizzati vanno ricompilati.
E' possibile eseguire l'exit (S5SMX_04y, dove y è un carattere impostato nello script di parametri) che permette di calcolare il tempo di attrezzaggio in modo personale.
A tal scopo è stato introdotto nella DS di dettaglio il campo attrezzaggio effettivo, che viene inizializzato al valore presente nel ciclo.
Nel programma di exit (che riceve il puntatore al dettaglio da schedulare) si puo modificare questo valore, che verrà successivamente utilizzato per schedulare la fase.
E' facilmente determinabile l'articolo trattato immediatamente prima sulla risorsa specifica, e determinare il tempo di attrezzaggio in base alle comunanze tra i due. Nell'esempio riportato si azzera il tempo di attrezzaggio effettito (XGHATR) se l'articolo da lavorare è lo stesso di quello precedente. Si possono realizzare anche comportamenti più sofisticati (per ora implementabili come personalizzazioni), quali la realizzazione di matrici di attezzaggio (l'attrezzaggio è composto da una somma di tempi ciascuno dei quali dipende da una coppia di caratteristiche dell'articolo lavorato e da quello da lavorare).

Si può impostare di calcolare la data/ora di fine attrezzaggio. Questo calcolo è reso opzionale, in quanto può non interessare, nel qual caso costituirebbe un inutile appesantimento. Esso viene eseguito se l'operazione non è iniziata e se il tempo di attrezzaggio è valorizzato.
Se è presente la fine attrezzaggio, nei GANTT viene evidenziata con una linea vericale all'interno della casella dell'operazione schedulata.
La data e ora di fine attrezzaggio vengono memorizzate ni campi Data/Ora Istante 1 dell'archivio S5IRIS0F, in cui è stata modificata la descrizione.
Oltre ai GANTT della BCD, è stat modificato il servizio S5SER_02 per presentare queste informazioni.

##  Data 17.07.06
Sono stati apportati miglioramenti alla comprensione della navigazione.
In particolare, in caso di alternative di ciclo NON gestite, è stata sostituita la voce "gruppo" con la decodifica del Tipo Risorsa Principale (ad esempio "Centro di lavoro"). Questa sostituzione è stata effettuata in tutti i punti dove compariva :  nelle colonne della matrice iniziale, nelle voci di popup e nel titolo del GANTT. Inoltre nel caso di GANTT relativo alla risorsa principale (ex GANTT di gruppo), nel titolo del GANTT stesso è stata aggiunta la decodifica della risorsa principale interessata (es. Centro di lavoro CDL01 - Centro per trattamento termico).

##  Data 17.07.06
E' stata modificata la definizione della tabella S5X (che fornisce i campi al £G30 di richiesta dati di lancio BCD) :  lo stato minimo ordini produzione è stato corretto da TA B£WP5 a TA B£WOP.

##  Data 17.07.06
Si può impostare una strategia di 'tiro', vale a dire, dopo aver schedulato un'impegno su una risorsa specifica, accodarvi altri impegni eseguibili sulla stessa risorsa, con comunanze con l'operazione schedulata (stesso articolo, attrezzaggio breve, ecc...), ed eventualmente all'interno di un determinato orizzonte temporale (per ottenere un compromesso tra la riduzione dell'attrezzaggio e l'eccessivo anticipo degli imepgni.
E' possibile eseguire l'exit (S5SMX_03y, dove y è un carattere impostato nello script di parametri) che riceve il puntatore all'ultimo dettagio eseguito, e torna quello successivo da schedulare.
Questa exit viene richiamata con l'ultimo punttatore che ha restituito, fino a quando torna un puntatore a zero. Essa inoltre viene richiamata a partire dal confine della zona iniziata + congelata, quindi opera in una zona libera.
Questa exit deve eseguire unicamente una scelta :  è compito della parte standard che la richiama schedulare l'operazione.
Nel dettaglio è stato aggiunto un flag valorizzato per gli impegni schdulati in 'tiro'.

##  Data 20.07.06
La normale strategia di sequenziazione in presenza di puù risorse specifiche è quella di scegliere la più scarica (quindi di scegliere un dettaglio, vale a dire una coppia impegno/risorsa).
E' possibile eseguire l'exit (S5SMX_05y, dove y è un carattere impostato nello script di parametri) che riceve il puntatore del dettaglio selezionato. In questo programma si può scegilere di eseguire un altro dettaglio (ad esempio lo stesso impegno su un'altra risorsa), vale a dire si decide quale dettaglio 'spingere' verso la risorsa.

##  Data 20.07.06
E' possibile, in presenza di risorse specifiche, per ogni articolo/fase, inserire un sottoinsieme di risorse specifiche appartenenti alla risorsa principale, all'interno del quale la schedulazione opererà la scelta.
Per attivare quresto comportamento si imposta il flag opportuno nello script dei parametri.
L'informazione del set delle risorse specifiche viene inserito come risorsa secondaria.
Si definisce un tipo risorsa GRM, tra i cui parametri (categoria in tabella BRM), si definisce un parametro multiplo in cui si inseriscono le macchine del gruppo.
Si definiscono i seguenti tipi risorse secondarie (tabella BRK)  : 
- GRM (gruppo) codice 3 :  RI/GRM
- MAC (macchina) codice 3 :  RI/MAC
che vanno inserite in due elementi di B£J della B£H degli sviluppi di fase (A-F2 + eventuale tipo ciclo).
Questi elementi devono avere come pgm BRBRG_10 e come paramenti aggiuntivi : 
RPSA/F0208MAC e RPSA/F0208GRM
La parte di consolidamento dello sviluppo delle risorse secondarie è per ora in test, nella libreria P_RS. In essa è contenuto l'archivio S5IRSE0F (con i suoi logici) che contiene lo sviluppo delle risorse secondarie legate ad un record di S5IRIS.
Per popolarlo, si deve impostare, in tabella P5S, il campo 'Suffisso agg.ris.sec.'.
Se impostato, nella costruzione degli impegni risorse viene lanciato il programma S5FUSEC_x.
Attualmente è stato realizzato il programma S5FUSEC_A che, se presente un gupoo macchine (esplicito o implicito) scrive un record per ogni macchina, con tipo risorsa 'RISP', eseguendo la risalita ordine / articolo / gruppo ciclo / operazione.
Questo archivio costituisce il filtro delle risorse specifiche per la schedulazione.
Ricordo che, all'interno del Gantt di schedulazione, è possibile spostare l'operazione su tutte le risorse specifiche del centro di lavoro, anche se non appartenenti al sottoinsieme impostato.

##  Data 20.07.06
Si possono manipolare le informazioni riportate nei vari GANTT della schedulazione, tramite l'exit S5SMX_06y, dove y è un carattere impostato nello script di parametri.
Questo programma riceve all'inzio la grigia, e ad ogni riga la stringa che sta per passare ed il puntatore del dettaglio.
Si possono aggiungere informazioni, semplicemente accodando la griglia ed i campi, oppure modificare l'esistente (ad esempio cambiando il campo presentato nella cella, nascondendo un campo, ecc...).
E' possibile, estremizzando, ristrutturare completamente la matrice, sostituendo la griglia e ricostruendo la stringa.

##  Data 21.07.06
E' stata estesa la DS degli impegni materiali (DSIRIS) con il puntatore al dettaglio schedulato per quell'impegno.

##  Data 24.07.06
E' stata estesa la DS delle sintesi ordini (DSSINT) con il seguente campo (di sviluppo futuro, per collegamento con l'analisi materiali).
- situazione materiali, che varrà  (oggetto V2/S5_CM)
  '1' copertura totale con fonti presenti
  '2' copertura totale con fonti future
  '3' copertura parziale
  '4' copertura nulla
  '5' materiali non richiesti
  '8' ordine non schedulato
  '9' errore nel gruppo fonti
e con il campo puntatore al primo materiale

##  Data 02.08.06
E' stata implementata la schdulazione delle operazioni a capacità infinita, con il seguente schema : 

Operazioni iniziate
. se impostate ore di carico avanza con queste ore
. se non impostate avanza con la coda
l'operazione è schedulata dall'inizio della schedulazione alla fine dell'avanzamento

Operazioni non iniziate
. se coda assente
--> avanza con le ore di carico :  l'operazione è schedulata dall'inizio alla fine del carico
. se coda presente
--> se ore di carico assenti avanza con la coda :  l'operazione è schedulata dall'inizio alla fine della coda
--> se ore di carico presenti avanza con la coda e con il carico :  l'operazione è schedulata dalla fine della coda alla fine del carico

In generale, se non impostate le ore di carico (normalmente nelle operazioni esterne) si considera che il carico sia rappresentato dalla coda.
Come carico si potrebbe utilizzare anche l'attesa successiva, ma essa è in ore solari, mentre la coda è calcolata con il calendario della risorsa principale, e può essere espressa anche in giorni.

##  Data 07.09.06
E' possibile dalla matrice di ingresso della schedulazione, passare al gantt di tutti i centri (totale) che verrà presentato 'chiuso' (una riga per ogni risorsa specifica, indipendentemente dalla scelta di impostazione).
Ricordo che è possibile eseguire le azioni di spostamento anche sul gantt chiuao :  viene controllato che esso venga eseguito su una risorsa specifica della stessa risorsa generale.

##  Data 08.09.06
E' stata estesa la DS delle sintesi ordini (DSSINT) con il seguente campo (di sviluppo futuro) con il campo puntatore all'assieme (per sviluppi futuri)

##  Data 12.09.06 e 13.09.06
Sono stati apportati miglioramenti alla comprensione della navigazione.
In particolare è stata sostituita la voce "risorsa" con la decodifica del Tipo Risorsa Specifica (ad esempio "Macchina"). Questa sostituzione è stata effettuata in tutti i punti dove compariva :  nelle colonne della matrice iniziale, nelle voci di popup e nel titolo del GANTT. Inoltre nel caso di GANTT relativo alla risorsa specifica (ex GANTT risorsa), nel titolo del GANTT stesso è stata aggiunta la decodifica della risorsa specifica interessata (es. Macchina RI0030 - Fresa Alesa).
E' stata inoltre corretta l'intestazione del GANTT code risorsa o gruppo risorsa nel caso di code assenti.
Infine nell'intestazione del GANTT odine è stata inserita la decodifica dell'ordine interessato.

##  Data 10.11.06
Sono stati aggiunti i seguenti comportamenti, settando opprtunamente lo script dei parametri : 
- Programma di aggiustamento della scrittura del gantt di dettaglio (con possibilità di aggiungere o di nscondere campi nel post -it, di aggiungere righe verticali ad un istante di tempo, ecc ...
- Determinazione stato materiali degli ordini schedulati. Si imposta un gruppo fonti. e si definiscono, come programmi di visualizzazione (in fondo allo script dei parametri) la scheda
copertura ordini (D4SW) e/o la scheda fattibilità impegni (D4SY)
- Efficienza anche per risorsa specifica (sia per il carico sia per l'attrezzaggio).
- Memorizzazione di un Setup utente, impostando il nome della memorizzazione stessa che andrà salvata all'inerno del gantt.
- Ammettere lo spostamento tra risorse specifiche solo su quelle abilitate nelle risorse secondarie.
- Laniciare un programma di emulazione, dal popup di una cella del gantt risorse, passamdogli l'IDOJ della cella stessa.

E' stata attivata la presentazione incolonnata, alternativa al gantt, con possibilità di switchare tra le due, e di impostare la forma di ingresso.
E' inoltre attivato (in entrambe le forme) lo spostamento relativo :  spostando una cella A sulla riga di una cella B, si ha l'effetto che la cella A sarà posizionata immediatamente prima o dopo la cella B, a seconda che la si metta a sinista a destra di quest'ultima.
Spostandola dopo l'ultima cella di un'altra risorsa specifica, si ha l'effetto che verrà forzata su questa risorsa specifica.

E' stata attivata la presentazione degl errori non bloccanti. Nella scheda di riepilogo, se ve ne sono, si presenta un bottone che permette di accedere alla matrice che li presenta.
Ad oggo sono stati intercettati i seguenti errori non bloccanti : 
- risorsa secondaria non apaprtenente alle risorse specifiche della generale (si elimina il vincolo)
- erroe nella determinazione della data/ora fine di una fase (dovuto ad un errore del calendario (si assume la fime uguale all'inizio)
- deadlock tra le fasi, se si assegna ad una fase precedente ad una congelata, la stessa risorsa specifica (inserendola come risorsa secondaria). Si ha una risorsa forzata prima di una congelata, con impossibilità di schedularle (la coda deve esaurire la parte congelata, ma non può farlo in quanto ce n'è una che non diventerà mai pronta, essendo preceduta da una fase solo forzata, che a sua volta non verrà mai schedulata, poichà la parte congelata non si svuota).
Si toglie implicitamente il comgelamento alla fase successiva.

E' stata estesa la gestione dei colori nei gantt, che si basa sul campo ZZCOLO.
Nello standard è riempito con la risorsa specifica se assente controllo materiali (gruppo fonti a blanks nello script), mentre se essa è presente, si utilizza la seguente corrispondenza : 

  Stato manteriali                               Codice colore
  '1' copertura totale con fonti presenti        1
  '2' copertura totale con fonti future          2
  '3' copertura parziale                         3
  '4' copertura nulla                            3
  '5' materiali non richiesti                    1
  '8' ordine non schedulato                      3
  '9' errore nel gruppo fonti                    3

Questo valore è modificabile nel programma di aggiustamento del postit, che può modificare la stringa £JAXCP, nella quale li colore è l'ultimo campo di questa stringa, non ancora chiuso con il pipe.
Si può quindi sia, in presenza di controllo materiali, modificare la precedente tabella di corrispondenza, sia, in ogno caso, scegliere l'oggetto di discriminazione del colore.

- Programma di aggiustamento delle alternative. Si può modificare il contenuto della DS (tempi..)
Si può anche modificare il contenuto della DSIRIS.


##  Data 23.11.06
- Programma di aggiustamento dopo aver memorizzato S5IRIS. Svolge le funzioni di un flusso di postmodifica. Non è stato attivato il flusso perchè non si avrebbe a disposizione la memoria della schedulazione.


##  Data 07.12.06
- Modificata memoria DSSINT :  aggiunti campi per appuntamenti statici
- Nuova memoria DSLEGA per appuntamenti statici
Le DS modificate sono £S5SMDS / £S5SMPI / £S5SMPO
E' necessario ricompliare tutti i programmi di exit.
- Aggiunto in £BCDDS1 campo puntatore associato, che contiene in ogni momento l'ultimo dettaglio schedulato. E' necessario aggiornare tutti i prmgrammi B£BCDxx.


##  Data 11.12.06
E' stata realizzata la funzione di appuntamenti statici, che permette di passare alla schedulazione legami di precedenza tra ordini.
per questa funzione sono state realizzate 3 repliche ai programmi S5SMES_07 e S5SMES_13 (definite, come al solito, in B£DP01). Assicunarsi che esse siano presenti).
Per un'esposizione completa della funzione, si rimanda alla documuentazione attiva dell'applicazione S5 (all'interno del capitolo 'documentazione specifica per modulo/ soluzioni particolari').


##  Data 18.12.06
Sono stati apportati vari miglioramenti ai programmi che rimangono in attesa sullla coda.
I programmi in questione sono stati "puliti" :  i cicli di attesa vengono effettuati mediante il richiamo di opportune /COPY.
In questo modo alla chiusura di loocup vengono chiusi anche i lavori LO_T.
Inoltre adesso funziona correttamente il cambio ambiente.
Per poter usufruire di questi miglioramenti, è necessario avere aggiornati (oltre ai programmi in BCDSRC) i programmi JAJAS1, JAJAS2 e le seguenti /COPY :  £JAX_C, £JAX_C0, £JAX_C3, £JAX_D e £JAX_D0.


##  Data 09.01.07
E' stato aggiunto un controllo bloccante (livello 99). Al primo record di S5IRIS che si incontra con IDOJ vuoto, viene registrato un errore.
Viene registrato un solo errore, indipendentemente dal fatto che ci sia uno o più IDOJ mancanti, in quanto presumibilmente questa situazione è presente per un gran numero di record (potenzialmente tutti). Per questo stesso motivo, non vengono riportati gli estermi del record anomalo.
La scheduiazione non viene eseguita in quanto, pur essendo corretta, potrebbe dar luogo ad errori imprevedibili nelle attività manuali.
Si deve rimuovere la causa dell'errore (presumibilmente mancanza del numeratore in tabella P51) rigenerare gli impegni risorse e rieseguire la schedulazione.


##  Data 10.01.07
Dopo aver impostato i dati per la schedulazione ed aver confermato l'esecuzione, se c'è una sola opzione selezionabile, viene eseguita direttamente senza dover premere sul relativo pulsante.
Se invece è possibile selezionare più opzioni, vengono mostrati i relativi pulsanti sullla destra.
In questo modo, se ad esempio è presento solo l'opzione di schedulazione, viene aperta direttamente la scheda della schedulazione.
E' stato corretto lo script standard :  anche nel lancio di S5SMES_D3 per presentare la memoria iniziale, gli vengono passate, nel parametro, le impostazioni fisse (che nell'interattivo sono impostate tramite F17).


##  Data 11.01.07
Se cerco di eseguire una memorizzazione quando è necessaria una rischedulazione, in grafica viene mostrato un messaggio di errore e viene impedita la memorizzazione stessa (così come accadeva già in emulazione 5250).


##  Data 16.01.07
Il campo XGTIRO del dettaglio (schedulazione in tiro) è valorizzato a '1' se l'operazione è tirante, a '2' se l'operazione è tirata.
Si possono inserire in questo campo altri valori (meglio se alfanumerici) in fase di spinta, per tenere traccia della modailità di spinta selezionata.


##  Data 24.01.07
Sono state attivate le funzionalità di scelta e filtro risorse sul menu a popup.
Riferirsi alla documentazione attiva del modulo Fine.up, nel paragrafo azioni manuali, per l'esposizione dettagliata. Ricordo che è necessario avere in linea le immagini.


##  Data 24.01.07
Se un'operazione è iniziata ma non è stata valorizzata la risorsa specifica su S5IRIS, l'operazione stessa viene declassata a pronta. Questa forzatura è ora stata intercettata come errore non bloccante e quindi viene presentata nella matrice degli errori.


##  Data 20.03.07
Sono stati aggiunti due richiami al pgm di aggiustamento di scrittura S5IRIS (S5SMX_08x), all'inizio e alla fine del processo di scrittura.
Chi ha già un pgm di aggiustamento deve modificarlo secondo lo scheletro :  la lettura del dettaglio schedulato va fatta solo nelle funzioni 'PRE' e 'POST'.


##  Data 22.03.07
E' stato inserito l'esempio di utilizzo programma mongolfiera di memorizzazione altri campi di S5IRIS.
Esempio di CALL da inserire nei programmi :  XXESE_01
Esempio di programma momglofiera :  XXESE_02


##  Data 23.03.07
E' stata modificata la memoria con aggiunta di due OAV di riclassifica alla DS delle risorse e del campo  numero di batch alla DS del dettaglio (quest'ultima per sviluppi futuri).
Nello script si possono inserire due OAV (in presenza di risorse specifiche si piò decidere se essi sono relativi alla risorsa generale oppure a quella specifica), che costituiscono un filtro sul Gantt di presentazione.
Nel popup di richiamo dei Gantt si presentano, se impostati gli OAV, le nuove opzioni, che consentono di presentare nel Gantt le sole risorse (generali o specifiche in base all'impostazione) il cui OAV è uguale a quello della risorsa puntata.
E' inoltre possibile decidere se in questo caso l'ingresso al Gantt è aperto o chiuso.
Per recepire questa modifica è necessario installare la versione aggiornata della scheda S5BASE.


##  Data 10.04.07
E' stato modificato il tracciato di S5IRSE0F. E' necessario inmstallare una versione a questa data della libreria P_RS.
Sono inoltre da aggiornare gli oggetti S5SMES_01K e S5SMES_02K.

##  Data 11.04.07
E' stata cambiata, in memoria (£S5SMDS) la DSIRSE, per comprendere le risorse produttive secondarie di S5IRSE.
E' quindi necessario caricare la nuova versione dei programmi e ricompilare le propie exit.
Questo sviluppo è in corso :  per ora è stato modificato lo script dei parametri (PAR_SCP) dove si imposta questo caricamento, lo script della BCD (INT) per lanciare il programma di caricamento S5SMES_02I.
!!! NON attivare per ora questa opzione in PAR_SCP !!!
Verificare inoltre, sempre in questo scrpit, che l'opzione 1 di caricamento IRSE da campo libero di S5IRIS abbia il valore 1 - 5 e non genericamente diverso da blanks.

##  Data 17.04.07
E' stata cambiata, in memoria (£S5SMDS) la DSSINT, per memorizzare le informazioni di anticipi, ritardi e tempi d attraversamento.


##  Data 19.04.07
E' stata cambiata, in memoria (£S5SMDS) la DSSINT, per memorizzare le informazioni di ore di carico tulale degli ordini.
E' stato inoltre modificato il lancio della scheda degli ordini, che non è più nelk pop-up della risorsa, nella matrice di lancio, ma un pulsate nella parte inferiore della stessa matrice, la cui pressione fa passare alla scheda degli ordini. In essa si deve scegliere l'ordinamento tra quelli previsti nelle linguette.
Questa scheda è stata potenziata con numerose rappresentazioni grafiche. E' possibile inoltre cliccando sull'ordine, passare al Gantt dell'ordine stesso.
E' stata creata la nuova scheda S5BASE04.
NB :  L'aggiustamento dei campi (S5SMX_06X) è stato esteso anche a questa matrice (programma SMES_D7).
Vanno quindi rivisti i programmi specifici, per evitare un loro malfunzionamento, se il loro comportamento non è condizionato espressamente dal programma lanciante (cosa che protegge da futuri implementi).


##  Data 27.04.07
Sono stati implementati i sgeuenti programmi di aggiustamento, lanciati condizionalmente se presente il suffisso nello script.
- S5SMX_11X Inizializzazione generale. Lanciato dopo aver costruito tutte le aree di memoria - S5SMX_12X Sospensione temporanea di una fase nel processo di schedulazione. Decide di non   trattare una fase fino a che si verificano determinate condizioni (ad esempio non sono pronte le altre fasi che insieme ad essa compongono un batch.


##  Data 08.05.07
E' stato aggiunta una modalità di lancio del programma di aggiustamento degli impegnI :  con funzione 'FIN' viene lanciato dopo aver costruito tutta la DS deglim impegnni (DSIMPE) in modo da poter eseguire controlli ed azioni globali (ad esempio sui batch).
Vanno controllati i programmi di aggiustamento per non eseguire azioni indiscriminate, ma solo se è stata ricevuta la funzione opportuna (passare da strutture IF / ELSE a strutture SELECT).
E'stato inoltre implementato il segnete programma di aggiustamento
- S5SMX_13X Ritorno informazioni di un  batch. Per ora riceve un dettaglio e ritorna se esso è un master (M) slave (S) o isolato (I).


##  Data 23.05.07
E' stato realizzata la scheda della cella :  viene lanciata da una cella del GANNT (della risorsa, dell'ordine, delle code) o dalla scheda dell'ordine (in questo caso viene presentata la scheda della prima fase dell'ordine).
Per attivare questa funzione, oltre ai programmi BCD è necessario aggiornare tutte le schede S5BASExx.
La funzione di popup 'SPOSTA NEL GRUPPO'  è stata rinominata in 'FORZA NEL GRUPPO' ed è stata aggiunta la funzione 'CONGELA NEL GRUPPO' che ha l'effetto di spostare la cella dopo l'ultima congelata nella coda della risorsa d'arrivo. Se non ve ne sono di congelate la sposta dopo l'ultima iniziata. Se non ve ne sono nemmeno di iniziate, viene spostata al primo posto.
La cella spostata, in questa fase, viene anche congelata.


##  Data 24.05.07
E' stata ricondotta la segnalazione degli errori alla gestione delle voci.
In tal modo, nella scheda degli errori, cliccando sull'errore, si accede alla scheda delal voce, in cui l'errore è descritto in modo esaustivo.
Per attivare questa funzione, è necessario installare i programmi descritti nella news che comunica la nascita dell'oggetto voce.
E' inoltre necessario copiare nel proprio ambiente il membro DOC_VOC/S5IRIS, che contiene le descrizioni degli errori.


##  Data 31.05.07

### Modifica allo script standard INT
. Il programma S5SMES_06 (già presente) assume il significato di completamento azioni iniziali
E' stata modificata l'intestazione del passo
. Il programma S5SMES_19 (nuovo) contiene le azioni finali di schedulazione
E' stato aggiunto nell'INT.
### Risorse produttive secondarie
E' stato consolidato lo sviluppo dell'11.04.07
In questo ambito è stata realizzata la scheda delle risorse produttive secondarie.
Si lancia : 
- dalla lista risorse :  presenta tutte le risorse secondarie (A)
- da una cella (di gantt risorse o gantt ordine)
.. presenta le risorse della fase (B) o dell'ordine (C)
- dalla lista ordine
.. presenta le risorse dell'ordine (C)
Dalla lista risorse si passa al dettaglio dei suoi impegni
Nel caso (A) vengono esposti tutti gli impegni
Nel caso (B) e (C) vengono esposti gli impegni rispettivacmente della fase o dell'ordine e quelli che vi si sovrappongono, anche parzialmente, con la possibilità di passare a tutti gli impegni.
### Implemento analisi memoria
E' stata aggiunta, nell'analisi della memoria, la DS degli imepgni secondari (DSIRSE).
### Visibilità risorse a capacità infinita
E' possibile visualizzare le risorse a caapcità infinita come risorse secondarie impoistando il campo opportuno in PAR_SCP. Riferirsi alla spiegazione contenuta in quel membro.
### Aggiustamento prima fase a capacità infinita
E' possibile, impostando un flag in PAR_SCP, accostare la prima fase, se a capacità infinita, sulla fase successiva. Riferirsi alla spiegazione contenuta in quel membro.
### Modifica alla memoria
E' stata modificata la memoria BCD (/Copy £S5SMDS, £S5SMPLI, £S5SMPLO.
Somo state aggiunti due elementi : 
- una schiera (XHISR) di storia della schedulazione. In ogni elemento viene riportato il dettaglio schedulato in quella posizione (il dettaglio schedulato per quarto, ad esempio, viene riportato nel quarto elemento di questa schiera, che è riempita per un numero di elementi pari a £BCDNP).
In questo modo all'interno della BCD è nota la sequenza di schedulazione per eventuali backtracking.
- la DSRSEC, contenete un elemento per ogni risorsa secondaria. E' stato inserito nella DSIRSE il puntatore a questo elemento.
In seguito a questo implemento vanno ricompilare tutte le proprie exit BCD.
Vanno inoltre aggiornate le schede S5BASExx.


##  Data 06.05.07
E' stata modificata la memoria BCD (/Copy £S5SMDS) :  nella DSRSEC è stato aggiunto il numero di impegni per la risorsa secondaria.
In seguito a questo implemento vanno ricompilare tutte le proprie exit BCD.


##  Data 18.06.07
### Controllo deadlock
E' stato esteso il controllo del dealock tra fasi.
Il controllo è stato reso parametrico (da script), da attivare solo se vi sono ordini che hanno più di una fase sulla stessa risorsa.
Il controllo individua i deadlock anche tra ordini diversi, mentre l'attuale individuava solo quelli nello stesso ordine.
Viene eseguito prima della schedulazione, ed ha come risultato lo scongelamento di una o più fasi, dandone segnalazione nella lista errori.
Qualora si introduca un deadlock nell'attività manuale sul Gentt, la segnalazione viene data alla successiva rischedulazione (obbligatoria se si vuol uscire salvando la sessione).
Oggetti modificati
INT (script) - PAR_SCP (script di parametri) - DOC_VOC/S5IRIS (script di voci :  aggiunta voce)
Oggetti nuovi
S5SMES_K0 - S5SMES_K2 - S5SMES_K3 - S5SMES_DJ - S5SMES_DJI - S5SMES_DK - S5SMES_DKI - S5SMES_DL
Oggetti diventati obsoleti
S5SMES_K1 (controllo deadlock singolo ordine)

### Segnalazione schedulazione incompleta
Se la schdulazione non si completa viene agguntom un messaggio di errore, e ne viene data evidenza nella scheda base.


##  Data 20.06.07
### Modifica memoria
E' stata modificata la memoria BCD (/Copy £S5SMDS) :  nella DSRSEC sono state apportate modifiche alle DS selle risorse secondarie
In seguito a questo implemento vanno ricompilare tutte le proprie exit BCD.
### Modifica tracciato S5IRSE
Vanno eseguite le attività esposte nel membro AA_LEGGIMI im P_RS/SRC, in questa stessa data.
Deve essere ricaricata una versione aggiornata di tutti i programmi di BCDSRC.


##  Data 22.06.07
Il seguente implemento potrebbe avere valenza di news, in quanto è stato relizzato su programmi rilasciati (in SMEDEV e in sorgenti diversi da BCDSRC) ma data la natura delicata del tema, ed il carattere evolutivo dei lavori collegati, ho preferito dare la minima pubblicità.
E' stato introdotto il valore V2/S5_TB (tipo batch) che descrive la modalità di esecuzione concorrente di più lavori. I valori inseriti sono ancora provvisori (non so se si dovrà specificare meglio la natura del batch). Per ora utilizzo il valore '1' (batch alternato) senza però essere sicuro che vi sia solo un tipo di batch alternato.
E' stata modificata la tabella BRM (gruppo risorse) per poter specificare questo valore.
E' stato inoltre riportato nel flag 14 di S5IRIS (programma S5FURIT_SC).


##  Data 10.07.07
### Filtro risorse
E' possibile impostare nello script di parametri uno stato delle risorse :  verranno escluse le risorse con stato uguale ad esso.
Dato che nell'archivio BRRISO non esiste il livello, e qunidi non c'è la possibilità di annullamento logico, questo implemento sopperisce a questa mancanza.
In tal modo si possono, ad esempio, escludere alcune risorse specifiche dalla schedulazione.
### Filtro risorse
E' stato introdutto inoltre un flag libero (controllato in *CN/S5) in tabella BRM, in cui si puè impostare una classe di schedulazione a disposizione dei programmi specifici. Ad esempio si può impostare che il tiro viene eseguito solo sulle risorse che hanno un valore specifico in questo campo.
NB :  è cura totale del programma specifico eseguire questo controllo :  come standard si può impostare solo di lanciare il programma specifico di tiro. All'interno di questo programma si decide se eseguire il tiro solo su una certa classe di risorse.
Tale flag è stato riportato nel flag 15 di S5IRIS (programmi S5FURIT_SC e S5IRIS0F_F).
Si deve quindi : 
- aggiungere il sottosettore S5 alla tabella *CN, col significato 'classe di schedulazione'
- aggiornare il settore BRM
Sono da aggiornare inoltre i programmi :  S5FURIT_SC, S5IRIS0F_F e S5S5C0.


##  Data 11.07.07
E' sttao aggiunta la possibilità di lanciare il pgm di aggiustamento che permette di scegliere in modo libero il dettaglio da schedulare. Si differenzia dalla spinta in quanto è totalmente estraneo al processo normale di schedulazione, con miglioramento delle prestazioni.


##  Data 12.07.07
Sono state modificate le seguenti DS di memoria, quindi vanno ricompilati tutti i programmi personali di BCD
- DSERRO :  è stato aggiunto un terzo oggetto, in cui si imposta l'IDOJ del dettaglio in errore, in modo da poter passare faclimente alla sua scheda
- DSRISO :  sono stati aggiunti i campi di tipo batch e classe schedulazione (definiti nell'elemento di tabella della risorsa generale), a disposizione dei programmi specifici per raffinare il processo di schedulazione.


##  Data 18.07.07
Dalla scheda di lista ordini, se è attivo il controllo materiali (ottenuto impostando il gruppo fonti nello script dei parametri) è possibile passare (via popup) alle schede di copertura impegni e copertura ordini.


##  Data 24.07.07
Sono stati aggiunti i campi di flag disponibilità impegni delle risorse secondarie nelle DS delle sintesi ordini, degli impegni, degli impegni di risorse secondarie e delle risorse secondarie.
Sono quindi da ricompilare le exit di schedulazione.
Tali campi attualmente sono valorizzati quando non è stato impostato nella tabella BRK il modo di reperimento del calendario (si assume che la risorsa sia sempre disponibile in quantità unitaria).
L'indisponibilità viene segnalata con semafori nella lista ordini e nella lista impegni risorse secondarie, ed è un campo selezionabile nei Gantt delle risorse e degli ordini.
Per decodificarlo è stato realizzato il nuovo valore V2/S5_DS.
Si rimanda al documento (provvisorio) NOT_001 (in questo stesso SRC) per un'esposizione completa dell'intervento, sia da un punto di vista tencico sia applicativo.


##  Data 15.10.07
E' stata razionalizzata la gestione di attributi specifici che condizionano la schedulazione (utilizzati in exit personali).
Si imposta la categoria nello script dei paramatri.
Riferirsi a questo membro (posizione 070) per una descrizione completa dell'intervento.


##  Data 17.01.08
E' stata realizzata la possibilità di eseguire azioni finali al termine della schedulazione.
E' guidata dalla presenza del suffisso del programma S5SMX_13x, in posizione 73 dello script dei parametri.


##  Data 29.01.08
E' stato aggiunto il richiamo al programma di aggiustamento di S5IRIS S5SMX_02x, lanciato da S5SMES_01I, anche il richiamo "INZ", prima della costruzione di DSIRIS. In esso si possono inizializzare aree sepcifiche, mongolfiere, riempite dall'IRIS.
E' possibile inserire errori personali e modificarle il contenuto di quelli standard.
A questo proposito va creato il file DOC_VOC nella libreria personale, con il membro X5IRIS.
Per modificare un messaggio (voce) standard, lo si compia dal membro SMEDEV/DOC_VOC (solo la o le voci che si intendono modificare).
La funzione di presentazione delle voci,(S5SMES_DE) ricerca la voce prima nel membro personale (X5IRIS di DOC_VOC nella libreria personale), se asseente la ricerca nel membro standard (S5IRIS di DOC_VOC in SMEDEV)
I messaggi persnlai vanno trattati nel seguente modo.Si inseriscono nel membro  personale (X5IRIS di DOC_VOC nella libreria personale) come Xyyyy, dove
yyyy sono quattro caratteri numerici.
Nell'applicazione, quando si ha la necessità di registrare un messaggio, si aggiunge un'occorrenza nella DSERRO. Nella categoria errore (XECTER) si inserisce, cambiato di segoo, il codice della voce personale. Il segno negativo individua i messaggi personali.

Ad esempio, per presentare il messaggio personale X0012, si devono scrivere la seguente istruzioni : 

     C                   EVAL      £T12=£T12+1
     C     £T12          OCCUR     DSERRO
     C                   CLEAR                   DSERRO
     C                   EVAL      XENERR=£T12
     C                   EVAL      XECTER=-12    <--- Codifica del messaggio X0012
     C                   EVAL      XELVER='50'   <--- Livello errore (se 99 bloccante)


##  Data 21.02.08
E' stato modificato lo script di schedulazione standard "INT" :  chi lo ha personalizzato deve riportarvi le proprie modifiche.
E' stato modificato il modo di definire il luogo in cui risiede lo scrpit dei parametri in tabella B§G.
Si devono quindi modificare i propri elementi di B§G. Riferirsi alla NEWS 1315 per un'esposizione completa della modifica.
Ne approfitto per ricordare gli elementi di B§G proposti : 
- INT Richiamo in emulazione. Viene sempre presentato in G18, sia in richiamo da 5250 nativo, sia in richiamo da Loocup.
- FIN Richiamo grafico. Se richiamato da Loocup, viene presentato graficamente, se invece viene  richiamato in modalitù 5250 nativa. viene presentato in G18.
E stato aggiunto, nel Popup della zona libera del Gantt di dettaglio un pulsante che permette il passaggio alla visualizzazione delle risorse secondarie totali.
E' stato aggiunto, nella DS degli impegni di risorse secondarie (DSIRSE) il flag 09 dell'archivio che individua se l'impegno secondario è escluso dalle righe slave (ad esempio, se è uno stampo).
In tal modo tali impegni potranno essere esclusi dalla visualizzazione.
E' stato introdotto il concetto di "Data obiettivo" per l'ordine da schedulare. IL calcolo di tale data (riportata sulla DS di sintesi degli ordini) è eseguito dal programma S5SMX_15x (dove x è un carattere impostato nello script di parametri). In assenza di tale programma viene riportata nella data obiettivo la fine richiesta.
Il calcolo dell'anticipo e del ritardo viene eseguito confrontando questa data con la fine schedulata, che quindi avrà infuenza su : 
- gli indici globali (lateness, tardines,e cc..)
- i segnali grafici di data fine sui Gantt
- gli ordinamenti sulla lista ordini (con l'etichetta variabile in funzione di quanto scelto)
Nei campi delle matrice dei vari Gantt, questa data verrà presentata se presente il programma di exit specifico.
Il lead time (presente nella lista ordini viene comunque calcolato come differenza tra data fine ed inizio richiesta.
Si può impostare nello script dei parametri, di calcolare le differenze di date (anticipi e ritardi, lead time, tempi di attraversamento) in giorni solari o del calendario del plant dell'ordine.
Nelle presentazioni Gantt (dettaglio, ordine e code) è stato uniformato il reperimento dell'anticipo ritardo (assunto dal valore di DSSINT) e quindi sensibile alle impostazioni definite in precedenza (data obiettivo e giorni solari / calendario).
E' possibile impostare nello script di parametri (PAR_SCP) un flag la cui presenza, se è impostata,
nello stesso script, il campo di costruzione batch, fa sì che nel lancio della schdulazione venga presentato un bottone di lancio lista famigla batch (programma S5BCHDV).
E' stata inserita la getsione dei batch "statici" (definiti all'esterno di Fine.Up) impostando il flag opportuno nello scripr dei parametri.
E' stata di conseguenza modificata la memoria degli impegni (DSIRIS) in modo da contenere i campi relativi ai batch dell'archivio impegni.

Le modifiche precedenti hanno reso necessario modificare la /Copy di descrizione della memoria £S5SMDS, e di conseguenza tutti i programmi di Fine_Up somo stati portati in DEV e ricompilati.
E' quindi necessari aggiurnare tutta l'applicazione presso i clienti (copiare £S5SMDS nella WILEGEN di SMEDEV, copiare la BCDSRC di SMEDEV e ricompilarla).
E' necessario inoltre ricompilare tutti i prorpi programmi di exit.
E' inoltre necessario riaggiornare le schede S5BASExx da SCP_SCH di SMEDEV.


##  Data 03.03.08
E' ora controllato che i legami tra ordini passati dal pgm di exit S5SMX_09x siano tra due ordini cha hanno almeno un impegno aperto (tecnicamente devono essere presenti nella DSSINT. Se aimeno uno dei due ordini è assente, il legame non viene registrato nella DSLEGA.
Sono stati modificati i pgm S5SMES_01i, S5SMES_07 e lo script INT.


##  Data 13.03.08
Da questa data vengono riportate, in testa, le modifiche nei programmi di Fine.Up.
NON viene riportata la modifica se è solo ricompilazione, dovuta ad un cambiamento delle DS di memoria.
E' stata modificata l'ampiezza della schiera della griglia SWKSCH nei programmi di presentazione grafica.
Progrmamma                   Da N.Elementi    A N.Elementi
S5SMES_D3  Matrice risorse        50                =
S5SMES_D4  Gantt risorse         100               300
S5SMES_D5  Gantt ordine          100               300
S5SMES_D7  Matrice ordini        100                =
S5SMES_D9  Gantt code            100               300
S5SMES_DF  Zoom cella             50               100

I programmi personali che la elaborano (di prototipo S5SMX_06x) devonmo essere adeguati :  la schiera SWKSCH va portata a 300 elementi (il prototipo è già adeguato).

E' stato corretto il pgm S5SMES_16 :  se non era attiva la gestione batch non schedulava più.


##  Data 31.03.08
Sono stati modificati i valori possibili del flag di batch congelato :  di conseguenza sono  stati variati i test all'intermo dei programmi.


##  Data 03.04.08
E' stata corretta la tipizzazione degli istanti (oggetto I1) :  nelle griglie di matrice era stato definito come I12 :  ore minuti secondi, mentre il suo valore corretto è I11 :  ore decimillesimi di ora


##  Data 11.04.08
E' stato corretta la partenza della disponibilità delle risorse. Fino ad ora era l'istante di inizio schedulazione :  è stato portato al primo istante maggiore o uguale alla partenza in cui la risorsa è aperta.
Cio porta ad una sequenziazione più corretta degli impegni. Im precedenza si poteva verificare che un impegno meno urgente ne sorpassasse uno più urgente, quando quest'ultimo era piazzato sulla risorsa chiusa all'istante di inizio schedulazione.
Con questa modifica è inoltre possibile, impostando un'apertura molto avanti nel tempo, "sospendere" logicamente una risorsa.
Se il sistema non riesce a determinare un istante di apertura maggiore o uuale all'inizio della schedulazione, viene mantenuto quest'ultimo istante, e viene data segnalazione com errore non bloccante.


##  Data 12.05.08
E' stata aggiunta la possibilità di presentare la registrazione dell'ultimo run di schedulazione che è stato memorizzato.
Ci si è avvalsi della nuova funzione di presentazione log dei motori BCD (riferirsi alla NEWS 1331).
Nello specifico, viene memorizzata in un elemento di B£MEDE l'intera stringa dei parametri richiesti (mappati dalla descrizione di tabella S5X), con la seguente chiave : 
- Tipo impegno risrse
- Scenario d'arrivo
- Ambito.
Nel formato di lancio, dove viene richiesto l'elemento di B§G, se è impostata la presentazione a livello 1 o 3, nel caso che ci sia un solo elemento menorizzato ne viene presentato il contenuto, se invece sono più d'uno, viene presentata la lista, da cui si può accedere alla visualizzazione di ogni singolo dettaglio.
In lancio da Loocup, se è impostata la presentazione a livello 2 o 3, viene aggiunto il bottone "Statistiche" nel lancio, da cui si accede alle stesse informazioni del caso precedente.


##  Data 10.09.08
E' stato uniformato lo script "INT" che ora può eseguire sia il lancio interattivo sia quello batch.
Ciò ha comportato un implemento al motore BCD (nello specifico al programma  B£BCD02), dove è stata aggiunta, come variabiel d'ambiente, anche il tipo lavoro :  I (interattivo o emulaziome Loocup),
L (Loocup puro, tarnsazionale) e B (Batch).
La segnalazione dei messaggi avviene in modo specifico : 
I - Nessuna segnalazione esplicita :  possibilità di accesso ad un G18 di lista errori
L - Segnalazione di un bottone nella scheda guida, da cui si accede ad una scheda di lista errori
B - Messaggio all'utente e stampa della lista errori
Il modo di definire il tipo di lavoro è esposto dettagliatamente nell'help della tabella B§G.


##  Data 04.11.08
E' possibile eseguire l'exit (S5SMX_16y, dove y è un carattere impostato nello script di parametri) che permette di modificare l'istante di partenza della disponibilità delle risorse.In questo modo è possibile ottenere una partenza "sfumata", dalla fine dell'ultima attività dichiarata sulla risorsa. A questo istante va sempre poi applicata la correzione con il calendario, per determinare l'effettivo istante di inizio. (Vedi News del 11.04.08).
L'inizio impostato come parametro di lancio si assume valido quindi solo per le risorse che non sono state mai dichiarate, e quelle a capacità infinita.
E' stato deciso, per ora, di non eseguire questo aggiustamento con un programma standard, per lasciare libertà all'implementatore.
Se l'istante di ultimo carico è inferiore all'istante di inizio, viene mantenuto quest'ultimo.


##  Data 26.05.09
Se si imposta nello script un tipo distinta (e sono attivati i legami statici) essi vengono letti da quanto scritto in distinta. Verosimilmente la distinta ha come oggetti (assiemi e componenti) degli ordini di produzione.


##  Data 16.11.09
Gstione a risprmio memoria, utile per aumentare le risorse specifiche possibili per una risorsa principale (limite portato da 40 a 200). E' attivabile da script (il default è NO) in quanto la percorrenza delle ds è più complessa (ad esempio nel tiro).

Split di fasi in sottofasi omogenee (in uno scenario dipendente).

Parallelismo tra fasi e sottofasi.

Schedulazione degli impegni dei colli MFP.

Attivazione gruppi temporanei da script (riferirsi alla documentazione contenuta in quest'ultimo).

Possibilità di visualizzare, come griglia di sfondo, batch, tiri, gruppi temporanei e intervalli di chiusura.

Congelamento / scongelamento di massa, fino ad una data prefissata.

Schedulazione "real time", con partenza dall'istante di lancio.


##  Data 09.12.09
Nella scheda di presentazazione iniziale della BCD, che riporta la lista delle risorse con relative ore di carico, date di fine, ecc... sono stati aggiunti i seguenti campi : 
- numero attrezzaggi (impegni con ore attrezzaggio effettive diverse da zero)
- ore attrezzaggio (somma delle ore attrezzaggio effettive)
- ore attrezzaggio teoriche (somma delle ore attrezzaggio teoriche)
- % di risparmio, se le ore di attrezzaggio effettive sono minori delle teoriche.
  Ad esempio, se le ore attrezzaggio effettive sono 40 e quelle teoriche 50, la % di risparmio è   del 20 %
  NON viene calcolata la % quando le ore effettive sono maggiori delle teoriche (cosa che non può   essere esclusa a priori, dato che il calcolo delle ore effettive è demandato ad un progranna di   aggiustamento).
- Grafico della % di risparmio, colorata in gradazioni di blu, degradanti al calare del risparmio.
  Nel caso di attrezzaggio effettivo maggiore del teorico, viene riportata una barretta rossa per l'intera lunghezza :  viene data segnalazione dello spreco senza   rappresentarne l'entità.


##  Data 10.12.09
E' stata definita la segtuente convenzione per siglare le exit standard, che man mano verranno realizzate.
I suffissi alfabetici sono riservati per le exit utente, quelli numerici per le exit standard, che implementeranno comportamenti variegati, guidati, se è il caso, da impostazioni tabellari.
Nello specifico, la prima exit implementata è lo S5SMX_041, relativa all'attrezzaggio. Per ora si limita ad azzerare l'attrezzggio, se sulla risorsa specifica l'operazione precedentemenet eseguita è dello stesso articolo e della stessa fase. In futuro ne aumenteremo le potenzialità, avvicinandoci, con gradualità, all'implementazione delle matrici di attrezzaggio.

E' possibile, impostandolo in PAR_SCP, che le operazioni iniziate vengono declassate a pronte.


##  Data 24.12.09
Nella scheda di presentazazione iniziale della BCD, per ogni risorsa viene riportata, per ogni risorsa. la somma delle quantità schedulate di tutti gli impegni.
E' possibile impostare in PAR_SCP, che vengano segnalati come errori gli impegni scartati perchè hanno le ore totali residue a zero.


##  Data 10.01.10
E' stato realizzato il pgm di tiro standard con prefisso '1' (S5SMX_031) che implementa l'accostamento :  dopo aver schedulato un impegno, viene tirato qullo immediatamente successivo dello stesso ordine, se è eseguibile sulla stessa risorsa specifica e non è iniziato.
Questo comportamento verrebbe eseguito anche impostando l'accostamento in tabella S5B ma, passando dal tiro, si hanno i vantaggi di una implementazione più standardizzata (ad esempio, il tiro viene segnalato e può costituire un gruppo temporaneo).
Se si imposta comunque il flag di accostamento nella tabella dell scenario, se è presente un tiro (suffisso nello script dei parametri) l'accostamento NON viene eseguito, e viene data segnalazione dell'incongruenza tra gli errori non bloccanti.


##  Data 21.01.10
E' possibile modificare, dall'interno della schedulazione, i suffissi dei programmi di exit, attraverso un alista in cui sono presentate tutte le exit possibili e, per ciascuna di esse, i programmi effettivamente presenti.
In modalità carattere, questa funzione viene richiamata con l'opzione 'LE' da una quanlsiasi riga della lista di presentazione delle risorse.
In modalità grafica, viene invece lanciata da un bottone nella scheda di analisi memoria.
Per attivarla, oltre ai programmi della BCD, vanno aggiornate le schede S5BASE e S5BAS02.


##  Data 24.01.10
E' possibile impostare che l'ottimizzazione della scelta di un singolo gruppo di schedulazione, sia esclusa per alcuni gruppi se, ad esempio, essi sono schedulati singolarmente con strategie particolari (backtracking, ecc...).


##  Data 08.03.10
E' stata aggiunta nella DS dei materiali (visibile nella scheda delle comperture e nella analisi della memoria) la risorsa principale a cui è legato l'impegno.
Queata informazione viene reperita dall'operazione di impiego del legame di distinta base (ricordiamo che se assente si assume la prima operazione).


##  Data 16.03.10
E' stata creata l'exit standard S5SMX_181, che disabilita in generale l'ottimizzazione nella scelta del gruppo da ottimizzare.


##  Data 13.05.10
E' possibile eseguire una exit che modifica l'instante di inizio disponibilità della risorsa, dopo aver schedulato un'operazione su di essa.


##  Data 01.09.10
Rilascio V3R1
E' stato introdotto di concetto di impegno con vincolo al più presto (vpp) bloccato.
Questa informazione risiede nel flag 22 di S5IRIS, ed attualmente va inserita unicamente con il programma di aggiustamento degli impegni (non c'è nessuna modalità di riemnpimento standard).
E' possibile, cliccando su una cella nel GANTT di dettaglio, se l'impegno non è iniziato e non ha il flag di vpp bloccato, accedere ad una finestra in cui si possono modificare data e ora del vpp (inserirli, nodificarli o annullarli).
NB :  la modifica viene recepita immediatamente dalla successiva rischedulazione in memoria, maviene consolidata in S5IRIS solo in uscita, all'atto del saolvataggio dei dati.
Questa operatività va attivata impostando un flag nello script dei parametri.

E' possibile, impostando un flag nello script dei parametri, rappresentare in modo diverso, nel GANTT di dettaglio, le celle che hanno un vpp (e che non sono iniziate).
E'possibile scegliere di modificare la forma di tutte le celle con vpp, o solo quelle con vpp non modificabile.
Nello specifico la forma diventa
- Celle congelate - da triangolo con angolo acuto a destra a trapezio con angolo acuto a destra
- Celle forzate   - da triangolo con angolo acuto a sinsitra a trapezio con angolo acuto a sinistra
- Celle libere    - da rettangolo pieno a rettanolo con l'angolo in alto a sinistra vuoto.

E'possibile, nel GANTT di dettaglio, impostare una scala di rappresentazione.
Cliccando in una zona vuota, nel menu di popup appare la voce scala, in cui si può sceglere il tipo di scala (giorni, settimane, mesi) e da esso il numero (di giorni, settimane o mesi).
Come priva voce appare la selezione memorizzata.
Selezionando la voce automatica si imposta la modalità precedente al presente intervento, vale a dire demandare al sistema la scelta della scala (ogni volta quella che presenta tutto il GANTT).

##  Data 80.02.11
E'stata aggiunta l'exit S5SMX_20x per eseguire azioni dall'opzione dei £G18 (in esecuzione in modalità 5250).
Attualmente è implementata in S5SMES_30 (lista dettagli)  e S5SMES_DB (storia schedulazione)

E'stata aggiunta l'exit S5SMX_22x per aggiungere indici personali alla schedulazione.
Gli indici personali vanno dal 61 al 90 (estremi compresi) e vanno definiti nel programma utente D5CO_12_U (a nome fisso), di cui è fornito un prototipo.
NB :  gli indici vanno impostati a livello generale della schedulazione.
Oltre ai programmi della BCDSRC, va aggiurnato il programma D5CO_12
E' stata riservata una stringa di 10 caratteri nello script dei parametri per parametrizzare il calcolo degli indici (ad esempio se si vuol calcolare una saturazione entro un limite) in questo campo si può impostare, nelle prime due posizioni, il numero di giorni che fissa l'orizzonte.

E' possibile aggiungere colonne anche nella matrice della storia della schdulazione.
Questa funzione è utile in fase di debug del motore.
La documentazione del colloquio è riportata nell'exit di esempio S5SMX_06X.

E' stata realizzata una funzione che presenta (con possibilità di modifica dei suffissi) le exit utente, con la lista delle exit esistenti, e con controllo (forzabile)  della presenza dell'oggetto.
Essa viene lanciata dalla visualizzazione dello script, a sua volta lanciato con il tasto F15 nel formato di richiesta dell'elemento di B§G (in modalità sla 5250 sia Grafica).
Per l'attivazione si rimanda alla News 1658.
Dato che il formato di richiesta può essere saltato, (impostando l'elemento B§G nel richiamo), la lista exit può essere anche lanciata : 
In modalità 5250, dalla lista risorse (S5SMES_D3) con l'opzione LE.
In modalità grafica, dal bottone "Lista Exit" presente nella scheda di analisi memoria.










