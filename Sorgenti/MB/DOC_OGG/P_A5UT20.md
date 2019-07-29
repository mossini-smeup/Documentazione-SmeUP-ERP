
## OBIETTIVO
Permettere di poter applicare/calcolare la rettifica relativamente agli iperammortamenti previsti dalla CIRCOLARE N.4/E del 30/03/2017.
In particolare la maggiorazione prevista è del 150% per i beni materiali ed il 40% per i beni immateriali

## NOTE SUI DATI DI INPUT
* Azienda :  codice azienda da elaborare
* Esercizio :  indica l'esercizio per il quale vogliono essere calcolate le rettifiche
* Linea % Ministeriali :  la maggiorazione  è applicabile solo in considerazione della quota di ammortamento definita dal Dm 31 dicembre 1988, per tale motivo, se nessuna delle linee in uso, corrisponde a tali % è necessario creare una linea apposita, sulla quale definire un piano di ammortamento che presenti le corrette % di ammortamento. NOTA BENE :  per il corretto calcolo della maggiore deduzione fiscale sarà necessario effettuare il calcolo ammortamenti per questa linea
* Causale Rettifica :  è un dato opzionale. Attraverso esso si può decidere di creare un movimento di rettifica che avrà il solo scopo di evidenziare nella stampa del registro il maggior ammortamento applicato. E' consigliabile utilizzare una causale differente dal superammortamento.
* Cespiti esclusi :  come si vedrà a seguire è possibile escludere manualmente alcuni cespiti, tramite questo campo sarà possibile decidere se visualizzare o meno i cespiti cui è stata applicata tale esclusione.
* Funzione :  la funzione 1 permette di selezionare i movimenti di acquisto soggetti ad iperammortamento, mentre la funzione 2 è l'applicazione della rettifica relativa all' iperammortamento.
**NOTA MOLTO BENE** :  la causale qui utilizzata deve avere le seguenti caratteristiche : 
 * Tipo movimento AL (Rettifica fiscale)
 * NESSUN totalizzatore indicato.
Questo perchè l'effetto finale sarà solo di avere la colonna ammortamento aumentata (con l'evidenza del subtotale di rettifica) senza andare a toccare i totali di capitale, fondo e residuo da ammortizzare. E' inoltre importante che venga indicata una causale appositamente creata per l'identificazione di questa agevolazione (altrimenti le azioni di generazione/cancellazione dei movimenti potrebbero operare in modo errato).


### FUNZIONE 1 :  SELEZIONA MOVIMENTI
Tramite la funzione '1' è possibile selezionare i movimenti di acquisto dell'esercizio indicato precedentemente suddivisi e totalizzati per categoria.
Dall'elenco è possibile tramite l'opzione 02 modificare il movimento del cespite indicando il flag di iperammortamento e la relativa data inizio iperammortamento.

 :  : T04 Dati incolonnati
* Cespite :  codice cespite per cui è avvenuto un movimento di acquisto nell'esercizio selezionato
* Descrizione :  descrizione anagrafica del cespite
* TM :  tipo movimento
* Data Reg. :  data registrazione  movimento di acquisto
* Data Iper. :  data inizio iperammortanento valorizzabile tramite l'opzione 02 di modifica
* Importo :  importo movimento di acquisto
* Note :  indica eventuale cespite usato

 :  : T04 Azioni eseguibili
* Opzioni applicabili al singolo cespite : 
** SK :  Scheda Cespite, mi permette di andare a richiamare la scheda di analisi del singolo cespite
** 02 :  Modifica movimento di acquisto cespite ove è possibile indicare flag e data inizio iperammortamento
** 05 :  Interroga movimento di acquisto
** 12 :  Modifica anagrafica cespite
** 15 :  Interroga anagrafica Cespite
** E  :  Escludi Cespite


### FUNZIONE 2 :  APPLICAZIONE IPERAMMORTAMENTO
Con questa funzione vengono visualizzati i movimenti di acquisto selezionati nella funzione 1 per applicare l'iperammortamento fino all'esercizio selezionato.
Se il cespite è stato completamente ammortizzato o venduto/alienato totalmente          in esercizi precedenti questo non viene visualizzato.

 :  : T04 Dati incolonnati
* Capitale :  è la sommatoria di questi elementi : 
** Nuovo parametro sul cespite (A8) che indica l'eventuale capitale iperammortizzato anno precedente. Questo parametro verrà scritto all'applicazione dell'iperammortamento.
** Movimenti di acquisto definiti come iperammortamento per l'esercizio selezionato.
** Qualora ci fosse una vendita/alienazione totale nell'esercizio selezionato, viene ricalcolato il capitale in base ai giorni di possesso ed evidenziato nella colonna vendita totale.
** Qualora ci fosse una vendita/alienazione parziale o comunque un qualsiasi altro movimento che tocca il capitale (tranne gli acquisti perchè già calcolati precedentemente), nell'esercizio selezionato viene effettuato il seguente calcolo : 
*** calcolato il valore del cespite alla data prima di ogni movimento di vendita
*** confrontato il valore del cespite rispetto al movimento di vendita
*** riproporziono il capitale iperammortizzato esercizio precedente
*** qualora la vendita sia maggiore rispetto al capitale iperammortizzato esercizio precedente effettuo la decurtazione sull'esercizio in corso. La sommatoria delle vendite/alienazioni parziali viene evidenziato nella colonna vendita parziale.
* % Maggiorazione :  nel caso dei materiali è 150%  mentre per gli immateriali il 40%
* Maggiorazione Capitale :  Capitale * Percentuale Maggiorazione /100
* Superammortamento :  sommatoria eventuali superammortamenti applicati in esercizi precedenti.
* Superammortamento :  qualora l'intero capitale del cespite è stato oggetto di  superammortamenti applicati in esercizi precedenti.
* Maggiorazione teorica :  ((Capitale Maggiorato - Superammortamento) * Aliquota Ammortamento) / 100.L'aliquota ammortamento per i cespiti non immateriali può essere 100% se cespite minore oppure  ridotta al 50% se primo anno rispetto data inizio ammortamento o data impostata sul piano di    di ammortamento. Per l'ultimo anno di ammortamento qualora la sommatoria delle applicazioni iperammortamenti anno precedenti + anno in corso sia superiore alla maggiorazione del capitale viene applicata la differenza ed evidenziato in reverse l'aliquota applicata.
* Maggiorazione effettiva :  verrà valorizzato quando si sceglierà di iperammortizzare il movimento tramite l'opzione X
* Vendita parziale :  verrà valorizzato quando ci saranno delle variazioni di capitale nell'esercizio selezionato.
* Vendita totale :  verrà valorizzato quando ci sarà una vendita totale nell'esercizio selezionato

**NOTA BENE** :  anche se non vengono creati i movimenti di rettifica è **FONDAMENTALE** per il corretto funzionamento del pgm che le rettifiche decise vengano sempre confermate attraverso le opzioni "X" riportate a seguire.

 :  : T04 Indicazioni particolari
* Capitale con inversione di fondo indica che al capitale è stato applicato il limite massimo ammortizzabile, ripreso dalla tabella della categoria.

* Aliquota sottolineata indica, che il cespite è nel primo anno di ammortamento e che per questo l'aliquota è stata dimezzata del 50%.

* Se l'aliquota è in alta intensità significa inoltre che è stata applicata un'aliquota non deducibile

* Se l'aliquota è in inversione vuol dire che è ultimo anno di ammortamento e quindi è stata calcolata una percentuale differente.

# AZIONI ESEGUIBILI
* Opzioni applicabili al singolo cespite : 
** SK :  Scheda Cespite, mi permette di andare a richiamare la scheda di analisi del singolo cespite
** X  :  Applica/Disapplica, mi permette di confermare la maggiorazione teorica come maggiorazione effettiva, oppure se era già stata definita una maggiorazione effettiva di annullarla. In applicazione scrive 2 parametri con esercizio/cespite/linea : 
*** A7 :  importo iperammortamento applicato
*** A8 :  capitale iperammortizzato
** MI :  Modifica importo iperammortamento
** MC :  Modifica capitale. Modificando il capitale viene ricalcolata anche la maggiorazione teorica qualora non fosse già stata modificata tramite l'opzione MI

* Tasti Funzione : 
** F06 = mi permette di creare o ricreare i movimenti di rettifica per il libro cespiti
** F16 = mi permette di cancellare gli eventuali movimenti di rettifica creati sul libro cespite

**NOTA BENE** : 
* verranno presi come importi i soli importi che sono stati caricati come maggiorazioni effettive
* tali funzioni sono disponibili solo se viene indicata una causale nei dati di input
* le medesime funzioni di disattivano quando la linea fiscale per il periodo indicato è stata chiusa

## NOTE AGGIUNTIVE
### Importo limite ammortizzabile e % non deducibile
L' iperammortamento deve tenere conto del limite massimo ammortizzabile. In presenza di cespiti di valore superiore al limite, il capitale e la relativa maggiorazione saranno esposti e calcolati su tale valore invece che sul valore reale del cespite. Il limite massimo ammortizzabile, andrà impostato sulla tabella della categoria cespite (A5A).

In modo similare qualora sia prevista per il bene una quota non deducibile, tale quota dovrà essere presa in considerazione per il calcolo dell'iperammortamento. La quota indeducibile può essere indicata a livello di categoria cespite (nella tabella A5A), oppure a livello di piano ammortamento indicano una aliquota con causale d'ammortamento non deducibile (a modello AN0).

### Variazioni valore cespite
Per quanto riguarda vendita/alienazione totale il capitale viene ricalcolato sulla base dei giorni di possesso del bene.
Per vendita/alienazione parziale non esistono chiarimenti normativi .Viene proposto il seguente calcolo : 
riproporzionati i capitali iperammortizzabili sulla base della percentuale tra il capitale prima della vendita ed l'importo di vendita.

### Superammortamento/Iperammortamento
Nella gestione degli iperammortamenti se il capitale del cespite è pari agli acquisti definiti come iperammortizzabili, o capitale del cespite inizio esercizio =capitale iperammortizzato esercizio precedente, allora il capitale viene decurtato dell'eventuale superammortamento
(1 movimento di acquisto che diventa da super ad iper), altrimenti si presuppone che ci siano acquisti differenti ed ognuno segue una  strada differente tra iper e super ammortamento.
