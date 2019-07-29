# Generalità
Le parzializzazioni sono uno strumento, comune a tutto Sme.up, con cui si può filtrare una lista di oggetti (es. una lista di articoli, di clienti, di ordini, ecc..)
Il filtro permette di  definire il range dei dati da visualizzare secondo le esigenze individuali.

Certe parzializzazioni, dove è stato ritenuto utile, hanno la possibilità di rappresentare la lista dei dati filtrati in modo ordinato secondo un ordine scelto tra quelli previsti per quella specifica parzializzazione.

Le modalità di utilizzo sono le stesse in tutto Sme.up.

# Formati video

Le parzializzazioni si possono attivare in modi diversi, tra questi, dal formato guida (ovvero dalla schermata di deifnizione dei parametri di lancio di un programma) o dal formato lista (ovvero dalla schermata in cui viene restituita la lista di oggetti interrogati) attraverso il tasto F13.

Se richiamate si presenta un formato video con un layout simile al seguente : 

![B£_01_01](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_01.png)
Nella parte superiore della schermata possono essere impostati l'ordinamento dei record restituiti dall'interogazione e lo schema di visualizzazione; nella parte centrale si trovano i campi che è possibile parzializzare mentre nella parte inferiore è possibile impostare la scansione degli oggetti restituiti dall'interrogazione.
Quando la lista è filtrata il tasto F13 è illuminato per indicare che la lista è filtrata.


## Utilizzo dei limiti
I limiti servono per filtrare la lista da un valore inferiore ad uno superiore, se sono compilati più limiti contemporaneamente il filtro si applica a tutti (in and).

### Convenzioni
Se il limite iniziale è bianco per convenzione si intende dall'inizio.
Esempio : 

|  Nam="Tabella1" |
| Limiti|Iniziale|Finale |
| ---|----|----|
| Provincia||RRRRRR |
| 

viene presentata la lista dei clienti che hanno nel campo provincia un valore compreso tra blank e RRRRRR.

Se il limite finale è asterisco ('*') per convenzione si intende fino alla fine.
Esempio : 

|  Nam="Tabella2" |
| Limiti|Iniziale|Finale |
| ---|----|----|
| Provincia|BBB|* |
| 

viene presentata la lista dei clienti che hanno nel campo provincia un valore maggiore o uguale a BBB.

Se è compilato solo il limite iniziale e quello finale è bianco viene impostato il limite finale uguale a quello iniziale.
Esempio : 

|  Nam="Tabella3" |
| Limiti|Iniziale|Finale |
| ---|----|----|
| Provincia|AN| |
| 

viene presentata la lista dei clienti che hanno nel campo provincia il valore AN.

Se limite iniziale e finale sono  bianchi vengono impostati a blank e *.
Esempio : 

|  Nam="Tabella4" |
| Limiti|Iniziale|Finale |
| ---|----|----|
| Provincia|| |
| 

diventa

|  Nam="Tabella5" |
| Limiti|Iniziale|Finale |
| ---|----|----|
| Provincia||* |
| 



## Utilizzo scansione
Alcuni formati di parzializzazione prevedono anche la "scansione", che si applica a codice e descrizione ed esegue la ricerca degli elementi che contengono i caratteri voluti, come da esempi seguenti.
Esempi : 

|  Nam="Tabella6" |
| Scansione|| |
| ---|----|----|
| |Descrizione|*SPA |
| 

Presenta tutti i clienti dove la descrizione finisce con i caratteri SPA


|  Nam="Tabella7" |
| Scansione|| |
| ---|----|----|
| |Descrizione|SA* |
| 

Presenta tutti i clienti dove la descrizione inizia con i caratteri SA


|  Nam="Tabella8" |
| Scansione|| |
| ---|----|----|
| |Descrizione|*SA* |
| 

Presenta tutti i clienti dove la descrizione contiene i caratteri SA in una posizione qualsiasi


|  Nam="Tabella9" |
| Scansione|(posizionale)| |
| ---|----|----|
| |Descrizione|   TT |
| 

(nel campo scansione è stato scritto blank, blank, blank, T, T)
Presenta tutti i clienti in cui la descrizione presenta i caratteri TT nella quarta e quinta posizione.


## Parametri interni
È presente solo in particolari formati e, se selezionato : 

![B£_01_02](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_02.png)
mostra un ulteriore formato di filtro sui parametri interni : 

![B£_01_03](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_03.png)
Selezionando opportunamente il valore del parametro specifico, si decodificano sia i parametri alfabetici che quelli numerici ed è possibile impostare questo ulteriore filtro.

## Ordinamento
Permette di ordinare la lista secondo uno degli ordinamenti previsti, nel caso particolare : 
1. Ordina la lista per codice
2. Ordina la lista per ragione sociale
3. Ordina la lista per categoria
4. Ordina la lista per descrizione breve
5. Ordina la lista per località

![B£_01_04](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_04.png)
### Tipo ordinamento
Di default è ascendente, se inserito D l'ordine di presentazione diventa discendente : 

![B£_01_05](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_05.png)
## Schema
Determina le colonne che saranno presentate nella lista
- [Schemi di visualizzazione e stampa](Sorgenti/MB/DOC_OPE/B£_SCH)

![B£_01_06](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_06.png)
## Memorizzazione dati video
È possibile impostare dei parametri di filtro più o meno complessi e memorizzarli per poi richiamarli e riutilizzarli successivamente
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

![B£_01_07](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_07.png)
## Parzializzazioni aggiuntive
Quando i campi di parzializzazione sono numerosi al punto da eccedere le righe visualizzabili in una sola schermata è possibile, attraverso il tasto F13 passare ad un secondo formato di parzializzazioni.

Da questa videata di ulteriori parzializzazioni si ritorna alla schermata principale nuovamente attraverso il tasto F13.

![B£_01_08](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_01_08.png)
## Parzializzazioni esterne
Oltre alle normali parzializzazioni che filtrano la lista basandosi sui campi dell'archivio, esistono delle parzializzazioni (parzializzazioni esterne) che permettono di filtrare anche attraverso dati esterni all'archivio.

Possono essere manualmente definiti dei gruppi di oggetti (es. gruppi di articoli) oppure delle caratteristiche (attributi) per le quali poi si apre una nuova finestra di impostazione limiti.

Inserendo "G" (gestione scenario) nel campo a destra delle parzializzazioni esterne e caratterizzato da >>, si apre una finestra contenente l'elenco di tutti gli scenari generati, che possono essere gestiti con le normali opzioni (1 = inserimento, 2 = modifica, ecc..).

Quando si inserisce un nuovo scenario, se il campo "Filtro batch" è = 1 significa che il filtro sarà costituito da un insieme di attributi :  quando nel campo >> si inserisce un "B" si apre una videata in cui definire quali sono gli attribuiti dell'oggetto da definire come ulteriori filtri.
Una volta definiti i filtri aggiuntivi, quando in parzializzazione si richiama questo scenario e si inserisce nel campo >> una "X"

![B£_04_05](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_04_05.png)
si presenta la videata delle parzializzazioni aggiuntive su cui impostare i nuovi filtri.

![B£_04_06](http://localhost:3000/immagini/MBDOC_OPE-B£_PAR/BX_04_06.png)

Se invece il campo "Filtro batch" è blank significa che il filtro sarà definito manualmente dall'utente :  quando nel campo >> si inserisce un "X" si apre una videatain cui inserire, via F15, uno ad uno, gli oggetti che costituiscono il filtro.
Quando in parzializzazione si richiama questo scenario saranno presentati solo gli oggetti citati nel filtro.
