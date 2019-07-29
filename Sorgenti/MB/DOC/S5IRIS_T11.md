# Introduzione
La schedulazione BCD si basa su una serie di aree di memoria (tecnicamente realizzate in DS ad occorrenze multiple) che contengono i dati di input ed i risultati dell'elaborazione.
Ogni elemento contiene, come primo campo, il numero relativo dell'occorenza. Tale informazione non è neceessaria, in quanto il puntamento all'elemento avviene tramite questo valore, ma è utile, in fase di debug, per conscere l'occorrenza attualmente in memoria (se, ad esempio, il puntatore non è più disponibile).

Nel seguito viene data una breve descrizione delle principali DS dell'applicazione. Esse sono definite nel membro QILEGEN/£S5SMDS.
 :  : DEC T(MB) P(QILEGEN) K(£S5SMDS) L(1)
Per ognuna di esse, se presenti, evidenzieremo le exit impostabili, con la loro funzione.
Ricordiamo che le exit si attivano impostando i relativi suffissi nello script dei parametri.
 :  : DEC T(MB) P(BCDSRC) K(PAR_SCP) L(1)

# Generalità DS multiple

Una DS multipla è sostanzialmente un archivio in memoria.
Si definisce con le seguenti istruzioni "D"

NOME_DS  DS   OCCUR(NNN)
   X1NOME 3
   X2NOME 4   0

Dove NOME_DS è il nome della DS
NNN è il numero di elementi (il numero massimo di record) :  può essere un numero o una costante numerica
X1NOME, X2NOME ... sono i nomi dei campi, con i rispettivi tipi e lunghezze.
La lunghezza della DS viene calcolata come somma delle lunghezze dei singoli campi.
Esiste un limite massimo di elementi NNN (dipende dalla versione del sistema).
Esiste inoltre un limite massimo per l'area di memoria occupata (che può ridurre il numero massimo di elementi), dato da NNN moltiplicato per la lunghezza della DS, anch'esso dipendente dalla versione del sistema.

Un elemento viene agganciato con l'istruzione (corrispondente alla CHAIN sugli archivi)
NNNN  OCCUR NOME_DS
Dove NNN è un numero o una variabile numerica (se vale 0 o supera il numero di elementi viene generato un CPF).
È sempre presente un solo elemento alla volta :  l'istruzione OCCUR fa sì che venga sostituito l'elemento precedente.
A differenza degli archivi, non esiste il concetto di UPDATE. Quando si modifica un campo della DS esso è subito scritto.
Quando si passa una DS multipla da un programma all'altro non viene passata in automatico la posizione a cui era presente nel chiamante.
Si accede al numero di elementi di una DS multipla con la funzione : 
%ELEM(NOME_DS), che può essere usato come punto di arrivo di un loop FOR.
Nel DEBUG è possibile vedere i campi dell'elemento in corso con il comando : 
DSPPGMVAR NOME_DS
Oppure vedere un elemento specifico, con il comando : 
DSPPGMVAR NOME_DS(NNN)
Dove NNN è esplicitamente il numero dell'elemento, ad esempio NOME_DS(4).



## Particolarità DS Multiple in Fine.Up

Le DS Multiple in Fine.Up hanno le seguenti caratteristiche.
Per ogni DS i primi due caratteri sono fissi (il primo è X), in analogia ai campi di data base.
Ad esempio tutti i campi della DS degli impegni (DSIRIS) si chiamano XIyyyy. La parte successiva (yyyy) ha xx dizionario.
Il primo campo di ogni DS è la sua posizione :  ad esempio la terza occorrenza riporta il numero 3.
Nel seguito ci riferiremo a questo campo con il termine "puntatore".
In questo modo, in debug, è immediato conoscere l'occorrenza attualmente presente in memoria.
Dato che l'accesso ad un elemento di DS avviene per posizione, per legare due DS (di cui una dipende dall'altra) si imposta in un campo della prima il primo campo della seconda.
Ad esempio, per legare DSIRIS (gli impegni) e DSSINT (gli oggetti a cui appartengono gli impegni, normalmente gli ordini di produzione), si è realizzata la seguente struttura : 
IN DSSINT il primo campo è XDNSIN.
In DSIRIS c'è, tra gli altri, il campo XINSIN, che contiene la posizione in DSSINT dell'ordine a cui appartiene l'impegno.
Quindi per agganciare l'elemento di DSSINT relativo all'impegno attualmente in memoria, è sufficiente eseguire l'istruzione
XINSIN OCCUR DSSINT


Sono presenti memorie "private" realizzate in alcuni programmi come estensione delle memorie standard (definite in £S5SMDS e allocate nel programma di innesco).
Un esempio è, in S5SMES77 (schedulazione delle risorse secondarie di vincolo) la DS DSPINT, che è un'estensione della memoria standard DSDEGR.
I motivi di questa scelta sono i seguenti.
Quando si modifica un'area di memoria standard bisogna ricompilare tutti i programmi della schedulazione, in quanto varia la lunghezza di ogni elemento). Questo impedisce modifiche immediate a queste memorie, cosa che risulta poco funzionale, specialmente in fase di implementazione.
L'estensione di una memoria potrebbe farla "esplodere", vale a dire superare il limite massimo consentito per la sua "area".
Queste memorie, infine, sono allocate solo all'atto del lancio del programma che le contiene. In una installazione che non utilizza le risorse secondarie di vincolo non viene sprecata memoria ram.


Nella costruzione delle aree di memoria si utilizzano alcuni "stili" di descrizione e di costruzione di cui diamo un esempio.

In DSSINT ci sono i puntatori al primo e all'ultimo DSIRIS dell'ordine.
Si costruiscono in questo modo.
Si scandiscono gli impegni S5IRIS in sequenza di ordine/fase :  a rottura di ordine si scrive un nuovo DSSINT riportando il puntatore di DSIRIS sia nel primo sia nell'ultimo puntatore in DSSINT. I successivi DSIRIS dello stesso ordine aggiorneranno col loro puntatore soltanto il puntatore finale, ogni volta ricoprendo il valore precedente. In questo modo, a rottura di ordine, rimarrà il puntatore all'ultimo elemento.



# DSIRIS - Impegni risorse
Viene costruita dal programma S5SMES_01I. Contiene gil elementi di S5IRIS oggetto della schedulazione (filtrati in base alle impostazioni iniziali).

Le informazioni contenute si suddividono in : 
 * informazioni generali dell'impegno risorse :  ordine, fase, quantità, articolo, cord, idoj,  vincoli esterni, priorità, date richieste, ecc...
 * tempi :  vengono ripresi dall'impegno risorse e riportati sulla DS delle alternative
 * dati dinamici :  si modificano nel corso della schedulazione
 ** stato (una fase inizialmente non pronta lo diventa quando viene schedulata la precedente)
 ** vincoli al più presto (valorizzati quando la fase diventa pronta)
 ** informazioni di schedulazione :  si modificano quando la fase è schedulata  (numero progressivo di schedulazione e numero dettaglio schedulato)
 ** forzature e congelamenti (ripresi dall'impegno e modificabili nel gantt)
 * legami con altre DS

E' possibile attivare la exit
 :  : DEC T(MB) P(BCDSRC) K(S5SMX_02X) L(1)
che permette di modificare dinaamicamente il contenuto dell'impegno risorse, ed eventualmente scartarlo per motivi specifici.
Consultare la documentazione in testa al prototipo per il dettaglio delle funzioni ammesse.

E' inoltre possibile attivare la exit
 :  : DEC T(MB) P(BCDSRC) K(S5SMX_15X) L(1)
che permette di determinare una data obiettivo nella memoria dell'ordine (DSSINT), che sostituisce il valore di default (data fine richiesta).

# DSRISO - Risorse primarie
Viene costruita dal programma S5SMES_01R, che va lanciato con la funzione 'PRI' o 'SPE', a seconda che si vogliono caricare le risorse principali o specifiche (del tipo impostato nello scenario di schedulazione). Se non sono previste le risorse specifiche (il tipo è uguale al tipo principale) esse non vengono caricate, anche se esplicitamente richieste. Contiene le informazioni delle risorse, suddivise in
 * informazioni generali :  tipo, codice, descrizione, risorsa principale se specifica, efficienza, tipo schdulazione, dati di coda e sovrapposizione,
 * informazioni modificate all'atto della schedulazione di un dettaglio sulla risorsa
 ** numero del dettaglio schedulato, utile per calcolare l'attrezzaggio incrementale, o per 'tirare' un'operazione successiva.
 ** data e ora di inizio disponibilità (coincidente con la fine schedulata dell'operazione, al netto dell'attesa successiva)
 ** numero di operazioni congelate (calcolato all'inizio e diminuito di un'unità ogni volta che si schedula un'operazione congelata :  quando si azzera, la risorsa é libera).
 ** numero progressivo di schedulazione per la zona congelata (di passo 10)
 * legami tra le DS di risorsa generale e specifica

Nella figura seguente è rappresentato il legame tra i puntatori delle risorse (principale e specifica) :  da ogni risorsa specifica si può passare alla principale, e da essa scorrere la catena delle risorse specifiche.
![FIG_016](http://localhost:3000/immagini/S5IRIS_T11/FIG_016.png)Per velocizzare l'aggancio alle risorse specifiche, vegnono create le schiere : 
XRIKY (tipo + codice risorsa) e XRIPN (puntatore), caricate dalla fine (e quindi è significativo l'inizio £I07, a cui si puà accedere con le seguenti istruzioni : 
>  C                   EVAL      $Z=£I07
  C     AAA018        LOOKUP    XRIKY($Z)                     50


dopo queste istruzioni in XRIPN($Z) si ha il puntatore della risorsa



# DSALTE - Alternative
Per ogni impegno vengono scritte tante alternative quante sono le risorse su cui può essere eseguito.
La ds DSIRIS  dell'impegno conntiene una schiera dei puntatori alle sue alternative, ed il riempimento di questa schiera.
In assenza di alternative di fase, viene scritta dal programma S5SMES_01K e, se presente il filtro sulle risorse secondarie , completata dal programma S5SMES_02K.

Ogni elemento di questa DS contiene
 * il dettaglio dei tempi :  per lo stesso impegno sono normalmente uguali (originano dalla stessa riga di ciclo), possono diversificarsi se è stato deciso di applicare la percentuale di efficienza a livello di risorsda specifica, ed inolre possono essere modificati con programmi di aggiustamento (ad esempio se alcuni tempi sono inseritii nelle risorse secondarie).
 * riferimenti all'impegno
 * riferimenti alle risorse principali e specifiche
 * legami con altre DS

Se la risorsa è a capacità infinita o non sono attive le risorse specifiche viene scritta una sola alternativa.
In caso contrario vengono scritte tante alternative quante sono le risorse specifiche.
Se l'alterntativa è fissata (impegno iniziato, congelato o forzato) viene scritta solo quella.
In caso contrario, se è presente un  filtro di risorse specifiche, vengono scritte solo le alternative di risorse specifiche che soddisfano il filtro.
Se si verificano entrambe le condizioni precedenti, per poter presentare il filtro di risorse specifiche nel popup di scelta del Gantt, si riportano, nella schiera delle alternative di DSIRIS, dal secondo elemento, i pumtatori alle risorse specifiche del filtro. In qusto caso il numero di alternative è sicuramente uno, essendo la risorsa fissata, e quindi queste ulteriori informazioni non vengono trattate dai programmi, che scorrono la schiera fino al numero di riempimento.

E' possibile attivare la exit
 :  : DEC T(MB) P(BCDSRC) K(S5SMX_07X) L(1)
che permette di modificare dinamicamente il contenuto dell'altertnativa, ad esempio modificare i tempi di ciascduna di esse, se, ad esempio, variano per risorsa specifica. Questa exit opera a valle dell'eventuale applicazione dell'efficienza.


# DSIRS Impegni secondari La DSIRSE contirene le risorse secondarie legate ad un impegno risorse. Il modo di collegarsi a quest'ultimo avviene nel seguente modo : 
su ogni DSIRIS c'è il puntatore al primo DSIRSE a cui è legato.
su ogni DSIRSE ci sono i puntatori
al successivo DSIRSE  dello stesso impegno,
al primo DSIRSE dello stesso impegno (in modo da poter ripercorrere la catena)
al DSIRIS a cui appartiene
alla DSRSEC a cui appartiene
Gli impegni secondari sono costruiti in due modi : 

Un'ulteriore suddivisione è tra gli impegni secondari di risorse specifiche e di altre risorse (fisiche e umane).



# DSANGR - Gruppi e DSDEGR - Dettagli
Per ogni alternativa viene scritto un dettaglio di schedulazione, che è l'effettivo oggetto che viene schedulato (su cui si aggiornano gli istanti di inizio e fine schedulazione), oppure eliminato (se appartiene ad una risorsa specifica diversa da quella scelta).
In entrambi i casi viene aggiornato lo stato del dettaglio, che passa a schedulato o eliminato.
Il dettaglio contiene i seguenti campi principali
 * puntatori all'alternativa, alla risorsa specifica, all'impegno risorse
 * numero dei gruppo
 * flag di stato
 * istanti di inizio e fine scheduiazione, e di fine attrezzaggio (se previsto il calcolo).
Contestualmente alla scrittura dei dettagli, vengono costruiti i gruppi di schedulazione :  per ciascuno di essi viene scritto un elemento della DSANGR.
Questa DS contiene essenzialmente i seguenti campi
 * flag di stato
 * puntatore al primo record di dettaglio (in assoluto e non ancora schedulato). I dettagli sono infatto ordinati per gruppo, e all'interno del gruppo per : 
 * iniziati (in  ordine lifo di data ultima attività)
 * congelati (in ordine di risorsa e posizione)
 * liberi (in ordine di priorità manuale e criterio di ordinamento.
In questo modo leggendo i dettagli pronti di un gruppo si ha possibilità di scorrere le code esistenti sulle varie risorse specifiche. Se un dettaglio può essere eseguito su più risorse specifiche esso viene riportato più volte (in elementi contigui).
Il programma che riempie queste DS è S5SMES_05

Nella figura seguente è rappresentato il legame tra gli impegni risorse, alternative e dettagli.

![FIG_018](http://localhost:3000/immagini/S5IRIS_T11/FIG_018.png)
![FIG_018leg](http://localhost:3000/immagini/S5IRIS_T11/FIG_018leg.png)
Nella figura seguente è rappresentato il legame tra gruppo e dettagli, questi ultimi suddivisi nelle sezioni descritte in precedenza. In questa figura è rappresentata la situazione dopo aver schedulato le operazioni iniziate, e quindi i puntatori alla prima operazione del gruppo (D1) e alla prima non schedulata (D3) sono diversi.
![FIG_019](http://localhost:3000/immagini/S5IRIS_T11/FIG_019.png)
Il motivo della duplicazione della memoria in alternative e dettagli, che appartenetemente sono in corrispondenza biunivoca, è duplice.
* data la limitazione delle DS multiple, la suddivisione in più DS consente di estendere le informazioni
* in caso di altrnative di ciclo (funzione attualmente non implementata) la corrispondenza tra alternatve e dettagli non è più biunivoca

# DSSINT - Sintesi
Contengono le informazioni riassuntive per ogni ordine
 * dati generali
 * inizio e fine schedulatzione
 * situazione dei materiali (se attivato il calcolo)
 * legami con altri ordini (se attivati i legami statici)

Nella figura seguente è rappresentato il legame tra i puntatori delle sintesi e gli impegni risorse :  da ogni impegno si  risorse si può passare alla prima sintesi, e da essa passare al primo impegno e quindi scorrere, in sequenza, tutti gli impegni dell'ordine
![FIG_017](http://localhost:3000/immagini/S5IRIS_T11/FIG_017.png)![FIG_016](http://localhost:3000/immagini/S5IRIS_T11/FIG_016.png)![FIG_018](http://localhost:3000/immagini/S5IRIS_T11/FIG_018.png)![FIG_018leg](http://localhost:3000/immagini/S5IRIS_T11/FIG_018leg.png)![FIG_019](http://localhost:3000/immagini/S5IRIS_T11/FIG_019.png)![FIG_017](http://localhost:3000/immagini/S5IRIS_T11/FIG_017.png)