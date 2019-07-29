# Obiettivo
Fornire un documento operativo utile a chi deve interrogare gli ordini di produzione.

# Sintesi Ordini
La sintesi ordini raggruppa tutte le principali visualizzazioni che si possono fare a fronte di un ordine di produzione.
Per chi ha già il documento di gestione degli ordini queste modalità sono le stesse che sono state descritte tra le funzioni oggetto dell'ordine di produzione.

Dato un ordine di produzione la sintesi si lancia attraverso questo formato : 

![P5_01_06](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_06.png)
## Funzioni ordine
Presenta, la lista delle funzioni di oggetto (F10) associate all'ordine in input : 

![P5_01_04](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_04.png)
Tra le funzioni presenti possiamo elencare : 

### Proprietà
Presenta il formato di dettaglio dell'ordine : 

![P5_01_01](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_01.png)
### Attributi
Presenta, in modo simile alla lista campi, tutte le informazioni associate all'oggetto in questione, ma oltre ai dati del record mostra anche altri attributi associati al record in maniera dinamica (cfr Doc. Applicativa B£OGAT Oggetto Attributo) : 

![P5_01_09](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_09.png)
### Numeri
Presenta i valori numerici dell'ordine : 

![P5_01_08](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_08.png)
### Lista campi
Presenta tutti i campi del record come sono memorizzati sul file : 

![P5_01_05](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_05.png)
di default vengono presentati solo i campi compilati, è possibile vedere anche i campi vuoti.

### Parametri per tipo
Se all'ordine di produzione, attraverso la customizzazione, è  stata attribuita la facoltà di gestire dei parametri aggiuntivi, questa opzione rimanda alla loro gestione (cfr Doc. Applicativa C£PARA Parametri).

### Ordini dipendenti
Ad un ordine di produzione si possono collegare N. ordini (es. quelli che servono per la produzione dei componenti) che si vogliono considerare come un unico raggruppamento. Questa funzione mostra l'elenco di tali ordini : 

![P5_01_11](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_11.png)
### Funzioni oggetto
Rimanda al formato delle funzioni (F10) dell'articolo presente nella testata ordine.

### Funzioni generali
Presenta, in funzione dell'opzione scelta, varie informazioni di carattere generale : 

![P5_01_07](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_07.png)
_2_Dati ordine
Presenta il formato di dettaglio dell'ordine

_2_Sintesi
Presenta i valori numerici dell'ordine : 

![P5_01_08](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_08.png)
_2_Dettaglio quantità
È la stessa interrogazione quantità che si può vedere da formato di dettaglio dell'ordine.

_2_Dettaglio date
È la stessa interrogazione date che si può vedere da formato di dettaglio dell'ordine.

_2_Ordini collegati
È la stessa interrogazione 'Ordini dipendenti' vista in precedenza.

_2_Funzioni oggetto
È la stessa interrogazione sulle funzioni articolo vista in precedenza.

_2_Ordini conto lavoro collegati
È valida nel caso di conto lavoro di fase, cioè quando una o più delle operazioni del ciclo di lavorazione associato all'ordine viene fatta all'esterno presso terzisti, a fronte di ciascuna di queste lavorazioni esterne può essere generata una riga di ordine di conto lavoro (Conto Lavoro di Fase). Questa funzione permette di interrogare tali righe ordine.

### Funzioni sui materiali
Presenta, in funzione dell'opzione scelta, varie informazioni legate ai componenti utilizzati nell'ordine : 

![P5_01_10](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_10.png)
_2_Distinta documento
Mostra la distinta dei materiali utilizzati dall'ordine di produzione, se scelta la funzione di riepilogo le quantità saranno sommate a parità di componente.
La distinta del documento è quella legata all'ordine di produzione, oppure (se questa manca ed in fase di customizzazione si è impostata la risalita) è la distinta base dell'articolo.

_2_Distinta memorizzata
È la distinta, se presente, legata all'ordine.
Una delle modalità di gestione della distinta del documento è la _5_'variazione' si applica quando la normalità è l'utilizzo della sola distinta base e in caso di eccezione di portare variazioni a questa (es. se un componente manca e si utilizza un componente alternativo) in questo caso se si impiega la distinta di variazione andremo a inserire solo i due componenti :  quello mancante (con qtà negativa) e quello in sostituzione con (qtà positiva) se esiste la distinta di variazione il sistema determina la distinta del documento partendo dalla da tinta base e filtrandola attraverso la distinta di variazione.

_2_Impegni residui
Presenta la lista dei materiali che ancora devono essere prelevati a fronte dell'ordine (totale fabbisogni meno fabbisogni già prelevati).

_2_Movimenti eseguiti
Se si sceglie questa funzione bisogna indicare lo schema informazioni da usare in fase di presentazione (cfr. Doc. Operativa B£_SCH Schemi di visualizzazione / stampa) e il tipo movimento da visualizzare, tipicamente VP per vedere i movimenti di versamento o PP per vedere i movimenti di prelievo.

_2_Materiali alla fase
Indicare la fase del ciclo di lavorazione della quale si vogliono vedere i componenti che utilizza. Se nella distinta base non viene specificata una operazione di impiego il sistema assegna tutti i materiali alla prima fase.

_2_Copertura impegni
Richiede l'impostazione delle opzioni di analisi : 

![P5_01_12](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_12.png)
quindi esegue l'analisi evadibilità (cfr. Doc. Operativa V5SP10 Analisi evadibilità ) : 

![P5_01_13](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_13.png)
_2_Richieste movimentazione collegate
Se per l'ordine sono già state generate le liste prelievo (cfr. Doc. Operativa GMRM01 - GMRM10 Richieste di movimentazione) la funzione le presenta.

### Funzioni su risorse
Presenta, in funzione dell'opzione scelta, varie informazioni legate al ciclo ed agli impegni di risorsa produttiva utilizzati nell'ordine : 

![P5_01_14](http://localhost:3000/immagini/MBDOC_OGG-P_P5SI02/P5_01_14.png)
_2_Ciclo documento
Mostra il ciclo di lavorazione utilizzato dall'ordine di produzione.
Il ciclo del documento è quello legato all'ordine di produzione, oppure (se questo manca ed in fase di customizzazione si è impostata la risalita) è il ciclo dell'articolo.

_2_Ciclo memorizzato
È il ciclo, se presente, legato all'ordine.

_2_Impegni residui
Presenta la lista delle operazioni che ancora devono essere eseguite a fronte dell'ordine (totale fabbisogni risorse meno attività già eseguite).

_2_Attività eseguite
Se si sceglie questa funzione bisogna indicare lo schema informazioni da usare in fase di presentazione (cfr. Doc. Operativa B£_SCH Schemi di visualizzazione / stampa), se è indicata una fase vengono visualizzate solo le attività dichiarate a fronte della fase in input, se la fase è blank si presentano tutte le attività.

_2_Sintesi avanzamento
Di default vengono visualizzate solo le informazioni relative all'ultima fase dichiarata, in alternativa si vedono le informazioni di tutte le fasi dichiarate.

_2_Ciclo logistico
Permette di vedere solo le faci logistiche oppure tutte ed i materiali assegnati a ciascuna fase visualizzata.

_2_Statistiche avanzamento
Se sono state dichiarate delle attività di produzione per l'ordine, con questa funzione si possono vedere dei dati statistici (es. numero operazioni tatli, eseguite, in corso e da iniziare, ecc..).
