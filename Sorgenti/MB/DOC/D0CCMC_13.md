# Costo  Base

Il costo base è un costo il cui calcolo è relativo alla politica dell'oggetto.

Sono implementate le seguenti politiche : 
* >Acquisto
* >Lavorazione
* >Produzione

## Acquisto
Un oggetto con politica di acquisto è un oggetto che viene interamente acquistato.
Il costo di acquisto è deteminato direttamente dalla lettura del tipo costo indicato come "Costo Materiale Acquisto" nei parametri di lancio.
Il costo è un valore unico.
L'indice di costo di default è quello presente nella tabella "D0D" come "Materiale", "Variabile".
E' possibile attribuire un indice di costo diverso da quello di default mediante un programma di exit (vedi Completamento costi, Struttura).
Il costo di acquisto può essere ricaricato di un valore calcolato a partire dal suo costo.
L'indice di ricarica di default è quello del costo di acquisto, in questo caso il risultato finale è un unico valore, dove però non è più possibile distinguere il costo di acquisto dal costo di ricarica.
Nel caso si volesse tenere i due valori separati è necessario attribuire un indice di costo specifico per la ricarica.

## Lavorazione
Un oggetto con politica di lavorazione è un oggetto che viene interamente lavorato da un ente esterno a cui si forniscono dei materiali.
Il suo costo è determinato da due componenti : 
* >Lavorazione
Il costo di lavorazione è deteminata direttamente dalla lettura del tipo costo indicato come "Costo Lavor.Est.Pieno" nei parametri di lancio.
Il costo è un valore unico.
L'indice di costo di default è quello presente nella tabella "D0D" come "Lavorazione esterna", "Variabile".
E' possibile attribuire un indice di costo diverso da quello di default mediante un programma di exit (vedi Completamento costi, Struttura).
Il costo di lavorazione può essere ricaricato di un valore calcolato a partire dal suo costo.
L'indice di ricarica di default è quello del costo di lavorazione, in questo caso il risultato finale è un unico valore, dove però non è più possibile distinguere il costo di lavorazione dal costo di ricarica.
Nel caso si volesse tenere i due valori separati è necessario attribuire un indice di costo specifico per la ricarica.

* >Materiali
Il costo dei materiali è la somma dei costi di tutti i componenti presenti al primo livello di distinta dell'oggetto in lavorazione.
Il costo di ciaccun componente è deteminato nel seguente modo : 
** Se valorizzato il campo "Costo Compon.Produzione" dei parametri di lancio" , direttamente dalla lettura di questo tipo di costo;
** Se non valorozzato il campo "Costo Compon.Produzione" nei parametri di lancio", dallo stesso tipo costo che si sta calcolando. In questo caso è necessario verificare che sia stato eseguito correttamente il ricalcolo del low-leve code degli oggetti in calcolo. Questo garantisce che prima vengano calcolati i costi di oggetti che serviranno poi a calcolare i costi di oggetti successivi.
Il costo non è un valore unico ma un schiera di valori
Di default solo l'indice di costo definito come "Materiali", "Variabile" in tabella "D0D", viene riportato nello stesso indice di costo del padre.
_7_Se nei materiali si gestiscono diversi indici di costo,  è necessario compilare il campo "Liv.Inf.Corrispondente" della tabella "IGI". Solo questi indici sono portati nel costo del padre
I costi di componenti con politica di acquisto sono messi allo stesso livello o a livello inferione del padre in funzione del campo "1° liv.Dist. in LIV" nella taella "D01"


## Produzione
Un oggetto con politica di produzione è un oggetto che viene prodotto dall'azienda con fasi di lavorazione interne e/o esterne e con l'utilizzo di materiali.
Il suo costo è determinato da due componenti : 
* >Produzione
Il costo di produzione è deteminato dal costo di ciascuna fase di lavorazione del ciclo di produzione.
Le fasi di lavoro sono di due tipi
** _9_Lavorazioni Interne
Il costo di lavorazione interna è determinato dai componenti di costo del ciclo moltiplicati per i corrispondenti valori di aliquote orarie.
I componenti di costo sono determinati dalla scansione del ciclo.
Le aliquote orarie sono determinate dalla lettura del tipo costo indicato come "Costo Aliquote" nei parametri di lancio.
Il costo è una serie di valori calcolati così come indicato dalla tabella "D0C". La struttura della "D0C" associa ciascuna aliquota oraria alle varie componenti di costo del ciclo e ai corrispondenti indici di costo per determinarne rispettivamente il valore e la destinazione nella struttura del costo. E' possibile attribuire un indice di costo diverso da quello di default della tabella "D0C" mediante un programma di exit (vedi Completamento costi, Struttura).
** _9_Lavorazioni Esterne
Vedi "Lavorazione" in politica lavorazione
Con le seguenti differenze : 
*** nei parameri di lancio il tipo costo è quello indicato come "Costo Lavor.Est.Fase".
*** viene determinato per la fase del ciclo, o dall'operazione se indicato dalla voce "Costo Fase per Operaz " nei parametri di lancio
*** viene determinato con l'ente, se presente, a cui appartene la fase del ciclo  e se indicato nella voce "Forn.Lav.Est.da Ciclo" nei parameti di lancio
* >Materiali
Vedi "Materiale" in politica Lavorazione.

## Ricariche oggetto
Determinato il costo dell'oggetto è possibile eseguire 9 ricariche finali.
Per il calcolo di ciascuna ricarica si hanno a disposizione tutte le voci di costo del costo finale. Sia del costo primo che del costo che ha subito ricariche precedenti.
L'indice di costo di defalut per ciscuna ricarica è definito nella tabella "D0D"
E' possibile attribuire un indice di costo diverso da quello di default mediante un programma di exit (vedi Completamento costi, Struttura).

## Nota Ricariche
il metodo di ricariche standard si basa sulla classe materiale dell'articolo.
Nella tabella "CLS" delle classi materiali deve essere indicato l'elemento della tabella "CSR" famiglia di ricariche.
In ogni caso il programma risale all'ememnto "***". (Generalmente in Smeup il default sono 2 asterischi, in questo caso sono 3)
La tabella "CSR" delle famiglie di ricariche definisce la modalità di ricarica.
Poichè la tabella si basa sull'oggetto articolo mentre ll caolco costi è eseguibile per qualunque oggetto, è stata estesa la sua funzionalità introducendo la gestione di un nuovo medoto "U" utente. Questo metodo è un programma di exit dove si può calcolare il valore della ricarica e indicarne l'indice di costo.



========================================================================

## Logiche di Calcolo

Il calcolo >"BASE" permette di generare un costo calcolato assumendo : 
 * Elementi di >Distinta Base e aggregandogli un >costo di Materiale, piuttosto che di semilavorato
 * Elementi di >Ciclo di lavoro e moltiplicandolo per le >aliquote assegnate alle risorse a cui appartengono quelle fasi di ciclo

>Elementi di Distinta Base possono essere : 
 * La distinta >standard dell'oggetto articolo
 * La distinta >effettiva di un oggetto, quale un articolo, un ordine, una riga di documento di conto lavoro, un lotto o una commessa; con possibilità di derivare la distinta di un qualsiasi oggetto da quella di un oggetto di livello più alto, oppure, nel caso di documento passivo, derivare la distinta della bolla di entrata da quella dell'ordine di acquisto che ha contribuito a generarlo.
 * La distinta  >consuntiva di un oggetto, generata nel valutare i movimenti di prelievo a magazzino (  _9_GMMOVI ) assegnati a quello specifico oggetto.

>Elementi di Ciclo di lavoro possono essere : 
 * Il ciclo >standard dell'oggetto articolo
 * Il Ciclo >effettivo di un oggetto, quale un articolo, un ordine,  un lotto o una commessa; con possibilità di derivarlo per un qualsiasi oggetto da quello di un oggetto di livello più alto.
 * Il Ciclo  >consuntivo di un oggetto, generato dal riepilogo delle attività produttive rilevate (  _9_P5ATTI ) per quello specifico oggetto.

>Elementi di Costo del Materiale e/o Semilavorato che possono essere assunti : 
 * Costi legati all'ultimo documento di entrata (bolla) di quel materiale
 * Costi legati all'ultimo ordine di acquisto di quel materiale
 * Costi medi del materiale e/o del semilavorato
 * Costi di listino del materiale e/o del semilavorato
 * Costi manuali legati al materiale e/o semilavorato

>Aliquote assegnate alle risorse che possono essere : 
 * Attribuite al Centro di Costo assegnato alla risorsa presente sulla fase
 * Attribuite alla Risorsa impostata sulla fase del ciclo
 * Attribuite alla Risorsa impostata sulla fase del ciclo e se non trovata l'aliquota, risalita fino al Centro di Costo assegnato a quella risorsa

## Lancio Calcolo costo Base Multicontesto
 :  : INI Esecuzione Calcolo costo Base Multicontesto >>
 :  : CMD CALL D0CO01B
 :  : FIN


## Autorizzazioni
_7_Documentazione in fase di sviluppo

## Impostazioni

Le impostazioni del calcolo costi si dividono in varie sezioni

![D0CCMC_21A](http://localhost:3000/immagini/D0CCMC_13/D0CCMC_21A.png)
### Impostazioni di Estrazione
Le impostazioni di estrazione sono specifiche per tipo contesto

### Impostazioni di Estrazione - Contesto AR (Articolo)
![D0CCMC_21B](http://localhost:3000/immagini/D0CCMC_13/D0CCMC_21B.png) * Ricalcolo LowLevelCode Si/No. Il LowLevelCode serve per ricalcolare i componenti base (di acquisto) prima degli altri così da calcolare gli articoli in sequenza discendente rispetto all'ordinamento di utilizzo nella distinta base presente nel parametro relativo della tabella >TCO specifica di quel tipo costo.

### Impostazioni di Estrazione - Contesto DR (Documento)
![D0CCMC_21C](http://localhost:3000/immagini/D0CCMC_13/D0CCMC_21C.png)
_7_Documentazione in fase di sviluppo

### Impostazioni di Estrazione - Contesto OR (Ordine Prodiuzione)
![D0CCMC_21D](http://localhost:3000/immagini/D0CCMC_13/D0CCMC_21D.png)
- [Calcolo costo di un oggetto](Sorgenti/MB/DOC_OGG/P_D0CO01B)

_7_Documentazione in fase di sviluppo


### Impostazioni di Calcolo
_7_Documentazione in fase di sviluppo

### Impostazioni di Completamento
_7_Documentazione in fase di sviluppo

### Impostazioni di Documentazione ed Errori
_7_Documentazione in fase di sviluppo

### Impostazioni di Memorizzazione
_7_Documentazione in fase di sviluppo


## Controllo dei risultati
_7_Documentazione in fase di sviluppo

