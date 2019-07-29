
## OBIETTIVO
Permettere di poter applicare/calcolare la rettifica relativa ai superammortamenti previsti dalla legge di stabilità 2016.

## NOTE SUI DATI DI INPUT
* Azienda :  codice azienda da elaborare
* Esercizio :  indica l'esercizio per il quale vogliono essere calcolate le rettifiche
* Linea % Ministeriali :  la maggiorazione è applicabile solo in considerazione della quota di ammortamento definita dal Dm 31 dicembre 1988, per tale motivo, se nessuna delle linee in uso, corrisponde a tali % è necessario creare una linea apposita, sulla quale definire un piano di ammortamento che presenti le corrette % di ammortamento. NOTA BENE :  per il corretto calcolo della maggiore deduzione fiscale sarà necessario effettuare il calcolo ammortamenti per questa linea
* Cespiti esclusi :  come si vedrà a seguire è possibile escludere manualmente alcuni cespiti, tramite questo campo sarà possibile decidere se visualizzare o meno i cespiti cui è stata applicata tale esclusione.
* Causale Rettifica :  è un dato opzionale. Attraverso esso si può decidere di creare un movimento di rettifica che avrà il solo scopo di evidenziare nella stampa del registro il maggior ammortamento applicato.
**NOTA MOLTO BENE** :  la causale qui utilizzata deve avere le seguenti caratteristiche : 
 * Tipo movimento AL (Rettifica fiscale)
 * NESSUN totalizzatore indicato.
Questo perchè l'effetto finale sarà solo di avere la colonna ammortamento aumentata (con l'evidenza del subtotale di rettifica) senza andare a toccare i totali di capitale, fondo e residuo da ammortizzare. E' inoltre importante che venga indicata una causale appositamente creata per l'identificazione di questa agevolazione (altrimenti le azioni di generazione/cancellazione dei movimenti potrebbero operare in modo errato).

## DATI DI OUTPUT
Confermando i dati di input verrà presentato un prospetto con i cespiti presi in considerazione.
Si tratta dei cespiti aventi le seguenti caratteristiche : 
* Se il cespite è nuovo (cosa che viene riconosciuta dal fatto che in anagrafica cespite non è stato valorizzato il campo "cespite usato")
* Se il cespite ha una data di riferimento compresa fra il 15/10/2015 ed il 31/12/2017. La data di riferimento viene determinata secondo la riclassifica riportata a seguire : 
** Per prima viene presa in considerazione la data specifica "Data riferimento superammortamento" che può essere indicata a livello di anagrafica cespite nei parametri per linea (tramite il tasto funzione F10, opzione parametri fissi e poi selezionando la linea di riferimento per le % ministeriali).
** In assenza della precedente data viene controllato se è presente una "Data inizio ammmortamento" indicata sull'anagrafica cespite
** In assenza della precedente data viene presa in considerazione la data documento del primo movimento d'acquisto
** In assenza della precedente data viene presa in considerazione la data ammortamento del primo movimento d'acquisto
** In assenza della precedente data viene presa in considerazione la data registrazione del primo movimento d'acquisto
* Se il cespite appartiene ad una categoria cespiti (tabella A5A) che NON è immateriale (quindi materiale)
* Se il cespite ha un aliquota ministeriale superiore a 6,5%
* A partire dal 2016, verranno esclusi i cespiti che sono stati completamente ammortizzati in un esercizio precedente.
* A partire dal 2017, verranno inoltre esclusi i cespiti che sono stati alienati in un esercizio precedente a quello in analisi.
* I cespiti che pur rientrando in tutti i parametri precedenti hanno una data inizio ammortamento successiva all'esercizio preso in considerazione. Verranno presi in considerazione a partire dall'esercizio in cui inizierà l'ammortamento (si assume che questa informazione vada a coincidere con la data di entrata in funzione del cespite).
* Se il cespite non ha iperammortamenti sull'intero capitale nell'esercizio selezionato.

Sarà poi possibile procedere all'esclusione manuale di determinati cespiti all'interno dell'interrogazione stessa come precisato più avanti in questo documento.

## Dati incolonnati
* Capitale :  è il valore del capitale alla fine dell'esercizio indicato in input. Qulora per il cespite ci siano degli incrementi di capitale soggetti ad iperammortamento questi vengono decurtati dal capitale.
* Percentuale Maggiorazione :  fino al 31/12/2017 è pari al 40%.Dal 01/01/2018 è pari al 30% ma può essere modificata tramite l'opzione P portandola al 40%
* Capitale * %Maggiorazione :  è il valore del capitale moltiplicato per la percentuale di maggiorazione di costo storico prevista dalla legge di stabilità 2016 e successive circolari 2017.
* Maggiorazione Teorica :  è calcolato applicando la percentuale prevista sulla linea ministeriale alla maggiorazione di capitale riportata nella precedente colonna.
* Maggiorazione Effettiva :  è la maggiorazione che si è deciso di apportare. Può coincidere con la maggiorazione teorica o meno a seconda delle azioni che vengono eseguite.

**NOTA BENE** :  anche se non vengono creati i movimenti di rettifica è **FONDAMENTALE** per il corretto funzionamento del pgm che le rettifiche decise vengano sempre confermate attraverso le opzioni "X" ed "M" riportate a seguire.

## Totali
* Se vengono apportate esclusioni o modifiche agli importi per vedere l'aggiornamento dei totali è necessario premere F05

* A meno che non si sia scelta la visualizzazione dei soli cespiti esclusi, i cespiti esclusi se visualizzati vengono comunque esclusi dati totali

## Indicazioni particolari
* Capitale con inversione di fondo indica che al capitale è stato applicato il limite massimo ammortizzabile, ripreso dalla tabella della categoria ed incrementato a sua volta della percentuale di maggiorazione

* Aliquota sottolineata indica, che il cespite è nel primo anno di ammortamento e che per questo l'aliquota è stata dimezzata del 50%.

* Se l'aliquota è in alta intensità significa inoltre che è stata applicata un'aliquota non deducibile

# AZIONI ESEGUIBILI
* Opzioni applicabili al singolo cespite : 
** SK :  Scheda Cespite, mi permette di andare a richiamare la scheda di analisi del singolo cespite
** X  :  Applica/Disapplica, mi permette di confermare la maggiorazione teorica come maggiorazione effettiva, oppure se era già stata definita una maggiorazione effettiva di annullarla
** M  :  Modifica, mi permette di applicare una maggiorazione differente da quella teorica
** E  :  Escludi Cespite, mi permette di escludere il cespite dai calcoli. NOTA :  Questa opzione è valida solo per l'esercizio di acquisizione del cespite.
** R  :  Ripristina esclusione :  se il cespite era stato escluso può essere ripristinato
** P  :  Modifica % :  solo dal 01/01/2018 è possibile modificare la percentuale di maggiorazione. Il default sarà il 30%, qualora si voglia cambiarla è possibile farlo tramite questa opzione

* Tasti Funzione : 
** F06 = mi permette di creare o ricreare i movimenti di rettifica per il libro cespiti
** F16 = mi permette di cancellare gli eventuali movimenti di rettifica creati sul libro cespite

**NOTA BENE** : 
* verranno presi come importi i soli importi che sono stati caricati come maggiorazioni effettive
* tali funzioni sono disponibili solo se viene indicata una causale nei dati di input
* le medesime funzioni di disattivano quando la linea fiscale per il periodo indicato è stata chiusa

## NOTE AGGIUNTIVE
### Importo limite ammortizzabile e % non deducibile
Il superammortamento deve tenere conto del limite massimo ammortizzabile. In presenza di cespiti di valore superiore al limite, il capitale e la percenutali di maggiorazione saranno esposti e calcolati su tale valore invece che sul valore reale del cespite. Il limite massimo ammortizzabile, andrà impostato sulla tabella della categoria cespite (A5A).

In modo similare qualora sia prevista per il bene una quota non deducibile, tale quota dovrà essere presa in considerazione per il calcolo del superammortamento. La quota indeducibile può essere indicata a livello di categoria cespite (nella tabella A5A), oppure a livello di piano ammortamento indicano una aliquota con causale d'ammortamento non deducibile (a modello AN0).

### Variazioni valore cespite
In merito a variazioni di valore, positive o negative, non sussiste una regolamentazione chiara.
Rispetto a tali operazioni in Smeup al momento viene sempre preso in considerazione il valore del bene a fine esercizio (quindi, compresivo di qualsiasi variazione positiva o negativa).

Unica eccezione la fa l'operazione di alienazione o vendita totale che è stata invece stata espressamente regolamentata :  ad essa va applicata il criterio pro rata temporis, per cui anche nell'anno di alienazione/vendita verrà considerata la maggiorazione sulla quota di capitale corrispondente al n° di giorni di possesso del cespite nell'esercizio.

